from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

px = 300; py = 300

def drawPlayer():
    glColor3f(1,1,0)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2i(px,py)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawPlayer()
    glutSwapBuffers()

# Here is my keyboard input code
def buttons(key,x,y):
    global px, py
    if key == b'a':
        px -= 5
    if key == b'd':
        px += 5
    if key == b'w':
        py -= 5
    if key == b's':
        py += 5
    glutPostRedisplay()

def init():
    glClearColor(0.3,0.3,0.3,0)
    gluOrtho2D(0,1024,512,0)    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1024, 512)
    display = glutCreateWindow("Raycaster in python")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()

if __name__ == "__main__":
    main()