from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('address/', views.AddressListView.as_view(), name='addresses'),
    path('address/<str:pk>', views.AddressDetailView.as_view(), name='address-detail'),
    path('blockchain/', views.BlockchainListView.as_view(), name='blockchains'),
    path('blockchain/<str:pk>', views.BlockchainDetailView.as_view(), name='blockchain-detail'),
]

urlpatterns += [  
    path('address/create/', views.AddressCreate.as_view(), name='address_create'),
    path('address/<str:pk>/update/', views.AddressUpdate.as_view(), name='address_update'),
    path('address/<str:pk>/delete/', views.AddressDelete.as_view(), name='address_delete'),
]