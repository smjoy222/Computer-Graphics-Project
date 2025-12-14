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

def calculate_tracking_angles():
    """Calculate azimuth and elevation to track satellite"""
    global dish_azimuth, dish_elevation
    
    # Get satellite orbital information
    sat_x, sat_y, depth_factor = satellite.get_satellite_position()
    orbit_angle = satellite.satellite_orbit_angle
    
    # Dish position
    dish_x = WINDOW_WIDTH // 2
    dish_y = 50 + 90  # base_y + dish offset
    
    # Calculate vector from dish to satellite
    dx = sat_x - dish_x
    dy = sat_y - dish_y
    
    # AZIMUTH CALCULATION (horizontal rotation)
    # Satellite orbital motion breakdown:
    # 0°: x=center (sin=0), depth=1 (cos=1) → FRONT-CENTER
    # 90°: x=right (sin=1), depth=0 (cos=0) → RIGHT-MIDDLE
    # 180°: x=center (sin=0), depth=-1 (cos=-1) → BACK-CENTER
    # 270°: x=left (sin=-1), depth=0 (cos=0) → LEFT-MIDDLE
    
    # For dish tracking: azimuth should directly follow the satellite's horizontal position
    # Use atan2 for proper angle calculation from dish to satellite
    if abs(dx) > 0.1 or abs(dy) > 0.1:
        # Calculate angle from dish perspective
        # atan2(dx, dy) gives angle where 0° is up, positive is clockwise
        dish_azimuth = math.degrees(math.atan2(dx, dy + 100))
    else:
        dish_azimuth = 0
    
    # ELEVATION CALCULATION (vertical tilt)
    # When satellite is in front (depth=1), higher elevation
    # When satellite is behind (depth=-1), lower elevation
    distance = math.sqrt(dx * dx + dy * dy)
    if distance > 0:
        # Base elevation from height difference
        base_elevation = math.degrees(math.atan2(dy, distance))
        
        # Adjust based on depth: front = tilt up more, back = tilt down more
        elevation_adjustment = depth_factor * 25
        
        dish_elevation = base_elevation + elevation_adjustment + 45
        
        # Clamp elevation
        dish_elevation = max(20, min(85, dish_elevation))

