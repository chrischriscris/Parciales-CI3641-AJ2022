import os
from cmd import Cmd
from textwrap import dedent
from typing import Union

from tdiagram.Machine import Machine


class MachineREPL(Cmd):
    """REPL del simulador de Máquina.
    
    Atributos:
        vm: Instancia que implementa una máquina con programas,
            intérpretes y compiladores.
    """
    # Mensajes de la REPL
    prompt = f'Machine Simulator > '
    intro = (f'Machine Simulator v1.0\n'
        'Utiliza "?" para mostrar los comandos disponibles.')
    doc_header = ('''Lista de comandos basicos (escribe 'help <nombre>' '''
        'para informacion detallada)')
    misc_header = ('''Lista de funciones disponibles (escribe 'help '''
        '''<nombre>' para informacion detallada)''')

    def __init__(self):
        # Llama el constructor de la superclase e inicializa la máquina virtual
        Cmd.__init__(self)
        self.vm = Machine()

    # ---------- COMANDOS DE DOCUMENTACION DE COMANDOS EN REPL ----------
    def help_EJECUTABLE(self):
        print(dedent('''
            EJECUTABLE <nombre>

            Representa una consulta de la posibilidad de ejecutar el programa de nombre
            <nombre>.

            Reporta un error e ignorar la acción si <nombre> no tiene un
            programa asociado.
            '''))

    def help_LIBERAR(self):
        print(dedent('''
            DEFINIR <tipo> [<argumentos>]

            Representa una definición de clase <tipo> con <argumentos>, que son:

            PROGRAMA <nombre> <lenguaje>
            Representa a un programa identificado por <nombre> escrito en <lenguaje>.
            
            INTERPRETE <lenguaje_base> <lenguaje>
            Representa a un intérprete para <lenguaje> escrito en <lenguaje_base>.
            
            TRADUCTOR <lenguaje_base> <lenguaje_origen> <lenguaje_destino>
            Representa a un traductor, desde <lenguaje_origen> hacia <lenguaje_destino>,
            escrito en <lenguaje_base>.
            
            Todos los lenguajes deben ser cadenas alfanuméricas

            Reporta un error e ignorar la acción si <nombre> ya tiene un
            programa asociado, en el caso de programas.
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
                super(MachineREPL, self).cmdloop(intro='')
                break
            except KeyboardInterrupt:
                return True

    def do_EJECUTABLE(self, line):
        ''' Extrae la información del comando, los valida, llama al
        método correspondiente de Machine y reporta el resultado.
        '''
        args = line.split()
        # Solo dos argumentos
        if len(args) != 1:
            return print("Uso: EJECUTABLE <nombre> <programa>, use el "
                "comando help o ? para más información")

        try:
            if self.vm.is_executable(args[0]):
                print(f"Si, es posible ejecutar el programa '{args[0]}'")
            else:
                print(f"No es posible ejecutar el programa '{args[0]}'")
        except ValueError:
            return self.print_error(f"El programa '{args[0]}' no existe en "
                "la máquina.")

    def do_DEFINIR(self, line):
        ''' Extrae la información del comando, los valida, llama al
        método correspondiente de Machine y reporta el resultado.
        '''
        args = line.split()
        # Solo dos argumentos
        if len(args) not in [3, 4]:
            return print("Uso: DEFINIR <tipo> [<argumentos>], use el comando "
                "help o ? para más información")

        try:
            if args[0] == 'PROGRAMA':
                if len(args) != 3:
                    return print("Uso: DEFINIR PROGRAMA <nombre> <lenguage>, "
                        "use el comando help o ? para más información")

                self.vm.add_program(args[1], args[2])
                print(f"Se definió el programa '{args[1]}', ejecutable en '{args[2]}'")

            elif args[0] == 'TRADUCTOR':
                if len(args) != 4:
                    return print("Uso: DEFINIR TRADUCTOR <lenguaje_base> <lenguage_origen> "
                        "<lenguaje_destino>, use el comando help o ? para más información")

                self.vm.add_compiler(args[2], args[3], args[1])
                print(f"Se definió un traductor de '{args[2]}' hacia '{args[3]}', escrito en '{args[1]}'")

            elif args[0] == 'INTERPRETE':
                if len(args) != 3:
                    return print("Uso: DEFINIR INTERPRETE <lenguaje_base> <lenguage>, "
                        "use el comando help o ? para más información")

                self.vm.add_interpreter(args[2], args[1])
                print(f"Se definió un intérprete para '{args[2]}', escrito en '{args[1]}'")
            else:
                return print("Uso: DEFINIR <tipo> [<argumentos>], use el comando"
                    "help o ? para más información")
        except ValueError:
            self.print_error("El nombre del lenguaje debe ser una cadena "
                "de caracteres alfanuméricos")

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

    def print_error(self, cause):
        print(f"\033[1m\033[91mERROR: \033[0m{cause}")
