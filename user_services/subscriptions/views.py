# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# from django.shortcuts import get_object_or_404
from .models import UserDetails
from .serializers import DataValidator

class SubscribeViewSet(ModelViewSet):
    def create(self, request):
        user_data = DataValidator(data=request.data)
        if user_data.is_valid():
            user, created = UserDetails.objects.get_or_create(email=user_data.validated_data['email'])
            if user.email:
                if not user.is_subscribed:
                    user.is_subscribed = True
                    user.save()
                    return Response({"success":"Email has subscribed Successfully"}, status=status.HTTP_201_CREATED)
                return Response({"error": "Email is already subscribed."}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Email is not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(user_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UnsubscribeViewSet(ModelViewSet):
    def create(self, request):
        user_data = DataValidator(data=request.data)
        if user_data.is_valid():
            user = UserDetails.objects.get(email=user_data.validated_data['email'])
            if user.email:
                if user.is_subscribed:
                    user.is_subscribed = False
                    user.save()
                    return Response({"message": "Successfully unsubscribed."}, status=status.HTTP_200_OK)
                return Response({"error": "Email is not subscribed."}, status=status.HTTP_404_NOT_FOUND)
            return Response({"error": "Email is not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(user_data.errors, status=status.HTTP_400_BAD_REQUEST)

# class SubscriptionStatus(ModelViewSet):
#     def list(self, request, email):
#         user_data = DataValidator(data=request.data)
#         if user_data.is_valid():
#             user = UserDetails.objects.get(email=user_data.validated_data['email'])
#             if user.email:
#                 data = {
#                     "email": user.email, 
#                     "is_subscribed": user.is_subscribed 
#                     }
#                 return Response(data, status=status.HTTP_200_OK)
#             return Response({"error": "Email is not found."}, status=status.HTTP_404_NOT_FOUND)
#         return Response(user_data.errors, status=status.HTTP_400_BAD_REQUEST)
                
               