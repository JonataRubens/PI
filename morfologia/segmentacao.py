import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para encontrar o limiar pelo método do vale
def metodo_do_vale(histograma):
    # Encontra os índices dos picos no histograma
    picos = np.where((histograma[1:-1] > histograma[:-2]) & (histograma[1:-1] > histograma[2:]))[0] + 1
    print("Picos encontrados:", picos)  # Diagnóstico

    if len(picos) >= 2:
        # Encontra o menor valor entre os dois maiores picos (vale)
        pico_1 = picos[0]
        pico_2 = picos[1]
        limiar = np.argmin(histograma[pico_1:pico_2]) + pico_1
        return limiar
    else:
        return None  # Caso não existam picos definidos

# Carrega a imagem em tons de cinza
imagem = cv2.imread(r"C:\Users\WEB\Documents\GitHub\PI\morfologia\imagem_teste.png", cv2.IMREAD_GRAYSCALE)
if imagem is None:
    print("Erro ao carregar a imagem. Verifique o caminho.")
else:
    # Calcula o histograma da imagem
    histograma = cv2.calcHist([imagem], [0], None, [256], [0, 256])
    histograma = histograma.flatten()
    print("Histograma:", histograma)  # Diagnóstico

    # Encontra o limiar pelo método do vale
    limiar = metodo_do_vale(histograma)

    # Limiariza a imagem usando o limiar encontrado
    if limiar is not None:
        _, imagem_limiarizada = cv2.threshold(imagem, limiar, 255, cv2.THRESH_BINARY)
        
        # Exibe a imagem original e a segmentada
        plt.figure(figsize=(10,5))

        plt.subplot(1, 3, 1)
        plt.title('Imagem Original')
        plt.imshow(imagem, cmap='gray')

        plt.subplot(1, 3, 2)
        plt.title('Histograma')
        plt.plot(histograma)

        plt.subplot(1, 3, 3)
        plt.title('Imagem Segmentada')
        plt.imshow(imagem_limiarizada, cmap='gray')

        plt.show()
    else:
        print("Não foi possível determinar o limiar pelo método do vale.")
