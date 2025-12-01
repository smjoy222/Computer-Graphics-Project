from OpenGL.GL import *
import random
import math


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
        x = cx + math.cos(angle) * 420
        y = cy + math.sin(angle) * 120
        alpha = 0.12 * (1.0 - i/steps*0.7)
        glColor4f(0.2, 0.22, 0.35, alpha)
        glVertex2f(x, y)
    glEnd()

    glDisable(GL_BLEND)

def draw_stars():
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

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h