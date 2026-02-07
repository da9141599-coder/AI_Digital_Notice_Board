from django.test import TestCase
from apps.ai_engine.predictor import predict_category
from apps.ai_engine.summarizer import summarize_text

class AIPredictorTests(TestCase):

    def test_keyword_prediction(self):
        cat = predict_category("Exam starts tomorrow")
        self.assertEqual(cat, "examination")

    def test_summary(self):
        summary = summarize_text("Sentence one. Sentence two. Sentence three.")
        self.assertIn("Sentence one", summary)
