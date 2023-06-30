# Juego de Nave Espacial

Este es un simple juego de nave espacial desarrollado utilizando la biblioteca Pygame en Python. El jugador controla una nave espacial y debe disparar a los enemigos que aparecen en la pantalla. El objetivo es obtener la mayor puntuación posible evitando que los enemigos colisionen con la nave.

## Requisitos

- Python 3.8 o superior
- Pygame 2.0.1

## Instalación

1. Clona el repositorio o descarga los archivos del proyecto.
2. Asegúrate de tener Python instalado en tu sistema.
3. Instala la biblioteca Pygame ejecutando el siguiente comando:
```python
pip install pygame
```


## Cómo jugar

1. Ejecuta el archivo para iniciar el juego con este comando
```python
python3 main.py
```
2. Controla la nave espacial utilizando las teclas de dirección izquierda y derecha.
3. Dispara proyectiles presionando la tecla de espacio.
4. Evita que los enemigos colisionen con tu nave. Si ocurre una colisión, perderás una vida.
5. Obtén puntos destruyendo a los enemigos con tus proyectiles.
6. El juego finaliza cuando pierdes todas tus vidas.
7. Intenta obtener la mayor puntuación posible y superar tu récord personal.

## Archivos del proyecto

- `main.py`: Archivo principal que contiene el bucle del juego y la lógica principal.
- `player.py`: Clase que representa al jugador y controla su movimiento.
- `projectile.py`: Clase que define los proyectiles y su movimiento.
- `enemy.py`: Clase que representa a los enemigos y su movimiento.
- `player.png`: Imagen de la nave espacial del jugador.
- `enemy.png`: Imagen de los enemigos.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el juego, puedes enviar un pull request con tus cambios.

## Licencia

Este proyecto está bajo la [licencia MIT](https://opensource.org/licenses/MIT).