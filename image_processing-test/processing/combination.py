# Processo de combinação das imagens
import numpy as np
# Pacote de peocessamento de imagem 'skimage' e varios modulos
from skimage.color import rgh2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1, image2): # Encontrar deferença entre duas imagens
    assert image1.shape == image2.shape, "Specify 2 images with de same shape."
    gray_image1 = rgb2gray(image1) # converte a imagem para tons de cinza
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True) # buscar por metodo 'score'(0 - 1) quanto as imagens são similares, e o 'difference_image' busca a diferença entre elas
    print("Similarity of the images:", score) # mostrando o 'score' valores referentes.
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image)) # Normalizando a diferença, para flotar.
    return normalized_difference_image

def transfer_histrogram(image1, image2):
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image # retornar uma imagems como as imagens como parametro.