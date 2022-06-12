import os
from cmd import Cmd
from textwrap import dedent
from typing import Union

from preg5.tdiagram.DoesItRun import BuddyAllocator

class BuddySystemREPL(Cmd):
    """REPL del simulador de Buddy Allocation System.
    
    Atributos:
        allocator: Instancia que implemente el Buddy System.
    """
    # Mensajes de la REPL
    prompt = f'\033[1;32mBuddy System > \033[0m'
    intro = (f'Buddy Allocation Simulator v1.0\n'
        'Utiliza "?" para mostrar los comandos disponibles.')
    doc_header = ('''Lista de comandos basicos (escribe 'help <nombre>' '''
        'para informacion detallada)')
    misc_header = ('''Lista de funciones disponibles (escribe 'help '''
        '''<nombre>' para informacion detallada)''')

    def __init__(self, size: int):
        # Llama el constructor de la superclase e inicializa la máquina virtual
        Cmd.__init__(self)
        self.allocator = BuddyAllocator(size)

    # ---------- COMANDOS DE DOCUMENTACION DE COMANDOS EN REPL ----------
    def help_RESERVAR(self):
        print(dedent('''
            RESERVAR <nombre> <número de bloques>

            Intenta asignar la cantidad de memoria indicada, asociándolo
            al identificador dado.

            Reporta error e ignora la petición si ya hay un bloque asignado
            con el mismo identificador o si no existe un espacio libre lo
            suficientemente grande como para satisfacer la petición usando
            Buddy System.
            '''))

    def help_LIBERAR(self):
        print(dedent('''
            LIBERAR <nombre>

            Libera la memoria asignada al bloque con el identificador dado.

            Reporta error e ignora la petición si no existe un bloque asignado
            con el identificador.
            '''))
    
    def help_MOSTRAR(self):
        print(dedent('''
            MOSTRAR

            Muestra el estado actual de la memoria, mediante una representación
            textual de la lista de bloques libres y ocupados.
            '''))

    def help_SALIR(self):
        print(dedent('''
            SALIR

            Finaliza la sesión del simulador.
            '''))

    # -------------- MÉTODOS SUPERCLASE CUSTOMIZADOS --------------
    def cmdloop(self, intro=None):
        """Ver clase base. Agrega manejo de interrupciones del teclado."""
        print(self.intro)
        while True:
            try:
                super(BuddySystemREPL, self).cmdloop(intro='')
                break
            except KeyboardInterrupt:
                return True

    def do_RESERVAR(self, line):
        ''' Extrae la información del comando, los valida, llama al
        método correspondiente del BuddyAllocator y reporta el resultado.
        '''
        args = line.split()
        # Solo dos argumentos
        if len(args) != 2:
            return print("Uso: RESERVAR <nombre> <número de bloques>, use el"
                "comando help o ? para más información")

        # El número de bloques es un entero positivo
        try:
            size = int(args[1])
            if size < 1:
                raise ValueError
        except ValueError:
            return self.print_error("Debe insertar un número entero positivo "
                "como número de bloques.")

        res = self.allocator.allocate(args[0], size)
        if res == 0:
            self.print_ok(f'{size} bloques de memoria asignados con el '
                f'identificador "{args[0]}".')
        elif res == 1:
            self.print_error("No existe un bloque disponible para cumplir la."
                "petición")
        elif res == 2:
            self.print_error(f'Ya existe un bloque con el identificador "{args[0]}"')

    def do_LIBERAR(self, line):
        ''' Extrae la información del comando, los valida, llama al
        método correspondiente del BuddyAllocator y reporta el resultado.
        '''
        args = line.split()
        # Solo dos argumentos
        if len(args) != 1:
            return print("Uso: LIBERAR <nombre>, use el comando help o ? "
                "para más información")

        if self.allocator.free(args[0]):
            self.print_ok("Bloques de memoria asociados al identificador "
                f'"{args[0]}" liberados.')
        else:
            self.print_error(f'No existe un bloque con el identicador "{args[0]}".')

    def do_MOSTRAR(self, line):
        if line:
            return print("Uso: MOSTRAR, use el comando help o ? "
                "para más información")
        print(f"{self.allocator}")

    def do_SALIR(self, line) -> bool:
        return True

    def do_EOF(self, line) -> bool:
        print()
        return True

    def do_clear(self, line):
        command = 'clear'

        # Si el SO es Windows, cambia el comando
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    def emptyline(self) -> bool:
        return False

    def default(self, line) -> Union[bool, None]:
        if line == '.':
            return True
        print("Comando inválido. Utilice el comando help o escriba ? para ver "
            "la lista de comandos.")

    def print_ok(self, message):
        print(f"\33[96m\033[1mOK: \033[0m{message}")

    def print_error(self, cause):
        print(f"\033[1m\033[91mERROR: \033[0m{cause}")