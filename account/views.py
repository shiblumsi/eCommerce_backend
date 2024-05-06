from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate, login

from .serializers import VendorSignupSerilizer, CustomerSignupSerilizer,LoginSerializer

class VendorSignupView(APIView):
    def post(self,request):
        serializer = VendorSignupSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerSignupView(CreateAPIView):
    serializer_class = CustomerSignupSerilizer


class CustomerLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)