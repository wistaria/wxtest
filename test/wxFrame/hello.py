#!/usr/bin/env python
 
import wx
 
class TestFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, -1, title, pos=(0, 0), size=(320, 240))
        panel = wx.Panel(self, -1)
        text = wx.StaticText(panel, -1, "Hello, World!", wx.Point(10, 5), wx.Size(-1, -1))
 
class TestApp(wx.App):
    def OnInit(self):
        frame = TestFrame(None, -1, "Hello, world!")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
 
if __name__ == '__main__':
    app = TestApp()
    app.MainLoop()
