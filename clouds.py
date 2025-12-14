from OpenGL.GL import *
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Cloud data: [x, y, speed, size_scale]
clouds = []

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h

def init_clouds():
    """Initialize clouds with random positions and properties"""
    global clouds
    clouds = [
        [-100, WINDOW_HEIGHT - 150, 0.3, 1.0],
        [200, WINDOW_HEIGHT - 200, 0.25, 0.8],
        [500, WINDOW_HEIGHT - 120, 0.35, 1.2],
        [150, WINDOW_HEIGHT - 280, 0.28, 0.9],
        [600, WINDOW_HEIGHT - 250, 0.32, 1.1]
    ]

def draw_filled_ellipse(cx, cy, rx, ry, segments=32):
    """Draw a filled ellipse for cloud puffs"""
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(segments + 1):
        a = 2.0 * math.pi * i / segments
        glVertex2f(cx + math.cos(a) * rx, cy + math.sin(a) * ry)
    glEnd()

def draw_single_cloud(x, y, scale=1.0):
    """Draw a single cloud made of multiple overlapping circles"""
    # Cloud color - soft white with slight transparency
    glColor4f(1.0, 1.0, 1.0, 0.85)
    
    # Main cloud body - multiple overlapping ellipses
    # Left puff
    draw_filled_ellipse(x - 25 * scale, y, 22 * scale, 15 * scale, segments=24)
    
    # Center-left puff
    draw_filled_ellipse(x - 8 * scale, y + 5 * scale, 25 * scale, 18 * scale, segments=24)
    
    # Center puff (largest)
    draw_filled_ellipse(x + 10 * scale, y + 8 * scale, 28 * scale, 20 * scale, segments=24)
    
    # Center-right puff
    draw_filled_ellipse(x + 30 * scale, y + 3 * scale, 24 * scale, 17 * scale, segments=24)
    
    # Right puff
    draw_filled_ellipse(x + 45 * scale, y - 2 * scale, 20 * scale, 14 * scale, segments=24)
    
    # Bottom fill puffs for smoother look
    draw_filled_ellipse(x, y - 5 * scale, 26 * scale, 12 * scale, segments=24)
    draw_filled_ellipse(x + 20 * scale, y - 3 * scale, 22 * scale, 11 * scale, segments=24)

def draw_clouds():
    """Draw all clouds"""
    global clouds
    
    for cloud in clouds:
        x, y, _, scale = cloud
        draw_single_cloud(x, y, scale)

speed_factor = 1.0

def adjust_speed(factor):
    """Adjust cloud speed by factor"""
    global speed_factor
    speed_factor *= factor

def update_clouds():
    """Update cloud positions for animation"""
    global clouds
    
    for cloud in clouds:
        # Move cloud to the right
        cloud[0] += cloud[2] * speed_factor
        
        # Wrap around when cloud goes off screen
        if cloud[0] > WINDOW_WIDTH + 100:
            cloud[0] = -100
