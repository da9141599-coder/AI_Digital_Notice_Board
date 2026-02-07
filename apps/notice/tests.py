from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Notice
from django.utils import timezone

class NoticeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass12345')
        self.notice = Notice.objects.create(
            title='Test Notice',
            description='Testing notice creation',
            posted_by=self.user,
            publish_date=timezone.now()
        )

    def test_notice_str(self):
        self.assertIn('Test Notice', str(self.notice))

class NoticeViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass12345')
        self.client.login(username='tester', password='pass12345')

    def test_create_notice_view(self):
        url = reverse('notice:create_notice')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_list_view(self):
        url = reverse('notice:notice_list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
