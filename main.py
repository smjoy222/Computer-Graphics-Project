from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Import all modules
import background
import sun
import moon
import earthsurface_satellite
import windturbine
import citybuildings 
import ufo
import airplane
import satellite
import clouds

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Day/Night mode
is_day = False  # False = night, True = day

def display():
    glClear(GL_COLOR_BUFFER_BIT)
   
    if is_day:
        # Day mode: draw sky background and sun
        background.draw_sky_background()
        clouds.draw_clouds()
        sun.draw_sun()
    else:
        # Night mode: draw space background and moon
        background.draw_milky_way_glow()
        background.draw_stars()
        moon.draw_moon()
    
    earthsurface_satellite.draw_earth_surface(is_day)
    citybuildings.draw_city_skyline(is_day)  
    earthsurface_satellite.draw_satellite_dish()
    windturbine.draw_wind_turbine(is_day)
    
    if is_day:
        airplane.draw_balloon()
    else:
        ufo.draw_ufo()
    
    satellite.draw_satellite()
    
    glutSwapBuffers()

def animate(v):
    background.update_stars()
    sun.update_sun_angle_animate()
    earthsurface_satellite.update_satellite_angle()
    windturbine.update_blade_angle() 
    ufo.update_ufo_position()
    airplane.update_balloon_position()
    satellite.update_satellite_position()
    clouds.update_clouds()
    glutPostRedisplay()
    glutTimerFunc(16, animate, 0)

def keyboard(key, x, y):
    global is_day
    if key == b'd' or key == b'D':
        is_day = True
        glClearColor(0.53, 0.81, 0.92, 1.0)  # Sky blue for day
        glutPostRedisplay()
    elif key == b'n' or key == b'N':
        is_day = False
        glClearColor(0.0, 0.0, 0.03, 1.0)  # Dark blue for night
        glutPostRedisplay()

def reshape(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h
    
   
    background.update_window_size(w, h)
    sun.update_window_size(w, h)
    moon.update_window_size(w, h)
    earthsurface_satellite.update_window_size(w, h)
    windturbine.update_window_size(w, h)
    citybuildings.update_window_size(w, h) 
    ufo.update_window_size(w, h)
    airplane.update_window_size(w, h)
    satellite.update_window_size(w, h)
    clouds.update_window_size(w, h)
    
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Space Environment - OpenGL")

    glClearColor(0.0, 0.0, 0.03, 1.0)
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    background.init_stars()
    clouds.init_clouds()
    satellite.init_satellite()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(0, animate, 0) 
    glutMainLoop()

if __name__ == "__main__":
    main()