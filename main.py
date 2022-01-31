from funcoes import *

print("Sê bem-vindo(a)!\n")
voltar_menu = "s"

while voltar_menu == "s":
  repetir_questao = "s"

  # MENU DE NAVEGAÇÃO
  print("""Por favor, escolha uma das opções abaixo:
  1. Soma de três números;")
  2. Quadrilha;
  3. Antecessor e Sucesssor;
  4. Par ou Ímpar;
  5. Calculadora Simples;
  6. Idade em Dias;
  7. Menor e Maior de 3 Números;
  8. Fatorial;
  9. Média da Sequência;
  10. Experiências;
  """)
  opcao = int(input("Digite: "))
  print("----------------------------------------------")

  while opcao < 1 or opcao > 10:
    print("Esta é uma opção inválida!\n")
    opcao = int(input("Digite: "))
    print("----------------------------------------------")

  while repetir_questao == "s":
    if opcao == 1:
      soma_de_tres_numeros()
      repetir_questao = input("\nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")
    
    elif opcao == 2:
      quadrilha()
      repetir_questao = input("\nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")
    
    elif opcao == 3:
      sucessor_e_antecessor()
      repetir_questao = input("\nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")

    elif opcao == 4:
      par_ou_impar()
      repetir_questao = input("\nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")

    elif opcao == 5:
      calculadora_simples()
      repetir_questao = input("\nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")

    elif opcao == 6:
      idade_em_dias()
      repetir_questao = input("\nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")

    elif opcao == 7:
      menor_e_maior_de_tres_numeros()
      repetir_questao = input("\nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")

    elif opcao == 8:
      fatorial()
      repetir_questao = input("\nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")

    elif opcao == 9:
      media_da_sequencia()
      repetir_questao = input("\nDeseja repetir (s ou n)? ")
      print("----------------------------------------------")

    else:
      experiencias()
  
  voltar_menu = input("Deseja voltar ao Menu (s ou n)? ")
  print("----------------------------------------------")

print("Okay! Tchau, tchau! :)")
