from OpenGL.GL import *
import math
import satellite

# Window size - will be updated from main
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Dish tracking angles
dish_azimuth = 0.0
dish_elevation = 45.0

def draw_earth_surface(is_day=False):
    # Main ground surface
    if is_day:
        glColor3f(0.2, 0.6, 0.3)  # Bright green for day
    else:
        glColor3f(0.1, 0.3, 0.2)  # Dark green earth
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(WINDOW_WIDTH, 0)
    glVertex2f(WINDOW_WIDTH, 80)
    glVertex2f(0, 80)
    glEnd()
    
    # Hills
    if is_day:
        glColor3f(0.15, 0.5, 0.25)  # Brighter green for day
    else:
        glColor3f(0.08, 0.25, 0.18)  
    glBegin(GL_TRIANGLES)
    # Hill 1 
    glVertex2f(0, 80)
    glVertex2f(0.125 * WINDOW_WIDTH, 80)
    glVertex2f(0.0625 * WINDOW_WIDTH, 100)
    
    # Hill 2 
    glVertex2f(0.25 * WINDOW_WIDTH, 80)
    glVertex2f(0.4375 * WINDOW_WIDTH, 80)
    glVertex2f(0.34375 * WINDOW_WIDTH, 95)
    
    # Hill 3 
    glVertex2f(0.625 * WINDOW_WIDTH, 80)
    glVertex2f(0.875 * WINDOW_WIDTH, 80)
    glVertex2f(0.75 * WINDOW_WIDTH, 110)
    glEnd()

def calculate_tracking_angles():
    global dish_azimuth, dish_elevation
    
    sat_x, sat_y, depth_factor = satellite.get_satellite_position()
    
    dish_x = WINDOW_WIDTH // 2
    dish_y = 140
    
    dx = sat_x - dish_x
    dy = sat_y - dish_y
    
    # Simple angle calculation
    dish_azimuth = math.degrees(math.atan2(dx, dy))
    dish_elevation = 45 + depth_factor * 20

def draw_satellite_dish():
    global dish_azimuth, dish_elevation
    
    calculate_tracking_angles()
    
    base_x = WINDOW_WIDTH // 2
    base_y = 50
    
    # Base platform
    glColor3f(0.35, 0.35, 0.35)
    glBegin(GL_QUADS)
    glVertex2f(base_x - 25, base_y - 8)
    glVertex2f(base_x + 25, base_y - 8)
    glVertex2f(base_x + 25, base_y + 8)
    glVertex2f(base_x - 25, base_y + 8)
    glEnd()
    
    # Vertical pole
    glColor3f(0.45, 0.45, 0.45)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glVertex2f(base_x, base_y + 8)
    glVertex2f(base_x, base_y + 60)
    glEnd()
    
    # Joint housing
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(base_x - 8, base_y + 60)
    glVertex2f(base_x + 8, base_y + 60)
    glVertex2f(base_x + 8, base_y + 70)
    glVertex2f(base_x - 8, base_y + 70)
    glEnd()
    
    # Dish setup
    dish_cx = base_x
    dish_cy = base_y + 90
    dish_radius = 45
    angle_rad = math.radians(dish_azimuth)
    segments = 32
    elevation_factor = math.cos(math.radians(dish_elevation)) * 0.5 + 0.3
    
    # Simple gray dish
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.6, 0.6, 0.6)
    glVertex2f(dish_cx, dish_cy - 15)
    for j in range(segments + 1):
        angle = 2.0 * math.pi * j / segments
        x = math.cos(angle + angle_rad) * dish_radius
        y = math.sin(angle) * dish_radius * elevation_factor
        glVertex2f(dish_cx + x, dish_cy + y)
    glEnd()
    
    # Dish rim
    glColor3f(0.2, 0.2, 0.2)
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2.0 * math.pi * i / segments
        x = math.cos(angle + angle_rad) * dish_radius
        y = math.sin(angle) * dish_radius * elevation_factor
        glVertex2f(dish_cx + x, dish_cy + y)
    glEnd()
    
    # Support arm
    glColor3f(0.4, 0.4, 0.4)
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glVertex2f(base_x, base_y + 70)
    glVertex2f(dish_cx, dish_cy - 20)
    glEnd()
    
    # LNB
    lnb_x = dish_cx
    lnb_y = dish_cy - 35
    
    glColor3f(0.85, 0.7, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(lnb_x - 6, lnb_y - 10)
    glVertex2f(lnb_x + 6, lnb_y - 10)
    glVertex2f(lnb_x + 6, lnb_y + 5)
    glVertex2f(lnb_x - 6, lnb_y + 5)
    glEnd()
    
    # LNB support arms (simple)
    glColor3f(0.5, 0.5, 0.5)
    glLineWidth(2.0)
    for i in range(4):
        arm_angle = math.radians(i * 90) + angle_rad
        offset_x = math.cos(arm_angle) * dish_radius * 0.6
        offset_y = math.sin(arm_angle) * dish_radius * elevation_factor * 0.6
        glBegin(GL_LINES)
        glVertex2f(dish_cx + offset_x, dish_cy + offset_y)
        glVertex2f(lnb_x, lnb_y + 5)
        glEnd()
    
    # LNB tip
    glColor3f(0.9, 0.75, 0.15)
    glBegin(GL_TRIANGLES)
    glVertex2f(lnb_x - 3, lnb_y + 5)
    glVertex2f(lnb_x + 3, lnb_y + 5)
    glVertex2f(lnb_x, lnb_y + 15)
    glEnd()
    
    # Simple signal waves
    sat_x, sat_y, depth_factor = satellite.get_satellite_position()
    
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    dx = sat_x - lnb_x
    dy = sat_y - lnb_y
    
    # Draw 10 signal arcs
    for i in range(10):
        distance = 25 + i * 30
        arc_x = lnb_x + (dx / 400) * distance
        arc_y = lnb_y + (dy / 400) * distance
        alpha = max(0.1, 0.9 - i * 0.08)
        
        glColor4f(0.2, 1.0, 0.3, alpha)
        glLineWidth(max(0.5, 2.5 - i * 0.2))
        glBegin(GL_LINE_STRIP)
        for j in range(9):
            offset = (j - 4) * 3
            glVertex2f(arc_x - offset, arc_y + offset * 0.3)
        glEnd()
    
    glDisable(GL_BLEND)

def update_satellite_angle():
    pass

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h