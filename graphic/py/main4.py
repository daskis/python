import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def body():
    glPushMatrix()
    glColor4f(0, 0, 0, 1.0)
    glTranslatef(0, 0, 0)
    glutSolidCube(2.0)  # Используем куб
    glPopMatrix()
    glRotatef(0.5, 1.0, 1.0, 0)


def interpolate_points(point1, point2, t):
    return [
        point1[i] * (1 - t) + point2[i] * t for i in range(len(point1))
    ]


def run():
    light_positions = [
        [0.0, 30.0, 0.0, 1.0],
        [30.0, 30.0, 30.0, 1.0],
        [-30.0, 30.0, 30.0, 1.0],
        [-30.0, 30.0, -30.0, 1.0],
        [30.0, 30.0, -30.0, 1.0],
        [0.0, 30.0, 0.0, 1.0]
    ]
    point_index = 0
    light_speed = 0.005
    t = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)

        light_position = interpolate_points(light_positions[point_index],
                                            light_positions[(point_index + 1) % len(light_positions)], t)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        body()

        pygame.display.flip()
        pygame.time.wait(10)

        t += light_speed
        if t >= 1:
            t = 0
            point_index = (point_index + 1) % len(light_positions)


def main():
    pygame.init()
    display = (1920, 1080)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glutInit()
    run()


if __name__ == "__main__":
    main()
