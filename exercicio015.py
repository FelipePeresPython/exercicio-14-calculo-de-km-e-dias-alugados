# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print("quantos kilometros seu carro alugado percorreu?")
L=float(input(""))
print()
print("agora me fale quantos dias você alugou ele")
A=int(input(""))
print()
print("agora vamos calcular o preço a pagar por dia e por km rodado")
B=L*0.15
C=A*60
D=B+C
print()
print(f"o valor de km rodados deu {B} e o valor por dias alugados deu {C} ")
print()
print(f"o valor total a pagar seria a soma entre esses dois valores,então \n daria o valor total de: R${D}")
print()

