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

    def test_allocate(self):
        self.allocator = BuddyAllocator(16)

        allocate = [4, 4, 4, 4]
        names = [f"bloque {randint(0, 10000)}" for _ in allocate]
        free_order = [1, 2, 3, 0]
        
        for name, size in zip(names, allocate):
            self.assertEqual(
                self.allocator.allocate(name, size),
                0
            )
        
        for i in free_order:
            self.assertEqual(
                self.allocator.free(names[i]),
                True
            )
        # No hay ningún bloque asignado y la memoria solo tiene un bloque
        self.assertDictEqual(self.allocator.blocks_map, {})
        self.assertEqual(sum(1 for block in self.allocator.free_blocks if block), 1)

    def test_allocate2(self):
        self.allocator = BuddyAllocator(16)

        allocate = [1]*16
        names = [f"bloque {randint(0, 10000)}" for _ in allocate]
        free_order = [0, 2, 4, 6, 8, 10, 12, 14, 15, 13, 11, 9, 7, 5, 3, 1]
        
        for name, size in zip(names, allocate):
            self.assertEqual(
                self.allocator.allocate(name, size),
                0
            )
        
        for i in free_order:
            self.assertEqual(
                self.allocator.free(names[i]),
                True
            )
        
        # No hay ningún bloque asignado y la memoria solo tiene un bloque
        self.assertDictEqual(self.allocator.blocks_map, {})
        self.assertEqual(sum(1 for block in self.allocator.free_blocks if block), 1)

if __name__ == '__main__':
    unittest.main()