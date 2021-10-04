from django.urls.conf import path

from api.views import (
    api_root,
    TaskCreateAPIView,
    TaskDetailAPIView,
    TaskListAPIView,
    TaskEditAPIView,
    TaskDeleteAPIView,
    UserCreateAPIView,
    UserDetailAPIView,
    UserListAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
    ChangePasswordView,
    )

# url patterns here

urlpatterns = [
    path('', api_root, name='api-root'),

    path('tasks/', TaskListAPIView.as_view(), name='tasks-list-api'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='tasks-create-api'),
    path('tasks/<pk>/', TaskDetailAPIView.as_view(), name='tasks-detail-api'),
    path('tasks/<pk>/edit/', TaskEditAPIView.as_view(), name='tasks-edit-api'),
    path('tasks/<pk>/delete/', TaskDeleteAPIView.as_view(), name='tasks-delete-api'),
    
    path('users/', UserListAPIView.as_view(), name='users-list-api'),
    path('users/create', UserCreateAPIView.as_view(), name='users-create-api'),
    path('users/<pk>/', UserDetailAPIView.as_view(), name='users-detail-api'),
    # path('users/<pk>/update/', UserUpdateAPIView.as_view(), name='users-update-api'),
    # path('users/<pk>/delete/', UserDeleteAPIView.as_view(), name='users-delete-api'),
    # path('users/<pk>/change_password/', ChangePasswordView.as_view(), name='users-password-api'),

]

