def menu():
    print('-Escolha uma das opçõoes abaixo-')
    print()
    print('[1] - Inserção de famílias')
    print('[2] - Busca dos dados da família por CPF')
    print('[3] - Listagem de CPFs cadastrados')
    print('[4] - Listagem do dados das famílias')
    print('[5] - Listagem de dados consolidados')
    print('[6] - Criação de backup de redundância de dados')
    print('[7] - Sair do programa')

def inserção_de_familias():
    while True:
        renda=[]
        renda_total=0
        número_de_pessoas=int(input('Quantidade de membros da família: '))
        cpf=int(input('CPF do responsável da família: '))
        for p in range(1,número_de_pessoas+1):
            r=int(input(f'Renda mensal do {p}° membro:'))
            renda.append(r)
        for i in renda:
            renda_total+=i
        renda_media=renda_total/número_de_pessoas
        print(f'Renda média: {int(renda_media)}, Renda total: {renda_total} e Número de pessoas: {número_de_pessoas}')

        with open("analise.txt", "a") as file:
            
            file.write(f"{cpf} ")
            file.write(f"{número_de_pessoas} ")
            file.write(f"{renda_total} ")
            file.write(f"{renda_media:.0f} \n")

        resp=input('Deseja adicionar uma outra família? ').strip()
        if resp[0] not in 'Ss':
            break

def busca_cpf():
    cpf=input('Digite o CPF do responsável: ')
    cpf_encontrado=False
    with open('analise.txt','r') as file:
        for linha in file:
            dados=linha.split()
            if dados[0]==cpf:
                cpf_encontrado=True
                print(f'Renda total: {dados[2]}\nRenda média: {dados[3]}\nNúmero de indivíduos: {dados[1]}')
    if not cpf_encontrado:
        print('CPF não encontrado!')

def listagem_cpf():
    with open('analise.txt','r') as file:
        for line in file:
            dados=line.split()
            print(dados[0])

def listagem_dados():
    with open('analise.txt','r') as file:
        for line in file:
            dados=line.split()
            print(f'CPF: {dados[0]}',end=', ')
            print(f'Quantidade de membros da família: {dados[1]}',end=', ')
            print(f'Renda total: {dados[2]}', end=', ')
            print(f'Renda média: {dados[3]}')

def listagem_consolidada():
    with open('analise.txt','r') as file:
        cont_familia=0
        cont_renda_cidade=0
        cont_individuos=0
        inferior=0
        superior=0
        for linha in file:
            dados=linha.split()
            cont_familia+=1
            cont_renda_cidade+=int(dados[3])
            cont_individuos+=int(dados[1])
            if int(dados[3])<1320:
                inferior+=1
            elif int(dados[3])>1320*10:
                superior+=1
        print(f'A renda familiar da cidade é {cont_renda_cidade/cont_familia:.2f}\nO número médio de indivíduos por família é {int(cont_individuos/cont_familia)}\nO percentual de famílias que possuem renda familiar média inferior a um salário mínimo é {(inferior/cont_familia)*100:.1f}%\nA quantidade de famílias com renda familiar superior a 10 salários mínimos é {(superior/cont_familia)*100:.1f}%')

def criação_backup():
    with open('analise.txt' , 'r') as file:
        with open('backup.txt','w') as backup:
            data_hora_atual=datetime.datetime.now()
            data_formatada = data_hora.strftime("%d/%m/%Y")
            hora_formatada = data_hora.strftime("%H:%M:%S")
            backup.write('')

import datetime

data_hora = datetime.datetime.now()
print("Data e hora atual:", data_hora)

data_formatada = data_hora.strftime("%d/%m/%Y")
print("Data formatada:", data_formatada)

hora_formatada = data_hora.strftime("%H:%M:%S")
print("Hora formatada:", hora_formatada)

import datetime

def criacao_de_backup():
    with open("analise.txt", "r") as file:
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%Mhs")
        linhas = file.readlines()
        numero_linhas = len(linhas)
        versao = obter_versao_atual() + 1

        with open("backup.txt", "w") as backup_file:
            backup_file.write(f"{data_hora} {numero_linhas} v{versao}\n")
            backup_file.writelines(linhas)

def obter_versao_atual():
    try:
        with open("backup.txt", "r") as backup_file:
            primeira_linha = backup_file.readline()
            versao_str = primeira_linha.split()[-1]
            versao = int(versao_str[1:])  # Extrai apenas o número da versão
            return versao
    except FileNotFoundError:
        return 0

#programa principal
from time import sleep
import datetime

print('-'*30)
print('    Cadastro de famílias')
print('-'*30)
sleep(2)
while True:
    menu()
    opc=int(input('Digite sua escolha: '))
    if opc==1: inserção_de_familias()
    elif opc==2: busca_cpf()
    elif opc==3: listagem_cpf()
    elif opc==4: listagem_dados()
    elif opc==5: listagem_consolidada()
    elif opc==6: criacao_de_backup
    elif opc==7: break
