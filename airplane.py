from OpenGL.GL import *
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

balloon_x = -150.0
balloon_base_y = 420.0
balloon_speed = 1.8
balloon_bob_phase = 0.0
balloon_bob_speed = 0.05
balloon_bob_amp = 6.0

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h

def _draw_filled_circle(cx, cy, r, segments=32):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(segments + 1):
        a = 2.0 * math.pi * i / segments
        glVertex2f(cx + math.cos(a) * r, cy + math.sin(a) * r)
    glEnd()

def draw_balloon():
    global balloon_x, balloon_base_y, balloon_bob_phase
    
    balloon_base_y = WINDOW_HEIGHT - 180
    
    # Vertical bobbing motion (like UFO)
    bob = math.sin(balloon_bob_phase) * balloon_bob_amp
    x = balloon_x
    y = balloon_base_y + bob
    
    # Balloon envelope (main balloon - simple orange)
    balloon_r = 45
    
    # Orange balloon
    glColor3f(1.0, 0.6, 0.2)
    _draw_filled_circle(x, y, balloon_r)
    
    # Balloon outline
    glColor3f(0.2, 0.2, 0.25)
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)
    for i in range(33):
        a = 2.0 * math.pi * i / 32
        glVertex2f(x + math.cos(a) * balloon_r, y + math.sin(a) * balloon_r)
    glEnd()
    
    # Basket connection lines (ropes)
    glColor3f(0.40, 0.30, 0.25)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    # Left rope
    glVertex2f(x - 25, y - balloon_r + 5)
    glVertex2f(x - 15, y - balloon_r - 25)
    # Center left rope
    glVertex2f(x - 10, y - balloon_r + 2)
    glVertex2f(x - 8, y - balloon_r - 25)
    # Center right rope
    glVertex2f(x + 10, y - balloon_r + 2)
    glVertex2f(x + 8, y - balloon_r - 25)
    # Right rope
    glVertex2f(x + 25, y - balloon_r + 5)
    glVertex2f(x + 15, y - balloon_r - 25)
    glEnd()
    
    # Basket (simple basket at bottom)
    basket_y = y - balloon_r - 35
    glColor3f(0.65, 0.45, 0.30)
    glBegin(GL_QUADS)
    glVertex2f(x - 18, basket_y)
    glVertex2f(x + 18, basket_y)
    glVertex2f(x + 15, basket_y + 18)
    glVertex2f(x - 15, basket_y + 18)
    glEnd()
    
    # Basket outline
    glColor3f(0.4, 0.25, 0.15)
    glLineWidth(2.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x - 18, basket_y)
    glVertex2f(x + 18, basket_y)
    glVertex2f(x + 15, basket_y + 18)
    glVertex2f(x - 15, basket_y + 18)
    glEnd()

speed_factor = 1.0

def adjust_speed(factor):
    """Adjust balloon speed by factor"""
    global speed_factor
    speed_factor *= factor

def update_balloon_position():
    global balloon_x, balloon_bob_phase
    
    balloon_x += balloon_speed * speed_factor
    balloon_bob_phase += balloon_bob_speed * speed_factor
    
    # Reset when off-screen
    if balloon_x - 150 > WINDOW_WIDTH:
        balloon_x = -150.0


