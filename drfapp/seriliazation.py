from .models import Student
from rest_framework import serializers

class StudentSerilization(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=(
            'name','age'
        )

