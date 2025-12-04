from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Global variables
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
satellite_x = 0
satellite_y = 450
satellite_speed = 0.5
satellite_rotation = 0
rotation_speed = 0.5
rotation_direction = 1  # 1 for clockwise, -1 for counter-clockwise

def update_window_size(w, h):
    """Update window dimensions"""
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h

def update_satellite_position():
    """Update satellite position for animation"""
    global satellite_x, satellite_rotation, rotation_direction
    satellite_x += satellite_speed
    
    # Update rotation
    satellite_rotation += rotation_speed * rotation_direction
    
    # Change rotation direction every 360 degrees
    if satellite_rotation >= 360:
        satellite_rotation = 0
        rotation_direction = -1  # Switch to counter-clockwise
    elif satellite_rotation <= -360:
        satellite_rotation = 0
        rotation_direction = 1  # Switch to clockwise
    
    # Reset position when it goes off screen
    if satellite_x > WINDOW_WIDTH + 100:
        satellite_x = -100

def draw_satellite():
    """Draw a 2D satellite moving across the sky"""
    glPushMatrix()
    glTranslatef(satellite_x, satellite_y, 0)
    glRotatef(satellite_rotation, 0, 0, 1)  # Rotate around Z-axis
    
    # Main satellite body (rectangular)
    glColor3f(0.7, 0.7, 0.7)  # Silver/gray color
    glBegin(GL_POLYGON)
    glVertex2f(-15, -10)
    glVertex2f(15, -10)
    glVertex2f(15, 10)
    glVertex2f(-15, 10)
    glEnd()
    
    # Central antenna/sensor (small rectangle on top)
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_POLYGON)
    glVertex2f(-3, 10)
    glVertex2f(3, 10)
    glVertex2f(3, 20)
    glVertex2f(-3, 20)
    glEnd()
    
    # Left solar panel
    glColor3f(0.2, 0.2, 0.5)  # Dark blue
    glBegin(GL_POLYGON)
    glVertex2f(-50, -8)
    glVertex2f(-15, -8)
    glVertex2f(-15, 8)
    glVertex2f(-50, 8)
    glEnd()
    
    # Left solar panel grid lines
    glColor3f(0.4, 0.4, 0.6)
    glBegin(GL_LINES)
    for i in range(-45, -15, 10):
        glVertex2f(i, -8)
        glVertex2f(i, 8)
    glVertex2f(-50, 0)
    glVertex2f(-15, 0)
    glEnd()
    
    # Right solar panel
    glColor3f(0.2, 0.2, 0.5)  # Dark blue
    glBegin(GL_POLYGON)
    glVertex2f(15, -8)
    glVertex2f(50, -8)
    glVertex2f(50, 8)
    glVertex2f(15, 8)
    glEnd()
    
    # Right solar panel grid lines
    glColor3f(0.4, 0.4, 0.6)
    glBegin(GL_LINES)
    for i in range(25, 50, 10):
        glVertex2f(i, -8)
        glVertex2f(i, 8)
    glVertex2f(15, 0)
    glVertex2f(50, 0)
    glEnd()
    
    # Add some detail panels on the body
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-10, -5)
    glVertex2f(10, -5)
    glVertex2f(10, 5)
    glVertex2f(-10, 5)
    glEnd()
    
    # Small blinking light indicator
    glColor3f(1.0, 0.0, 0.0)  # Red light
    glPointSize(4.0)
    glBegin(GL_POINTS)
    glVertex2f(0, 0)
    glEnd()
    
    glPopMatrix()
