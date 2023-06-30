import pygame
import random
from player import Player
from projectile import Projectile
from enemy import Enemy

# Configuraciones del juego
window_width = 800
window_height = 600
player_speed = 5
projectile_speed = 5
enemy_speed = 2
player_lives = 3

# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana del juego
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Juego de Nave Espacial")

# Crear instancia del jugador
player = Player(window_width // 2 - 25, window_height - 50, 50, 50, player_speed)

# Lista de proyectiles y enemigos
projectiles = []
enemies = []

# Fuente para el marcador
font = pygame.font.Font(None, 36)

# Función para generar enemigos
def generate_enemies():
    x = random.randint(0, window_width - 50)
    y = -50
    enemy = Enemy(x, y, 50, 50, enemy_speed)
    enemies.append(enemy)

# Función para verificar colisiones
def check_collisions():
    global player_lives

    # Colisiones entre proyectiles y enemigos
    for projectile in projectiles:
        for enemy in enemies:
            if projectile.x < enemy.x + enemy.width and projectile.x + projectile.width > enemy.x and \
               projectile.y < enemy.y + enemy.height and projectile.y + projectile.height > enemy.y:
                projectiles.remove(projectile)
                enemies.remove(enemy)

    # Colisiones entre enemigos y jugador
    for enemy in enemies:
        if enemy.x < player.x + player.width and enemy.x + enemy.width > player.x and \
           enemy.y < player.y + player.height and enemy.y + enemy.height > player.y:
            player_lives -= 1
            enemies.remove(enemy)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)  # Limitar el juego a 60 FPS

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectile = Projectile(player.x + player.width // 2 - 2, player.y, 4, 8, projectile_speed)
                projectiles.append(projectile)

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.move_left()
    if keys[pygame.K_RIGHT] and player.x < window_width - player.width:
        player.move_right()

    # Movimiento de los proyectiles
    for projectile in projectiles:
        projectile.move()
        if projectile.y < 0:
            projectiles.remove(projectile)

    # Generar enemigos
    if len(enemies) < 5:  # Puedes ajustar el número de enemigos según tus necesidades
        generate_enemies()

    # Movimiento de los enemigos
    for enemy in enemies:
        enemy.move_down()
        if enemy.y > window_height:
            enemies.remove(enemy)

    # Verificar colisiones
    check_collisions()

    # Dibujar el juego en la ventana
    window.fill((255, 255, 255))
    player.draw(window)
    for projectile in projectiles:
        projectile.draw(window)
    for enemy in enemies:
        enemy.draw(window)

    # Mostrar marcador de vidas
    lives_text = font.render("Vidas: " + str(player_lives), True, (0, 0, 0))
    window.blit(lives_text, (10, 10))

    pygame.display.flip()

    # Verificar vidas del jugador
    if player_lives <= 0:
        running = False

# Salir del juego
pygame.quit()
