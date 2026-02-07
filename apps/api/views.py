from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.notice.models import Notice
from apps.ai_engine.predictor import predict_category
from .serializers import NoticeSerializer, AIPredictionSerializer


# ------------------------- NOTICE API ------------------------------

class NoticeListCreateAPI(generics.ListCreateAPIView):
    queryset = Notice.objects.all().order_by('-created_at')
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class NoticeDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]


# ------------------------- AI PREDICTION API ------------------------------

class AIPredictAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AIPredictionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data['text']
        category = predict_category(text)

        return Response({
            "input": text,
            "predicted_category": category
        }, status=status.HTTP_200_OK)
