tabuada=int(input("Digite um numero para exibir a tabuada: "))
print("Tabuada do número", tabuada)
for valor in range (1,11,1): #INICIOU NO 1 , VAI ATÉ O 10 E É DE UM EM UM
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))