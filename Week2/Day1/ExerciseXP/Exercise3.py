# Step 1: Create the Song class
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Step 2: Create a Song object
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Step 3: Call the method to print the lyrics
stairway.sing_me_a_song()
