from rest_framework.generics import (CreateAPIView,RetrieveAPIView,ListAPIView,CreateAPIView)
from rest_framework.permissions import IsAuthenticated
from .serializers import (UserCreateSerializer, PackagesListSerializer,PackagesDetailSerializer,BookingSerializer,MyTokenObtainPairSerializer)
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

class BookPackage(CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        package = Package.objects.get(id=self.kwargs['package_id'])
        serializer.save(user=self.request.user, package=package)
