from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog


volume = float(0.5)


# Funcoes
def play_song():
    filename = filedialog.askopenfilename(initialdir="C:/", title="Selecione um arquivo")
    song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]

    try:
        mixer.init()
        mixer.music.load(song)
        mixer.music.set_volume(volume)
        mixer.music.play()
        song_title_label.config(fg="green", text="Tocando Agora : " + str(song_title))
        volume_label.config(fg="green", text="Volume : " + str(volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Erro de Reprodução")


def diminuir_volume():
    try:
        global volume
        if volume <= 0:
            volume_label.config(fg="red", text="Volume : Mudo")
            return
        volume = volume - float(0.1)
        volume = round(volume, 1)
        mixer.music.set_volume(volume)
        volume_label.config(fg="green", text="Volume : " + str(volume))
    except Exception as e:
        print(e)
        volume_label.config(fg="red", text="A faixa ainda não foi selecionada")


def aumentar_volume():
    try:
        global volume
        if volume >= 1:
            volume_label.config(fg="green", text="Volume : Maximo")
            return
        volume = volume + float(0.1)
        volume = round(volume, 1)
        mixer.music.set_volume(volume)
        volume_label.config(fg="green", text="Volume : " + str(volume))
    except Exception as e:
        print(e)
        volume_label.config(fg="red", text="A faixa ainda não foi selecionada")


def pausa():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        volume_label.config(fg="red", text="A faixa ainda não foi selecionada")


def retomar():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        volume_label.config(fg="red", text="A faixa ainda não foi selecionada")


# Tela Principal
janela = Tk()
janela.title("Reprodutor de Música")
janela.resizable(False, False)
janela["bg"] = "black"

# Labels
Label(janela, text="Reprodução Personalizada", font=("Calibri", 14), fg="red", bg="black").grid(sticky="N", row=0, padx=120)
Label(janela, text="Por favor, selecione uma faixa de música que você gostaria de tocar",
      font=("Calibri", 12), fg="blue", bg="black").grid(sticky="N", row=1, padx=120)
Label(janela, text="Volume", font=("Calibri", 14), fg="red", bg="black").grid(sticky="N", row=4, padx=120)

song_title_label = Label(janela, font=("calibri", 12), bg="black")
song_title_label.grid(sticky="N", row=3)

volume_label = Label(janela, font=("Calibri", 12), bg="black")
volume_label.grid(sticky="N", row=5)

# Botoes
Button(janela, text="Selecione a música", font=("Calibri", 12), command=play_song, relief="raised", bd=7).grid(row=2, sticky="N")
Button(janela, text="Pausa", font=("Calibre", 12), command=pausa, relief="raised", bd=7).grid(row=3, sticky="E")
Button(janela, text="Retomar", font=("Calibre", 12), command=retomar, relief="raised", bd=7).grid(row=3, sticky="W")
Button(janela, text="-", font=("Calibre", 12), width=5, command=diminuir_volume, relief="raised", bd=7).grid(row=5, sticky="W")
Button(janela, text="+", font=("Calibre", 12), width=5, command=aumentar_volume, relief="raised", bd=7).grid(row=5, sticky="E")


janela.mainloop()
