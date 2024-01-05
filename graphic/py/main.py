import pygame as pg
from OpenGL.GL import *
from OpenGL.GL import shaders
from math import sin, cos, radians


class App:
    def __init__(self):
        self._set_up_pygame()
        self._set_up_timer()
        self._set_up_opengl()
        self._create_union_jack()
        self._create_rotated_cross()
        self._create_white_cross()
        self._create_rotated_white_cross()
        self._create_shader_program()

    def _set_up_pygame(self):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_CORE)
        self.display = pg.display.set_mode((1024, 480), pg.OPENGL | pg.DOUBLEBUF)

    def _set_up_timer(self):
        self.clock = pg.time.Clock()

    def _set_up_opengl(self):
        glClearColor(0.0, 0.33, 0.71, 1.0)  # Синий фон

    def _create_union_jack(self):
        # Создание координат для перекрестья (Union Jack)
        cross_vertices = [
            # Горизонтальные полосы
            -1, 0.08,
            1, 0.08,
            -1, -0.08,
            1, -0.08,

            # Вертикальные полосы
            -0.08, 1,
            0.08, 1,
            -0.08, -1,
            0.08, -1,

        ]
        # rotated_cross = [

        # ]
        self.cross_indices = [
            0, 1, 2,
            1, 2, 3,
            4, 5, 6,
            5, 6, 7,
            8, 9, 10,
            9, 10, 11
        ]

        self.vao_cross = glGenVertexArrays(1)
        glBindVertexArray(self.vao_cross)

        self.vbo_union_jack = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo_union_jack)
        glBufferData(GL_ARRAY_BUFFER, len(cross_vertices) * 4,
                     (GLfloat * len(cross_vertices))(*cross_vertices), GL_STATIC_DRAW)

        self.ebo_union_jack = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo_union_jack)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(self.cross_indices) * 4,
                     (GLuint * len(self.cross_indices))(*self.cross_indices), GL_STATIC_DRAW)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glBindVertexArray(0)

        # Создание координат для перекрестья (Union Jack)
        cross_white_vertices = [
            # Горизонтальные полосы
            -1, 0.2,
            1, 0.2,
            -1, -0.2,
            1, -0.2,

            # Вертикальные полосы
            -0.2, 1,
            0.2, 1,
            -0.2, -1,
            0.2, -1,

        ]
        self.cross_white_indices = [
            0, 1, 2,
            1, 2, 3,
            4, 5, 6,
            5, 6, 7,
            8, 9, 10,
            9, 10, 11
        ]

        self.vao_white_cross = glGenVertexArrays(1)
        glBindVertexArray(self.vao_white_cross)

        self.vbo_white_union_jack = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo_white_union_jack)
        glBufferData(GL_ARRAY_BUFFER, len(cross_white_vertices) * 4,
                     (GLfloat * len(cross_white_vertices))(*cross_white_vertices), GL_STATIC_DRAW)

        self.ebo__white_union_jack = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo__white_union_jack)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(self.cross_white_indices) * 4,
                     (GLuint * len(self.cross_white_indices))(*self.cross_white_indices), GL_STATIC_DRAW)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glBindVertexArray(0)

    def _create_rotated_cross(self):
        # Create vertices for the rotated cross
        angle = 45  # Угол поворота в градусах
        rotation_matrix = [
            cos(radians(angle)), -sin(radians(angle)),
            sin(radians(angle)), cos(radians(angle))
        ]

        window_width, window_height = 1024, 480  # Ширина и высота окна

        # Вычислите половину ширины и высоты окна
        half_width = window_width / 2
        half_height = window_height / 2

        cross_vertices = [
            # Горизонтальные полосы
            -half_width, 0.025,  # Лево
            half_width, 0.025,  # Право
            -half_width, -0.025,  # Лево
            half_width, -0.025,  # Право

            # Вертикальные полосы
            -0.025, half_height,  # Верх
            0.025, half_height,  # Низ
            -0.025, -half_height,  # Верх
            0.025, -half_height,  # Низ
        ]

        for i in range(len(cross_vertices) // 2):
            x, y = cross_vertices[i * 2], cross_vertices[i * 2 + 1]
            cross_vertices[i * 2] = rotation_matrix[0] * x + rotation_matrix[1] * y
            cross_vertices[i * 2 + 1] = rotation_matrix[2] * x + rotation_matrix[3] * y

        self.rotated_cross_indices = [
            0, 1, 2,
            1, 2, 3,
            4, 5, 6,
            5, 6, 7,
        ]

        self.vao_rotated_cross = glGenVertexArrays(1)
        glBindVertexArray(self.vao_rotated_cross)

        self.vbo_rotated_cross = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo_rotated_cross)
        glBufferData(GL_ARRAY_BUFFER, len(cross_vertices) * 4,
                     (GLfloat * len(cross_vertices))(*cross_vertices), GL_STATIC_DRAW)

        self.ebo_rotated_cross = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo_rotated_cross)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(self.rotated_cross_indices) * 4,
                     (GLuint * len(self.rotated_cross_indices))(*self.rotated_cross_indices), GL_STATIC_DRAW)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glBindVertexArray(0)

    def _create_rotated_white_cross(self):
        angle = 45  # Угол поворота в градусах
        rotation_matrix = [
            cos(radians(angle)), -sin(radians(angle)),
            sin(radians(angle)), cos(radians(angle))
        ]

        window_width, window_height = 1024, 720  # Ширина и высота окна

        # Вычислите половину ширины и высоты окна
        half_width = window_width / 2
        half_height = window_height / 2

        rotated_white_cross_vertices = [
            # Горизонтальные полосы
            -half_width, 0.1,  # Лево
            half_width, 0.1,  # Право
            -half_width, -0.1,  # Лево
            half_width, -0.1,  # Право

            # Вертикальные полосы
            -0.1, half_height,  # Верх
            0.1, half_height,  # Низ
            -0.1, -half_height,  # Верх
            0.1, -half_height,  # Низ
        ]

        for i in range(len(rotated_white_cross_vertices) // 2):
            x, y = rotated_white_cross_vertices[i * 2], rotated_white_cross_vertices[i * 2 + 1]
            rotated_white_cross_vertices[i * 2] = rotation_matrix[0] * x + rotation_matrix[1] * y
            rotated_white_cross_vertices[i * 2 + 1] = rotation_matrix[2] * x + rotation_matrix[3] * y

        self.rotated_white_cross_indices = [
            0, 1, 2,
            1, 2, 3,
            4, 5, 6,
            5, 6, 7,
        ]

        self.vao_rotated_white_cross = glGenVertexArrays(1)
        glBindVertexArray(self.vao_rotated_white_cross)

        self.vbo_rotated_white_cross = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo_rotated_white_cross)
        glBufferData(GL_ARRAY_BUFFER, len(rotated_white_cross_vertices) * 4,
                     (GLfloat * len(rotated_white_cross_vertices))(*rotated_white_cross_vertices), GL_STATIC_DRAW)

        self.ebo_rotated_white_cross = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo_rotated_white_cross)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(self.rotated_white_cross_indices) * 4,
                     (GLuint * len(self.rotated_white_cross_indices))(*self.rotated_white_cross_indices), GL_STATIC_DRAW)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glBindVertexArray(0)

    def _create_white_cross(self):
        # Создание координат для белого креста
        white_cross_vertices = [
            # Горизонтальные полосы
            -1, 0.15,  # Лево
            1, 0.15,  # Право
            -1, -0.15,  # Лево
            1, -0.15,  # Право

            # Вертикальные полосы
            -0.15, 1,  # Верх
            0.15, 1,  # Низ
            -0.15, -1,  # Верх
            0.15, -1,  # Низ
        ]

        self.white_cross_indices = [
            0, 1, 2,
            1, 2, 3,
            4, 5, 6,
            5, 6, 7,
            8, 9, 10,
            9, 10, 11
        ]

        self.vao_white_cross = glGenVertexArrays(1)
        glBindVertexArray(self.vao_white_cross)

        self.vbo_white_cross = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo_white_cross)
        glBufferData(GL_ARRAY_BUFFER, len(white_cross_vertices) * 4,
                     (GLfloat * len(white_cross_vertices))(*white_cross_vertices), GL_STATIC_DRAW)

        self.ebo_white_cross = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo_white_cross)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(self.white_cross_indices) * 4,
                     (GLuint * len(self.white_cross_indices))(*self.white_cross_indices), GL_STATIC_DRAW)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glBindVertexArray(0)

    def _create_shader_program(self):
        # Компиляция вершинного и фрагментного шейдеров
        vertex_shader = shaders.compileShader("""
        #version 330 core
        in vec2 position;
        void main() {
            gl_Position = vec4(position, 0.0, 1.0);
        }
        """, GL_VERTEX_SHADER)

        fragment_shader = shaders.compileShader("""
        #version 330 core
        out vec4 fragColor;
        void main() {
            fragColor = vec4(1.0, 0.0, 0.0, 1.0);  // Синий цвет для флага Великобритании
        }
        """, GL_FRAGMENT_SHADER)

        white_fragment_shader = shaders.compileShader("""
                #version 330 core
                out vec4 fragColor;
                void main() {
                    fragColor = vec4(1.0, 1.0, 1.0, 1.0);  // Белый цвет для белого креста
                }
                """, GL_FRAGMENT_SHADER)
        # Создание и связывание программы шейдеров
        self.shader_program = shaders.compileProgram(vertex_shader, fragment_shader)
        self.white_shader_program = shaders.compileProgram(vertex_shader, white_fragment_shader)

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            glClear(GL_COLOR_BUFFER_BIT)

            # Рисует повернутый белый крест
            glUseProgram(self.white_shader_program)
            glBindVertexArray(self.vao_rotated_white_cross)
            glDrawElements(GL_TRIANGLES, len(self.rotated_white_cross_indices), GL_UNSIGNED_INT, None)

            # Рисуем красный повернутый крест
            glUseProgram(self.shader_program)
            glBindVertexArray(self.vao_rotated_cross)
            glDrawElements(GL_TRIANGLES, len(self.rotated_cross_indices), GL_UNSIGNED_INT, None)

            # Рисуем белый крест
            glUseProgram(self.white_shader_program)
            glBindVertexArray(self.vao_white_cross)
            glDrawElements(GL_TRIANGLES, len(self.white_cross_indices), GL_UNSIGNED_INT, None)

            # Рисуем красный Union Jack
            glUseProgram(self.shader_program)
            glBindVertexArray(self.vao_cross)
            glDrawElements(GL_TRIANGLES, len(self.cross_indices), GL_UNSIGNED_INT, None)

            pg.display.flip()
            self.clock.tick(60)

        glDeleteProgram(self.shader_program)
        glDeleteProgram(self.white_shader_program)
        glDeleteVertexArrays(1, [self.vao_cross, self.vao_rotated_cross, self.vao_white_cross])
        glDeleteBuffers(1, [self.vbo_union_jack, self.ebo_union_jack, self.vbo_rotated_cross, self.ebo_rotated_cross,
                            self.vbo_white_cross, self.ebo_white_cross])

    def quit(self):
        pg.quit()


if __name__ == "__main__":
    myApp = App()
    myApp.run()
    myApp.quit()
