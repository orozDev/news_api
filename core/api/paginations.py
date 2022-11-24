from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings
from rest_framework.response import Response

from utils.constants import USE_PAGINATION, PAGE_SIZE
from utils.utils import make_bool


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = PAGE_SIZE
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = PAGE_SIZE
    max_page_size = 100 
    
    
class PaginationBreaker(object):
    
    def get(self, request, *args, **kwargs):
        use_pagination = make_bool(request.GET.get(USE_PAGINATION, True))
        if not use_pagination:
            self.pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        return super().list(request, *args, **kwargs)
