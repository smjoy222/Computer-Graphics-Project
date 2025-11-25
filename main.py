from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
#eikhn a background banate shudu random and opengl use krsi,glow colour er jonno just colour define korsi
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

random.seed(123)  

stars = []

def init_stars():
    global stars
    stars = []

   
    for _ in range(180): 
        x = random.randint(0, WINDOW_WIDTH)
        y = random.randint(0, WINDOW_HEIGHT)
        size = random.choice([1.0, 1.3, 1.6, 2.0])
        brightness = random.uniform(0.5, 0.9)
        stars.append((x, y, size, brightness))

    # loop use kore random place a draw krsi no extra libray just opengl and random function
    for _ in range(9):
        x = random.randint(100, WINDOW_WIDTH - 100)
        y = random.randint(80, WINDOW_HEIGHT - 80)
        size = random.uniform(2.8, 4.5)
        brightness = 1.0
        stars.append((x, y, size, brightness))

def draw_milky_way_glow():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glBegin(GL_TRIANGLE_FAN)
    cx, cy = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
    glColor4f(0.25, 0.28, 0.4, 0.12)         
    glVertex2f(cx, cy)

    steps = 100
    for i in range(steps + 1):
        angle = 2.0 * math.pi * i / steps
        # Wide horizontal ellipse
        x = cx + math.cos(angle) * 420
        y = cy + math.sin(angle) * 120
        alpha = 0.12 * (1.0 - i/steps*0.7)
        glColor4f(0.2, 0.22, 0.35, alpha)
        glVertex2f(x, y)
    glEnd()

    glDisable(GL_BLEND)


#-------sun draw suru----------
sun_angle = 0

def draw_filled_circle(cx, cy, r, segments=32):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(segments + 1):
        a = 2 * math.pi * i / segments
        glVertex2f(cx + math.cos(a) * r, cy + math.sin(a) * r)
    glEnd()

def draw_sun():
    global sun_angle
    sx = WINDOW_WIDTH - 120
    sy = WINDOW_HEIGHT - 100
    r = 40

    glColor3f(1.0, 0.85, 0.1)
    draw_filled_circle(sx, sy, r, 48)

    glPushMatrix()
    glTranslatef(sx, sy, 0)
    glRotatef(sun_angle, 0, 0, 1)

    N = 8
    inner = r + 5
    outer = r + 22

    glColor3f(1.0, 0.8, 0.1)
    for i in range(N):
        ang = 2 * math.pi * i / N
        left = ang - 0.15
        right = ang + 0.15

        glBegin(GL_TRIANGLES)
        glVertex2f(math.cos(left) * inner, math.sin(left) * inner)
        glVertex2f(math.cos(right) * inner, math.sin(right) * inner)
        glVertex2f(math.cos(ang) * outer, math.sin(ang) * outer)
        glEnd()
    glPopMatrix()

#----------sun draw sesh-------
def display():
    glClear(GL_COLOR_BUFFER_BIT)

   
    draw_milky_way_glow()

  
    for (x, y, size, brightness) in stars:
        glPointSize(size)
        if size > 3.0:
            glColor3f(1.0, 1.0, 1.0)                  
        elif brightness > 0.8:
            glColor3f(0.9, 0.92, 1.0)
        else:
            glColor3f(brightness, brightness*0.94, brightness + 0.08)

        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
    draw_sun()  #sun function call
    glutSwapBuffers()

#sun animation
def animate(v):
    global sun_angle
    sun_angle = (sun_angle + 2) % 360
    glutPostRedisplay()
    glutTimerFunc(16, animate, 0)


def reshape(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Calm Starry Sky - Pure OpenGL")

    glClearColor(0.0, 0.0, 0.03, 1.0)   # almost pure black
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    init_stars()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, animate, 0) 
    glutMainLoop()

if __name__ == "__main__":
    main()