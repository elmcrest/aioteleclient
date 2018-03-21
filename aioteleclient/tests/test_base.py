import unittest
from aioteleclient import TelegramClient


class BaseTest(unittest.TestCase):
    def test_travis(self):
        client = TelegramClient()
        self.assertTrue(client.test)
