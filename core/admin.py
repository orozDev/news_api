from core.models import News, Category, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django import forms


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(label=_('Контент'), widget=CKEditorUploadingWidget())
    description = forms.CharField(label=_('Краткое описание'), 
            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAmin(admin.ModelAdmin):

    list_display = (
        'id', 
        'title', 
        'created_at', 
        'category', 
        'views', 
        'is_published', 
        'get_image',
    )
    list_display_links = ('id', 'title',)
    list_filter = ('category',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    prepopulated_fields = {
        'slug': ['title'],
    }
    form = NewsAdminForm
    fieldsets = (
        (_('Оснавная информация'), {'fields': (
            'slug',
            'title',
            'image',
            'category',
            'tags',
            'description',
            'content',
        )}),
        (_('Авторство'), {'fields': (
            'views',
            'is_published',
            'author',
        )}),
        (_('Дополнительная информация'), {'fields': (          
            'created_at',
            'updated_at',
            'get_image',
        )}),
    )
    add_fieldsets = (
        (_('Оснавная информация'), {
            'classes': ('wide',),
            'fields': (
                    'slug',
                    'title',
                    'image',
                    'category',
                    'tags',
                    'description',
                    'content',
            ),
        }),
        (_('Авторство'), {'fields': (
            'is_published',
            'author',
        )}),
    )

    readonly_fields = ('created_at', 'updated_at', 'get_image', 'views',)
    
    @admin.display(description=_('Изображение'))
    def get_image(self, obj):
        return mark_safe('<img src="%s" alt="%s" width="200px" />' % \
            (obj.image.url, obj.title))
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    
# Register your models here.
