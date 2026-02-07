from django.urls import path
from .views import (
    NoticeListView,
    NoticeDetailView,
    NoticeCreateView
)

app_name = 'notice'

urlpatterns = [
    path('', NoticeListView.as_view(), name='notice_list'),
    path('create/', NoticeCreateView.as_view(), name='create_notice'),  # ✅ ADD THIS
    path('<int:pk>/', NoticeDetailView.as_view(), name='notice_detail'),
]
