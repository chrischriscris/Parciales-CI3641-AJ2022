"""Módulo que implementa el método de asignación de memoria Buddy Allocator
CI3641 - Lenguajes de Programación I
Pregunta 3

Christopher Gómez (c) 2022
"""
from __future__ import annotations

from math import ceil, log2


class Block:
    '''Implementación de bloque de memoria de Buddy System.

    Atributos:
        start: Dirección donde comienza el bloque.
        size: Tamaño del bloque.
        bucket: Índice del bloque en caso de estar en la lista
            de bloque libres.
    '''
    def __init__(self: Block, start: int, size: int):
        self.start = start
        self.size = size
        self.bucket = ceil(log2(size))

    def __str__(self: BuddyAllocator) -> str:
        if self.size == 1:
            return f'[{self.start}]'
        return f'[{self.start} - {self.start + self.size-1}]'
    
    def __repr__(self: BuddyAllocator) -> str:
        return self.__str__()


class BuddyAllocator:
    '''Clase que implementa el Buddy System como método de asignación de
    memoria.
    
    Atributos:
        n: Número de listas de bloques libres que maneja el sistema.
        free_blocks: Lista bloques libres, el elemento i-ésimo contiene
            los bloques libres de tamaño 2^i.
        blocks_map: Diccionario que lleva cuenta de los bloques asignados
            por su identificador.
    Argumentos:
        size: Tamaño de la memoria.
    '''
    def __init__(self: BuddyAllocator, size: int):
        if (not isinstance(size, int)      # Entero
            or size & (size-1) or not size # Potencia de base 2
            or size < 1                    # Positivo
        ):
            raise ValueError("El número de bloques deber ser una potencia de "
                "base 2 positiva")
        
        self.n = ceil(log2(size)) + 1
        self.free_blocks = [[] for _ in range(self.n)]
        self.blocks_map = {}

        # Al comienzo solo está libre un bloque de tamaño
        # maximal que ocupa toda la memoria
        self.free_blocks[self.n - 1].append(Block(0, size))

    def allocate(self: BuddyAllocator, name: str, size: int) -> int:
        '''Asigna un bloque de memoria de tamaño [size] con el identificador
        [name].
        
        Retorna:
            - 0 si la operación fue exitosa.
            - 1 si no hay suficiente memoria libre.
            - 2 si ya existe un bloque con el identificador [name].
        '''
        if name in self.blocks_map:
            return 2
        
        # Buscamos el indice del bloque que se necesita
        needed = ceil(log2(size))
        n = needed
        
        if n >= self.n:
            return 1

        # Si hay memoria disponible directamente en el bucket
        if self.free_blocks[n]:
            # Se elimina el primer bloque libre de la lista de bloques libres
            block = self.free_blocks[n].pop(0)

            # Se añade a la tabla de bloques ocupados
            self.blocks_map[name] = block
            return 0

        for i in range(n+1, self.n):
            # El primero con suficiente tamaño
            if self.free_blocks[i]:
                n = i
                break
        else:
            # No hay ningún bloque libre de tamaño suficiente
            return 1

        # Se elimina de la lista de bloques libres
        temp = self.free_blocks[n].pop(0)

        # Se recorta el bloque
        for i in range(n-1, needed-1, -1):
            # Divide el bloque en dos mitades
            new_size = temp.size // 2

            new_block1 = Block(temp.start, new_size)
            new_block2 = Block(temp.start + new_size, new_size)

            # Se añaden a la lista de bloques libres
            self.free_blocks[i].append(new_block1)
            self.free_blocks[i].append(new_block2)

            # Se elimina el bloque de la lista de bloques libres
            # Para seguir partiéndolo en la próxima iteración
            temp = self.free_blocks[i].pop(0)

        # Se añade a la tabla de bloques ocupados
        self.blocks_map[name] = temp
        
        return 0

    def free(self: BuddyAllocator, name: str) -> bool:
        '''Libera el bloque de memoria con el identificador [name].

        Retorna:
            - True si la operación fue exitosa.
            - False si no existe un bloque con el identificador [name].
        '''
        if name not in self.blocks_map:
            return False

        block = self.blocks_map[name]

        # Se añade a la lista de bloques libres
        self.free_blocks[block.bucket].append(block)
        del self.blocks_map[name]

        # Se mezclan los bloques con su buddy mientra esté libre
        temp = self.coalesce(block)
        while temp != block:
            block, temp = temp, self.coalesce(temp)

        return True

    def coalesce(self: BuddyAllocator, block: Block) -> bool:
        '''Fusiona [block] con su buddy si este está libre.
        
        Retorna:
            - El nuevo bloque si se fusionó exitosamente
            - El mismo bloque si no se hizo fusión
        '''
        # Se calcula el bloque donde está el buddy y la dirección
        # donde comienza, para buscar si está disponible
        n = block.start // block.size
        a = block.start + block.size * (-1 if n % 2 else 1)

        # Busca el buddy en la lista
        for i, b in enumerate(self.free_blocks[block.bucket]):
            if b.start == a:
                # Saca los dos bloques de la lista y los mezcla
                self.free_blocks[block.bucket].pop(i)
                if (self.free_blocks[block.bucket].pop() != block):
                    raise Exception("Error al mezclar los bloques")

                # Se crea el nuevo bloque y se coloca en el siguiente bucket
                m = min(a, block.start)
                merged_block = Block(m, 2*block.size)
                self.free_blocks[block.bucket + 1].append(merged_block)

                return merged_block
        return block


    def __str__(self: BuddyAllocator) -> str:
        strbuilder = []
        if any(self.free_blocks):
            strbuilder.append("=" * 30)
            strbuilder.append("Lista de bloques libres:\n")
            for i, block_list in enumerate(self.free_blocks):
                if block_list:
                    strbuilder.append(f"Tamaño {2**i}:")
                    for block in block_list:
                        strbuilder.append(f"\t{block}")

        if self.blocks_map:
            strbuilder.append("=" * 30)
            strbuilder.append("Bloques reservados:\n")
            for name, block in self.blocks_map.items():
                strbuilder.append(f"<{name}>\n\t{block}")

        strbuilder.append("=" * 30)
        return '\n'.join(strbuilder)