from django.urls import include, path
from . import views


urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('users/create', views.RegisterUserAPIView.as_view()),
    path('users/update/<int:pk>', views.UpdateProfileView.as_view()),
    path('users/reset-password/<int:pk>', views.ResetPasswordView.as_view()),
    path('users/delete/<int:pk>', views.deleteUser, name="station-delete")
]
