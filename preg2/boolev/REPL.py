import os
from cmd import Cmd
from textwrap import dedent
from typing import Union

from boolev.BooleanEvaluator import BooleanEvaluator

class BooleanEvaluatorREPL(Cmd):
    """REPL de BooleanEvaluator.
    
    Atributos:
        parser: Instancia que implementa el BooleanEvaluator.
    """
    # Mensajes de la REPL
    prompt = f'\033[1;32mBooleanEvaluator> \033[0m'
    intro = (f'BooleanEvaluator v1.0\n'
        'Utiliza "?" para mostrar los comandos disponibles.')
    doc_header = ('''Lista de comandos basicos (escribe 'help <nombre>' '''
        'para informacion detallada)')
    misc_header = ('''Lista de funciones disponibles (escribe 'help '''
        '''<nombre>' para informacion detallada)''')

    def __init__(self):
        # Llama el constructor de la superclase e inicializa la máquina virtual
        Cmd.__init__(self)
        self.parser = BooleanEvaluator()

    # ---------- COMANDOS DE DOCUMENTACION DE COMANDOS EN REPL ----------
    def help_EVAL(self):
        print(dedent('''
            EVAL <orden> <expr>

            Evalúa la expresión booleana dada, escrita de acuerdo a <orden>,
            que puede ser PRE o POST (para expresiones prefijas y posfijas,
            respectivamente).

            Reporta error si la expresión no es válida.
            '''))

    def help_MOSTRAR(self):
        print(dedent('''
            MOSTRAR <orden> <expr>

            Imprime en orden infijo la expresión dada, escrita de acuerdo a
            <orden>, que puede ser PRE o POST (para expresiones prefijas y
            posfijas, respectivamente).

            Reporta error si la expresión no es válida.
            '''))

    def help_SALIR(self):
        print(dedent('''
            SALIR

            Finaliza la sesión del evaluador.
            '''))

    # -------------- MÉTODOS SUPERCLASE CUSTOMIZADOS --------------
    def cmdloop(self, intro=None):
        """Ver clase base. Agrega manejo de interrupciones del teclado."""
        print(self.intro)
        while True:
            try:
                super(BooleanEvaluatorREPL, self).cmdloop(intro='')
                break
            except KeyboardInterrupt:
                return True

    def do_EVAL(self, line):
        ''' Extrae la información del comando, y llama al método
        correspondiente del BooleanEvaluator, reportando el resultado.
        '''
        args = line.split()

        if len(args) < 2:
            return print("Uso: MOSTRAR [<orden>] <expr>.\nUtilice el comando "
                "help o escriba ? ver la lista de comandos.")

        try:
            if args[0] == "PRE":
                del args[0]
                expr = ' '.join(args)
                res = self.parser.evaluate(expr, True)
            elif args[0] == "POST":
                del args[0]
                expr = ' '.join(args)
                res = self.parser.evaluate(expr)
            else:
                return print("Uso: MOSTRAR <orden> <expr>.\nUtilice el comando "
                    "help o escriba ? ver la lista de comandos.")
        except:
            return self.print_error("Expresión inválida.")

        self.print_ok(f'{res}')

    def do_MOSTRAR(self, line):
        ''' Extrae la información del comando, y llama al método
        correspondiente del BooleanEvaluator, reportando el resultado.
        '''
        args = line.split()

        if len(args) < 2:
            return print("Uso: MOSTRAR [<orden>] <expr>.\nUtilice el comando "
                "help o escriba ? ver la lista de comandos.")

        try:
            if args[0] == "PRE":
                del args[0]
                expr = ' '.join(args)
                res = self.parser.show(expr, True)
            elif args[0] == "POST":
                del args[0]
                expr = ' '.join(args)
                res = self.parser.show(expr)
            else:
                return print("Uso: MOSTRAR <orden> <expr>.\nUtilice el comando "
                    "help o escriba ? ver la lista de comandos.")
        except:
            return self.print_error("Expresión inválida.")

        self.print_ok(f'{res}')

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