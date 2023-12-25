
#3-4 + 5(поворот фигуры)

# import json
# import math
# import sys
# from os import environ
#
# environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
#
# import pygame
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from pygame.locals import *
#
#
# def draw_truncated_elliptical_cone(
#         major_radius_bottom: float = 1.0,
#         minor_radius_bottom: float = 0.5,
#         major_radius_top: float = 0.5,
#         minor_radius_top: float = 0.25,
#         height: float = 1.0,
#         sides: int = 100) -> None:
#     angle_step = 360 / sides
#
#     glBegin(GL_QUAD_STRIP)
#     for i in range(sides + 1):
#         angle = i * angle_step
#         x1_bottom = major_radius_bottom * math.cos(math.radians(angle))
#         y1_bottom = minor_radius_bottom * math.sin(math.radians(angle))
#         x1_top = major_radius_top * math.cos(math.radians(angle))
#         y1_top = minor_radius_top * math.sin(math.radians(angle))
#
#         x2_bottom = major_radius_bottom * math.cos(math.radians(angle + angle_step))
#         y2_bottom = minor_radius_bottom * math.sin(math.radians(angle + angle_step))
#         x2_top = major_radius_top * math.cos(math.radians(angle + angle_step))
#         y2_top = minor_radius_top * math.sin(math.radians(angle + angle_step))
#
#         glVertex3f(x1_bottom, y1_bottom, -height / 2.0)
#         glVertex3f(x1_top, y1_top, height / 2.0)
#         glVertex3f(x2_bottom, y2_bottom, -height / 2.0)
#         glVertex3f(x2_top, y2_top, height / 2.0)
#
#     glEnd()
#
#     # Create the bottom base
#     glBegin(GL_TRIANGLE_FAN)
#     glVertex3f(0.0, 0.0, -height / 2.0)
#     for i in range(sides + 1):
#         angle = i * angle_step
#         x1_bottom = major_radius_bottom * math.cos(math.radians(angle))
#         y1_bottom = minor_radius_bottom * math.sin(math.radians(angle))
#         glVertex3f(x1_bottom, y1_bottom, -height / 2.0)
#     glEnd()
#
#     # Create the top base
#     glBegin(GL_TRIANGLE_FAN)
#     glVertex3f(0.0, 0.0, height / 2.0)
#     for i in range(sides + 1):
#         angle = i * angle_step
#         x1_top = major_radius_top * math.cos(math.radians(angle))
#         y1_top = minor_radius_top * math.sin(math.radians(angle))
#         glVertex3f(x1_top, y1_top, height / 2.0)
#     glEnd()
#
#
# def start_render(appsettings_path: str = None):
#     if appsettings_path is None:
#         major_radius_bottom = 1.0
#         minor_radius_bottom = 0.5
#         major_radius_top = 0.5
#         minor_radius_top = 0.25
#         height = 1.0
#         sides = 100
#         color = [1.0, 0, 0, 1.0]
#     else:
#         with open(appsettings_path, encoding='UTF-8') as app_s:
#             appsettings = json.load(app_s)
#         major_radius_bottom = appsettings['major_radius_bottom']
#         minor_radius_bottom = appsettings['minor_radius_bottom']
#         major_radius_top = appsettings['major_radius_top']
#         minor_radius_top = appsettings['minor_radius_top']
#         height = appsettings['height']
#         sides = appsettings['sides']
#         color = appsettings['color']
#     flag = True
#
#     pygame.init()
#     display = (720, 720)
#     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
#     gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
#     glTranslatef(0.0, 0.0, -5.0)
#
#     glEnable(GL_LIGHTING)
#     glEnable(GL_DEPTH_TEST)
#
#     glMaterial(GL_FRONT, GL_DIFFUSE, color)
#
#     light_position = [0, 1, 0, 3]
#     rotation_delta = 0
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     rotation_delta = 1
#                 elif event.key == pygame.K_RIGHT:
#                     rotation_delta = -1
#                 elif event.key == pygame.K_w:
#                     light_position[2] += 0.2
#                 elif event.key == pygame.K_a:
#                     light_position[3] -= 0.2
#                 elif event.key == pygame.K_s:
#                     light_position[2] -= 0.2
#                 elif event.key == pygame.K_d:
#                     light_position[3] += 0.2
#             elif event.type == pygame.KEYUP:
#
#                 if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
#                     rotation_delta = 0
#
#         if flag:
#             glRotatef(110, 1, 0, 0)
#             flag = False
#
#         glRotatef(rotation_delta, 1, 0, 0)
#
#         glLightfv(GL_LIGHT0, GL_POSITION, light_position)
#         glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 0.2])
#         glEnable(GL_LIGHT0)
#
#         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#         draw_truncated_elliptical_cone(major_radius_bottom, minor_radius_bottom, major_radius_top, minor_radius_top,
#                                        height, sides)
#         pygame.display.flip()
#         pygame.time.wait(10)
#
#
# if __name__ == '__main__':
#     try:
#         if len(sys.argv) > 1:
#             start_render(sys.argv[1])
#         else:
#             start_render()
#
#     except OSError:
#         print('OSError: could not open settings file!')
#     except json.decoder.JSONDecodeError:
#         print('JSONDecodeError: settings file is empty!')


