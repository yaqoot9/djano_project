from django.urls import path
from . import views

urlpatterns = [
path('',views.home),
path('<pk>/',views.board_topics.as_view()),
path('<pk>/new',views.new_topic)

    ]