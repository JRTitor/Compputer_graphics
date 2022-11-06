import pygame
import numpy as np
from pygame.locals import *
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from OpenGL.GL import *
from OpenGL.GLU import *

def get_xyz(r_outter=2, r_inner=1, nt=5, a=00.5, h=1):
    def cylinder(r, a=0, nt=5, h=1):
        theta = np.linspace(-np.pi/2, np.pi/2, nt)
        v = np.ones(nt) * h
        x = r*np.cos(theta) - a
        y = r*np.sin(theta)
        z = v
        return x, y, z

    x, y, z = cylinder(r_outter, nt=nt, h=h)
    x_1, y_1, z_1 = cylinder(r_outter, nt=nt, h=h)
    z_1 = np.zeros_like(z_1)
    x = np.concatenate((x, x_1[::-1]), axis=0)
    y = np.concatenate((y, y_1[::-1]), axis=0)
    z = np.concatenate((z, z_1[::-1]), axis=0)

    x_2, y_2, z_2 = cylinder(r_inner, nt=nt, a=a, h=h)
    x_3, y_3, z_3 = cylinder(r_inner, nt=nt, a=a, h=h)
    z_3 = np.zeros_like(z_3)
    x_2 = np.concatenate((x_2, x_3[::-1]), axis=0)
    y_2 = np.concatenate((y_2, y_3[::-1]), axis=0)
    z_2 = np.concatenate((z_2, z_3[::-1]), axis=0)

    x = np.concatenate((x, x_2), axis=0)
    y = np.concatenate((y, y_2), axis=0)
    z = np.concatenate((z, z_2), axis=0)

    return x, y, z

def get_verticies(x, y, z):
    verticies = []
    for i in range(x.shape[0]):
        verticies.append(tuple([x[i], y[i], z[i]]))
    return tuple(verticies)

def get_edges(x):
    edges = []
    size = x.shape[0]
    line = int(size / 4)
    i = 0
    j = 1
    while (j < size):
        if i == 2* line - 1:
            i += 1
            j += 1
            continue
        edges.append(tuple([i, j]))
        i += 1
        j += 1
    
    edges.append(tuple([0 , 2*line - 1]))
    edges.append(tuple([0 , 2*line]))
    edges.append(tuple([2*line - 1, 4*line - 1]))
    edges.append(tuple([2*line, 4*line - 1]))
    edges.append(tuple([line-1, 3*line-1]))
    edges.append(tuple([line, 3*line]))
    return tuple(edges)

#global variables
x, y, z = get_xyz()
verticies = get_verticies(x, y, z)
edges = get_edges(x)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )
surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()



def main():
    #n = int(input())
    pygame.init()
    display = (800,600)
    #slider = Slider(display, 50, 50, 400, 40, min=3, max=100, step=1)
    #output = TextBox(display, 475, 200, 50, 50, fontSize=30)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0,0, -10)

    glRotatef(30, 2, 1, 0)

    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)

                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)
                if event.key == pygame.K_x:
                    glRotatef(30, 1, 0, 0)
                if event.key == pygame.K_y:
                    glRotatef(30, 0, 1, 0)
                if event.key == pygame.K_z:
                    glRotatef(30, 0, 0, 1)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)

        #glRotatef(1, 3, 1, 1)
        #output.setText(slider.getValue())
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)



if __name__ == '__main__':
    main()

