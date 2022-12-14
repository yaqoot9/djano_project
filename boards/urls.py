from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [

path('home/',views.home,name='home'),
path('get/<pk>/',views.board_topics,name='border_topic'),
path('add/<pk>/new',views.new_topic,name='new_topic'),
path('update/',views.update,name='update'),
#path('board/',views.BoardList.as_view(),name='django_rest'),

path('creat/',views.creat_board,name='create_board'),
path('update/<str:pk>/',views.UpdateBoard,name='Update_Board'),
path('delete/<str:pk>/',views.DeleteBoard,name='Delete_Board'),


path('list/',views.boardList,name='BoardList'),
path('Create/',views.boardCreate,name='BoardCreate'),
path('UpdateBoard/<str:pk>',views.boardUpdate,name='BoardUpdate'),
path('DeleteBoard/<str:pk>',views.boardDelete,name='BoardDelete'),

path('',views.user_login,name='login'),
path('logout/',views.user_logout,name='logout'),

path('hello/',views.HelloView.as_view(),name='hello'),
    ]