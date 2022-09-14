from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import  Board,Topic,Post
from django.views import View
# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect


def home(request):
    boards=Board.objects.all()
    return render(request,'home.html',{'boards':boards})




class board_topics(View):

     def get (self,request, pk):
         board = get_object_or_404(Board, pk=pk)
         return render(request, 'topics.html', {'board': board})




def new_topic(request,pk):
    board=get_object_or_404(Board,pk=pk)
    user=User.objects.first()
    if request.method=='POST':
        subject=request.POST['subject']
        message=request.POST['message']

        topic=Topic.objects.create(
        subject=subject,
        board=board,
        starter=user
         )
        post=Post.objects.create(
        message=message,
        topic=topic,
        created_by=user
        )

    return render(request,'new_topic.html',{'board':board})







