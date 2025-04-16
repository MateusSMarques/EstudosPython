import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Variáveis globais
current_volume = 0.5
loaded = False  # Controla se um arquivo foi carregado


# Funções
def load_music():
    global loaded
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")])

    if file_path:
        try:
            pygame.mixer.music.load(file_path)
            lbl_status.config(text=f"🎵 Arquivo carregado: {file_path.split('/')[-1]}")
            loaded = True
            update_buttons()  # Ativa os botões
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar o arquivo:\n{str(e)}")
            loaded = False


def play_music():
    if not loaded:
        messagebox.showwarning("Aviso", "Carregue um arquivo de áudio primeiro!")
        return

    if pygame.mixer.music.get_busy():  # Pausar se já estiver tocando
        pygame.mixer.music.pause()
        btn_play.config(text="▶ Play")
    else:  # Tocar ou despausar
        pygame.mixer.music.play()
        btn_play.config(text="⏸ Pausar")


def stop_music():
    pygame.mixer.music.stop()
    btn_play.config(text="▶ Play")


def set_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)


def update_buttons():
    if loaded:
        btn_play.config(state=tk.NORMAL)
        btn_stop.config(state=tk.NORMAL)
    else:
        btn_play.config(state=tk.DISABLED)
        btn_stop.config(state=tk.DISABLED)


# Interface gráfica
root = tk.Tk()
root.title("Player de Áudio")

# Botões
btn_load = tk.Button(root, text="📂 Carregar Música", command=load_music)
btn_load.pack(pady=10)

btn_play = tk.Button(root, text="▶ Play", command=play_music, state=tk.DISABLED)
btn_play.pack(pady=5)

btn_stop = tk.Button(root, text="⏹ Parar", command=stop_music, state=tk.DISABLED)
btn_stop.pack(pady=5)

# Controle de volume
tk.Label(root, text="Volume:").pack()
scale_volume = tk.Scale(root, from_=0, to=100, orient="horizontal", command=set_volume)
scale_volume.set(50)
scale_volume.pack()

# Status
lbl_status = tk.Label(root, text="Nenhum arquivo carregado")
lbl_status.pack(pady=10)

root.mainloop()