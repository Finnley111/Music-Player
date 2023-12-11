import musicalbeeps
from melody import Melody

if __name__ == "__main__":
    player = musicalbeeps.Player()
    melody = Melody("Megalovania.txt")
    for note in melody.notes:
        print(note)
#     melody.change_tempo(0.75)
    print(melody.get_total_duration())
#     melody.lower_octave()
    
#     melody.lower_octave()
#     melody.upper_octave()
#     melody.upper_octave()
    melody.play(player)