from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle=0
x=0
right = True
z=0
forward = True
f=0
def myinit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,1,60)
    gluLookAt(5,11,10,
              0,0,0,
             0,1,0)
    glClearColor(0,0,0,1)
    glClear(GL_COLOR_BUFFER_BIT)

def linesxyz():
    glBegin(GL_LINES)
    glColor3f(0, 1, 0)
    glVertex(-10, 0, 0)
    glVertex(10, 0, 0)
    glEnd()
    glBegin(GL_LINES)
    glVertex(0, 10, 0)
    glVertex(0, -10, 0)
    glEnd()
    glBegin(GL_LINES)
    #glColor3f(1, 0, 0)
    glVertex(0, 0, 10)
    glVertex(0, 0, -10)
    glEnd()


    glFlush()

def drawother():
    glLoadIdentity()
    glColor3f(0,.8,0)
    glTranslate(15,0,-13)
    glScale(5,.2,11)
    glutSolidCube(4)


    glLoadIdentity()
    glColor3f(0,.8,0)
    glTranslate(-24,0,-15)
    glScale(5,.2,13)
    glutSolidCube(5)









def draw():
    global angle
    global x
    global right
    global z
    global f
    global forward




    #glTranslate(x, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(0,0,0,1)


    glClear(GL_COLOR_BUFFER_BIT)




    glLoadIdentity()
    glColor3f(.2,.2 ,.3 )
    glTranslate(1, 0, -17)
    glScale(5, .01, 9)
    glutSolidCube(6)
    glFlush()
    #
    # glColor3f(0,1,1)
    #
    #linesxyz()
    #
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glRotate(90, 0,1 ,0)
    glScale(7, .01, 1)
    glutSolidCube(1)
    glFlush()

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glRotate(90,0,1,0)
    glTranslate(4, 0, -5)
    glScale(7, .01, 1)
    glutSolidCube(1)
    glFlush()

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glRotate(90,0,1,0)
    glTranslate(-4, 0, -5)
    glScale(7, .01, 1)
    glutSolidCube(1)
    glFlush()

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-0, 0, 4)
    glScale(7, .01, 1)
    glutSolidCube(1)
    glFlush()

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(10, 0, 0)
    glScale(7, .01, 1)
    glutSolidCube(1)
    glFlush()






    glLoadIdentity()
    glColor3f(1,0,0)
    glTranslate(z, 0, -x)
    glRotate(90,0,1,0)
    glScale(1, 0.25, 0.5)
    glutWireCube(5)

    glColor3f(1,1,.1)
    glLoadIdentity()
    glTranslate(0+z, 0,-x)
    glTranslate(0,5*0.25,0)
    glRotate(90,0,1,0)
    glScale(0.5, 0.25, 0.5)
    glutWireCube(5)

    glLoadIdentity()
    glTranslate(0+z, 0, -x)
    glColor3f(0,0,1)
    glRotate(90, 0, 1, 0)
    glTranslate(5*0.5,-5*0.25*0.5,(0.5*5*0.5))
    glRotate(angle,0,0,1)
    glutWireTorus(.125,.5,12,10)

    glLoadIdentity()
    glTranslate(z,0,-x)
    glRotate(90,0,1,0)
    glTranslate(-5*0.5,-5*.25*.5,(0.5*5*.5))
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125,.5,12,10)

    glLoadIdentity()
    glTranslate(z,0,-x)
    glRotate(90,0,1,0)
    glTranslate(-5*.5, -5*.5*.25, -5*.5*.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 10)


    glLoadIdentity()
    glTranslate(z,0,-x)
    glRotate(90,0,1,0)
    glTranslate(5 * 0.5, -5 * 0.25 * 0.5, (-0.5 * 5 * 0.5))
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 10)


    if f <=9 :
        f+=.1
    else:
        f=-27


    glLoadIdentity()
    glColor3f(1,0,0)
    glTranslate(0,0,f)
    glutWireSphere(1,20,20)



    drawother()


    glutSwapBuffers()

    if right :
       angle-=1
       x+=.02
       if x>25:
           right=False
    else:
        angle+=1
        x-=.02
        if x < -5:
           right = True








def specialkeyboardfun(key,x,y):
    global z
    if key == GLUT_KEY_RIGHT:
        if z<=2:
            z+=1
    if key == GLUT_KEY_LEFT:
        if z>=-5:
            z-=1

    draw()






glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"movingcar")
myinit()
glutIdleFunc(draw)
glutDisplayFunc(draw)
glutSpecialFunc(specialkeyboardfun)
glutMainLoop()