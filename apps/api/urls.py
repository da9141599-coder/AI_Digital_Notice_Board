from django.urls import path
from .views import (
    NoticeListCreateAPI,
    NoticeDetailAPI,
    AIPredictAPI
)
app_name = "api" 
urlpatterns = [
    path('notices/', NoticeListCreateAPI.as_view(), name='api_notice_list'),
    path('notices/<int:pk>/', NoticeDetailAPI.as_view(), name='api_notice_detail'),
    path('predict/', AIPredictAPI.as_view(), name='api_predict'),
]
