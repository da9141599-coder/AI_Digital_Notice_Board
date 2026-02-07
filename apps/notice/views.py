from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Notice
from .forms import NoticeForm
from apps.ai_engine.predictor import predict_category  # uses ai_engine model if available
from django.contrib import messages




class NoticeListView(ListView):
    model = Notice
    template_name = 'notice/notice_list.html'
    context_object_name = 'notices'
    paginate_by = 12

    def get_queryset(self):
        # Show active notices (all, not only published)
        return Notice.objects.filter(is_active=True).order_by('-publish_date')

class NoticeDetailView(DetailView):
    model = Notice
    template_name = 'notice/notice_detail.html'
    context_object_name = 'notice'


class DisplayBoardView(ListView):
    model = Notice
    template_name = "notice/display_board.html"
    context_object_name = "notices"

    def get_queryset(self):
        return Notice.objects.filter(is_archived=False).order_by("-publish_date")
    
    
def classify_priority(text):
    if not text:
        return 'low'

    text = text.lower().strip()

    high_keywords = [
        'urgent',
        'emergency',
        'asap',
        'as soon as possible',
        'immediately',
        'critical',
        'last date',
        'last day',
        'exam today',
        'today is the last',
        'fine will be added',
    ]

    medium_keywords = [
        'important',
        'attention',
        'mandatory',
        'submit',
        'submission',
        'deadline',
        'meeting',
        'exam',
        'fees',
        'payment',
        'pay',
    ]

    for word in high_keywords:
        if word in text:
            return 'high'

    for word in medium_keywords:
        if word in text:
            return 'medium'

    return 'low'

class NoticeListView(ListView):
    model = Notice
    template_name = 'notice/notice_list.html'
    context_object_name = 'notices'
    paginate_by = 12

    def get_queryset(self):
        return Notice.objects.filter(is_active=True).order_by('-publish_date')


class NoticeCreateView(CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notice/create_notice.html'
    success_url = reverse_lazy('notice:notice_list')

    def form_valid(self, form):
        notice = form.save(commit=False)
        notice.posted_by = self.request.user

        # ✅ DEBUG PRINT (TEMPORARY)
        print("DESCRIPTION:", notice.description)

        # 🔥 AUTO PRIORITY CLASSIFICATION
        notice.priority = classify_priority(notice.description)

        print("PRIORITY SET TO:", notice.priority)

        notice.save()
        return super().form_valid(form)


class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notice/update_notice.html'

    def get_success_url(self):
        return reverse_lazy('notice:notice_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        obj = self.get_object()
        # allow editing if posted_by or staff/superuser
        return (self.request.user == obj.posted_by) or self.request.user.is_staff

    def form_valid(self, form):
        notice = form.save(commit=False)
        # re-run AI prediction on update
        try:
            combined = f"{notice.title} {notice.description}"
            notice.category = predict_category(combined)
        except Exception:
            pass
        notice.save()
        messages.success(self.request, "Notice updated successfully.")
        return super().form_valid(form)

class NoticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notice
    template_name = 'notice/confirm_delete.html'
    success_url = reverse_lazy('notice:notice_list')

    def test_func(self):
        obj = self.get_object()
        return (self.request.user == obj.posted_by) or self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        # Soft delete: mark inactive
        obj = self.get_object()
        obj.is_active = False
        obj.save()
        messages.success(request, "Notice archived.")
        return super().post(request, *args, **kwargs)
    
    
    
    
