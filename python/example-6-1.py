import sys
import wx
from wx import glcanvas
from OpenGL.GL import *

class MyCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        super(MyCanvas, self).__init__(parent, -1, attribList=[])
        self.context = glcanvas.GLContext(self)
        self.initialized = False
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitGL(self):
        glClearColor(1.0, 1.0, 1.0, 1.0)

    def OnSize(self, event):
        w, h = self.GetClientSize()
        glViewport(0, 0, w, h)
        glLoadIdentity()
        glOrtho(-w/200.0, w/200.0, -h/200.0, h/200.0, -1.0, 1.0)
        
    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.initialized:
            self.InitGL()
            self.initialized = True
        self.OnSize(event)
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POLYGON)
        glColor3d(1.0, 0.0, 0.0) # red
        glVertex2d(-0.9, -0.9)
        glColor3d(0.0, 1.0, 0.0) # green
        glVertex2d(0.9, -0.9)
        glColor3d(0.0, 0.0, 1.0) # blue
        glVertex2d(0.9, 0.9)
        glColor3d(1.0, 1.0, 0.0) # yellow
        glVertex2d(-0.9, 0.9)
        glEnd()
        glFlush()

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, sys.argv[0], size=(300,300))
    canvas = MyCanvas(frame)
    frame.Show()
    app.MainLoop()
    app.Destroy()
