from rest_framework.generics import (CreateAPIView,RetrieveAPIView,ListAPIView)
from .serializers import (UserCreateSerializer, PackagesListSerializer,PackagesDetailSerializer,MyTokenObtainPairSerializer)
from .models import Package
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class PackagesListView(ListAPIView):
    serializer_class =PackagesListSerializer
    queryset = Package.objects.all()

class PackageDetailView(RetrieveAPIView):
    queryset = Package.objects.all()
    serializer_class =PackagesDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'package_id' 
