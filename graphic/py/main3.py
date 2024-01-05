import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def body():
    glPushMatrix()
    glColor4f(0, 0, 1, 1.0)  # Устанавливаем белый цвет для сферы
    glTranslatef(0, 0, 0)  # Перемещаем куб левее начальной позиции
    glScalef(1.0, 1.0, 1.5)  # Масштабирование сферы по оси Z (вытягивание вглубь)
    glutSolidSphere(1, 20, 20)  # Создаем сферу с радиусом 1 и количеством сегментов 20
    glPopMatrix()


def line(x,y,z, scale):
    glPushMatrix()
    glColor4f(0.2, 0.4, 0.5, 1.0)  # Устанавливаем белый цвет для сферы
    glTranslatef(x,y,z)  # Перемещаем куб левее начальной позиции
    glScalef(0.5 * scale, 0.5 * scale, 2.5)  # Масштабируем куб по X на 10, по Y и Z на 0.1 (очень узкий куб)
    glutSolidCube(1.0) # Создаем сферу с радиусом 1 и количеством сегментов 20
    glPopMatrix()

def blade(x,y,z, rotate):
    glPushMatrix()
    glColor4f(0.3, 1, 0.1, 1.0)  # Устанавливаем белый цвет для сферы
    glTranslatef(x, y, z)  # Перемещаем куб левее начальной позиции
    glRotatef(90, 0, 1 * rotate, 0)  # Поворот на 90 градусов вокруг оси X
    glScalef(0.3, 0.01, 5)  # Масштабируем куб по X на 10, по Y и Z на 0.1 (очень узкий куб)
    glutSolidCube(1.0)  # Создаем сферу с радиусом 1 и количеством сегментов 20
    glPopMatrix()

def tailBlade(x,y,z, deg):
    glPushMatrix()
    glColor4f(1, 0, 0.1, 1.0)  # Устанавливаем белый цвет для сферы
    glTranslatef(x, y, z)  # Перемещаем куб левее начальной позиции
    glRotatef(deg, 1, 0, 0)  # Поворот на 90 градусов вокруг оси X
    glScalef(0.01, 0.1, 1)  # Масштабируем куб по X на 10, по Y и Z на 0.1 (очень узкий куб)
    glutSolidCube(1.0)  # Создаем сферу с радиусом 1 и количеством сегментов 20
    glPopMatrix()

def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        # Тело
        body()


        # Хвост
        line(0, 0.0, 2.0, 0.7)

        # Ноги
        line(0.8, -0.8, 0, 0.5)

        line(-0.8, -0.8, 0, 0.5)

        # Вертушки
        blade(0, 1, 0, 0)
        blade(0, 1, 0, 1)

        # Вертушки хвоста
        tailBlade(0.2, 0, 3, 30)
        tailBlade(0.2, 0, 3, 120)


        pygame.display.flip()
        pygame.time.wait(10)


def main():
    pygame.init()
    display = (1920, 1080)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glutInit()  # Инициализация библиотеки glut


if __name__ == "__main__":
    main()
    run()
