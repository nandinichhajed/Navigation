from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.MytableViewSet)

urlpatterns = [
    path('v1/ships/', include(router.urls)),
]
