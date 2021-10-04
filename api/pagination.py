from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class TaskLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 7
    max_limit = 13

class TaskPageNumberPagination(PageNumberPagination):
    page_size = 7