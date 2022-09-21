from rest_framework import serializers
from .models import Board

class BoardSerializ(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields='__all__'

    def validate_name(self, value):
        if len(value) >8:
            raise serializers.ValidationError("error message")
        return value

