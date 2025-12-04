from OpenGL.GL import *
import random
import math


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

random.seed(123)
stars = []
blink_time = 0

def init_stars():
    global stars
    stars = []
   
    for _ in range(180): 
        x_ratio = random.random()  # 0.0 to 1.0
        y_ratio = random.random()  # 0.0 to 1.0
        size = random.choice([1.0, 1.3, 1.6, 2.0])
        brightness = random.uniform(0.5, 0.9)
        blink_phase = random.uniform(0, math.pi * 2)  # Random starting phase
        blink_speed = random.uniform(0.02, 0.05)  # How fast it blinks
        stars.append((x_ratio, y_ratio, size, brightness, blink_phase, blink_speed))

    for _ in range(9):
        x_ratio = random.uniform(0.125, 0.875)  # 100/800 to 700/800
        y_ratio = random.uniform(0.133, 0.867)  # 80/600 to 520/600
        size = random.uniform(2.8, 4.5)
        brightness = 1.0
        blink_phase = random.uniform(0, math.pi * 2)
        blink_speed = random.uniform(0.03, 0.06)  # Brighter stars blink faster
        stars.append((x_ratio, y_ratio, size, brightness, blink_phase, blink_speed))

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
    for (x_ratio, y_ratio, size, base_brightness, blink_phase, blink_speed) in stars:
        x = x_ratio * WINDOW_WIDTH
        y = y_ratio * WINDOW_HEIGHT
        
        # Calculate blinking brightness using sine wave
        blink_factor = (math.sin(blink_time * blink_speed + blink_phase) + 1) / 2  # 0 to 1
        # Blend between 10% and 100% of base brightness for very noticeable blink
        brightness = base_brightness * (0.1 + 0.9 * blink_factor)
        
        # Increase overall brightness significantly
        brightness = min(1.0, brightness * 1.5)
        
        glPointSize(size)
        if size > 3.0:
            glColor3f(brightness, brightness, brightness)                  
        elif base_brightness > 0.8:
            glColor3f(brightness, brightness, brightness)
        else:
            glColor3f(brightness, brightness, brightness)

        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h

def update_stars():
    """Update star blinking animation"""
    global blink_time
    blink_time += 1