import sys
import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLU import *

class MyCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        super(MyCanvas, self).__init__(parent, -1, attribList=[])
        self.context = glcanvas.GLContext(self)
        self.initialized = False
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.InitVertices()

    def InitVertices(self):
        self.vertex = [  [ 0.0, 0.0, 0.0 ],
                         [ 1.0, 0.0, 0.0 ],
                         [ 1.0, 1.0, 0.0 ],
                         [ 0.0, 1.0, 0.0 ],
                         [ 0.0, 0.0, 1.0 ],
                         [ 1.0, 0.0, 1.0 ],
                         [ 1.0, 1.0, 1.0 ],
                         [ 0.0, 1.0, 1.0 ]]

        self.edge = [ [ 0, 1 ],
                      [ 1, 2 ],
                      [ 2, 3 ],
                      [ 3, 0 ],
                      [ 4, 5 ],
                      [ 5, 6 ],
                      [ 6, 7 ],
                      [ 7, 4 ],
                      [ 0, 4 ],
                      [ 1, 5 ],
                      [ 2, 6 ],
                      [ 3, 7 ]]



    def InitGL(self):
        glClearColor(1.0, 1.0, 1.0, 1.0)

    def OnSize(self, event):
        w, h = self.GetClientSize()
        glViewport(0, 0, w, h)
        glLoadIdentity()
        gluPerspective(30.0, 1.0*w / h, 1.0, 100.0);
        gluLookAt(3.0, 4.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        
    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.initialized:
            self.InitGL()
            self.initialized = True
        self.OnSize(event)
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3d(0.0, 0.0, 0.0)
        glBegin(GL_LINES)
        for e in self.edge:
          glVertex3dv( self.vertex[e[0]])
          glVertex3dv( self.vertex[e[1]])
        glEnd()
        glFlush()

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, sys.argv[0], size=(300,300))
    canvas = MyCanvas(frame)
    frame.Show()
    app.MainLoop()
    app.Destroy()
