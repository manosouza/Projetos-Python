num1 = int(input("Digite valor 1: "))
num2 = int(input("Digite valor 2: "))
num3 = int(input("Digite valor 3: "))

if num1 > num2 and num2 > num3:
    print("Ordem decrescente:" , num1 , num2 , num3)
elif num1 > num3  and num3 > num2:
    print("Ordem decrescente:" , num3 , num1 , num2)
elif num2 > num3  and num3 > num1:
    print("Ordem decrescente:" , num2 , num3 , num1)
elif num2 > num1  and num1 > num3:
    print("Ordem decrescente:" , num2 , num1 , num3)
elif num3 > num1  and num1 > num2:
    print("Ordem decrescente:" , num3 , num1 , num2)
elif num3 > num1  and num2 > num1:
    print("Ordem decrescente:" , num3 , num2 , num1)
else:
    print("valores iguais")