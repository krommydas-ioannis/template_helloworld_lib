import unittest

from template_helloworld_lib import tell_me_hello_world


class HelloWorldTestCase(unittest.TestCase):
    def test_tell_me_hello_world(self):
        self.assertEqual(tell_me_hello_world(), "Hello World!")


    def test_tell_me_hello_world_with_name(self):
        name = "Fritz"
        self.assertEqual(tell_me_hello_world(name), f"Hello World, {name}!")


    def test_hello_me_hello_world_not_equal(self):
        self.assertNotEqual(tell_me_hello_world(), "Hello")


if __name__ == '__main__':
    unittest.main(verbosity=2)
