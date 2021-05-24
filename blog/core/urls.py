from django.urls import path, include
from .views import hello_blog
from .views import post_detail, save_form


urlpatterns = [
    path('', hello_blog, name='home'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('save_form', save_form, name='save_form'),
]
