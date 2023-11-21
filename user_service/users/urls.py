from django.urls import path
from .views import UserView

urlpatterns = [
    path('user/<int:user_id>/', UserView.as_view(), name='user_detail'),
    path('user/', UserView.as_view(), name='create_user'),
]
