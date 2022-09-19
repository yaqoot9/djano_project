from django.urls import path
from . import views

urlpatterns = [

path('',views.home,name='home'),
path('get/<pk>/',views.board_topics,name='border_topic'),
path('add/<pk>/new',views.new_topic,name='new_topic'),
path('update/',views.update,name='update'),
path('board/',views.BoardList.as_view()),
path('creat/',views.creat_board,name='create_board'),
path('update/<str:pk>/',views.UpdateBoard,name='Update_Board'),
path('delete/<str:pk>/',views.DeleteBoard,name='Delete_Board'),
    ]