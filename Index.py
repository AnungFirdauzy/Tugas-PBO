import wx
import pboprak


class frame(pboprak.Main_Frame):
    def __init__(self, parent):
        pboprak.Main_Frame.__init__(self, parent)


app = wx.App()
Frame = frame(parent=None)
Frame.Show()
app.MainLoop()
