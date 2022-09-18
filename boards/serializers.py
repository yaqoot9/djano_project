from rest_framework import serializers
from .models import Board
from .models import Board

class BoardSerializ(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields='__all__'

