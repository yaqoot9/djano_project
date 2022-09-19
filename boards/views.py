from django.contrib.auth.models import User

from .models import  Board,Topic,Post
from django.views import View
# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.views.decorators.http import require_http_methods

from  rest_framework.views import  APIView
from .serializers import  BoardSerializ
from rest_framework.response import Response
from rest_framework import status
from .forms import BoardForm
@require_http_methods(['GET'])
def home(request):
    boards=Board.objects.all()
    return render(request,'home.html',{'boards':boards})




def board_topics(request,pk):
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


def update(request):
    board=Board.objects.all().update( description='This ....')
    return redirect('home')



class BoardList(APIView):
    def get(self,request):
        board=Board.objects.all()
        serialize= BoardSerializ(board,many=True)
        return Response(serialize.data)

    def post(self, request):
        serializer = BoardSerializ(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def creat_board(request):
    form = BoardForm()
    if request.method=='POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'new_board.html',context)

def UpdateBoard(request,pk):
    board=Board.objects.get(id=pk)
    form = BoardForm(instance=board)
    if request.method=='POST':
        form = BoardForm(request.POST,instance=board)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}

    return render(request, 'new_board.html', context)


def DeleteBoard(request,pk):
    board = Board.objects.get(id=pk)
    if request.method=='POST':
        board.delete()
        return redirect('/')

    context={'item':board}
    return render(request,'delete.html',context)