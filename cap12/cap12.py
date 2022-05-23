# Capitulo 12 Livro

# Importando bibliotecas
from statistics import variance
from skimage import io, data
from matplotlib import pyplot as plt
import numpy as np

# Importando a imagem no código
img = io.imread('cap12/teste.jpg')
grayimg = io.imread('cap3/teste.jpg', as_gray=True) # Imagem em grayscale

# Mostrando as imagens
plt.subplot(1,2,1)
plt.title("imagem Original")
plt.imshow(img)
plt.subplot(1,2,2)
plt.title("Imagem em escala de cinza")
plt.imshow(grayimg, cmap='gray')

plt.show()