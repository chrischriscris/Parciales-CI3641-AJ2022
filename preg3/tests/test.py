import unittest
from balloc.BuddyAllocator import BuddyAllocator

class TestBuddyAllocator(unittest.TestCase):
    def setUp(self):
        self.allocator = BuddyAllocator(16)
    def test_allocation():
        pass