from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import UserCreateSerializer, PackagesSerializer, MyTokenObtainPairSerializer
from .models import Package
from rest_framework_simplejwt.views import TokenObtainPairView


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class PackagesListView(ListAPIView):
    serializer_class =PackagesSerializer
    queryset = Package.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer