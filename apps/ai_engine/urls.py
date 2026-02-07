from django.urls import path
from . import views

app_name = "ai_engine"

urlpatterns = [
    path('predict/', views.CategoryPredictView.as_view(), name='category_predict'),
    path('ocr/', views.OCRExtractView.as_view(), name='ocr_extract'),
]
