import unittest
from random import randint
from balloc.BuddyAllocator import BuddyAllocator

class TestBuddyInitialization(unittest.TestCase):
    def test_empty_allocator(self):
        self.assertRaises(ValueError, BuddyAllocator, 0)
    
    def test_not_powers_of_two(self):
        for n in range(1025):
            if n & (n-1) or not n:
                self.assertRaises(ValueError, BuddyAllocator, n)

    def test_not_integer(self):
        self.assertRaises(ValueError, BuddyAllocator, 1.0)
        self.assertRaises(ValueError, BuddyAllocator, 2.5)
        self.assertRaises(ValueError, BuddyAllocator, 'nice')

class TestBuddyAllocator(unittest.TestCase):

    def test_allocate_and_empty_allocator(self):
        self.allocator = BuddyAllocator(16)

        allocate = [4, 4, 4, 4]
        names = [f"bloque {randint(0, 10000)}" for _ in allocate]
        free_order = [1, 2, 3, 0]
        
        for name, size in zip(names, allocate):
            self.assertEquals(
                self.allocator.allocate(name, size),
                0
            )
        
        for i in free_order:
            self.assertEquals(
                self.allocator.free(names[i]),
                True
            )

        self.assertDictEqual(self.allocator.blocks_map, {})

if __name__ == '__main__':
    unittest.main()