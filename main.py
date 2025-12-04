from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Import all modules
import background
import sun
import earthsurface_satellite
import windturbine
import citybuildings 
import ufo
import satellite

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def display():
    glClear(GL_COLOR_BUFFER_BIT)
   
    background.draw_milky_way_glow()
    background.draw_stars()
    sun.draw_sun()
    earthsurface_satellite.draw_earth_surface()
    citybuildings.draw_city_skyline()  
    earthsurface_satellite.draw_satellite_dish()
    windturbine.draw_wind_turbine()
    ufo.draw_ufo()
    satellite.draw_satellite()
    
    glutSwapBuffers()

def animate(v):
    background.update_stars()
    sun.update_sun_angle_animate()
    earthsurface_satellite.update_satellite_angle()
    windturbine.update_blade_angle() 
    ufo.update_ufo_position()
    satellite.update_satellite_position()
    glutPostRedisplay()
    glutTimerFunc(16, animate, 0)

def reshape(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = w, h
    
   
    background.update_window_size(w, h)
    sun.update_window_size(w, h)
    earthsurface_satellite.update_window_size(w, h)
    windturbine.update_window_size(w, h)
    citybuildings.update_window_size(w, h) 
    ufo.update_window_size(w, h)
    satellite.update_window_size(w, h)
    
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

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, animate, 0) 
    glutMainLoop()

if __name__ == "__main__":
    main()