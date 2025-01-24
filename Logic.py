import pygame


class MusicPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        pygame.mixer.init()
        self.paused = False

    def play(self):
        song = self.playlist.get_current_song()
        if song:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            self.paused = False
            print(f"Odtwarzanie: {song}")

    def stop(self):
        pygame.mixer.music.stop()
        print("Zatrzymano odtwarzanie.")

    def pause(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
            print("Odtwarzanie zatrzymane.")
        else:
            pygame.mixer.music.unpause()
            self.paused = False
            print("Wznowiono odtwarzanie.")

    def next(self):
        self.playlist.next_song()
        self.play()

    def previous(self):
        self.playlist.previous_song()
        self.play()

    def shuffle(self):
        self.playlist.random_song()
        self.play()

    def replay(self):
        song = self.playlist.get_current_song()
        if song:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(start=0.0)
            print(f"Ponownie odtwarzanie: {song}")
