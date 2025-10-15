from django.urls import path
from .views import WargaListView, WargaDetailView, PengaduanListView, WargaCreateView,WargaUpdateView,WargaDeleteView,PengaduanUpdateView,PengaduanDeleteView
from .views import WargaListAPIView,WargaDetailAPIView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'), 
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'), 
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),
    path('<int:pk>/edit/', PengaduanUpdateView.as_view(), name='Pengaduan-edit'), 
    path('<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='Pengaduan-hapus'),
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('api/warga/<int:pk>/', WargaDetailAPIView.as_view(), name='warga-detail'),
]
