import numpy as np
from PIL import Image


def adicao(imagem_01, imagem_02):
  #dimensões das duas imagens (largura e altura) sem considerar o número de canais de cor
  _largura_01, _altura_01 = imagem_01.shape[:2]
  _largura_02, _altura_02 = imagem_02.shape[:2]

  #maior largura e altura
  largura = _largura_01 if _largura_01 > _largura_02 else _largura_02
  altura = _altura_01 if _altura_01 > _altura_02 else _altura_02

  #nova imagem (matriz) cheia de zeros, com as mesmas dimensões (largura e altura) e três canais de cor
  nova_imagem = np.zeros((largura, altura, 3), dtype=np.uint8)

  #percorre cada pixel da nova imagem e faz a adição dos valores de cor de cada imagem no mesmo pixel, dividindo por 2 para criar uma média.
  for x in range(largura):
    for y in range(altura):
      try:
        if (x < _largura_01 and y < _altura_01) and (x < _largura_02 and y < _altura_02):
          # fix((g1 + g2) / 2)
          nova_imagem[x, y] = (imagem_02[x, y] + imagem_01[x, y]) / 2
      except:
        pass

  return nova_imagem

def subtracao(imagem_01, imagem_02):
  _largura_01, _altura_01 = imagem_01.shape[:2]
  _largura_02, _altura_02 = imagem_02.shape[:2]

  largura = _largura_01 if _largura_01 > _largura_02 else _largura_02
  altura = _altura_01 if _altura_01 > _altura_02 else _altura_02

  nova_imagem = np.zeros((largura, altura, 3), dtype=np.uint8)
#subtrai o valor de cada pixel de imagem_02 do valor correspondente em imagem_01
  for x in range(largura):
    for y in range(altura):
      try:
        if (x < _largura_01 and y < _altura_01) and (x < _largura_02 and y < _altura_02):
          nova_imagem[x, y] = imagem_01[x, y] - imagem_02[x, y]
      except:
        ...

  return nova_imagem

def espelhamento(imagem):
  #dimensões da imagem
  largura, altura = imagem.shape[:2]

  imagem_espelhada = np.zeros((largura, altura, 3), dtype=np.uint8)

# para cada pixel na posição (x, y), ele copia o valor do pixel da posição inversa (largura - x - 1, y) na nova imagem
  for x in range(largura):
      for y in range(altura):
          # Largura - x Ele pega o pixel invertido da imagem
          imagem_espelhada[largura - x - 1, y] = imagem[x, y]

  return imagem_espelhada

# Transformando a imageme em uma matrix
imagem_01 = Image.open(r"C:\Users\WEB\Documents\GitHub\IA\op_aritimetica\sextou.png")
imagem_02 = Image.open(r"C:\Users\WEB\Documents\GitHub\IA\op_aritimetica\sextou.png")

#adicao_imagem = adicao(np.array(imagem_01), np.array(imagem_02))
#resultado_adicao_imagem = Image.fromarray(adicao_imagem)
#resultado_adicao_imagem.save('imagem_somada.jpg')

imagem_subtraida = subtracao(np.array(imagem_01), np.array(imagem_02))
resultado_imagem_subtraida = Image.fromarray(imagem_subtraida)
resultado_imagem_subtraida.save('imagem_subtraida01.jpg')

#imagem_espelhamento = espelhamento(np.array(imagem_01))
#resultado_imagem_espelhamento = Image.fromarray(imagem_espelhamento)
#resultado_imagem_espelhamento.save('imagem_espelhamento.jpg')