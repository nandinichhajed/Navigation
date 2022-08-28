from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'', views.MytableViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('v1/ships/', views.table, name="table"),
    path('v1/ships/<int:id>/', views.table_detail, name="table_detail"),
]
