from django.test import LiveServerTestCase
from mtestapp.models import SomeData

class TestIt(LiveServerTestCase):
   serialized_rollback = True

   def test_one(self):
       self.assertEqual(1, SomeData.objects.all().count())

   def test_two(self):
       self.assertEqual(1, SomeData.objects.all().count())
