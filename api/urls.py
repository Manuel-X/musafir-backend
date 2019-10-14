from django.urls import path
from .views import UserCreateAPIView,PackagesListView,MyTokenObtainPairView,PackageDetailView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('packages/', PackagesListView.as_view(), name='packages'),
    path('packages/<int:package_id>/', PackageDetailView.as_view(), name='packages_detail'),


]