from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pdf import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'pdf'

urlpatterns = [
    path('', include(router.urls))
]
