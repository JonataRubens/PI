import numpy as np
import matplotlib.pyplot as plt
import cv2

# Função de convolução 2D manual
def convolucao_2d(imagem, kernel):
    altura, largura = imagem.shape
    kernel_size = kernel.shape[0]
    pad = kernel_size // 2

    # Adiciona padding à imagem para evitar problemas nas bordas
    imagem_padded = np.pad(imagem, pad, mode='constant', constant_values=0)

    # Inicializa a imagem de saída
    output = np.zeros_like(imagem)

    # Aplica a convolução
    for i in range(pad, altura + pad):
        for j in range(pad, largura + pad):
            # Extrai a região da imagem que será multiplicada pela máscara
            regiao = imagem_padded[i-pad:i+pad+1, j-pad:j+pad+1]
            # Realiza o produto elemento a elemento e soma os resultados
            output[i-pad, j-pad] = np.sum(regiao * kernel)
    
    return output

# Carregar imagem em escala de cinza
imagem = cv2.imread(r"C:\Users\WEB\Documents\GitHub\PI\filtros\meia-lua.jpg", 0)

# Definir as quatro máscaras Laplacianas
laplacian_mask_1 = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])

laplacian_mask_2 = np.array([[1, 1, 1],
                             [1, -8, 1],
                             [1, 1, 1]])

laplacian_mask_3 = np.array([[0, -1, 0],
                             [-1, 4, -1],
                             [0, -1, 0]])

laplacian_mask_4 = np.array([[-1, -1, -1],
                             [-1, 8, -1],
                             [-1, -1, -1]])

# Aplicar a convolução com cada máscara
resultado_laplaciano_1 = convolucao_2d(imagem, laplacian_mask_1)
resultado_laplaciano_2 = convolucao_2d(imagem, laplacian_mask_2)
resultado_laplaciano_3 = convolucao_2d(imagem, laplacian_mask_3)
resultado_laplaciano_4 = convolucao_2d(imagem, laplacian_mask_4)

# Exibir os resultados para as 4 máscaras
plt.subplot(2, 3, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')

plt.subplot(2, 3, 2)
plt.imshow(resultado_laplaciano_1, cmap='gray')
plt.title('Laplaciano 1')

plt.subplot(2, 3, 3)
plt.imshow(resultado_laplaciano_2, cmap='gray')
plt.title('Laplaciano 2')

plt.subplot(2, 3, 5)
plt.imshow(resultado_laplaciano_3, cmap='gray')
plt.title('Laplaciano 3')

plt.subplot(2, 3, 6)
plt.imshow(resultado_laplaciano_4, cmap='gray')
plt.title('Laplaciano 4')

plt.show()
