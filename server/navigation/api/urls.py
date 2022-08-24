from django.urls import path, include
from rest_framework import routers
from .views import MytableViewSet
from . import views


router = routers.DefaultRouter()
router.register(r'', views.MytableViewSet, basename='Mytable')


urlpatterns = [
    path('v1/ships/', include(router.urls)),  
    # path('v1/ships/<int:ID>/', views.MytableViewSet.as_view({'get': 'list'}), name='Mytable'),
]
