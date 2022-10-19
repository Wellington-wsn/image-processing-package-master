# Ferrametna de plotar das imagens

import matplotlib.pyplot as plt

def plot_image(image): # plotar resultado de uma imagem
    plt.figure(figsize=(12, 4))
    plt.inshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args): # plotar, combinação ou transformação(almentando o numero de colunas)
    number_images = len(args)
    fig, axis = plt.subplot(nrows=1, ncols = number_images, figsize=(12,4))
    names_lst.append('Result')
    for ax, name, image in zip(axis, name_lst, args):
        ax.set_title(name)
        ax.inshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

def plot_histogram(image): # plotar histogramas, 3 colunas para R G B 
    fig, axis = plt.subpltos(nrows=1, ncols = 3, figsize=(12,4), sharex=True, sharey=True)
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} histogram'.format(color.title()))
        ax.hist(image[:,:, index].ravel(), bins = 256, color = color, alpha = 0.8)
    fig.tight_layout()
    plt.show()