def draw_satellite_dish():
    global dish_azimuth, dish_elevation
    
    # Calculate tracking angles first
    calculate_tracking_angles()
    
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
    
    # 4. dish position with tracking rotation
    dish_cx = base_x
    dish_cy = base_y + 90
    dish_radius = 45
    
    # Use azimuth angle for horizontal rotation
    angle_rad = math.radians(dish_azimuth)
    
    # 5. parabolic dish with elevation tilt and directional segments
    segments = 32
    
    # Calculate elevation factor (higher elevation = more compressed vertically)
    elevation_factor = math.cos(math.radians(dish_elevation)) * 0.5 + 0.3
    
    # Draw dish with colored sectors to show rotation
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.6, 0.6, 0.6)  # Center color
    glVertex2f(dish_cx, dish_cy - 15)
    
    for j in range(segments + 1):
        angle = 2.0 * math.pi * j / segments
        x = math.cos(angle + angle_rad) * dish_radius
        y = math.sin(angle) * dish_radius * elevation_factor
        
        # Different colors for different sectors (8 sectors)
        sector = int((j / segments) * 8) % 8
        if sector == 0:  # Red sector (top)
            glColor3f(0.8, 0.3, 0.3)
        elif sector == 1 or sector == 7:
            glColor3f(0.65, 0.65, 0.65)
        elif sector == 2 or sector == 6:
            glColor3f(0.55, 0.55, 0.55)
        elif sector == 3 or sector == 5:
            glColor3f(0.7, 0.7, 0.7)
        else:  # sector == 4 (bottom)
            glColor3f(0.45, 0.45, 0.45)
        
        glVertex2f(dish_cx + x, dish_cy + y)
    glEnd()
    
    # Draw radial lines from center to show rotation clearly
    glColor3f(0.3, 0.3, 0.3)
    glLineWidth(2.0)
    for i in range(8):
        angle = 2.0 * math.pi * i / 8
        x_inner = math.cos(angle + angle_rad) * dish_radius * 0.2
        y_inner = math.sin(angle) * dish_radius * elevation_factor * 0.2
        x_outer = math.cos(angle + angle_rad) * dish_radius
        y_outer = math.sin(angle) * dish_radius * elevation_factor
        
        glBegin(GL_LINES)
        glVertex2f(dish_cx + x_inner, dish_cy + y_inner - 15)
        glVertex2f(dish_cx + x_outer, dish_cy + y_outer)
        glEnd()
    
    # 6. dish rim with elevation
    glColor3f(0.2, 0.2, 0.2)
    glLineWidth(4.0)
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2.0 * math.pi * i / segments
        x = math.cos(angle + angle_rad) * dish_radius
        y = math.sin(angle) * dish_radius * elevation_factor
        
        glVertex2f(dish_cx + x, dish_cy + y)
    glEnd()
    
    # 6.5 Big directional arrow on dish surface pointing upward (showing dish orientation)
    arrow_angle = angle_rad
    arrow_length = dish_radius * 0.6
    
    # Arrow shaft
    glColor3f(1.0, 0.8, 0.0)  # Yellow/orange color
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glVertex2f(dish_cx, dish_cy - 15)
    arrow_tip_x = dish_cx + math.cos(arrow_angle + math.pi/2) * arrow_length
    arrow_tip_y = dish_cy - 15 + math.sin(arrow_angle + math.pi/2) * arrow_length * elevation_factor
    glVertex2f(arrow_tip_x, arrow_tip_y)
    glEnd()
    
    # Arrow head (triangle)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.6, 0.0)  # Orange color
    
    head_size = 12
    # Arrow tip point
    glVertex2f(arrow_tip_x, arrow_tip_y)
    
    # Left wing
    left_angle = arrow_angle + math.pi/2 - 2.8
    left_x = arrow_tip_x + math.cos(left_angle) * head_size
    left_y = arrow_tip_y + math.sin(left_angle) * head_size * elevation_factor
    glVertex2f(left_x, left_y)
    
    # Right wing
    right_angle = arrow_angle + math.pi/2 + 2.8
    right_x = arrow_tip_x + math.cos(right_angle) * head_size
    right_y = arrow_tip_y + math.sin(right_angle) * head_size * elevation_factor
    glVertex2f(right_x, right_y)
    glEnd()
    
    # 7. Main support arm from pole to dish
    glColor3f(0.4, 0.4, 0.4)
    glLineWidth(3.0)
    
    glBegin(GL_LINES)
    glVertex2f(base_x, base_y + 70)
    glVertex2f(dish_cx, dish_cy - 20)
    glEnd()
    
    # Side mounting bracket (asymmetric - shows rotation clearly)
    bracket_angle = angle_rad + math.pi/4  # 45 degrees offset
    bracket_x = dish_cx + math.cos(bracket_angle) * dish_radius * 0.85
    bracket_y = dish_cy + math.sin(bracket_angle) * dish_radius * elevation_factor * 0.85
    
    glColor3f(0.3, 0.3, 0.35)
    glLineWidth(4.0)
    glBegin(GL_LINES)
    glVertex2f(dish_cx, dish_cy - 20)
    glVertex2f(bracket_x, bracket_y)
    glEnd()
    
    # Bracket end piece (visible marker)
    glColor3f(0.8, 0.2, 0.2)  # Red marker
    glBegin(GL_QUADS)
    perp_x = -math.sin(bracket_angle) * 5
    perp_y = math.cos(bracket_angle) * 5 * elevation_factor
    glVertex2f(bracket_x - perp_x, bracket_y - perp_y)
    glVertex2f(bracket_x + perp_x, bracket_y + perp_y)
    glVertex2f(bracket_x + perp_x + math.cos(bracket_angle) * 8, bracket_y + perp_y + math.sin(bracket_angle) * 8 * elevation_factor)
    glVertex2f(bracket_x - perp_x + math.cos(bracket_angle) * 8, bracket_y - perp_y + math.sin(bracket_angle) * 8 * elevation_factor)
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
    
    # LNB support arms (asymmetric to show rotation)
    glColor3f(0.5, 0.5, 0.5)
    glLineWidth(2.5)
    
    # Main support arm (thicker, aligned with dish orientation)
    main_arm_angle = angle_rad
    main_offset_x = math.cos(main_arm_angle) * dish_radius * 0.7
    main_offset_y = math.sin(main_arm_angle) * dish_radius * elevation_factor * 0.7
    
    glBegin(GL_LINES)
    glVertex2f(dish_cx + main_offset_x, dish_cy + main_offset_y)
    glVertex2f(lnb_x, lnb_y + 5)
    glEnd()
    
    # Secondary support arms (thinner)
    glLineWidth(1.5)
    for i in [2, 4, 6]:  # Only 3 arms, asymmetric
        arm_angle = math.radians(i * 45) + angle_rad
        offset_x = math.cos(arm_angle) * dish_radius * 0.5
        offset_y = math.sin(arm_angle) * dish_radius * elevation_factor * 0.5
        
        glBegin(GL_LINES)
        glVertex2f(dish_cx + offset_x, dish_cy + offset_y)
        glVertex2f(lnb_x, lnb_y + 5)
        glEnd()
    
    # LNB antenna tip
    glColor3f(0.9, 0.75, 0.15)
    glBegin(GL_TRIANGLES)
    glVertex2f(lnb_x - 3, lnb_y + 5)
    glVertex2f(lnb_x + 3, lnb_y + 5)
    glVertex2f(lnb_x, lnb_y + 15)
    glEnd()
    
    # Draw signal waves from LNB to satellite
    sat_x, sat_y, depth_factor = satellite.get_satellite_position()
    orbit_angle = satellite.satellite_orbit_angle
    
    # Draw signals when satellite is somewhat visible (not completely behind)
    # Stronger signal when satellite is in front
    if depth_factor > -0.5:
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        # Calculate signal direction from LNB to satellite
        signal_dx = sat_x - lnb_x
        signal_dy = sat_y - (lnb_y + 15)
        signal_distance = math.sqrt(signal_dx * signal_dx + signal_dy * signal_dy)
        
        if signal_distance > 0:
            # Normalize direction
            signal_dx /= signal_distance
            signal_dy /= signal_distance
            
            # Signal strength based on alignment (stronger when satellite is in front)
            signal_strength = (depth_factor + 1.0) / 2.0  # 0 (back) to 1 (front)
            
            # Draw signal wave arcs
            num_waves = 4
            for wave_num in range(num_waves):
                wave_distance = 25 + wave_num * 30
                wave_center_x = lnb_x + signal_dx * wave_distance
                wave_center_y = lnb_y + 15 + signal_dy * wave_distance
                
                # Alpha decreases with distance and depends on signal strength
                alpha = (0.7 - wave_num * 0.15) * signal_strength
                
                # Color: Green when tracking well (front), yellow/red when weak (back)
                if signal_strength > 0.6:
                    glColor4f(0.2, 1.0, 0.3, alpha)  # Strong green
                elif signal_strength > 0.3:
                    glColor4f(0.8, 0.9, 0.2, alpha)  # Yellow
                else:
                    glColor4f(1.0, 0.5, 0.2, alpha)  # Orange/red
                
                # Draw wave arc perpendicular to signal direction
                glLineWidth(2.5 - wave_num * 0.3)
                glBegin(GL_LINE_STRIP)
                for i in range(11):
                    angle_offset = (i - 5) * 0.12
                    # Perpendicular vector
                    perp_x = -signal_dy
                    perp_y = signal_dx
                    
                    wave_x = wave_center_x + perp_x * angle_offset * 18
                    wave_y = wave_center_y + perp_y * angle_offset * 18
                    
                    glVertex2f(wave_x, wave_y)
                glEnd()
            
            # Draw direct line to show tracking direction (thin dashed line)
            if signal_strength > 0.4:
                glColor4f(0.5, 0.8, 1.0, 0.3)
                glLineWidth(1.0)
                glEnable(GL_LINE_STIPPLE)
                glLineStipple(2, 0x00FF)
                glBegin(GL_LINES)
                glVertex2f(lnb_x, lnb_y + 15)
                glVertex2f(lnb_x + signal_dx * 100, lnb_y + 15 + signal_dy * 100)
                glEnd()
                glDisable(GL_LINE_STIPPLE)
        
        glDisable(GL_BLEND)

def update_satellite_angle():
    """Update function (now uses real-time tracking in draw function)"""
    pass

def update_window_size(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h