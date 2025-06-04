from django.urls import path
from .views import RegisterView, ChatView,ChatHistoryView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/token', TokenRefreshView.as_view(), name='token_refresh'),

    path('chat/', ChatView.as_view(), name='chat'),
    path('chat/history/', ChatHistoryView.as_view(), name='chat_history'),

]
