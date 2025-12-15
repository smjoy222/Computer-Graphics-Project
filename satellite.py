from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Global variables
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Satellite 3D orbit around star
satellite_orbit_angle = 0.0
satellite_orbit_speed = 0.3
satellite_rotation = 0
rotation_speed = 0.5

def update_window_size(w, h):
    """Update window dimensions"""
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h

def init_satellite():
    """Initialize satellite orbit parameters"""
    global satellite_orbit_angle, satellite_rotation
    satellite_orbit_angle = 0.0
    satellite_rotation = 0

def get_star_position():
    #y=(dis_cy 50+80)+ 280)"""
    star_x = WINDOW_WIDTH / 2
    star_y = 420  # base_y + dish_offset + star_offset
    return star_x, star_y

def get_satellite_position():
    """Calculate satellite 3D orbit around star - horizontal depth rotation"""
    star_x, star_y = get_star_position()
    
    angle_rad = math.radians(satellite_orbit_angle)
    
    # Horizontal orbital motion (left-right across screen)
    orbit_width = 280
    
    # Depth calculation (back and forth)
    # When cos = 1, satellite is in front (closer)
    # When cos = -1, satellite is in back (farther)
    depth_factor = math.cos(angle_rad)
    
    # X position: moves left to right
    x = star_x + math.sin(angle_rad) * orbit_width
    
    # Y stays relatively constant (slight vertical for perspective)
    y = star_y + depth_factor * 30
    
    return x, y, depth_factor

def set_speed_forward():
    global satellite_orbit_speed
    satellite_orbit_speed = 0.6

def set_speed_backward():
    global satellite_orbit_speed
    satellite_orbit_speed = -0.6

def set_speed_normal():
    global satellite_orbit_speed
    satellite_orbit_speed = 0.3

def adjust_speed(factor):
    global satellite_orbit_speed, rotation_speed
    satellite_orbit_speed *= factor
    rotation_speed *= factor

def update_satellite_position():
    global satellite_orbit_angle, satellite_rotation
    
    satellite_orbit_angle = (satellite_orbit_angle + satellite_orbit_speed) % 360
    satellite_rotation = (satellite_rotation + rotation_speed) % 360

def draw_satellite():
    sat_x, sat_y, depth = get_satellite_position()
    
    # Scale based on depth (farther = smaller)
    scale = 0.7 + (depth * 0.3)  
    glPushMatrix()
    glTranslatef(sat_x, sat_y, 0)
    glScalef(scale, scale, 1.0)  
    glRotatef(satellite_rotation, 0, 0, 1) 
    # Main satellite body 
    glColor3f(0.7, 0.7, 0.7)  # Silver/gray color
    glBegin(GL_POLYGON)
    glVertex2f(-15, -10)
    glVertex2f(15, -10)
    glVertex2f(15, 10)
    glVertex2f(-15, 10)
    glEnd()
    
    # Central antenna/sensor
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
