import time

while True:
    pessoa=str(input("Antes de começarmos,seu cliente é uma pessoa comum ou algum Policial?(N/PM)")).upper()

    if pessoa not in ["N", "PM"]:
        print("Não entendi, responda apenas com 'N' ou 'PM'")
        time.sleep(2)
    else:
        break

def performace():
    print("Responda com 'S/N' se os itens foram colocados (ou não) no veículo")

    pp1=str(input("Motor")).upper()
    pp2=str(input("Cambio")).upper()
    pp3=str(input("Freios")).upper()
    pp4=str(input("Suspensão")).upper()
    pp5=str(input("Blindagem")).upper()
    pp1 = 1 if pp1=="S" else 0
    pp2 = 1 if pp2=="S" else 0
    pp3 = 1 if pp3=="S" else 0
    pp4 = 1 if pp4=="S" else 0
    pp5 = 1 if pp5=="S" else 0

    somapp=pp1*50000 + pp2*40000 + pp3*30000 + pp4*25000 + pp5*80000
    
    if pessoa=="N":
        total2=somapp
        print("A soma de todos os valores deram {}".format(somapp))
    elif pessoa=="PM":
         total2=somapp*0.8
         print("A soma de todos os valores deram {}".format(somapp*0.8))
    return total2

def estetica():
    p1=str(input("pintura?(S/N)")).upper()
    p2=str(input("roda?(S/N)")).upper()
    p3=int(input("quantas outras peças?"))
    p1 = 1 if p1=="S" else 0
    p2 = 1 if p2=="S" else 0
    soma2= p1*3000 + p2*4000 + p3*2000

   
    ptotal=str(input("O Veículo dele é da categoria nacional, importado ou governamental?(N,I,G")).upper()

    if ptotal=="N":
        total= soma2
        print("A soma das tunagens deu um total de {}".format(soma2))

    elif ptotal=="I":
        total= soma2*1.5
        print("A soma das tunagens deu um total de {}".format(soma2*1.5))

    elif ptotal=="G":
        total= soma2*0.8
        print("A soma das tunagens deu um total de {}".format(soma2*0.8))
    return total

kit=int(input("Quantos kits de reparo o cliente precisa?"))
pneu=int(input("Quantos Pneus o cliente precisa?"))              
chave=int(input("Ele quis quantas chave(s) de roda?"))
macaco=int(input("E macaco hidráulico, quantos ele pediu?"))
soma1=(kit*2500 + pneu*1500 + chave*2000 + macaco*2000)
if pessoa=="N":
    print("A soma de todos os valores deram {}".format(soma1))
elif pessoa=="PM":
    print("A soma de todos os valores deram {}".format(soma1*0.8))

''
tunar=str(input("Abrir tunagem? (S/N)")).upper()
total = 0
total2 = 0
if tunar=='S':

    motor=int(input("A pessoa quer tunagem (1)performace ou (2)estética? ou os (3)dois? \
    (1,2,3)"))

    if motor==1:
        total2=performace()
        print("o valor total deu {}".format(total2))

    elif motor==2:
        total=estetica()
        print("o valor total deu {}".format(total))

    elif motor==3:
        moto3=int(input("Vamos começar por onde, (1)performace ou (2)estética?"))
        if moto3==1:
            total2=performace()
            total=estetica()
        elif moto3==2:
            total=estetica()
            total2=performace()
    print("A soma total deu {}".format(total2+total))

elif tunar=='N':
    print("Como decidiu não, acaba por aqui")
    exit()

"""
valores tunagem performace:
motor 50000
cambio 40000
blindagem 80000
Freios 30000
Suspensao 25000

valores tunagem estetica:
pintura 3000
roda (com pintura) 4000
todo resto 2000 cada


Valores itens soltos
kit reparo= 2500
pneu= 1500
chave de roda= 2000
macaco= 2000

itens soltos por pessoas servidores (policial, bombeiro) -20%

tunagem de veiculos do governo (ambulancia, viatura) -20%
veiculos importados (porsche, lamborghini) +50%
"""
