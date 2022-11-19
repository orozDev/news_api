from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from core.api.paginations import StandardResultsSetPagination
from core.api.permissions import IsOwner, PermissionByAction
from core.api.serializers import NewsSerializer, CategorySerializer
from core.models import Category, News, Tag


class NewsViewSet(PermissionByAction, ModelViewSet):
    
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
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'tags', 'is_published', 'author']
    ordering_fields = ['views',]
    search_fields = ['title', 'slug',]
    permission_classes_by_action = {
        'create': [IsAuthenticated, IsAdminUser | IsOwner],
        'list': [AllowAny,],
        'update': [IsAuthenticated, IsAdminUser | IsOwner],
        'retrieve': [AllowAny,],
        'destroy': [IsAuthenticated, IsAdminUser | IsOwner],
    }
    
    def retrieve(self, request, pk, *args, **kwargs):
        news = self.queryset.get(id=pk)
        news.views += 1
        news.save()
        return super().retrieve(self, request, *args, **kwargs)
    

class CategoryViewSet(PermissionByAction, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes_by_action = {
        'create': [IsAuthenticated, IsAdminUser],
        'list': [AllowAny,],
        'update': [IsAuthenticated, IsAdminUser],
        'retrieve': [AllowAny,],
        'destroy': [IsAuthenticated, IsAdminUser],
    }
    


class TagViewSet(PermissionByAction, ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = CategorySerializer
    permission_classes_by_action = {
        'create': [IsAuthenticated, IsAdminUser],
        'list': [AllowAny,],
        'update': [IsAuthenticated, IsAdminUser],
        'retrieve': [AllowAny,],
        'destroy': [IsAuthenticated, IsAdminUser],
    }