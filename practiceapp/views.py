from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .serializers import StudentSerializers,UserSerializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Students
from rest_framework import status
from django.shortcuts import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class RegisterUser(APIView):
    def post(self,request):
        serializer=UserSerializers(data=request.data)
        if not serializer.is_valid():
            return Response({'status':'404','errors':serializer.errors,'message':'Something went wrong'})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        refresh=RefreshToken.for_user(user)
        #token_obj,_=Token.objects.get_or_create(user=user)
            
        return Response({'status':200,'payload':serializer.data,'refresh':str(refresh),'access':str(refresh.access_token),'message':'your data saved'})
            
            
class StudentView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        result=Students.objects.all()
        serializer=StudentSerializers(result,many=True)
        return Response({'status':'Success','data':serializer.data},status=status.HTTP_200_OK)
    
    
    def post(self,request):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({'status':'success','data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'status':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,id=None):
        
        result=get_object_or_404(Students,id=id)      
        result.delete()
        return Response({'status':'successfully deleted'},status=status.HTTP_200_OK)
    
    
    def put(self,request,id):
        try:
             result=Students.objects.get(id=id)
             
        except:
            return Response({'status':'error','data':'sorry id was not found'})
        
        serializer=StudentSerializers(result,data=request.data)      
        if serializer.is_valid():
            serializer.save()
            return Response({'staus':'success','data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'status':'error'},status=status.HTTP_404_NOT_FOUND)