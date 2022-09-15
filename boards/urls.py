from django.urls import path
from . import views

urlpatterns = [

path('',views.home,name='home'),
path('<pk>/',views.board_topics,name='border_topic'),
path('<pk>/new',views.new_topic,name='new_topic'),
path('update/',views.update,name='update'),
    ]