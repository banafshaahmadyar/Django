from rest_framework.views import APIView
from .serializers import StudentSerializer
from django.http.response import JsonResponse
from .models import Student
from django.http.response import Http404
from rest_framework.response import Response
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from backend.permissions import IsOwnerOrReadOnly




class StudentView(APIView):
    
    permission_classes =[IsOwnerOrReadOnly]

    def get_student(self, pk):
        try:
            student = Student.objects.get(studentId=pk)
            self.check_object_permissions (self.request, state)
            return student
        except:
            return JsonResponse("Student Does Not Exist", safe=False)

    def get(self, request, pk=None):
        if pk:
            data = self.get_student(pk)
            serializer = StudentSerializer(data)
        else:
            data = Student.objects.all()
            serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Created Successfully", safe=False)
        return JsonResponse("Failed to Add Student", safe=False)

    def put(self, request, pk=None):
        student_to_update = Student.objects.get(studentId=pk)
        serializer = StudentSerializer(instance=student_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Student")

    def delete(self, request, pk=None):
        student_to_delete = Student.objects.get(studentId=pk)
        student_to_delete.delete()
        return JsonResponse("Student Deleted Successfully", safe=False)


