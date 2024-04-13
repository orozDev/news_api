from rest_framework import serializers
from core.api.auth.serializers import UserSerializer
from core.models import News, Category, Tag


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
    
    category_detail = CategorySerializer(read_only=True, many=False, source='category')
    tags_detail = TagSerializer(read_only=True, many=True, source='tags')
    author_detail = UserSerializer(read_only=True, many=False, source='author')
    
    class Meta:
        model = News
        fields = '__all__'
        extra_kwargs = {
            'category_detail': {'read_only': True},
            'tags_detail': {'read_only': True},
        }

    def create(self, validated_data):
        request = self.context['request']
        validated_data['author'] = request.user
        return super().create(validated_data)
