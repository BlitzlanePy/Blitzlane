import asyncio
import unittest

async def my_func():
    await asyncio.sleep(0.1)
    print("my_func")
    return True

class TestStuff(unittest.IsolatedAsyncioTestCase):

    async def test_my_func(self):
        r = await my_func()
        self.assertTrue(r)
