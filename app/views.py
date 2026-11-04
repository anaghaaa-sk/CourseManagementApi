from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Course
from app.serializers import CourseSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

#CREATE A NEW COURSE
class CourseCreate(APIView):
    def post(self,request):
        serializer_instance=CourseSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#RETRIEVE ALL RECORDS
class CourseList(APIView):
    def get(self,request):
        c=Course.objects.all()
        serializer_instance=CourseSerializer(c,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)


#RETRIEVE A SINGLE COURSE USING ITS ID
class CourseRetrieve(APIView):
    def get(self,request,pk):
        c=get_object_or_404(Course,id=pk)
        serializer_instance=CourseSerializer(c)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

#UPDATING AN EXISTING COURSE USING PUT AND PATCH

class CourseUpdate(APIView):
    def put(self,request,pk):
        c=get_object_or_404(Course,id=pk)
        serializer_instance=CourseSerializer(instance=c,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class CoursePartialUpdate(APIView):
    def patch(self,request,pk):
        c=get_object_or_404(Course,id=pk)
        serializer_instance=CourseSerializer(instance=c,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


#DELETE A COURSE
class CourseDelete(APIView):
    def delete(self,request,pk):
        c=get_object_or_404(Course,id=pk)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)