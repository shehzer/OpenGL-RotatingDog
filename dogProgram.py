import sys

import pygame
import numpy as np
from pygame.locals import QUIT
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL import *

WIDTH = 600
HEIGHT = 600
NUM_DOGS = 8

def ReadFile(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.extend([float(x) for x in line.strip().split()])
    return data

def DrawPolyline(data):
    glBegin(GL_LINE_STRIP)
    for i in range(0, len(data), 2):
        glVertex2f(data[i], data[i + 1])
    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 60, 0, 60, -1, 1)
    glClearColor(1, 1, 1, 1)
    data = ReadFile('dog.txt')
    clock = pygame.time.Clock()
    rotation = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT)
        for i in range(NUM_DOGS):
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

            glTranslatef(30 + (25 * np.cos((45 * np.pi * i) / 180)),
                         30 + (25 * np.sin((45 * np.pi * i) / 180)), 
                         0)
            glRotatef(rotation, 0, 0, 1)

            glColor3f(0, 0, 0)
            DrawPolyline(data)
        
        rotation = (rotation + 1) % 360

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
