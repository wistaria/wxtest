import sys
import wx
from wx import glcanvas

class GLFrame(wx.Frame):
    """A simple class for using OpenGL with wxPython.
    """
    def __init__(self, parent, id, title, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='frame'):
        super(GLFrame, self).__init__(parent, id, title, pos, size, style, name)
        self.canvas = glcanvas.GLCanvas(self)

app = wx.App()
frame = GLFrame(None, -1, sys.argv[0])
frame.Show()

app.MainLoop()
app.Destroy()
