import numpy as np
import cv2
import matplotlib.pyplot as plt

# Função para realizar o preenchimento de regiões (Flood Fill)
def preenchimento_regioes(imagem, seed_point):
    # Criar uma cópia da imagem binária
    preenchida = np.copy(imagem)
    
    # Tamanho da imagem
    i_height, i_width = imagem.shape
    
    # Lista para armazenar os pontos que serão preenchidos
    stack = [seed_point]  # Ponto inicial (semente)
    
    # Manter o processo de preenchimento enquanto houver pontos na lista
    while stack:
        # Pegar o ponto atual
        x, y = stack.pop()
        
        # Verificar se o ponto está dentro dos limites da imagem e se ainda não foi preenchido
        if preenchida[x, y] == 0:  # Se for preto (0), vamos preencher
            preenchida[x, y] = 255  # Preencher com branco (255)
            
            # Adicionar os vizinhos à lista de pontos a preencher
            if x > 0:  # Cima
                stack.append((x - 1, y))
            if x < i_height - 1:  # Baixo
                stack.append((x + 1, y))
            if y > 0:  # Esquerda
                stack.append((x, y - 1))
            if y < i_width - 1:  # Direita
                stack.append((x, y + 1))
    
    return preenchida

# Carregar a imagem binária
imagem_binaria = cv2.imread(r"C:\Users\WEB\Documents\GitHub\PI\morfologia\imagem_binaria_para_preenchimento.png", cv2.IMREAD_GRAYSCALE)

# Definir o ponto de semente dentro de uma área preta (por exemplo, fora do quadrado branco)
seed_point = (10, 10)  # Escolhendo uma área que está preta (0)

# Aplicar o preenchimento de regiões
imagem_preenchida = preenchimento_regioes(imagem_binaria, seed_point)

# Exibir as imagens usando matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Imagem Binária Original')
plt.imshow(imagem_binaria, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Imagem Preenchida')
plt.imshow(imagem_preenchida, cmap='gray')

plt.show()
