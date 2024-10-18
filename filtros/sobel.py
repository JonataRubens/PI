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
imagem = cv2.imread(r"C:\Users\WEB\Documents\GitHub\PI\filtros\sobe.png", 0)


# Máscaras de Sobel
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

sobel_y = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])

# Aplica a convolução para calcular o gradiente em X e Y
gradiente_x = convolucao_2d(imagem, sobel_x)
gradiente_y = convolucao_2d(imagem, sobel_y)

# Combina os gradientes para obter a magnitude do gradiente final
gradiente_final = np.sqrt(gradiente_x**2 + gradiente_y**2)

# Exibe os resultados
plt.subplot(1, 3, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')

plt.subplot(1, 3, 2)
plt.imshow(gradiente_x, cmap='gray')
plt.title('Sobel X')

plt.subplot(1, 3, 3)
plt.imshow(gradiente_y, cmap='gray')
plt.title('Sobel Y')

plt.figure()
#plt.imshow(gradiente_final, cmap='gray')
plt.title('Magnitude do Gradiente (Sobel)')
plt.show()