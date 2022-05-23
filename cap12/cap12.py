# Capitulo 12 Livro

# Importando bibliotecas
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("cap12/teste.jpg") # Importando a imagem no código
color = ('b','g','r') # Nomeando as cores

# Criando um loop de interações para criação do histrograma
for i, j in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histr, color = j)
    plt.xlim([0,256])
plt.show()

# Mostrando imagem no openCV
cv.imshow("imagem", img)
cv.waitKey(0)
cv.destroyAllWindows()