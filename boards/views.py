from django.contrib.auth.models import User
from .models import  Board,Topic,Post
from django.views import View
# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect,reverse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view

from  rest_framework.views import  APIView
from .serializers import  BoardSerializ
from rest_framework.response import Response
from rest_framework import status
from .forms import BoardForm
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import IsAuthenticated


def user_login(request):
    context={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('home'))

        else:
            context["error"]="provide valid credentials!"
            return render(request, 'login.html', context)

    else:
        return render(request,'login.html',context)


def user_logout(request):
     logout(request)
     return HttpResponseRedirect(reverse('login'))



class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
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



@api_view(['GET'])
def boardList(request):
     board=Board.objects.all()
     serializer=BoardSerializ(board,many=True)
     return Response(serializer.data)


@api_view(['POST'])
def boardCreate(request):
    serializer=BoardSerializ(data=request.data)
    serializer.validate_name(request.data['name'])
    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response (serializer.data)



@api_view(['PUT'])
def boardUpdate(request,pk):
    board=Board.objects.get(id=pk)
    serializer=BoardSerializ(instance=board,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response (serializer.data)

@api_view(['delete'])
def boardDelete(request,pk):
    board=Board.objects.filter(id=pk).first()
    board.delete()
    return Response ('Deleted!')












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