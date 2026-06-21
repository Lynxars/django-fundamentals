from django.urls import path
from . import views
 
app_name = 'blog'  
 
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    # Add the edit route 
    path('post/<slug:slug>/edit/', views.update_post, name='update_post'),
    
]