import wx
import Variables as vb
import Video
from functools import partial
import sys


def cargar_video(e, numero):
    cargar = wx.Frame(None, -1, 'win.py')
    cargar.SetSize(0, 0, 200, 50)

    dlg = wx.FileDialog(cargar)

    if dlg.ShowModal() == wx.ID_OK:
        if numero == 1:
            vb.video_principal = dlg.GetPath()
            input_video.SetValue(dlg.GetPath())
        else:
            vb.video_cabecera = dlg.GetPath()
            input_cabecera.SetValue(dlg.GetPath())


def salir(e):
    sys.exit(0)


def combinar(e):
    Video.video(e)


app = wx.App()
frame = wx.Frame(None, size=(500, 300), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

panel = wx.Panel(frame)

texto_video = wx.StaticText(panel, label="Video principal", pos=(20, 40))

texto_cabecera = wx.StaticText(panel, label="Video Cabecera", pos=(20, 100))

input_video = wx.TextCtrl(panel, pos=(120, 38), style=wx.TE_READONLY)

input_cabecera = wx.TextCtrl(panel, pos=(120, 98), style=wx.TE_READONLY)

boton_video = wx.Button(panel, pos=(250, 37), label="Cargar vídeo principal")
boton_video.Bind(wx.EVT_BUTTON, partial(cargar_video, numero=1))

boton_cabecera = wx.Button(panel, pos=(250, 97), label="Cargar vídeo de cabecera")
boton_cabecera.Bind(wx.EVT_BUTTON, partial(cargar_video, numero=0))

boton_salir = wx.Button(panel, pos=(150, 160), label="Salir")
boton_salir.Bind(wx.EVT_BUTTON, salir)

boton_combinar = wx.Button(panel, pos=(20, 160), label="Combinar Vídeos")
boton_combinar.Bind(wx.EVT_BUTTON, combinar)

frame.Show()
app.MainLoop()
