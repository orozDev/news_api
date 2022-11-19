from rest_framework import serializers
from core.models import News, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__' 
        

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__' 


class NewsSerializer(serializers.ModelSerializer):
    
    category_detail = CategorySerializer(read_only=True, many=False, source='category')
    tags_detail = TagSerializer(read_only=True, many=True, source='tags')
    
    class Meta:
        model = News
        fields = '__all__'
        extra_kwargs = {
            'category_detail': {'read_only': True},
            'tags_detail': {'read_only': True},
        }