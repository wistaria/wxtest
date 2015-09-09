import sys
import wx
from wx import glcanvas

class MyCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        super(MyCanvas, self).__init__(parent, -1, attribList=[])

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, sys.argv[0], size=(300,300))
    canvas = MyCanvas(frame)
    frame.Show()
    app.MainLoop()
    app.Destroy()
