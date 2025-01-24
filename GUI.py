import os
from tkinter import Button, Listbox, END


class MusicPlayerGUI:
    def __init__(self, player, root):
        self.player = player
        self.root = root
        self.root.title("Odtwarzacz Muzyki")

        Button(root, text="Odtwórz", command=self.play_selected_song).pack()
        Button(root, text="Zatrzymaj", command=self.player.stop).pack()
        Button(root, text="Pauza/Wznowienie", command=self.player.pause).pack()
        Button(root, text="Odtwórz od nowa", command=self.player.replay).pack()
        Button(root, text="Poprzedni", command=self.player.previous).pack()
        Button(root, text="Następny", command=self.player.next).pack()
        Button(root, text="Losowe", command=self.player.shuffle).pack()

        self.song_list = Listbox(root, width=50, height=5)
        self.song_list.pack()

        for song in self.player.playlist.songs:
            self.song_list.insert(END, os.path.basename(song))
    def play_selected_song(self):
        selected_index = self.song_list.curselection()
        if len(selected_index) != 0:
            self.player.playlist.current_index = selected_index[0]
            self.player.play()

