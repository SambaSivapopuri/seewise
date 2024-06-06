from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Machine, ProductionLog
from .serializers import MachineSerializer, ProductionLogSerializer, OEESerializer
from .utils import calculate_oee

class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class UserHome(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        user = request.user
        home_data = {
            'user_id': user.id,
            'username': user.username,
            
        }
        return Response(home_data, status=status.HTTP_200_OK)


class MachineListCreate(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        machines = Machine.objects.all()
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductionLogListCreate(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        logs = ProductionLog.objects.all()
        serializer = ProductionLogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductionLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OEEView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        logs = ProductionLog.objects.all()
        oee_data = calculate_oee(logs)
        serializer = OEESerializer(oee_data)
        return Response(serializer.data)

class FilterOEEView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        machine_id = request.query_params.get('machine_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        logs = ProductionLog.objects.all()

        if machine_id:
            logs = logs.filter(machine_id=machine_id)

        if start_date and end_date:
            logs = logs.filter(start_time__gte=start_date, end_time__lte=end_date)

        oee_data = calculate_oee(logs)
        serializer = OEESerializer(oee_data)
        return Response(serializer.data)