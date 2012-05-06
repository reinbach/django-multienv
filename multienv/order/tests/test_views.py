import unittest

from django.test.contrib import Client

#===============================================================================
class TestOrderViews(unittest.TestCase):

    #---------------------------------------------------------------------------
    def setUp(self):
        self.client = Client()

    #---------------------------------------------------------------------------
    def test_order_home(self):
        self.client.get(reverse('order_home'))