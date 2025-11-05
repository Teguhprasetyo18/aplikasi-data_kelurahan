from django.urls import path, include
from .views import WargaListAPIView, WargaCreateAPIView, WargaDetailAPIView
from rest_framework.routers import DefaultRouter
from .views import PengaduanViewSet
router = DefaultRouter()
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')


urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/tambah/', WargaCreateAPIView.as_view(), name='warga-create'),
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='warga-detail'),
    path('', include(router.urls)),

]
