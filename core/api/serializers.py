from rest_framework import serializers
from core.api.auth.serializers import UserSerializer
from core.models import News, Category, Tag
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    
    count = serializers.IntegerField(read_only=True, source='news_count')
    
    class Meta:
        model = Category
        fields = '__all__' 
        

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__' 


class NewsSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = News
        fields = '__all__'
        

class ReadUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = (
            'is_active',
            'is_staff',
            'date_joined',
            'is_superuser',
            'groups',
            'user_permissions',
            'password',
            'last_login',
        )
    
class CreateUpdateNewsSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = News
        exclude = ('author',)
        
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)


class ListNewsSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    author = ReadUserSerializer()
    
    
    class Meta:
        model = News
        exclude = ('content',)
        

class DetailNewsSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    author = ReadUserSerializer()
    
    
    class Meta:
        model = News
        fields = '__all__'

