from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drfapp.seriliazation import StudentSerilization
from drfapp.models import Student
from rest_framework.permissions import IsAuthenticated


class Testapi(APIView):
    permission_classes=(IsAuthenticated,)
    def get(sef, request,*args,**kwargs):
        qs=Student.objects.all()
        student1=qs.first()
        serialiazer=StudentSerilization(student1)
        return Response(serialiazer.data)
    def post(self, request,*args,**kwargs):
        seriliazer=StudentSerilization(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response(seriliazer.errors)
    