#------------------------


#лр 6
import json
import math
import sys
from os import environ
import time
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


def draw_truncated_elliptical_cone(
        major_radius_bottom: float = 1.0,
        minor_radius_bottom: float = 0.5,
        major_radius_top: float = 0.5,
        minor_radius_top: float = 0.25,
        height: float = 1.0,
        sides: int = 100) -> None:
    angle_step = 360 / sides

    glBegin(GL_QUAD_STRIP)
    for i in range(sides + 1):
        angle = i * angle_step
        x1_bottom = major_radius_bottom * math.cos(math.radians(angle))
        y1_bottom = minor_radius_bottom * math.sin(math.radians(angle))
        x1_top = major_radius_top * math.cos(math.radians(angle))
        y1_top = minor_radius_top * math.sin(math.radians(angle))

        x2_bottom = major_radius_bottom * math.cos(math.radians(angle + angle_step))
        y2_bottom = minor_radius_bottom * math.sin(math.radians(angle + angle_step))
        x2_top = major_radius_top * math.cos(math.radians(angle + angle_step))
        y2_top = minor_radius_top * math.sin(math.radians(angle + angle_step))

        glVertex3f(x1_bottom, y1_bottom, -height / 2.0)
        glVertex3f(x1_top, y1_top, height / 2.0)
        glVertex3f(x2_bottom, y2_bottom, -height / 2.0)
        glVertex3f(x2_top, y2_top, height / 2.0)

    glEnd()

    # Create the bottom base
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, -height / 2.0)
    for i in range(sides + 1):
        angle = i * angle_step
        x1_bottom = major_radius_bottom * math.cos(math.radians(angle))
        y1_bottom = minor_radius_bottom * math.sin(math.radians(angle))
        glVertex3f(x1_bottom, y1_bottom, -height / 2.0)
    glEnd()

    # Create the top base
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, height / 2.0)
    for i in range(sides + 1):
        angle = i * angle_step
        x1_top = major_radius_top * math.cos(math.radians(angle))
        y1_top = minor_radius_top * math.sin(math.radians(angle))
        glVertex3f(x1_top, y1_top, height / 2.0)
    glEnd()


def start_render(appsettings_path: str = None):
    if appsettings_path is None:
        major_radius_bottom = 1.0
        minor_radius_bottom = 0.5
        major_radius_top = 0.5
        minor_radius_top = 0.25
        height = 1.0
        sides = 100
        color = [1.0, 0, 0, 1.0]
    else:
        with open(appsettings_path, encoding='UTF-8') as app_s:
            appsettings = json.load(app_s)
        major_radius_bottom = appsettings['major_radius_bottom']
        minor_radius_bottom = appsettings['minor_radius_bottom']
        major_radius_top = appsettings['major_radius_top']
        minor_radius_top = appsettings['minor_radius_top']
        height = appsettings['height']
        sides = appsettings['sides']
        color = appsettings['color']

    flag = True

    pygame.init()
    display = (720, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)

    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)

    light_position = [0, 1, 0, 3]
    rotation_delta = 0

    color_cycle_duration = 5.0  # seconds for one full color cycle
    start_time = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotation_delta = 1
                elif event.key == pygame.K_RIGHT:
                    rotation_delta = -1
                elif event.key == pygame.K_w:
                    light_position[2] += 0.2
                elif event.key == pygame.K_a:
                    light_position[3] -= 0.2
                elif event.key == pygame.K_s:
                    light_position[2] -= 0.2
                elif event.key == pygame.K_d:
                    light_position[3] += 0.2
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    rotation_delta = 0

        current_time = time.time()
        elapsed_time = current_time - start_time

        # Calculate color based on a sinusoidal function
        color_value = 0.5 + 0.5 * math.sin(2 * math.pi * elapsed_time / color_cycle_duration)
        color = [color_value, 0, 0, 1.0]

        glMaterial(GL_FRONT, GL_DIFFUSE, color)

        if flag:
            glRotatef(110, 1, 0, 0)
            flag = False

        glRotatef(rotation_delta, 1, 0, 0)

        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 0.2])
        glEnable(GL_LIGHT0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_truncated_elliptical_cone(major_radius_bottom, minor_radius_bottom, major_radius_top, minor_radius_top,
                                       height, sides)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            start_render(sys.argv[1])
        else:
            start_render()
    except OSError:
        print('OSError: could not open settings file!')
    except json.decoder.JSONDecodeError:
        print('JSONDecodeError: settings file is empty!')
