from OpenGL.GL import *
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h

def draw_filled_circle(cx, cy, r, segments=32):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(segments + 1):
        a = 2.0 * math.pi * i / segments
        glVertex2f(cx + math.cos(a) * r, cy + math.sin(a) * r)
    glEnd()

def draw_moon():
    """Draw a moon in the top right corner"""
    mx = WINDOW_WIDTH - 120
    my = WINDOW_HEIGHT - 100
    r = 35

    # Main moon body - pale white/gray
    glColor3f(0.95, 0.95, 0.95)
    draw_filled_circle(mx, my, r, segments=48)

    # Draw some craters for detail
    glColor3f(0.75, 0.75, 0.8)
    draw_filled_circle(mx - 10, my + 8, 6, segments=24)
    draw_filled_circle(mx + 12, my - 5, 4, segments=24)
    draw_filled_circle(mx - 5, my - 12, 5, segments=24)
    draw_filled_circle(mx + 8, my + 10, 3, segments=24)

    # Add a subtle glow around the moon
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glColor4f(0.9, 0.9, 1.0, 0.15)
    draw_filled_circle(mx, my, r + 12, segments=48)
    
    glDisable(GL_BLEND)
