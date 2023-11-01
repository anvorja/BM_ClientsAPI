from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clientesapp import views
from rest_framework import routers
from . import views
# from .views import ClientList

router = routers.DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, 'clientes')

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('clients/', views.clients, name='clients'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('create_client/', views.create_client, name='create_client'),
    path('clients/<int:client_id>', views.client_detail, name='client_detail'),
    path('clients/<int:client_id>/delete', views.delete_client, name='delete_client'),
    path('priority_client/', views.prioritary_clients, name='prioritario_clients'),
    path('listado/', views.get_clients_as_json),
    # path('api/clients/', ClientList.as_view(), name='client-list'),
    path('api/', include(router.urls)),
]
