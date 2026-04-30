import time

while True:
    nome=str(input("Qual seu nome?")).upper()
    if nome != "Matheus":
        print("Nome Incorreto, insira denovo")
        time.sleep(1)
    else:
        break
while True:
    senha6=(input("Seja bem vindo Matheus! Para segurança, digite sua senha de 6 dígitos"))
    if senha6 !="123123":
        print("Senha incorreta! Tente novamente.")
        time.sleep(1)
    else:
        break       
print("Seja bem vindo Matheus! Aguarde enquanto preparamos tudo pra você!")
time.sleep(2)

while True:
    print(" O que faremos hoje?")

    opcao=(input(" 1- Consultar Saldo \n 2- Fazer um deposito \n 3- Fazer um Pix \n 4- Sair"))
    
    if not opcao.isdigit():
        print("Apenas números de 1 a 4")
        time.sleep(2)
        continue

    opcoes=int(opcao)

    if opcoes not in[1,2,3,4]:
        print("Número invalido")
        time.sleep(2)
        continue

    match opcoes:
        case 1:
            print("Seu saldo é de R$0,00. Sinto muito.")
            op1=input("deseja voltar ao início? Responda com (S/N)").upper()
            if op1=="S":
                print("você será redirecionado ao início")
                time.sleep(2)
            else:
                print("O programa será encerrado, muito obrigado e até breve.")
                time.sleep(1)
                exit()

        case 2:
            while True:
                deposito=input("Muito bem, quanto você gostaria de depositar?")
                if deposito.isdigit():
                    break
                else:
                    print("Você precisa inserir um valor em números! Tente denovo.")
                    time.sleep(1)

            while True:
                senha4=(input("Digite sua senha de 4 dígitos pra confirmar o depósito de R${} na sua conta.".format(deposito)))
                
                if not senha4.isdigit():
                    print("Digite apenas números")
                    continue

                if int(senha4) != 1231:
                    print("Senha incorreta, tente novamente")
                    time.sleep(1)
                else:
                    print("Seu valor de {} foi depositado com sucesso!".format(deposito))
                    time.sleep(1)
                    break

            op2=input("deseja voltar ao início? Responda com (S/N)").upper()
            if op2=="S":
                print("você será redirecionado ao início")
                time.sleep(2)
            else:
                print("O programa será encerrado, muito obrigado e até breve.")
                time.sleep(1)
                exit()

        case 3:
                while True:
                    op3=input("Para quem você quer fazer o pix? Apenas primeiro nome").capitalize()
                    if op3.isalpha():
                        break
                    else:
                        print("Você precisa inserir um nome, sem números!")
                        time.sleep(1)

                while True:
                    opp3=input("Quanto você quer enviar?")
                    if opp3.isdigit():
                        valor=int(opp3)
                        break
                    else: 
                        print("você precisa inserir um valor aqui! tente novamente...")
                        time.sleep(1)


                oppp3=input("Você tem certeza que deseja enviar R${} para {}? essa operação é irreversível(S/N)".format(valor, op3)).upper()
                if oppp3== "S":
                    print("Seu valor foi enviado com sucesso.")
                    time.sleep(1)

                else:
                    print("OK, a sua transação foi cancelada.")
                    time.sleep(1)

                ooppp3=input(" Deseja fazer mais alguma operação?(S/N)").upper()
                if ooppp3=="S":
                    print("você será redirecionado ao início.")
                    time.sleep(1)
                else:
                    print("O sistema está sendo encerrado...")
                    time.sleep(2)
                    exit()
        case 4:
            sair=input("Tem certeza que deseja mesmo sair? (S/N)").upper()
            
            if sair == "S":
                print("O sistema está sendo encerrado... Até breve!")
                time.sleep(2)
                exit()

            else:
                print("Você será redirecionado ao início...")
                time.sleep(2)
