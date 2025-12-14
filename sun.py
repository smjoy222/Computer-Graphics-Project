from OpenGL.GL import *
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sun_angle = 0.0

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

def rotate_point(x, y, cx, cy, angle_deg):
    ang = math.radians(angle_deg)
    tx = x - cx
    ty = y - cy
    rx = tx * math.cos(ang) - ty * math.sin(ang)
    ry = tx * math.sin(ang) + ty * math.cos(ang)
    return rx + cx, ry + cy

def draw_sun():
    sx = WINDOW_WIDTH - 120
    sy = WINDOW_HEIGHT - 100
    r = 40

    # Sun body
    glColor3f(1.0, 0.85, 0.10)
    draw_filled_circle(sx, sy, r, segments=48)

    # Sun rays using OpenGL matrix transformations
    N = 8
    inner = r + 5
    outer = r + 22
    spread = 8.6

    glPushMatrix()
    glTranslatef(sx, sy, 0)  # Move to sun center
    glRotatef(sun_angle, 0, 0, 1) 
    
    glColor3f(1.0, 0.8, 0.10)
    for i in range(N):
        ang = 360.0 * i / N
        
        glPushMatrix()
        glRotatef(ang, 0, 0, 1)  
        
        
        glBegin(GL_TRIANGLES)
        glVertex2f(-spread, inner)  
        glVertex2f(spread, inner)   
        glVertex2f(0, outer)       
        glEnd()
        
        glPopMatrix()
    
    glPopMatrix()

sun_rotation_speed = 2.0

def adjust_speed(factor):
    """Adjust sun rotation speed by factor"""
    global sun_rotation_speed
    sun_rotation_speed *= factor

def update_sun_angle_animate():
    global sun_angle
    sun_angle = (sun_angle + sun_rotation_speed) % 360.0
