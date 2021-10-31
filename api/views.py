from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView, 
    UpdateAPIView, 
    RetrieveUpdateAPIView,
    DestroyAPIView, 
    )
from api.serializers import (
    TaskCreateSerializer,
    TaskDetailSerializer,
    TaskListSerializer,
    TaskEditSerializer,
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer,
    UserUpdateSerializer,
    ChangePasswordSerializer
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    )
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from api.models import Task
from api.permissions import IsOwnerOrReadOnly
from api.pagination import TaskPageNumberPagination

# Views From Here

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tasks': reverse('tasks-list-api', request=request, format=format),
        'users': reverse('users-list-api', request=request, format=format),
    })

class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    #permission_classes = [IsAuthenticated]

class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

    pagination_class = TaskPageNumberPagination

class TaskDetailAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer

class TaskDeleteAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    #permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

class TaskEditAPIView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskEditSerializer
    #permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    #permission_classes = [IsAuthenticated]

class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    #permission_classes = [IsAuthenticated]

class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    #permission_classes = [IsAuthenticated, IsAdminUser]

