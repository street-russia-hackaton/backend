from rest_framework.pagination import PageNumberPagination


class DisciplinesPagination(PageNumberPagination):
    page_size = 11
    page_size_query_param = "page_size"
    max_page_size = 100


class EventsShotPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 100


class NewsPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 100
