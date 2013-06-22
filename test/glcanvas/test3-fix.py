import wx
import sys

from wx import glcanvas

# The Python OpenGL package can be found at
# http://PyOpenGL.sourceforge.net/
from OpenGL.GL import *
from OpenGL.GLUT import *

class MyCanvasBase(glcanvas.GLCanvas):

    def __init__(self, parent):

        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.context = wx.glcanvas.GLContext(self)
        self.init = False
        # initial mouse position
        self.lastx = self.x = 30
        self.lasty = self.y = 30
        self.size = None
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)


    def OnEraseBackground(self, event):
        pass # Do nothing, to avoid flashing on MSW.


    def OnSize(self, event):
        if (self.size == None):
            self.size = self.GetClientSize()
        # self.SetCurrent(self.context)
        glViewport(0, 0, self.size.width, self.size.height)
        event.Skip()


    def OnPaint(self, event):

        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()


    def OnMouseDown(self, evt):

        self.CaptureMouse()
        self.x, self.y = self.lastx, self.lasty = evt.GetPosition()


    def OnMouseUp(self, evt):

        self.ReleaseMouse()


    def OnMouseMotion(self, evt):

        if evt.Dragging() and evt.LeftIsDown():
            self.lastx, self.lasty = self.x, self.y
            self.x, self.y = evt.GetPosition()
            self.Refresh(False)


class CubeCanvas(MyCanvasBase):

    def InitGL(self):

        # set viewing projection
        glMatrixMode(GL_PROJECTION)
        glFrustum(-0.5, 0.5, -0.5, 0.5, 1.0, 3.0)

        # position viewer
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -2.0)

        # position object
        glRotatef(self.y, 1.0, 0.0, 0.0)
        glRotatef(self.x, 0.0, 1.0, 0.0)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)


    def OnDraw(self):

        # clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # draw six faces of a cube
        glutSolidTeapot(2)
        #glBegin(GL_QUADS)
        #glNormal3f( 0.0, 0.0, 1.0)
        #glVertex3f( 0.5, 0.5, 0.5)
        #glVertex3f(-0.5, 0.5, 0.5)
        #glVertex3f(-0.5,-0.5, 0.5)
        #glVertex3f( 0.5,-0.5, 0.5)

        #glNormal3f( 0.0, 0.0,-1.0)
        #glVertex3f(-0.5,-0.5,-0.5)
        #glVertex3f(-0.5, 0.5,-0.5)
        #glVertex3f( 0.5, 0.5,-0.5)
        #glVertex3f( 0.5,-0.5,-0.5)

        #glNormal3f( 0.0, 1.0, 0.0)
        #glVertex3f( 0.5, 0.5, 0.5)
        #glVertex3f( 0.5, 0.5,-0.5)
        #glVertex3f(-0.5, 0.5,-0.5)
        #glVertex3f(-0.5, 0.5, 0.5)

        #glNormal3f( 0.0,-1.0, 0.0)
        #glVertex3f(-0.5,-0.5,-0.5)
        #glVertex3f( 0.5,-0.5,-0.5)
        #glVertex3f( 0.5,-0.5, 0.5)
        #glVertex3f(-0.5,-0.5, 0.5)

        #glNormal3f( 1.0, 0.0, 0.0)
        #glVertex3f( 0.5, 0.5, 0.5)
        #glVertex3f( 0.5,-0.5, 0.5)
        #glVertex3f( 0.5,-0.5,-0.5)
        #glVertex3f( 0.5, 0.5,-0.5)

        #glNormal3f(-1.0, 0.0, 0.0)
        #glVertex3f(-0.5,-0.5,-0.5)
        #glVertex3f(-0.5,-0.5, 0.5)
        #glVertex3f(-0.5, 0.5, 0.5)
        #glVertex3f(-0.5, 0.5,-0.5)
        #glEnd()

        size = self.GetClientSize()
        w, h = size
        w = max(w, 1.0)
        h = max(h, 1.0)
        xScale = 180.0 / w
        yScale = 180.0 / h
        glRotatef((self.y - self.lasty) * yScale, 1.0, 0.0, 0.0);
        glRotatef((self.x - self.lastx) * xScale, 0.0, 1.0, 0.0);

        self.SwapBuffers()


app = wx.App(0)

frame = wx.Frame(None, -1, size=(400,400))
canvas = CubeCanvas(frame)
frame.Show(True)

app.MainLoop()
