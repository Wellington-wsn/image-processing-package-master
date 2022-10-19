# Passas uma  imagen muito grande para uma proporção menor. 
from skimage.transform import resize

def resize_image(image, proportion): # passa a imagens e sua proporção
    assert 0 <= proportion <=1, "Specify a valid proportion between 0 and 1."
    height = round(image.shape[0]*proportion) # pega a autura e multiplia pela forma da proporção desejada, uso do 'round' para que o valore sejá passado como um numero inteiro
    width = round(image.shape[1]*proportion) # pega a largura e multiplia pela forma da proporção desejada
    image_resized = resize(image, (height, width), anti_aliasing=True) # função passa a imagem para proporção.
    return image_resized