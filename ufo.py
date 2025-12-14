from OpenGL.GL import *
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

ufo_x = -150.0        
ufo_base_y = 420.0        
ufo_speed = 2.0            
ufo_bob_phase = 0.0        
ufo_bob_speed = 0.06
ufo_bob_amp = 8.0          

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h

def _draw_filled_ellipse(cx, cy, rx, ry, segments=32):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(segments + 1):
        a = 2.0 * math.pi * i / segments
        glVertex2f(cx + math.cos(a) * rx, cy + math.sin(a) * ry)
    glEnd()

def draw_ufo():
    global ufo_x, ufo_base_y, ufo_bob_phase

    ufo_base_y = WINDOW_HEIGHT - 180

    bob = math.sin(ufo_bob_phase) * ufo_bob_amp
    y = ufo_base_y + bob

    body_rx = 60
    body_ry = 18
    dome_rx = 30
    dome_ry = 14

    glColor3f(0.22, 0.22, 0.25)
    _draw_filled_ellipse(ufo_x, y - 4, body_rx, body_ry * 0.9, segments=36)

    glColor3f(0.72, 0.72, 0.74)
    _draw_filled_ellipse(ufo_x, y, body_rx, body_ry, segments=40)

    glColor4f(0.18, 0.6, 0.95, 0.9)
    _draw_filled_ellipse(ufo_x + 6, y + 8, dome_rx, dome_ry, segments=32)
    glDisable(GL_BLEND)

    light_count = 4
    for i in range(light_count):

        t = (i / float(light_count - 1)) * (dome_rx * 1.4) - (dome_rx * 0.7)

        lx = ufo_x + t
        ly = y - (dome_ry * 0.5)

        if i % 2 == 0:
            glColor3f(1.0, 0.95, 0.45)
        else:
            glColor3f(0.4, 0.95, 0.75)

        s = 4.0
        glBegin(GL_QUADS)
        glVertex2f(lx - s, ly - s)
        glVertex2f(lx + s, ly - s)
        glVertex2f(lx + s, ly + s)
        glVertex2f(lx - s, ly + s)
        glEnd()



speed_factor = 1.0

def adjust_speed(factor):
    """Adjust UFO speed by factor"""
    global speed_factor
    speed_factor *= factor

def update_ufo_position():
    global ufo_x, ufo_bob_phase

    ufo_x += ufo_speed * speed_factor

    ufo_bob_phase += ufo_bob_speed * speed_factor

    if ufo_x - 200 > WINDOW_WIDTH:
        ufo_x = -200.0
