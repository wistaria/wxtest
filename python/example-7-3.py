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
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.lines = []
        self.rubberband = False

    def InitGL(self):
        glClearColor(1, 1, 1, 1)

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
        glBegin(GL_LINES)
        for l in self.lines:
            glVertex2iv(l[0])
            glVertex2iv(l[1])
        glEnd()
        glFlush()

    def OnMouseLeftDown(self, event):
        x, y = event.GetPosition()
        self.start = [x, y]

    def OnMouseLeftUp(self, event):
        x, y = event.GetPosition()
        stop = [x, y]
        self.lines.append([self.start, stop])
        glColor3d(0.0, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex2iv(self.start)
        glVertex2iv(stop)
        glEnd()
        glFlush()
        self.rubberband = False

    def OnMouseMotion(self, event):
        if event.Dragging() and event.LeftIsDown():
            glEnable(GL_COLOR_LOGIC_OP)
            glLogicOp(GL_INVERT)

            glBegin(GL_LINES)
            if (self.rubberband):
                glVertex2iv(self.start)
                glVertex2iv(self.stop)

            x, y = event.GetPosition()
            self.stop = [x, y]
            glVertex2iv(self.start)
            glVertex2iv(self.stop)
            glEnd()
            glFlush()

            glLogicOp(GL_COPY)
            glDisable(GL_COLOR_LOGIC_OP)

            self.rubberband = True

    def OnKeyDown(self, event):    
        keycode = event.GetKeyCode()
        if keycode == 0x51 or keycode == 0x1b:
            wx.Exit()
            
if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, sys.argv[0])
    canvas = MyCanvas(frame)
    frame.Show()
    app.MainLoop()
    app.Destroy()
