from OpenGL.GL import *
import math


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

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

def update_sun_angle():
    global sun_angle
    sun_angle = (sun_angle + 2) % 360

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h