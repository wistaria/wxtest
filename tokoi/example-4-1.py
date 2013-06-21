import sys
import wx

app = wx.App()
frame = wx.Frame(None, -1, sys.argv[0])
frame.Show()

app.MainLoop()
app.Destroy()
