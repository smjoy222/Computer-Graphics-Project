from OpenGL.GL import *
import math
#Mim-khan

# Window size - will be updated from main
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


blade_angle = 0

def draw_wind_turbine():
    global blade_angle
    
    
    base_x = WINDOW_WIDTH - 180
    base_y = 50
    
    # 1. Draw base platform
    glColor3f(0.35, 0.35, 0.35)  # Dark gray
    glBegin(GL_QUADS)
    glVertex2f(base_x - 15, base_y - 10)
    glVertex2f(base_x + 15, base_y - 10)
    glVertex2f(base_x + 15, base_y)
    glVertex2f(base_x - 15, base_y)
    glEnd()
    
   
    tower_height = 120
    glColor3f(0.85, 0.85, 0.85)  
    
    
    glBegin(GL_QUADS)
    glVertex2f(base_x - 12, base_y)           # Bottom left
    glVertex2f(base_x + 12, base_y)           # Bottom right
    glVertex2f(base_x + 6, base_y + tower_height)   # Top right
    glVertex2f(base_x - 6, base_y + tower_height)   # Top left
    glEnd()
    
    
    glColor3f(0.6, 0.6, 0.6)
    glLineWidth(1.5)
    glBegin(GL_LINE_LOOP)
    glVertex2f(base_x - 12, base_y)
    glVertex2f(base_x + 12, base_y)
    glVertex2f(base_x + 6, base_y + tower_height)
    glVertex2f(base_x - 6, base_y + tower_height)
    glEnd()
    
    
    nacelle_y = base_y + tower_height
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex2f(base_x - 8, nacelle_y)
    glVertex2f(base_x + 8, nacelle_y)
    glVertex2f(base_x + 8, nacelle_y + 12)
    glVertex2f(base_x - 8, nacelle_y + 12)
    glEnd()
    

    hub_x = base_x
    hub_y = nacelle_y + 6
    hub_radius = 5
    
    glColor3f(0.5, 0.5, 0.5)
   
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(hub_x, hub_y)
    segments = 16
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        glVertex2f(hub_x + math.cos(angle) * hub_radius, 
                   hub_y + math.sin(angle) * hub_radius)
    glEnd()
    
    
    glPushMatrix()
    glTranslatef(hub_x, hub_y, 0)
    glRotatef(blade_angle, 0, 0, 1)  
    
    for i in range(3):
        blade_rotation = i * 120 
        
        glPushMatrix()
        glRotatef(blade_rotation, 0, 0, 1)
        
        # Blade shape 
        blade_length = 35
        blade_width = 8
        
        glColor3f(0.9, 0.9, 0.9) 
        glBegin(GL_TRIANGLES)
        # Blade triangle
        glVertex2f(0, 0)  # Hub connection
        glVertex2f(-blade_width/2, hub_radius)  # Left edge
        glVertex2f(blade_width/2, hub_radius)   # Right edge
        
        glVertex2f(-blade_width/2, hub_radius)
        glVertex2f(blade_width/2, hub_radius)
        glVertex2f(0, blade_length + hub_radius)  # Tip
        glEnd()
        
        # Blade outline
        glColor3f(0.6, 0.6, 0.6)
        glLineWidth(1.0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(0, 0)
        glVertex2f(-blade_width/2, hub_radius)
        glVertex2f(0, blade_length + hub_radius)
        glVertex2f(blade_width/2, hub_radius)
        glEnd()
        
        glPopMatrix()
    
    glPopMatrix()

def update_blade_angle():
    global blade_angle
    # Rotate blades clockwise slowly
    blade_angle = (blade_angle + 3) % 360  # 3 degrees per frame

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h