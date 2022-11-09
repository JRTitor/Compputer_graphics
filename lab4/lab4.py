import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def make_vertices(r_outter=2, r_inner=1, nt=5, a=00.5, h=1):
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
    x = np.concatenate((x, x_1), axis=0)
    y = np.concatenate((y, y_1), axis=0)
    z = np.concatenate((z, z_1), axis=0)

    x_2, y_2, z_2 = cylinder(r_inner, nt=nt, a=a, h=h)
    x_3, y_3, z_3 = cylinder(r_inner, nt=nt, a=a, h=h)
    z_3 = np.zeros_like(z_3)
    x_2 = np.concatenate((x_2, x_3), axis=0)
    y_2 = np.concatenate((y_2, y_3), axis=0)
    z_2 = np.concatenate((z_2, z_3), axis=0)

    x = np.concatenate((x, x_2), axis=0)
    y = np.concatenate((y, y_2), axis=0)
    z = np.concatenate((z, z_2), axis=0)

    vert = (tuple(x), tuple(y), tuple(z))
    vertices = tuple(map(list, zip(*vert)))
    return vertices

def make_surfaces(nt=5):
    i = np.array([])
    j = np.array([])
    k = np.array([])

    for c in range(nt-1):
        i = np.append(i, c)
        j = np.append(j, c + 1)
        k = np.append(k, c + nt)

    for c in range(nt-1):
        i = np.append(i, c + nt + 1)
        j = np.append(j, c + nt)
        k = np.append(k, c + 1)

    for c in range(nt-1):
        j = np.append(j, c + 2*nt)
        i = np.append(i, c + 2*nt + 1)
        k = np.append(k, c + 3*nt)

    for c in range(nt-1):
        j = np.append(j, c + 3*nt + 1)
        i = np.append(i, c + 3*nt)
        k = np.append(k, c + 2*nt + 1)

    for c in range(nt-1):
        j = np.append(j, 3*nt + c)
        i = np.append(i, c + 3*nt + 1)
        k = np.append(k, c + nt)

    for c in range(nt-1):
        j = np.append(j, c + nt + 1)
        i = np.append(i, c + nt)
        k = np.append(k, c + 3*nt + 1)

    for c in range(nt-1):
        i = np.append(i, c + 2*nt)
        j = np.append(j, c +  2*nt + 1)
        k = np.append(k, c)

    for c in range(nt-1):
        i = np.append(i, c + 1)
        j = np.append(j, c)
        k = np.append(k, c + 2*nt + 1)

    j = np.append(j, 0)
    i = np.append(i, 2*nt)
    k = np.append(k, nt)

    j = np.append(j, 2*nt)
    i = np.append(i, 3*nt)
    k = np.append(k, nt)

    j = np.append(j, nt - 1)
    i = np.append(i, 4*nt - 1)
    k = np.append(k, 3*nt - 1)

    j = np.append(j, nt - 1)
    i = np.append(i, 2*nt - 1)
    k = np.append(k, 4*nt - 1)

    i = i.astype("int")
    k = k.astype("int")
    j = j.astype("int")

    i = tuple(i)
    j = tuple(j)
    k = tuple(k)
    sur = (i, j, k)
    surfaces = list(map(list, zip(*sur)))
    return surfaces

def Cube(r_outter=2, r_inner=1, nt=5, a=00.5, h=1):
    verticies = make_vertices(r_outter=r_outter, r_inner=r_inner, nt=nt, a=a, h=1)
    surfaces = make_surfaces(nt=nt)
    glBegin(GL_TRIANGLES)
    for surface in surfaces:
        for vertex in surface:
            COLOR = ((1, 0, 0))
            glMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE, COLOR)
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0,0, -10)
    glRotatef(25, 2, 1, 0)

    run = True
    approx = 5
    r_outter = 2
    r_inner = 1
    a = 0.05
    h = 1
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
                if event.key == pygame.K_EQUALS:  # approx+ =
                    approx += 1
                if event.key == pygame.K_MINUS:  # approx- -
                    if approx > 3:
                        approx -= 1
                if event.key == pygame.K_h:  #  height+ h
                    h += 1
                if event.key == pygame.K_j:  #  height- j
                    if h > 1:
                        h -= 1
                if event.key == pygame.K_r:  #  r_outter+ r
                    r_outter += 1
                if event.key == pygame.K_t:  #  r_outter- t
                    if r_outter > r_inner + 1:
                        r_outter -= 1  
                if event.key == pygame.K_f:  #  r_inner+ r
                    if r_outter > r_inner + 1:
                        r_inner += 1
                if event.key == pygame.K_g:  #  r_inner- t
                    if r_inner > 1:
                        r_inner -= 1
                if event.key == pygame.K_a:  #  distance_between_routter_and_r_inner+  a
                    a += 0.01
                if event.key == pygame.K_s:  #  distance_between_routter_and_r_inner-  s
                    if a > 0.03:
                        a -= 0.01
  
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glEnable(GL_CULL_FACE)
        glCullFace(GL_FRONT)

        glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 2, 1))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        Cube(r_outter=r_outter, r_inner=r_inner, nt=approx, a=a, h=1)
       
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
