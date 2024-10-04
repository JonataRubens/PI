import numpy as np
import matplotlib.pyplot as plt
import cv2

#carregar a imagem em escala de cinza
imagem = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

#calcular o histograma da imagem é gerado contando quantos pixels há em cada nível de intensidade 0 a 255
histograma, _ = np.histogram(imagem.flatten(), bins=256, range=[0, 256])

#(é a soma acumulada dos valores no histograma. para cada nível de intensidade, a proporção de pixels que têm intensidade menor ou igual àquela. Ela acumula os valores do histograma.)
cdf = histograma.cumsum()  

#(permite que redistribuamos os pixels de modo que as áreas escuras e claras sejam mais equilibradas.)
cdf_normalizado = cdf * (255 / cdf[-1])  

# mapeamento de intensidades baseado na CDF (os pixels originais da imagem são mapeados para novas intensidades, ajustando o contraste)
imagem_equalizada = np.interp(imagem.flatten(), np.arange(0, 256), cdf_normalizado)

# Reshape a imagem de volta para seu formato original
imagem_equalizada = imagem_equalizada.reshape(imagem.shape).astype(np.uint8)

# Exibir a imagem original e a imagem equalizada
plt.figure(figsize=(10, 5))

# Imagem original
plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

# Imagem equalizada
plt.subplot(1, 2, 2)
plt.imshow(imagem_equalizada, cmap='gray')
plt.title('Imagem Equalizada')
plt.axis('off')

plt.show()
