import unittest


class McpTestCase(unittest.TestCase):

    def setUp(self):
        print(f"\n### starting {unittest.TestCase.id(self)}")

    def tearDown(self):
        print(f"\n### ending {unittest.TestCase.id(self)}")
