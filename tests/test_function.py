from unittest import TestCase

from functions import my_sum

class TestFunctions(TestCase):

    def test_equality(self):
        self.assertEqual(1,1)

#    def test_failure(self):
#        self.assertEqual(0,1)

    def text_in(self):
        l = [i for i in range(5)]
        self.assertIn(4,l)
        self.assertNotIn(5,l)

    def test_my_sum(self):
        result = my_sum(5, 10 ,15)
        self.assertEqual(result,30)
        result = my_sum()
        self.assertEqual(result, 0)
        result = my_sum(-20,-40, 10)
        self.assertEqual(result, -50)
        with self.assertRaises(TypeError):
            my_sum("hello")