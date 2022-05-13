# Resumo Capitulo 3 Livro

# Importando bibliotecas
from statistics import variance
from skimage import io, data
from matplotlib import pyplot as plt
import numpy as np

# Pegando a imagem e mostrando elas
img = io.imread('cap3/teste.jpg')
grayimg = io.imread('cap3/teste.jpg', as_gray=True)
plt.subplot(2,2,1)
plt.title("imagem Original")
plt.imshow(img)
plt.subplot(2,2,2)
plt.title("Imagem em escala de cinza")
plt.imshow(grayimg, cmap='gray')

# Apresentando o histograma
histogram, bin_edges = np.histogram(grayimg, bins=256, range=(0, 1))
plt.subplot(2,1,2)
plt.title("Historiograma em escala de cinza") # Title
plt.xlabel("Valores em escala de cinza") # X title
plt.ylabel("Contagem de pixels") # Y title
plt.xlim([0.0, 1.0]) # Define the limits of x values on the figure
plt.plot(bin_edges[0:-1], histogram)

# Computando as informações do terceiro capítulo
minpixel = np.amin(grayimg) # Valor mínimo de pixel da imagem em grayscale
maxpixel = np.amax(grayimg) # Valor máximo de pixel na imagem em grayscale
media = np.mean(grayimg) # Média da imagem
variancia = np.var(grayimg) # Variância da imagem
mediana = np.median(grayimg) # Mediana da imagem

print('O valor mínimo de pixel :', minpixel, '\nValor máximo de pixel :', maxpixel)
print('Média da imagem :', media, '\nVariância da imagem: ', variancia, '\nMediana da imagem: ', mediana)
plt.show()