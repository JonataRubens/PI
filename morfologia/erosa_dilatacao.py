from matplotlib import pyplot as plt
import numpy as np
import cv2

# Função para aplicar erosão
def erosao(imagem, kernel):
    # Tamanho do kernel
    k_height, k_width = kernel.shape
    # Tamanho da imagem
    i_height, i_width = imagem.shape
    
    # Definir borda para evitar problemas nas extremidades
    pad_height, pad_width = k_height // 2, k_width // 2
    imagem_padded = np.pad(imagem, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=255)
    
    # Imagem resultante da erosão
    imagem_erodida = np.zeros_like(imagem)
    
    # Aplicar erosão (mínimo local)
    for i in range(i_height):
        for j in range(i_width):
            # Extrair a região de interesse (ROI)
            roi = imagem_padded[i:i + k_height, j:j + k_width]
            # Aplicar o mínimo (erosão)
            imagem_erodida[i, j] = np.min(roi[kernel == 1])
    
    return imagem_erodida

# Função para aplicar dilatação
def dilatacao(imagem, kernel):
    # Tamanho do kernel
    k_height, k_width = kernel.shape
    # Tamanho da imagem
    i_height, i_width = imagem.shape
    
    # Definir borda para evitar problemas nas extremidades
    pad_height, pad_width = k_height // 2, k_width // 2
    imagem_padded = np.pad(imagem, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    
    # Imagem resultante da dilatação
    imagem_dilatada = np.zeros_like(imagem)
    
    # Aplicar dilatação (máximo local)
    for i in range(i_height):
        for j in range(i_width):
            # Extrair a região de interesse (ROI)
            roi = imagem_padded[i:i + k_height, j:j + k_width]
            # Aplicar o máximo (dilatação)
            imagem_dilatada[i, j] = np.max(roi[kernel == 1])
    
    return imagem_dilatada

# Carregar a imagem em tons de cinza
imagem = cv2.imread(r"C:\Users\WEB\Documents\GitHub\PI\morfologia\erosao.png", cv2.IMREAD_GRAYSCALE)

# Definir um kernel de exemplo (3x3)
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=np.uint8)

# Aplicar erosão
imagem_erodida = erosao(imagem, kernel)

# Aplicar dilatação
imagem_dilatada = dilatacao(imagem, kernel)

# Exibir a imagem usando matplotlib
plt.figure(figsize=(10,5))

plt.subplot(1, 3, 1)
plt.title('Imagem Original')
plt.imshow(imagem, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Imagem Erodida')
plt.imshow(imagem_erodida, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Imagem Dilatada')
plt.imshow(imagem_dilatada, cmap='gray')

plt.show()
