import wx

app = wx.App()

frm = wx.Frame(None, title="一个窗口", size=(400, 300), pos=(100, 200))

frm.Show()

app.MainLoop()
