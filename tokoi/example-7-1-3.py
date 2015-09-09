import sys
import wx
from wx import glcanvas
from OpenGL.GL import *

class MyCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        super(MyCanvas, self).__init__(parent, -1, attribList=[])
        self.context = glcanvas.GLContext(self)
        self.initialized = False
        self.point = []
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)

    def InitGL(self):
        glClearColor(1.0, 1.0, 1.0, 1.0)

    def OnSize(self, event):
        w, h = self.GetClientSize()
        glViewport(0, 0, w, h)
        glLoadIdentity()
        glOrtho(-0.5, w - 0.5, h - 0.5, -0.5, -1.0, 1.0);
        
    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.initialized:
            self.InitGL()
            self.initialized = True
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3d(0.0, 0.0, 0.0);
        glBegin(GL_LINES);
        for p in self.point:
            glVertex2iv(p);
        glEnd();
        glFlush()
        self.OnSize(event)

    def OnMouse(self, event):
        if (event.IsButton() and event.GetButton() == wx.MOUSE_BTN_LEFT):
            x, y = event.GetPosition()
            self.point.append([x, y])
            if (event.ButtonUp()):
                glColor3d(0.0, 0.0, 0.0)
                glBegin(GL_LINES)
                glVertex2iv(self.point[-2])
                glVertex2iv(self.point[-1])
                glEnd()
                glFlush()

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, sys.argv[0], pos=(100,100), size=(320,240))
    canvas = MyCanvas(frame)
    frame.Show()
    app.MainLoop()
    app.Destroy()
