from django.contrib import admin
from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users',views.UserProfileViewSet)

urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
]
