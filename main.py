def soma_de_tres_numeros():
  parcelas = input("Digite três inteiros separados por espaço: ").split()
  soma = int(parcelas[0]) + int(parcelas[1]) + int(parcelas[2])

  print("A soma dos três inteiros é: ", soma)

def quadrilha():
  homem = input("Digite quatro nomes masculinos separados por espaço: ").split()
  mulher = input("Agora, digite três femininos separados por espaço: ").split()

  print(" ")
  
  print(homem[0] + " amava " + mulher[0] + " que amava " + homem[1])
  print("que amava " + mulher[1] + " que amava " + homem[2] + " que amava " + mulher[2])
  print("que não amava ninguém.")
  print(homem[0] + " foi para os Estados Unidos, " + mulher[0] + " para o convento,")
  print(homem[1] + " morreu de desastre, " + mulher[1] + " ficou para a tia,")
  print(homem[2] + " suicidou-se e " + mulher[2] + " casou com " + homem[3])
  print("que não tinha entrado na história.")

def sucessor_e_antecessor():
  numero_do_pedido = int(input("Qual o númedo do pedido? "))
  antecessor = numero_do_pedido - 1
  sucessor = numero_do_pedido + 1

  print(" ")
  if numero_do_pedido == 1:
    print("O sucessor do pedido", numero_do_pedido, "é", sucessor)

  else: 
    print("O antecessor do pedido", numero_do_pedido, "é", antecessor)
    print("O sucessor do pedido", numero_do_pedido, "é", sucessor)

voltar_menu = "s"

print("Sê bem-vindo(a)!")
print(" ")

while voltar_menu == "s":
  repetir_questao = "s"

  # MENU DE NAVEGAÇÃO
  print("Por favor, escolha uma das opções abaixo:")
  print("1. Soma de três números;")
  print("2. Quadrilha;")
  print("3. Antecessor e Sucesssor;")
  print("4. Par ou Ímpar;")
  print("5. Calculadora Simples;")
  print("6. Idade em Dias;")
  print("7. Menor e Maior de 3 Números;")
  print("8. Fatorial;")
  print("9. Média da Sequência;")
  print("10. Experiências;")
  print("")
  opcao = int(input("Digite: "))
  print("----------------------------------------------")

  while opcao < 1 or opcao > 10:
    print("Esta é uma opção inválida!")
    print("")
    opcao = int(input("Digite: "))
    print("----------------------------------------------")

  while repetir_questao == "s":
    #QUESTÃO 1 - SOMA DE TRÊS NÚMEROS
    if opcao == 1:
      print("Escolheste Soma de três números!\n ")

      soma_de_tres_numeros()

      repetir_questao = input(" \nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")

    # QUESTÃO 2 - QUADRILHA
    if opcao == 2: 
      print("Escolheste Quadrilha!\n ")
      
      quadrilha()

      repetir_questao = input(" \nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")

    #QUESTÃO 3 - SUCESSOR E ANTECESSOR
    if opcao == 3:
      print("Escolheste Sucessor e Antecessor!\n ")

      sucessor_e_antecessor()

      repetir_questao = input(" \nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")

    #QUESTÃO 4 - PAR OU ÍMPAR
    if opcao == 4:
      print("Escolheste Par ou Ímpar!")
      print(" ")

      numero = int(input("Digite um número inteiro: "))

      print(" ")
      if numero % 2 != 0:
        print("ÍMPAR")
      else:
        print("PAR")

      print("")
      repetir_questao = input("Deseja repetir (s ou n)? ")
      print("----------------------------------------------")

    #QUESTÃO 5 - CALCULADORA SIMPLES
    if opcao == 5:
      print("Escolheste Calculadora Simples!")
      print(" ")

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
        
      print("")
      repetir_questao = input("Deseja repetir (s ou n)? ")
      print("----------------------------------------------")

    #QUESTÃO 6 - IDADE EM DIAS
    #um problema faz com que as saídas nao coincidam a partir de 360 dias
    if opcao == 6:
      print("Escolheste Idade em Dias!")
      print(" ")

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

      print("")
      repetir_questao = input("Deseja repetir (s ou n)? ")
      print("----------------------------------------------")

    #QUESTÃO 7 - MENOR E MAIOR DE 3 NÚMEROS
    if opcao == 7:
      print("Escolheste Menor e Maior de 3 Números!")
      print(" ")

      a = float(input("Digite um número: "))
      b = float(input("Digite outro: "))
      c = float(input("E agora mais outro: "))
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

      print("")
      repetir_questao = input("Deseja repetir (s ou n)? ")
      print("----------------------------------------------")

    #QUESTÃO 8 - FATORIAL
    if opcao == 8:
      print("Escolheste Fatorial!")
      print(" ")

      n = int(input("Digite um número natural: "))
      fatorial = n

      if n < 0:
        fatorial = "você precisa digitar um número natural"

      if n == 0:
        fatorial = 1

      if n > 0:
        while n > 1:
          n = n - 1
          fatorial = fatorial * n

      print(" ")
      print(fatorial)

      print("")
      repetir_questao = input("Deseja repetir (s ou n)? ")
      print("----------------------------------------------")

    #QUESTÃO 9 - MÉDIA DA SEQUÊNCIA
    if opcao == 9:
      print("Escolheste Média da Sequência!")
      print(" ")
      print("Digite os números para calcular a Média. Quando terminar, digite '0'")
      print("")

      entrada = float(input("Digite: "))
      soma = 0
      contador = 0

      while entrada != 0:
        soma = soma + entrada
        contador = contador + 1
        entrada = float(input("Digite: "))

      media = soma / contador

      print("A média é: {:2.2f}".format(media))

      print("")
      repetir_questao = input("Deseja repetir (s ou n)? ")
      print("----------------------------------------------")

    #QUESTÃO 10 - EXPERIÊNCIAS
    if opcao == 10:
      print("Escolheste Experiências!")
      print(" ")

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

      print("")
      print("Total:", total_cobaia, "cobaias")
      print("Total de coelhos:", total_coelho)
      print("Total de ratos:", total_rato)
      print("Total de sapos:", total_sapo)
      print("Percentual de coelhos: {:2.2f}".format(percent_coelho), "%")
      print("Percentual de ratos: {:2.2f}".format(percent_rato), "%")
      print("Percentual de sapos: {:2.2f}".format(percent_sapo), "%")

      print("")
      repetir_questao = input("Deseja repetir (s ou n)? ")
      print("----------------------------------------------")

  voltar_menu = input("Deseja voltar ao Menu (s ou n)? ")
  print("----------------------------------------------")

print("Okay! Tchau, tchau! :)")