import pygame
from pygame.locals import *
from math import sin, cos, pi
from OpenGL.GL import *
from OpenGL.GLU import *

vertices_A = (
    (-1, 0, 0),  # Вершина A1ц
    (1, 0, 0),  # Вершина A2
    (0, 1, 0)  # Вершина A3
)

vertices_B = (
    (-1, 0, 0.5),  # Вершина B1 (на глубине 1 по Z)
    (1, 0, 0.5),  # Вершина B2 (на глубине 1 по Z)
    (0, 1, 0.5)  # Вершина B3 (на глубине 1 по Z)
)


def Triangle(vertices_A, vertices_B):
    # Стороны треугольника A
    sides_A = (
        (0, 1),  # Сторона A1A2
        (1, 2),  # Сторона A2A3
        (2, 0)  # Сторона A3A1
    )

    # Стороны треугольника B
    sides_B = (
        (0, 1),  # Сторона B1B2
        (1, 2),  # Сторона B2B3
        (2, 0)  # Сторона B3B1
    )

    # Соединяющие рёбра между треугольниками
    connecting_edges = (
        (vertices_A[0], vertices_B[0]),  # Ребро A1B1
        (vertices_A[1], vertices_B[1]),  # Ребро A2B2
        (vertices_A[2], vertices_B[2])  # Ребро A3B3
    )

    glBegin(GL_LINES)

    # Рисуем треугольник A
    for side in sides_A:
        for vertex in side:
            glVertex3fv(vertices_A[vertex])

    # Рисуем треугольник B
    for side in sides_B:
        for vertex in side:
            glVertex3fv(vertices_B[vertex])

    # Рисуем соединяющие рёбра
    for edge in connecting_edges:
        for vertex in edge:
            glVertex3fv(vertex)

    glEnd()


def Cube():
    cubeVerticies = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

    cubeSurfaces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    glBegin(GL_QUADS)
    glColor3f(0.647, 0.164, 0.164)
    for surface in cubeSurfaces:
        for vertex in surface:
            glVertex3fv(cubeVerticies[vertex])
    glEnd()

def drawCuboid(width, height, depth):
    half_width = width / 2
    half_height = height / 2
    half_depth = depth / 2

    vertices = (
        (-half_width, -half_height, -half_depth),
        (half_width, -half_height, -half_depth),
        (half_width, half_height, -half_depth),
        (-half_width, half_height, -half_depth),
        (-half_width, -half_height, half_depth),
        (half_width, -half_height, half_depth),
        (half_width, half_height, half_depth),
        (-half_width, half_height, half_depth)
    )

    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7)
    )

    faces = (
        (0, 1, 2, 3),
        (3, 2, 6, 7),
        (7, 6, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 6, 2),
        (4, 0, 3, 7)
    )

    glBegin(GL_LINE_LOOP)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def drawCylinder(radius, height, num_segments=30):
    glBegin(GL_LINES)

    for i in range(num_segments + 1):
        theta = 2 * pi * i / num_segments
        x = radius * cos(theta)
        y = radius * sin(theta)
        z = height / 2

        glVertex3f(x, y, z)
        glVertex3f(x, y, -z)

    glEnd()

    # Draw the top and bottom circles of the cylinder
    glBegin(GL_LINES)

    for i in range(num_segments):
        theta1 = 2 * pi * i / num_segments
        x1 = radius * cos(theta1)
        y1 = radius * sin(theta1)
        z1 = height / 2

        theta2 = 2 * pi * (i + 1) / num_segments
        x2 = radius * cos(theta2)
        y2 = radius * sin(theta2)
        z2 = height / 2

        glVertex3f(x1, y1, z1)
        glVertex3f(x2, y2, z2)

        glVertex3f(x1, y1, -z1)
        glVertex3f(x2, y2, -z2)

    glEnd()


def main():
    pygame.init()
    display = (1920, 1080)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Гусеница
        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)
        glTranslatef(0, -1.2, 1)  # Смещение влево
        Triangle(vertices_A, vertices_B)
        glPopMatrix()

        # Гусеница
        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)
        glTranslatef(0, -1.2, -1.5)  # Смещение вправо
        glColor3f(1.0, 1.0, 1.0)  # Установка белого цвета
        Triangle(vertices_A, vertices_B)
        glPopMatrix()


        # Тело
        Cube()


        # Рука
        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)
        glTranslatef(1, 0.5, 1)
        drawCuboid(2, 0.1, 0.1)  # Задайте ширину, высоту и глубину четырехугольника
        glPopMatrix()

        # Рука
        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)
        glTranslatef(1, 0.5, -1)
        drawCuboid(2, 0.1, 0.1)  # Задайте ширину, высоту и глубину четырехугольника
        glPopMatrix()

        # Шея
        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)
        glTranslatef(0, 1, 0)
        drawCuboid(0.1, 0.6, 0.1)  # Задайте ширину, высоту и глубину четырехугольника
        glPopMatrix()



        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)
        glTranslatef(0, 1.4, -0.3)  # Позиция цилиндра
        glRotatef(90, 0, 1, 0)
        drawCylinder(0.3, 1.0)  # Задайте радиус и высоту цилиндра
        glPopMatrix()

        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)
        glTranslatef(0, 1.4, 0.3)  # Позиция цилиндра
        glRotatef(90, 0, 1, 0)
        drawCylinder(0.3, 1.0)  # Задайте радиус и высоту цилиндра
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


main()
