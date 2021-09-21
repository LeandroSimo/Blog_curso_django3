from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path, re_path
from .views import hello_world
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = ( [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('', include("core.urls")),
    re_path('ckeditor/', include('ckeditor_uploader.urls')),  
] 
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)