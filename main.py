from Queue import Queue

clientes = Queue()

print("\nBoas Vindas ao nosso sistema online de atendimento ao cliente!\n")

quantidade = int(input("Quantos clientes há na fila? "))

if (quantidade > 5):
    print("\nLimite máximo atingido!\n")
else:
    for i in range(quantidade):
        cliente = input(
            'Insira seu nome para informarmos o código do seu atendimento...: ')
        clientes.push(cliente)

    clientes.validacao_fila()

    for i in range(quantidade):
        nota_atendimento = int(input('\nIremos encerrar o atendimento. \n->Insira sua nota sobre o atendente: '))
        nota_tempo_espera = int(input('->Insira sua nota para o tempo de espera: '))
        clientes.pop(nota_atendimento, nota_tempo_espera)
