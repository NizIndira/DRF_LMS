from django.urls import path

from users.apps import UsersConfig
from users.views import UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_get'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
]