saldo_conta = 0
print('==='*35)
print('>>> CAIXA ELETRÔNICO <<<')
print('==='*35)

print('DADOS DO CLIENTE')
print('-=-'*35)

nome = str(input('Digite o seu nome: '))
print('---'*35)
cpf = int(input('Digite o seu CPF: '))
print('---'*35)

print('Seu saldo no momento, está zerado.')
deposito = float(input('Quanto você deseja depositar? R$'))
saldo_conta = deposito
print('-=-'*35)
print(f'Você depositou a quantia de R${deposito:.2f}')  
print('-=-'*35)
print(' --- SAQUES ---')
print('-=-'*35)
sacar = float(input('Quanto você quer sacar? R$'))
if sacar <= saldo_conta:
    saldo_conta -= sacar
    valor = int(sacar)
    notas = [200, 100, 50, 20, 10, 5]
    quantidade_notas = {}
    
    for nota in notas:
        if valor >= nota:
            quantidade = valor // nota
            quantidade_notas[nota] = quantidade
            valor -= quantidade * nota
    print('---'*35)
    print(f'Você sacou R${sacar:.2f} e seu saldo atual é: R${saldo_conta:.2f}') 
    print('Notas fornecidas:')
    for nota, quantidade in quantidade_notas.items():
        print(f'{quantidade}x Nota(s) de {nota}')
else:
    print('Saldo insuficiente, por favor tente novamente!')

print('==='*35)
print('>>> FIM DA EXECUÇÃO DO ALGORITMO <<<')