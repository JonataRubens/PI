<<<<<<< HEAD
import cv2
import numpy as np
import matplotlib.pyplot as plt

def metodoDoVale(imagem):
    # Converte para escala de cinza
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Calcula o histograma
    histograma = cv2.calcHist([cinza], [0], None, [256], [0, 256]).flatten()
    
    # Diagnóstico: exibe o histograma
    plt.plot(histograma)
    plt.title("Histograma da Imagem em Tons de Cinza")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequência")
    plt.show()

    # Encontra os vales no histograma
    vales = [i for i in range(1, 255) if histograma[i-1] > histograma[i] and histograma[i+1] > histograma[i]]
    
    # Diagnóstico: Exibe os vales encontrados
    print("Vales encontrados:", vales)
    
    # Verifica se há vales; se não, retorna um limiar padrão
    if vales:
        limiar = vales[0]
    else:
        print("Nenhum vale claro encontrado no histograma; usando limiar padrão de 128.")
        limiar = 128  # Limiar padrão

    return limiar

def segmentacaoPorLimiarizacao(imagem, limiar):
    # Converte a imagem para escala de cinza
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Aplica a limiarização de forma mais eficiente
    _, binaria = cv2.threshold(cinza, limiar, 255, cv2.THRESH_BINARY)
    
    return binaria

imagem = cv2.imread(r"C:\Users\WEB\Documents\GitHub\PI\morfologia\erosao.png")
if imagem is None:
    print("Erro ao carregar a imagem. Verifique o caminho do arquivo.")
    exit()

limiar = metodoDoVale(imagem)
imagemBinaria = segmentacaoPorLimiarizacao(imagem, limiar)

cv2.imwrite('resultanteSegmentacao.png', imagemBinaria)
=======
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
>>>>>>> 91ae82711db42962d1c0d6e8fd7552bb64bdecc3
