import pygame
from game import Game

# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana del juego
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Juego de Nave Espacial")

# Crear instancia del juego
game = Game(window)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)  # Limitar el juego a 60 FPS

    # Actualizar el juego
    game.update()

    # Dibujar el juego en la ventana
    game.draw()
    pygame.display.flip()

# Salir del juego
pygame.quit()
