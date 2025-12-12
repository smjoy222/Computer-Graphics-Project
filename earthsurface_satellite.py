from OpenGL.GL import *
import math

# Window size - will be updated from main
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

satellite_angle = 0

def draw_earth_surface():
    # Main ground surface
    glColor3f(0.1, 0.3, 0.2)  # Dark green earth
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(WINDOW_WIDTH, 0)
    glVertex2f(WINDOW_WIDTH, 80)
    glVertex2f(0, 80)
    glEnd()
    
  
    glColor3f(0.08, 0.25, 0.18)  
    glBegin(GL_TRIANGLES)
    # Hill 1 (left side, 0-12.5% of width)
    glVertex2f(0, 80)
    glVertex2f(0.125 * WINDOW_WIDTH, 80)
    glVertex2f(0.0625 * WINDOW_WIDTH, 100)
    
    # Hill 2 (middle left, 25-43.75% of width)
    glVertex2f(0.25 * WINDOW_WIDTH, 80)
    glVertex2f(0.4375 * WINDOW_WIDTH, 80)
    glVertex2f(0.34375 * WINDOW_WIDTH, 95)
    
    # Hill 3 (middle right, 62.5-87.5% of width)
    glVertex2f(0.625 * WINDOW_WIDTH, 80)
    glVertex2f(0.875 * WINDOW_WIDTH, 80)
    glVertex2f(0.75 * WINDOW_WIDTH, 110)
    glEnd()

def draw_satellite_dish():
    global satellite_angle
    
    # Satellite base position - centered
    base_x = WINDOW_WIDTH // 2
    base_y = 50
    
    glColor3f(0.35, 0.35, 0.35)
    glBegin(GL_QUADS)
    glVertex2f(base_x - 25, base_y - 8)
    glVertex2f(base_x + 25, base_y - 8)
    glVertex2f(base_x + 25, base_y + 8)
    glVertex2f(base_x - 25, base_y + 8)
    glEnd()
    
    # 2.vertical support pole
    glColor3f(0.45, 0.45, 0.45)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glVertex2f(base_x, base_y + 8)
    glVertex2f(base_x, base_y + 60)
    glEnd()
    
    # 3. rotating joint/housing at top of pole
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(base_x - 8, base_y + 60)
    glVertex2f(base_x + 8, base_y + 60)
    glVertex2f(base_x + 8, base_y + 70)
    glVertex2f(base_x - 8, base_y + 70)
    glEnd()
    
    # 4. e dish position with rotation
    dish_cx = base_x
    dish_cy = base_y + 90
    dish_radius = 45
    
    angle_rad = math.radians(satellite_angle)
    
    # 5. parabolic dish
    segments = 32
    
    #  parabolic surface
    for i in range(1, 6):
        current_radius = dish_radius * (1.0 - i/10.0)
        y_offset = -i * 4 
        
        glColor3f(0.7 - i*0.05, 0.7 - i*0.05, 0.7 - i*0.05)
        glBegin(GL_LINE_LOOP)
        for j in range(segments):
            angle = 2.0 * math.pi * j / segments
            x = math.cos(angle + angle_rad) * current_radius
            y = math.sin(angle) * current_radius * 0.3
            
            glVertex2f(dish_cx + x, dish_cy + y + y_offset)
        glEnd()
    
    # 6. dish rim
    glColor3f(0.3, 0.3, 0.3)
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2.0 * math.pi * i / segments
        x = math.cos(angle + angle_rad) * dish_radius
        y = math.sin(angle) * dish_radius * 0.3
        
        glVertex2f(dish_cx + x, dish_cy + y)
    glEnd()
    
    # 7.  support arms
    glColor3f(0.4, 0.4, 0.4)
    glLineWidth(2.5)
    
    # Main support arm 
    glBegin(GL_LINES)
    glVertex2f(base_x, base_y + 70)
    glVertex2f(dish_cx, dish_cy + 20)
    glEnd()
    
    # Diagonal support arms
    support_angles = [0, 90, 180, 270]
    for angle_deg in support_angles:
        angle = math.radians(angle_deg + satellite_angle)
        x_arm = math.cos(angle) * dish_radius * 0.7
        y_arm = math.sin(angle) * dish_radius * 0.3 * 0.7
        
        glBegin(GL_LINES)
        glVertex2f(dish_cx, dish_cy + 20)
        glVertex2f(dish_cx + x_arm, dish_cy + y_arm)
        glEnd()
    
    
    lnb_x = dish_cx
    lnb_y = dish_cy - 35
    
    # LNB housing
    glColor3f(0.85, 0.7, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(lnb_x - 6, lnb_y - 10)
    glVertex2f(lnb_x + 6, lnb_y - 10)
    glVertex2f(lnb_x + 6, lnb_y + 5)
    glVertex2f(lnb_x - 6, lnb_y + 5)
    glEnd()
    
    # LNB support arms
    glColor3f(0.5, 0.5, 0.5)
    glLineWidth(1.5)
    
    for i in range(4):
        arm_angle = math.radians(i * 90)
        offset_x = math.cos(arm_angle) * 4
        offset_y = math.sin(arm_angle) * 2
        
        glBegin(GL_LINES)
        glVertex2f(dish_cx + offset_x, dish_cy + offset_y)
        glVertex2f(lnb_x, lnb_y + 5)
        glEnd()
    
   
    glColor3f(0.9, 0.75, 0.15)
    glBegin(GL_TRIANGLES)
    glVertex2f(lnb_x - 3, lnb_y + 5)
    glVertex2f(lnb_x + 3, lnb_y + 5)
    glVertex2f(lnb_x, lnb_y + 15)
    glEnd()

def update_satellite_angle():
    global satellite_angle
    satellite_angle = (satellite_angle + 1) % 360

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h