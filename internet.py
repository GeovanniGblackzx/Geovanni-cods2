minutos = int(input("Quanto tempo você ficou na internet? "))
if minutos <= 200:
    valor = 0.20
    print (valor * minutos)
elif minutos >= 200 and minutos <= 400:
    valor = 0.18
    print (valor * minutos)
elif minutos >= 400:
    valor = 0.15
    print (valor * minutos)
else :
    print ("ERRO")