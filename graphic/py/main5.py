import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

screen_width = 750
screen_height = 650

pygame.init()
display = (screen_width, screen_height)
pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()
FPS = 60

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -10)

# Включаем использование тумана
glEnable(GL_FOG)

# Устанавливаем режим тумана (экспоненциальный)
glFogi(GL_FOG_MODE, GL_EXP)

# Устанавливаем плотность тумана
glFogf(GL_FOG_DENSITY, 4)

# Устанавливаем цвет тумана (серый)
glFogfv(GL_FOG_COLOR, [0.5, 0.5, 0.5, 1.0])

def dodecahedron():
    glutWireDodecahedron()
    glRotatef(1.0, 1.0, 0.0, 0.0)

def main_game():
    glutInit()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        dodecahedron()
        pygame.display.flip()
        clock.tick(FPS)

main_game()
