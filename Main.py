import wx

app = wx.App()
frame = wx.Frame(None, size=(500, 300), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

panel = wx.Panel(frame)

texto_video = wx.StaticText(panel, label="Video principal", pos=(20, 40))

texto_cabecera = wx.StaticText(panel, label="Video Cabecera", pos=(20, 100))

input_video = wx.TextCtrl(panel, pos=(120, 38), style=wx.TE_READONLY)

input_cabecera = wx.TextCtrl(panel, pos=(120, 98), style=wx.TE_READONLY)

boton_video = wx.Button(panel, pos=(250, 37), label="Cargar vídeo principal")

boton_cabecera = wx.Button(panel, pos=(250, 97), label="Cargar vídeo de cabecera")

boton_salir = wx.Button(panel, pos=(20, 160), label="Salir")

boton_combinar = wx.Button(panel, pos=(120, 160), label="Combinar Vídeos")

frame.Show()
app.MainLoop()
