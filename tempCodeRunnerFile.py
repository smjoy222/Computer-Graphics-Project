    light_count = 6
    for i in range(light_count):
        t = (i / float(light_count - 1)) * (body_rx * 1.6) - (body_rx * 0.8)
        lx = ufo_x + t * 0.6
        ly = y
        if i % 2 == 0:
            glColor3f(1.0, 0.9, 0.3)
        else:
            glColor3f(0.4, 0.9, 0.6)
        s = 3.0
        glBegin(GL_QUADS)
        glVertex2f(lx - s, ly - s)
        glVertex2f(lx + s, ly - s)
        glVertex2f(lx + s, ly + s)
        glVertex2f(lx - s, ly + s)
        glEnd()