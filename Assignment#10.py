import pygame
# Play a music
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('wow.mp3')
pygame.mixer.music.play()
pygame.event.wait()


