from __future__ import annotations
from networkx import Graph, has_path, to_dict_of_dicts

class Machine():
    def __init__(self):
        self.programs = {}
        self.compilers = {}
        self.enviroment = Graph
        self.enviroment.add_node('LOCAL')

    def add_languages(self, *args: str):
        for lang in args:
            if not lang.isalnum():
                raise ValueError('El nombre del lenguaje debe ser una cadena '
                    'de caracteres alfanuméricos')
            self.enviroment.add_node(lang)

    def add_program(self, name: str, written_in: str):
        self.programs[name] = written_in
        self.add_languages(written_in)

    def add_compiler(self, src: str, dest: str, written_in: str):
        self.add_languages(src, dest, written_in)

        # Si se puede llegar del lenguaje en que está escrito
        # el compilador a local, se puede ejecutar el compilador
        if has_path(self.enviroment, src, 'LOCAL'):
            return self.enviroment.add_edge(src, dest)
        self.compilers[src] = (dest, written_in)

    def add_interpreter(self, interprets: str, written_in: str):
        # Se añaden los lenguajes al entorno, y un lado entre
        # el lenguaje interpretado y el lenguaje que interpreta
        self.add_languages(interprets, written_in)
        self.enviroment.add_edge(interprets, written_in)

    def is_executable(self, program: str) -> bool:
        if program not in self.programs:
            raise ValueError(f'El programa "{program}" no existe en la máquina.')

        if has_path(self.enviroment, program, 'LOCAL'):
            return True
        return False

    def __str__(self) -> str:
        return (f'Programs:\n'
            '{self.programs}\n'
            'Compilers:\n'
            '{self.compilers}\n'
            'Enviroment:\n'
            f'{to_dict_of_dicts(self.enviroment)}'
        )


def main():
    m = Machine()
    m.add_program('fibonacci', 'LOCAL')
    print(m.is_executable('fibonacci'))
    m.add_program('factorial', 'Java')
    print(m.is_executable('factorial'))
    m.add_interpreter('Java', 'C')
    m.add_compiler('Java', 'C', 'C')
    print(m.is_executable('factorial'))
    m.add_interpreter('C', 'LOCAL')
    print(m.is_executable('factorial'))
    print(m)

if __name__ == '__main__':
    main()