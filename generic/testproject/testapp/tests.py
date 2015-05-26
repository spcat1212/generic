from django.test import TestCase

# Create your tests here.

from django.conf import settings



class TestYourModels(TestCase):


    def setUp(self):
        """
            Things that should happen before each test.
        """


    def test_that_will_run(self):
        """
            just make methods that start with "test_"
        """

        self.assertTrue(True != False)
