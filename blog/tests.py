# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Post


class PostTests(TestCase):

    def test_str(self):
        test_title = Post(title='Test Title')
        self.assertEqual(str(test_title), 'Test Title')


