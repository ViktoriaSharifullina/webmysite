from . import views
from django.urls import path

urlpatterns = [
                  path('', views.index, name='index'),
                  path('mammals', views.mammals, name='mammals'),
                  path('ecoproblems', views.ecoproblems, name='ecoproblems'),
                  path('post/', views.post_list, name='post'),
                  path('post/create/', views.PostCreate.as_view(), name='post_create_url'),
                  path('post/<str:slug>/', views.post__detail, name='post_detail_url'),
              ]