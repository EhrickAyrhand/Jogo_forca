import random

print("Bem-vindo ao jogo da Forca!")

palavras = ["python", "forca", "jogos", "codigo"]
palavra_escolhida = random.choice(palavras).upper()
letras_descobertas = ["_" for _ in palavra_escolhida]
letras_erradas = []
tentativas = 6 

while tentativas > 0 and "_" in letras_descobertas:
    print("\nPalavra:", " ".join(letras_descobertas))
    print(f"Erros ({tentativas} vidas restantes):", " ".join(letras_erradas))
    
    chute = input("Digite uma letra: ").upper().strip()

    if not chute.isalpha() or len(chute) != 1:
        print("Por favor, digite apenas UMA letra.")
        continue

    if chute in letras_descobertas or chute in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    if chute in palavra_escolhida:
        for idx, letra in enumerate(palavra_escolhida):
            if letra == chute:
                letras_descobertas[idx] = chute
        print(f"Boa! A letra '{chute}' está na palavra.")
    else:
        letras_erradas.append(chute)
        tentativas -= 1
        print(f"Ops! A letra '{chute}' não está na palavra.")

if "_" not in letras_descobertas:
    print("\nParabéns! Você adivinhou a palavra:", palavra_escolhida)
else:
    print("\nFim de jogo! A palavra era:", palavra_escolhida)
