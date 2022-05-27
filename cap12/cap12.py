# Capitulo 12 Livro

# Importando bibliotecas
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("cap12/teste.jpg") # Importando a imagem no código
color = ('b','g','r') # Nomeando as cores

# Criando um loop de interações para criação do histrograma
for i, j in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histr, color = j)
    plt.xlim([0,256])

# Conversão para grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# Conversão para HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# Conversão para YUV
yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
cv.imshow("yuv", yuv)

#Conversão para YCRCB
ycbcr = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
cv.imshow("ycbcr", ycbcr)

# Mostrando imagem no openCV / Matplotlib
cv.imshow("imagem", img)
cv.waitKey(0)
cv.destroyAllWindows()
plt.show()