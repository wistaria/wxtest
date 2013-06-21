import sys
import wx
from wx import glcanvas
from OpenGL.GL import *

class GLFrame(wx.Frame):
    """A simple class for using OpenGL with wxPython.
    """
    def __init__(self, parent, id, title, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='frame'):
        super(GLFrame, self).__init__(parent, id, title, pos, size, style, name)
        self.canvas = glcanvas.GLCanvas(self)
        self.context = glcanvas.GLContext(self.canvas)
        self.initialized = False
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitGL(self):
        glClearColor(0, 0, 0, 1)
        width, height = self.GetClientSize()
        glViewport(0, 0, width, height)

    def OnPaint(self, event):
        self.canvas.SetCurrent(self.context)
        if not self.initialized:
            self.InitGL()
            self.initialized = True
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3d(1.0, 0.0, 0.0)
        glBegin(GL_POLYGON)
        glVertex2d(-0.9, -0.9)
        glVertex2d(0.9, -0.9)
        glVertex2d(0.9, 0.9)
        glVertex2d(-0.9, 0.9)
        glEnd()
        glFlush()
        self.canvas.SwapBuffers()

if __name__ == '__main__':
    app = wx.App()
    frame = GLFrame(None, -1, sys.argv[0])
    frame.Show()
    app.MainLoop()
    app.Destroy()
