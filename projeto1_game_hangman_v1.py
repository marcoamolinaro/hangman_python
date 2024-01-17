# Projeto 1 - Desenvolvimento de Game em Linguagem Python - V 1.0

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    
    if name == 'nt': # Windows
        _ = system('cls')
    
    else: # Mac or Linux
        _ = system('clear')
  
# Função      
def game():
    limpa_tela()
    
    print("\nBem-vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)
    
    # List comprehension
    letras_descobertas = ['_' for letra in palavra]
    
    # Número de chances
    chances = 6
    
    # Lista para as letras erradas
    letras_erradas = []
    
    # Loop enquanto número de chances > 0
    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas:", " ".join(letras_erradas))
        
        # Tentativas
        tentativa = input("\nDigite uma letra: ").lower()
    
        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)      
        
        # Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
        
    # Condicinal
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)
        
# Bloco main
if __name__ == "__main__":
    game()
