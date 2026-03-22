import random
import string

print("=== GERADOR DE SENHAS PROFISSIONAL ===\n")

# tamanho da senha
tamanho = int(input("Digite o tamanho da senha: "))

# quantidade de senhas
quantidade = int(input("Quantas senhas deseja gerar? "))

# opções
usar_letras = input("Deseja incluir letras? (s/n): ").lower()
usar_numeros = input("Deseja incluir números? (s/n): ").lower()
usar_simbolos = input("Deseja incluir símbolos? (s/n): ").lower()

# montar caracteres
caracteres = ""

if usar_letras == "s":
    caracteres += string.ascii_letters

if usar_numeros == "s":
    caracteres += string.digits

if usar_simbolos == "s":
    caracteres += string.punctuation

# verificação
if caracteres == "":
    print("\n❌ Erro: você precisa escolher pelo menos uma opção!")
else:
    print("\n🔐 Senhas geradas:\n")

    senhas = []

    for i in range(quantidade):
        senha = ""
        for j in range(tamanho):
            senha += random.choice(caracteres)
        
        senhas.append(senha)
        print(f"{i+1} - {senha}")

    # salvar em arquivo
    salvar = input("\nDeseja salvar em arquivo? (s/n): ").lower()

    if salvar == "s":
        with open("senhas.txt", "w") as arquivo:
            for senha in senhas:
                arquivo.write(senha + "\n")
        
        print("✅ Senhas salvas em 'senhas.txt'")