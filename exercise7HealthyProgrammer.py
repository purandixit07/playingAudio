import pygame
import time
pygame.init()
song = "D:\\drive 2\\puran\\Data_science\\python\\1_Chapter_1\\play.mp3"
pygame.mixer.music.load(song)
pygame.mixer.music.play()
time.sleep(10)
print("Bye")
