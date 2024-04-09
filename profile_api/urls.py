from django.urls import path
from .views import HelloAPIView, HelloViewSet
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', HelloAPIView.as_view()),
    path('', include(router.urls))

]