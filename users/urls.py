from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from .views import UserProfileView, NewUserView, FileuploadView


router = DefaultRouter()
router.register("register", RegisterView)
router.register("user-profile", UserProfileView)
router.register("file", FileuploadView)


urlpatterns = [
    path("", include(router.urls))
   
]
