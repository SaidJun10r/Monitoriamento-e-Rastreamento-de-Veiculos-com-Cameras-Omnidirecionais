# Capitulo 12 Livro

# Importando bibliotecas
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Importando a imagem no código
img = cv.imread("teste.jpg")

# Mostrando as imagens
plt.title("imagem Original")
plt.imshow(img)

plt.show()