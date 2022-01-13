from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from .views import UserProfileView, NewUserView, FileuploadView, RegisterView


router = DefaultRouter()
router.register("register", RegisterView)
router.register("user-profile", UserProfileView)
router.register("file", FileuploadView)
#router.register("login", LoginView)



urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginView.as_view()),
]
