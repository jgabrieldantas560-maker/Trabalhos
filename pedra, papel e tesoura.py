import random

print("=== PEDRA, PAPEL E TESOURA ===\n")

opcoes = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("Escolha (pedra/papel/tesoura) ou 'sair': ").lower()

    if jogador == "sair":
        print("Jogo encerrado!")
        break

    if jogador not in opcoes:
        print("Opção inválida!")
        continue

    computador = random.choice(opcoes)

    print(f"\nVocê escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "papel" and computador == "pedra") or
        (jogador == "tesoura" and computador == "papel")
    ):
        print("Você ganhou!")
    else:
        print("Computador ganhou!")