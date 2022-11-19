from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class TimeAbstractModel(models.Model):
    
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='дата добавления')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='дата изменения')
    
    class Meta:
        abstract = True
        
        
class News(TimeAbstractModel):
    
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ('-created_at', '-updated_at',)
        
    slug = models.SlugField(unique=True, null=True)
    title = models.CharField(max_length=100, verbose_name=_('заголовок'))
    image = models.ImageField(verbose_name=_('изображение'), upload_to='news_images/')
    category = models.ForeignKey('Category',
            on_delete=models.PROTECT, verbose_name=_('категория'))
    tags = models.ManyToManyField('Tag', verbose_name=_('теги'))
    description = models.CharField(max_length=100, verbose_name=_('краткое описание'))
    content = models.TextField(verbose_name=_('контент'))
    views = models.PositiveIntegerField(verbose_name=_('просморы'), default=0)
    is_published = models.BooleanField(verbose_name=_('опубликовать'), default=True)
    author = models.ForeignKey(User, related_name='news', 
            verbose_name=_('автор'), on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    
class Category(TimeAbstractModel):
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('-created_at', '-updated_at',)
        
    title = models.CharField(max_length=100, 
            verbose_name=_('название категории'), unique=True)
    
    def __str__(self) -> str:
        return f'{self.title}'
    

class Tag(TimeAbstractModel):
    
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ('-created_at', '-updated_at',)
        
    title = models.CharField(max_length=100, 
            verbose_name=_('название тега'), unique=True)
    
    def __str__(self) -> str:
        return f'{self.title}'

# Create your models here.
