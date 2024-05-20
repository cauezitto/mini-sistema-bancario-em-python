menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
extrato = ''''''
numero_de_saques=0
LIMITE_SAQUES = 3
LIMITE = 500

PERGUNTA_VALOR_DEPOSITO = 'Qual valor deseja depositar? '
PERGUNTA_VALOR_SAQUE = 'Qual valor deseja sacar? '
MENSAGEM_LIMITE_DEPOSITO_REALIZADO = 'Seu deposito foi realizado com sucesso!'
MENSAGEM_FINALIZA_SESSAO = 'Sessão finalizada até mais!'

MENSAGEM_EXTRATO_VAZIO = '\nAinda não foram realizadas movimentações na conta!\n'

MENSAGEM_ERRO_LIMITE_DE_SAQUES_ATINGIDO = '''
Ops... parece que você já atingiu seu limite de saques diario! Por favor tente novamente amanhã

'''

MENSAGEM_ERRO_LIMITE_VALOR_POR_SAQUE = '''
Você só pode sacar R$500.00 por operação!

'''

MENSAGEM_ERRO_VALOR_NEGATIVO = '''
OPERAÇÃO ABORTADA!!!
O valor do deposito precisa ser um numero inteiro positivo!

'''
MENSAGEM_ERRO_VALOR_NAO_NUMERICO = '''
OPERAÇÃO ABORTADA!!!
Por favor digite apenas valores numericos nas operacoes de deposito e saque.

'''

MENSAGEM_ERRO_SALDO_INSUFICIENTE = '''
OPERAÇÃO ABORTADA!!!
Você não tem saldo suficiente para realizar este saque.

'''
#As variaveis estaticas contendo o identificador DINAMICA abaixo devem ser usadas com .format() hidratando os valores dinamicos na string
#Exemplo: print(MENSAGEM_DINAMICA_SUCESSO_DEPOSITO.format(saldo=saldo))
MENSAGEM_DINAMICA_SUCESSO_DEPOSITO = 'Deposito efetuado com sucesso! Seu atual saldo é de: R${saldo}'
MENSAGEM_DINAMICA_SUCESSO_SAQUE = 'Saque efetuado com sucesso! Seu saldo atual é de: R${saldo} e você tem um limite de {limite_de_saques_disponivel} saque(s) disponivel para hoje.'
MENSAGEM_ERRO_OPCAO_INVALIDA = '''
Não foi possível processar sua solicitação. Por favor digite uma opção válida!

'''

LOG_EXTRATO_SAQUE = 'SAQUE REALIZADO NO VALOR DE R${valor_saque}. Saldo atual de: R${saldo}\n\n'
LOG_EXTRATO_DEPOSITO = 'DEPOSITO REALIZADO NO VALOR DE R${valor_deposito}. Saldo atual de: R${saldo}\n\n'

while True:
    opcao = input(menu).lower()

    #OPERACAO DE DEPOSITO
    if opcao == 'd':
        valor_depositado =  input(PERGUNTA_VALOR_DEPOSITO)
        valor_depositado_float = 0
        try:
            valor_depositado_float = float(valor_depositado)
        except:
            print(MENSAGEM_ERRO_VALOR_NAO_NUMERICO)
            continue
        if(valor_depositado_float > 0):
            saldo += valor_depositado_float
            extrato += LOG_EXTRATO_DEPOSITO.format(valor_deposito=f'{valor_depositado_float:.2f}', saldo=f'{saldo:.2f}')
            print(MENSAGEM_DINAMICA_SUCESSO_DEPOSITO.format(saldo=f'{saldo:.2f}'))
        else:
            print(MENSAGEM_ERRO_VALOR_NEGATIVO)
    #FIM OPERACAO DE DEPOSITO

    #OPERACAO DE SAQUE
    elif opcao == 's':
        if numero_de_saques >= LIMITE_SAQUES:
            print(MENSAGEM_ERRO_LIMITE_DE_SAQUES_ATINGIDO)
            continue

        valor_sacado =  input(PERGUNTA_VALOR_SAQUE)
        valor_sacado_float = 0
        try:
            valor_sacado_float = float(valor_sacado)
        except:
            print(MENSAGEM_ERRO_VALOR_NAO_NUMERICO)
            continue
        if valor_sacado_float < 1:
            print(MENSAGEM_ERRO_VALOR_NEGATIVO)
        elif saldo < valor_sacado_float:
            print(MENSAGEM_ERRO_SALDO_INSUFICIENTE)
        elif LIMITE < valor_sacado_float:
            print(MENSAGEM_ERRO_LIMITE_VALOR_POR_SAQUE)
        elif numero_de_saques < LIMITE_SAQUES:
            saldo -= valor_sacado_float
            numero_de_saques += 1
            extrato += LOG_EXTRATO_SAQUE.format(valor_saque=f'{valor_sacado_float:.2f}', saldo=f'{saldo:.2f}')
            print(MENSAGEM_DINAMICA_SUCESSO_SAQUE.format(saldo=f'{saldo:.2f}', limite_de_saques_disponivel = LIMITE_SAQUES - numero_de_saques))
        #FIM OPERACAO DE SAQUE

    elif opcao == 'e':
        print('\n################ EXTRATO ################\n')
        print(MENSAGEM_EXTRATO_VAZIO if not extrato else extrato)
        print('################ EXTRATO ################')
    elif opcao == 'q':
        print(MENSAGEM_FINALIZA_SESSAO)
        break

    else:
        print(MENSAGEM_ERRO_OPCAO_INVALIDA)