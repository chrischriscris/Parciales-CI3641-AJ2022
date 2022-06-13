"""Módulo que implementa una máquina con programas, compiladores e intérpretes.
CI3641 - Lenguajes de Programación I
Pregunta 5

Christopher Gómez (c) 2022
"""
from __future__ import annotations

class Digraph():
    '''Clase que implementa un grafo dirigido como mapa de adyacencias
    y lados que no se repiten, soporta las operaciones de añadir nodo,
    añadir lado y halla un camino entre un par de nodos.
    '''
    def __init__(self, *args):
        self.adj = {}
        for node in args:
            self.add_node(node)

    def add_node(self, node: str):
        '''Añade un nodo nuevo al grafo.'''
        if node not in self.adj:
            self.adj[node] = set()

    def add_edge(self, node1: str, node2: str):
        '''Añade un arco nuevo al grafo, de [node1] a [node2].'''
        self.adj[node1].add(node2)

    def has_path(self, _from: str, to: str) -> bool:
        '''Retorna un booleano indicando si existe n camino de [_from] a [to]'''
        if _from == to:
            return True

        queue = [_from]
        visited = set()
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                for v in self.adj[node]:
                    if v == to:
                        return True
                    queue.append(v)
        return False

    def __str__(self):
        strbuilder = []
        for u, v in self.adj.items():
            strbuilder.append(f'[{u}] -> {v}')
        return '\n'.join(strbuilder)

class Machine():
    '''Clase que simula una máquina en la que se descargan programas,
    compiladores e intérpretes.
    
    Atributos:
        programs: Diccionario que relaciona los nombres de los programas
            con el lenguaje en que se escribe.
        compilers: Lista de tripletas (fuente, destino, escrito_en) que
            representan los compiladores que no se pueden ejecutar.
        compilers_set: Conjunto de tripletas (fuente, destino, escrito_en) que
            representan los compiladores que no se pueden ejecutar.
        env: Digrafo de dependencias del entorno computacional, donde la relación
            a -> b indica que el lenguaje a se pude interpretar/compilar a b.
    Argumentos:
        size: Tamaño de la memoria.
    '''
    def __init__(self):
        self.programs = {}
        self.compilers = []
        self.compilers_set = set()
        self.env = Digraph('LOCAL')

    def add_languages(self, *args: str):
        '''Añade lenguajes de programación a la máquina.'''
        for lang in args:
            if not lang.isalnum():
                raise ValueError('El nombre del lenguaje debe ser una cadena '
                    'de caracteres alfanuméricos')
            self.env.add_node(lang)

    def add_program(self, name: str, written_in: str):
        '''Añade um programa a la máquina.'''
        if name not in self.programs:
            self.programs[name] = []
        if written_in not in self.programs[name]:
            self.programs[name].append(written_in)
        self.add_languages(written_in)

    def add_compiler(self, src: str, dest: str, written_in: str):
        '''Añade un compilador la máquina.'''
        self.add_languages(src, dest, written_in)

        # Si se puede llegar del lenguaje en que está escrito
        # el compilador a local, se puede ejecutar el compilador
        if self.env.has_path(src, 'LOCAL'):
            return self.env.add_edge(src, dest)
        
        compiler = (src, dest, written_in)
        self.compilers.append(compiler)
        self.compilers_set.add(compiler)

    def add_interpreter(self, interprets: str, written_in: str):
        '''Añade un intérprete la máquina.'''
        # Se añaden los lenguajes al entorno, y un lado entre
        # el lenguaje interpretado y el lenguaje que interpreta
        self.add_languages(interprets, written_in)
        self.env.add_edge(interprets, written_in)

    def update_dependencies(self):
        '''Actualiza las dependencias de la máquina.'''
        for compiler in self.compilers:
            src, dest, written_in = compiler
            if self.env.has_path(written_in, 'LOCAL'):
                self.env.add_edge(src, dest)
                self.compilers.remove(compiler)
                self.update_dependencies()

    def is_executable(self, program: str) -> bool:
        '''Retorna un booleano indicando si un determinado programa es
        ejecutable en la máquina en su estado actual..'''
        if program not in self.programs:
            raise ValueError(f'El programa "{program}" no existe en la máquina.')

        self.update_dependencies()
        for language in self.programs[program]:
            if self.env.has_path(language, 'LOCAL'):
                return True
        return False

    def __str__(self) -> str:
        return (f'Programas:\n'
            f'{self.programs}\n'
            'Compiladores que no corren:\n'
            f'{self.compilers}\n'
            'Entorno:\n'
            f'{self.env}')