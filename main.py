from tkinter import Tk

import Data
import GUI
import Logic
import os


def main():
    music_directory = os.path.join(os.getcwd(),"music")
    playlist = Data.Playlist(music_directory)
    player = Logic.MusicPlayer(playlist)

    root = Tk()
    app = GUI.MusicPlayerGUI(player, root)
    root.mainloop()


if __name__ == "__main__":
    main()
