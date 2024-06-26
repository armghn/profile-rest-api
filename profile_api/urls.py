from django.urls import path
from .views import HelloAPIView, HelloViewSet, UserProfileViewSet, UserProfileFeedViewSet, LoginViewSet
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, basename='login')
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', HelloAPIView.as_view()),
    path('', include(router.urls))

]