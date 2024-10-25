import cv2
import numpy as np

def metodoDoVale(imagem):
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    histograma = cv2.calcHist([cinza], [0], None, [256], [0, 256])

    vales = []
    for i in range(1, 255):
        if histograma[i-1] > histograma[i] and histograma[i+1] > histograma[i]:
            vales.append(i)
    
    vales.sort()

    limiar = int(vales[0])
    return limiar


def segmentacaoPorLimiarizacao(imagem, limiar):
    # Convertendo a imagem para escala de cinza
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Criar uma imagem binária vazia com o mesmo tamanho da imagem original
    binaria = np.zeros_like(cinza)

    for i in range(cinza.shape[0]):
        for j in range(cinza.shape[1]):
            if cinza[i, j] > limiar:
                binaria[i, j] = 255 
            else:
                binaria[i, j] = 0    
    
    return binaria



imagem = cv2.imread('imagemSegmentacao.png')

limiar = metodoDoVale(imagem)

imagemBinaria = segmentacaoPorLimiarizacao(imagem, limiar)

cv2.imwrite('resultanteSegmentacao.png', imagemBinaria)
