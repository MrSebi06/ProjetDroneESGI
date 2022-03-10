# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:02:21 2022

@author: mihne
"""

import pygame
from pygame.locals import QUIT

W, H = 1000, 1000
lar, lon = 400, 900

# Initialisation de la fenêtre
pygame.init()
fenetre = pygame.display.set_mode((W, H))
pygame.display.set_caption('Plan de la pièce')

# Remplissage de l'arrière-plan
background = pygame.Surface(fenetre.get_size())
background = background.convert()
background.fill((70, 70, 70))

# Blit à la fenêtre
fenetre.blit(background, (0, 0))
pygame.display.flip()

# Boucle
continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    
    fenetre.blit(background, (0, 0))
    
    pygame.draw.rect(fenetre, (0, 0, 0), ((W-lar)/2, (H-lon)/2, lar, lon), 10)
    pygame.draw.circle(fenetre, (0, 0, 0), pygame.mouse.get_pos(), 20)
    
    pygame.display.flip()
    
