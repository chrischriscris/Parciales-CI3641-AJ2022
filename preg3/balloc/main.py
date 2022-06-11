from BuddyAllocator import *
from random import randint

def main():
    allocate = [4, 4, 4, 4]
    names = [f"bloque {randint(0, 10000)}" for _ in allocate]
    free_order = [1, 2, 3, 0]
    allocator = BuddyAllocator(16)
    
    for name, size in zip(names, allocate):
        print(f'Asignando {size} bloques con el nombre "{name}"')
        allocator.allocate(name, size)
        print(allocator)
        print("\n")
    
    for i in free_order:
        print(f'Liberando bloque de nombre "{names[i]}"')
        allocator.free(names[i])
        print(allocator)
        print("\n")

if __name__ == '__main__':
    main()