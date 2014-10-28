from django.test import LiveServerTestCase

class TestIt(LiveServerTestCase):
   serialized_rollback = True

   def test_one(self):
       self.assertTrue(True)

   def test_two(self):
       self.assertTrue(True)
