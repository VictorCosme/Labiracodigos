def soma_de_tres_numeros():
  print("Escolheste Soma de três números!\n ")
  
  parcelas = input("Digite três inteiros separados por espaço: ").split()
  soma = int(parcelas[0]) + int(parcelas[1]) + int(parcelas[2])

  print("A soma dos três inteiros é: ", soma)
 
def quadrilha():
  print("Escolheste Quadrilha!\n ")

  homem = input("Digite quatro nomes masculinos separados por espaço: ").split()
  mulher = input("Agora, digite três femininos separados por espaço: ").split()

  print("\nQUADRILHA")
  
  print(homem[0] + " amava " + mulher[0] + " que amava " + homem[1])
  print("que amava " + mulher[1] + " que amava " + homem[2] + " que amava " + mulher[2])
  print("que não amava ninguém.")
  print(homem[0] + " foi para os Estados Unidos, " + mulher[0] + " para o convento,")
  print(homem[1] + " morreu de desastre, " + mulher[1] + " ficou para a tia,")
  print(homem[2] + " suicidou-se e " + mulher[2] + " casou com " + homem[3])
  print("que não tinha entrado na história.")

def sucessor_e_antecessor():
  print("Escolheste Sucessor e Antecessor!\n ")
  
  numero_do_pedido = int(input("Qual o número do pedido? "))
  antecessor = numero_do_pedido - 1
  sucessor = numero_do_pedido + 1

  if numero_do_pedido == 1:
    print("\nO sucessor do pedido", numero_do_pedido, "é", sucessor)

  else: 
    print("\nO antecessor do pedido", numero_do_pedido, "é", antecessor)
    print("O sucessor do pedido", numero_do_pedido, "é", sucessor)

def par_ou_impar():
  print("Escolheste Par ou Ímpar!\n")

  numero = int(input("Digite um número inteiro: "))

  if numero % 2 != 0:
    print("\nÍMPAR")
  
  else:
    print("\nPAR")

def calculadora_simples():
  print("Escolheste Calculadora Simples!\n")

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo: "))
  operacao = input("Escolha uma operação (+, -, *, /): ")

  print(" ")

  if operacao == "+":
    print(num1 + num2)

  elif operacao == "-":
    print(num1 - num2)

  elif operacao == "*":
    print(num1 * num2)

  elif operacao == "/":
    if num2 == 0:
      print("Não se pode dividir por 0")
    else:
      print(num1 / num2)

def idade_em_dias(): #ISSUE: não coincidem em 360+ dias
  print("Escolheste Idade em Dias!\n")

  entrada = int(input("Digite a quantidade de dias: "))
  dias = entrada
  meses = 0
  anos = 0

  while dias >= 30:
    dias = dias - 30
    meses = meses + 1

  while meses >= 12:
    meses = meses - 12
    anos = anos + 1

  print(" ")
  print(entrada, "dia(s) <=>", anos, "ano(s),", meses, "mes(es) e", dias, "dia(s)")

def menor_e_maior_de_tres_numeros():
  print("Escolheste Menor e Maior de 3 Números!\n")

  a = float(input("Digite um número: "))
  b = float(input("Digite outro: "))
  c = float(input("E agora um terceiro: "))
  
  menor = 0
  maior = 0

  if a <= b and a <= c:
    menor = a
    if b >= c:
      maior = b
    else:
      maior = c

  if b <= a and b <= c:
    menor = b
    if a >= c:
      maior = a
    else:
      maior = c

  if c <= a and c <= b:
    menor = c
    if b >= a:
      maior = b
    else:
      maior = a

  print(" ")
  print(menor, "é o menor dos 3 números")
  print(maior, "é o maior dos 3 números")

def fatorial():
  print("Escolheste Fatorial!\n")

  n = int(input("Digite um número natural: "))
  fatorial = n

  if n < 0:
    fatorial = "Precisas digitar um número natural"

  if n == 0:
    fatorial = 1

  if n > 0:
    while n > 1:
      n = n - 1
      fatorial = fatorial * n

  print(" ")
  print(fatorial)

def media_da_sequencia():
  print("Escolheste Média da Sequência!\n")

  print("Digite os números para calcular a Média. Para terminar, digite '0'\n")

  entrada = float(input("Digite: "))
  soma = 0
  contador = 0

  while entrada != 0:
    soma += entrada
    contador += 1
    entrada = float(input("Digite: "))

  media = soma / contador

  print("A média é: {:2.2f}".format(media))

def experiencias():
  print("Escolheste Experiências!\n")

  numero_casos_de_teste = int(input("Quantos casos de teste queres adicionar? "))
  total_coelho = 0
  total_sapo = 0
  total_rato = 0

  while 0 < numero_casos_de_teste:
    entrada = input("Digite (Ex. 5 C): ").split()

    quantidade = int(entrada[0])
    tipo = entrada[1]

    if tipo == "C":
      total_coelho = total_coelho + quantidade
  
    if tipo == "S":
      total_sapo = total_sapo + quantidade

    if tipo == "R":
      total_rato = total_rato + quantidade  

    numero_casos_de_teste = numero_casos_de_teste - 1

  total_cobaia = total_coelho + total_sapo + total_rato
  percent_coelho = (total_coelho * 100) / total_cobaia 
  percent_sapo = (total_sapo * 100) / total_cobaia 
  percent_rato = (total_rato * 100) / total_cobaia 

  print("\nTotal:", total_cobaia, "cobaias")
  print("Total de coelhos:", total_coelho)
  print("Total de ratos:", total_rato)
  print("Total de sapos:", total_sapo)
  print("Percentual de coelhos: {:2.2f}".format(percent_coelho), "%")
  print("Percentual de ratos: {:2.2f}".format(percent_rato), "%")
  print("Percentual de sapos: {:2.2f}".format(percent_sapo), "%")