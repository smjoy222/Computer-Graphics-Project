from OpenGL.GL import *
import math
##Lamia-Liza

# Window size - will be updated from main
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def draw_city_skyline():
    """
    Draw city skyline with buildings positioned to not clash with hills
    Hills are at: x=0-100, x=200-350, x=500-700
    Buildings positioned in gaps and right side
    """
    
    # Building colors (dark for night scene)
    building_colors = [
        (0.15, 0.15, 0.2),   # Dark blue-gray
        (0.18, 0.18, 0.22),  # Slightly lighter
        (0.12, 0.12, 0.18),  # Darker
        (0.2, 0.2, 0.25),    # Medium gray
        (0.16, 0.16, 0.2),   # Dark gray
    ]
    
    window_color = (0.9, 0.85, 0.3)  # Yellow windows (lit up)
    
    # Buildings defined as proportions of window width (x_ratio, width_ratio, height, color_idx)
    # x_ratio: 0.0 to 1.0 representing position across screen width
    buildings = [
       
       
        (0.14, 0.044, 95, 0),   # (110/800, 35/800)
        (0.19, 0.035, 110, 1),  # (150/800, 28/800)
        
       
        (0.46, 0.050, 130, 2),  # (370/800, 40/800)
        (0.52, 0.040, 100, 3),  # (415/800, 32/800)
        (0.57, 0.048, 145, 0),  # (452/800, 38/800)
        (0.62, 0.038, 85, 1),   # (495/800, 30/800)
        
      
        (0.89, 0.044, 120, 4),  # (710/800, 35/800)
        (0.94, 0.053, 90, 2),   # (750/800, 42/800)
    ]
    
   
    for (x_ratio, width_ratio, height, color_idx) in buildings:
        x_pos = x_ratio * WINDOW_WIDTH
        width = width_ratio * WINDOW_WIDTH
        base_y = 80 
        
        glColor3f(*building_colors[color_idx])
        glBegin(GL_QUADS)
        glVertex2f(x_pos, base_y)
        glVertex2f(x_pos + width, base_y)
        glVertex2f(x_pos + width, base_y + height)
        glVertex2f(x_pos, base_y + height)
        glEnd()
        
      
        glColor3f(0.05, 0.05, 0.08)
        glLineWidth(1.5)
        glBegin(GL_LINE_LOOP)
        glVertex2f(x_pos, base_y)
        glVertex2f(x_pos + width, base_y)
        glVertex2f(x_pos + width, base_y + height)
        glVertex2f(x_pos, base_y + height)
        glEnd()
        
        # Draw windows (small rectangles in grid pattern)
        window_width = 4
        window_height = 5
        window_spacing_x = 8
        window_spacing_y = 12
        
        # Calculate number of window rows and columns
        num_cols = max(1, int((width - 8) // window_spacing_x))
        num_rows = max(1, (height - 20) // window_spacing_y)
        
        # Starting position for windows (centered)
        start_x = x_pos + (width - (num_cols * window_spacing_x)) / 2
        start_y = base_y + 10
        
        glColor3f(*window_color)
        
        for row in range(num_rows):
            for col in range(num_cols):
                # Randomly skip some windows (not all lit)
                import random
                random.seed(int(x_pos) + row * 100 + col)  # Consistent randomness
                if random.random() > 0.3:  # 70% windows lit
                    win_x = start_x + col * window_spacing_x
                    win_y = start_y + row * window_spacing_y
                    
                    glBegin(GL_QUADS)
                    glVertex2f(win_x, win_y)
                    glVertex2f(win_x + window_width, win_y)
                    glVertex2f(win_x + window_width, win_y + window_height)
                    glVertex2f(win_x, win_y + window_height)
                    glEnd()

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h