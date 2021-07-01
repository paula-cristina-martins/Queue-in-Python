from datetime import datetime

class Queue:

    def __init__(self, limite_max=5):
        self.fila_cliente = []
        self.notas_atendimento = []
        self.limite_max = limite_max
        self.hora_inicio = datetime.now()
        self.hora_final = datetime.now()

    def push(self, nome_cliente):
        if len(self.fila_cliente) < self.limite_max:

            inicio = datetime.now()
            self.hora_inicio = inicio

            cliente = {
                'Nome do Cliente': nome_cliente,
                'Horário de Entrada': inicio
            }
            self.fila_cliente.append(cliente)

            return len(self.fila_cliente)

        else:
            print("Limite máximo atingido!")
            return None

    def validacao_fila(self):
        if self.fila_cliente == []:
            print(
                f'No momento todas as filas de atendimento estão lotadas, por favor, aguarde um momento!')
        else:
            print(
                "\n\n-> Relação de clientes aguardando na fila................................: ")
            for idx, informacao in enumerate(self.fila_cliente):
                print(
                    f"Cliente {informacao['Nome do Cliente']} entrou às {informacao['Horário de Entrada']} e está na posição {idx+1} da fila.")

    def pop(self, nota_atendimento, nota_tempo_esperado):
        if self.fila_cliente == []:
            print("Fila Vazia!")
            return None

        else:
            final = datetime.now()
            self.hora_final = final
            cliente = self.fila_cliente.pop(0)

            cliente['Horário de Saída'] = final
            cliente['Nota Atendimento'] = nota_atendimento
            cliente['Nota Tempo Espera'] = nota_tempo_esperado

            print(
                f"\n\nATENDIMENTO FINALIZADO p/ {cliente['Nome do Cliente']}!!!")
            print(f"\n-> Informações sobre o atendimento............:")
            print("Nome do Cliente...............................:",
                  cliente['Nome do Cliente'])
            print("Horário de Entrada............................:",
                  cliente['Horário de Entrada'])
            print("Horário de Saída..............................:",
                  cliente['Horário de Saída'])
            print("Tempo esperado de atendimento.................:",
                  cliente['Horário de Saída'] - cliente['Horário de Entrada'])
            print("Nota em relação ao atendimento................:",
                  cliente['Nota Atendimento'])
            print("Nota em relação ao tempo aguardado............:",
                  cliente['Nota Tempo Espera'])
            return cliente
