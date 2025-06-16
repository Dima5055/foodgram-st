from rest_framework.pagination import PageNumberPagination


class CustomHomePagination(PageNumberPagination):
    page_size_query_param = 'limit'
