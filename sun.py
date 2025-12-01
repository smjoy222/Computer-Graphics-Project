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

    glColor3f(1.0, 0.85, 0.10)
    draw_filled_circle(sx, sy, r, segments=48)


    N = 8
    inner = r + 5
    outer = r + 22

    glColor3f(1.0, 0.8, 0.10)
    for i in range(N):
        ang = 360.0 * i / N

        ang_animated = ang + sun_angle

        spread = 8.6 
        left_ang = ang_animated - spread
        right_ang = ang_animated + spread

        lx, ly = rotate_point(sx + inner, sy, sx, sy, left_ang)
        rx, ry = rotate_point(sx + inner, sy, sx, sy, right_ang)
        ox, oy = rotate_point(sx + outer, sy, sx, sy, ang_animated)

        glBegin(GL_TRIANGLES)
        glVertex2f(lx, ly)
        glVertex2f(rx, ry)
        glVertex2f(ox, oy)
        glEnd()

def update_sun_angle_animate():
    global sun_angle
    sun_angle = (sun_angle + 2.0) % 360.0
