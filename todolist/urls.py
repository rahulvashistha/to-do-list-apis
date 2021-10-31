from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', include('api.urls'), name='api-app'),
    url(r'^api_doc$', get_swagger_view(title='Rest API Document')),
]
