import numpy as np 
import cv2
from matplotlib import pyplot as plt
from os import scandir, getcwd
from os.path import abspath

def procesar(imagen):
    imagen = cv2.imread(imagen, cv2.IMREAD_COLOR)
    #cv2.imshow('original', imagen)

    imagen = cv2.GaussianBlur(imagen ,(9,9),0)

    imgray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 80, 255, cv2.THRESH_BINARY)
    #cv2.imshow('silueta', thresh)

    im2, contornos, jerarquía = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contornosGrandes = []
    areas = []
    for i in contornos:
        areas.append(cv2.contourArea(i))

    for i in contornos:
        if(cv2.contourArea(i) == max(areas)):
            contornosGrandes.append(i)      

    cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    cv2.drawContours(imagen, contornosGrandes,-1, (255,0,0), -1)

    #cv2.imshow('mano', imagen)

    HU = cv2.HuMoments(cv2.moments(contornosGrandes[0]))
    return imagen, HU

def imprimirImagen(imagen, titulo = ""):
    plt.subplot(111), plt.title(titulo), plt.axis("off")
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.show()

def ls(ruta = '.'):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]