from django.test import TransactionTestCase

class TestIt(TransactionTestCase):
   serialized_rollback = True

   def test_one(self):
       self.assertTrue(True)

   def test_two(self):
       self.assertTrue(True)
