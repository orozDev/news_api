from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from core.api.paginations import StandardResultsSetPagination
from core.api.permissions import IsOwner
from core.api.serializers import ListNewsSerializer, DetailNewsSerializer, CreateUpdateNewsSerializer, CategorySerializer
from core.models import Category, News, Tag
from .mixins import UltraModelViewSet


class NewsViewSet(UltraModelViewSet):
    
    """
        Permissions:
            * stuffs and super admin have an access for every opportunity 
            * only owners can edit and delete own news
        Pagination: 
            * default 12 items. with "page_size" parameter would be changable 
                count of items to get them
        Filters: 
            * Filter by 'category', 'tags', 'is_published', 'author'
    """
    
    pagination_class = StandardResultsSetPagination
    queryset = News.objects.all()
    serializer_classes = {
        'list': ListNewsSerializer,
        'retrieve': DetailNewsSerializer,
        'create': CreateUpdateNewsSerializer,
        'update': CreateUpdateNewsSerializer,
    }
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'tags', 'is_published', 'author']
    ordering_fields = ['views', 'created_at']
    search_fields = ['name', 'slug', 'description', 'content']
    permission_classes_by_action = {
        'create': [IsAuthenticated, IsAdminUser | IsOwner],
        'list': [AllowAny,],
        'update': [IsAuthenticated, IsAdminUser | IsOwner],
        'retrieve': [AllowAny,],
        'destroy': [IsAuthenticated, IsAdminUser | IsOwner],
    }
    
    def retrieve(self, request, pk, *args, **kwargs):
        try:
            news = self.queryset.get(id=pk)
            news.views += 1
            news.save()
        except News.DoesNotExist:
            pass
        return super().retrieve(self, request, *args, **kwargs)
    

class CategoryViewSet(UltraModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes_by_action = {
        'create': [IsAuthenticated, IsAdminUser],
        'list': [AllowAny,],
        'update': [IsAuthenticated, IsAdminUser],
        'retrieve': [AllowAny,],
        'destroy': [IsAuthenticated, IsAdminUser],
    }
    


class TagViewSet(UltraModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = CategorySerializer
    permission_classes_by_action = {
        'create': [IsAuthenticated, IsAdminUser],
        'list': [AllowAny,],
        'update': [IsAuthenticated, IsAdminUser],
        'retrieve': [AllowAny,],
        'destroy': [IsAuthenticated, IsAdminUser],
    }
