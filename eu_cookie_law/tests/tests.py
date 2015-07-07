from django.core.urlresolvers import reverse
from django.test import TestCase


class ContextProcessorTests(TestCase):

    def test_no_cookie_at_start(self):
        r = self.client.get('/')
        self.assertEqual(r.client.cookies.items(), [])

    def test_cookie_after_post(self):
        self.client.post(reverse('hide_cookie_message'))
        r = self.client.get('/')
        self.assertEqual(r.client.cookies.keys(), ['cookie_message'])
