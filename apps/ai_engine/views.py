from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.urls import reverse_lazy
from django import forms

from .predictor import predict_category
from .ocr import extract_text_from_image
from .summarizer import summarize_text


class AITextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="Enter Text")


class AIImageForm(forms.Form):
    image = forms.ImageField(label="Upload Image")


class CategoryPredictView(FormView):
    template_name = "ai_engine/category_predict.html"
    form_class = AITextForm
    success_url = reverse_lazy("ai_engine:category_predict")

    def form_valid(self, form):
        text = form.cleaned_data["text"]
        category = predict_category(text)
        summary = summarize_text(text)
        return render(self.request, self.template_name, {
            "form": form,
            "category": category,
            "summary": summary,
        })


class OCRExtractView(FormView):
    template_name = "ai_engine/ocr_extract.html"
    form_class = AIImageForm
    success_url = reverse_lazy("ai_engine:ocr_extract")

    def form_valid(self, form):
        image = form.cleaned_data["image"]
        text = extract_text_from_image(image)
        summary = summarize_text(text)
        category = predict_category(text)
        return render(self.request, self.template_name, {
            "form": form,
            "text": text,
            "summary": summary,
            "category": category
        })
