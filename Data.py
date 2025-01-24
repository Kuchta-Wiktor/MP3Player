import os
import random


class Playlist:
    def __init__(self, directory):
        self.songs = self.load_songs(directory)
        self.current_index = 0

    def load_songs(self, directory):
        return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".mp3")]

    def get_current_song(self):
        return self.songs[self.current_index] if self.songs else None

    def next_song(self):
        if self.songs:
            self.current_index = (self.current_index + 1) % len(self.songs)
            return self.get_current_song()
        return None

    def previous_song(self):
        if self.songs:
            self.current_index = (self.current_index - 1) % len(self.songs)
            return self.get_current_song()
        return None

    def random_song(self):
        if self.songs:
            self.current_index = random.randint(0, len(self.songs) - 1)
            return self.get_current_song()
        return None
