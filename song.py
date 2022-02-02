def format_sec(sec):
    l_mn = int(sec / 60)
    l_sc = sec % 60
    return f"{l_mn}:{f'0{l_sc}' if l_sc < 10 else l_sc}"

class Song:
    def __init__(self, song_name, song_length, song_performer, song_key, song_genre):
        self.name = song_name
        self.length = song_length
        self.performer = song_performer
        self.key = song_key
        self.genre = song_genre
    def get_song(self):
        return {
            "song_name": self.name,
            "song_length": self.length,
            "song_performer": self.performer,
            "song_key": self.key,
            "song_genre": self.genre
        }
    def get_song_as_string(self):
        return f"{self.genre}: {self.name} ({format_sec(self.length)}) in {self.key} - by {self.performer}"
    def is_it_long(self):
        return True if self.length >= 300 else False
    

def main():
    song = Song('Gdzie jest biały węgorz ?', 243, 'Cypis', 'A Minor', 'rap')
    print(song.get_song_as_string())
    print(song.get_song())
    print(song.is_it_long())

if __name__ == '__main__':
    main()