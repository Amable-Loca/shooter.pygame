# Guerra de las Galaxias

Este código implementa un juego de disparos en 2D utilizando la librería Pygame, donde el jugador controla una nave que debe disparar a enemigos y esquivar meteoritos. A continuación se detallan los componentes y su funcionamiento:

Constantes y configuración inicial
Dimensiones de pantalla:
ANCHO y ALTO definen el tamaño de la ventana del juego.
Imágenes y colores:
Se definen las rutas de imágenes y algunos colores para el fondo, texto y otros elementos visuales.
Pantalla y fuentes:
Se inicializa la pantalla del juego y las fuentes para los textos.
Variables de juego
Puntaje ( poins), fallos ( misses), vidas ( vidas):
Llevan la cuenta del progreso del jugador.
Clases principales
GameSprite:
Clase base para todos los sprites (jugador, enemigos, balas, asteroides). Gestiona la carga de imágenes, posición y el método resetpara dibujarse en pantalla.
Jugador:
Hereda de GameSprite. Permite al jugador moverse a la izquierda y derecha con las teclas 'A' y 'D'. El método firecrea balas nuevas.
Enemigo:
Hereda de GameSprite. Se mueve hacia abajo constantemente. Si sale de la pantalla, suma un fallo y reaparece en una posición aleatoria arriba.
Bullet (Bala):
Hereda de GameSprite. Se mueve hacia arriba y se elimina si sale de la pantalla.
Inicialización de Entidades
Jugador:
Se crea la nave principal controlada por el usuario.
Grupos de Sprites:
Se crean grupos para las balas, enemigos (alienígenas) y asteroides, inicializándolos con posiciones y velocidades aleatorias.
Bucle principal del juego
Eventos:
Se detecta el cierre de la ventana y la pulsación de la barra espaciadora (para disparar).
Reinicio:
Si el juego termina, se puede reiniciar con la tecla 'R'.
Actualización y dibujo:
Si el juego está en curso, se actualizan y dibujan todos los elementos: fondo, texto de puntuación, fallos y vidas, jugador, enemigos, balas y asteroides.
Colisiones:
Balas vs. enemigos: al colisionar, aumentan los puntos y aparece un nuevo enemigo.
Enemigos vs. jugador: reduce una vida y aparece un nuevo enemigo.
Condiciones de fin:
Perder: Si los fallos llegan a 10 o las vidas a 0, se muestra la pantalla de "Game Over".
Ganar: Si el puntaje llega a 50, se muestra la pantalla de victoria.
Actualización de pantalla:
Se actualiza la pantalla y el juego corre a 60 FPS.
