# Name: Finnley Howald
# Student ID: 261099492


import musicalbeeps
import note


class Melody:
    ''' A class representing a melody of made of musical note.
    Instance Attributes:
    * title: str
    * author: str
    * notes: list<Note>
    ''' 
    def __init__(self, filename):
        ''' (str) -> NoneType
        Creates an object of Melody type.
        
        >>> m = Melody('hotcrossbuns.txt')
        >>> m.title
        'Hot Cross Buns'
        >>> m.author
        'Traditional'
        >>> m = Melody('birthday.txt')
        >>> m.title
        'Happy Birthday'
        '''
        fobj = open(filename, 'r')
        content_list = fobj.read().split('\n')
        fobj.close()
        
        self.title = content_list[0]
        self.author = content_list[1]
        self.notes = []
    
        line_i = 2
        while line_i < len(content_list):
            
            note_list = content_list[line_i].split()
            
            if note_list[-1] == 'true':
                
                start = line_i
                
                for line_2 in range(line_i + 1, len(content_list)):
                    
                    if 'true' in ''.join(content_list[line_2]):
                        stop = line_2
                        break
                        
                for time in range(2):
                    
                    for n in range(start, stop + 1):
                        note_list = content_list[n].split()
                        if note_list[1] == 'R':
                            new_note = note.Note(float(note_list[0]), note_list[1])
                        else:
                            new_note = note.Note(float(note_list[0]), note_list[1], int(note_list[2]), note_list[3].lower())
                        self.notes.append(new_note)
                line_i = line_2 + 1
            else:
                if note_list[1] == 'R':
                    new_note = note.Note(float(note_list[0]), note_list[1])
                else:
                    new_note = note.Note(float(note_list[0]), note_list[1], int(note_list[2]), note_list[3].lower())
                self.notes.append(new_note)
                line_i += 1
        
        
    def play(self, player):
        ''' (player) -> NoneType
        Returns void, plays a melody of notes.
        '''
        for n in self.notes:
            n.play(player)
            
    
    def get_total_duration(self):
        ''' () -> float
        Returns the total duration of a melody as a float.
        
        >>> m = Melody('birthday.txt')
        >>> m.get_total_duration()
        13.0
        >>> m = Melody('tetris.txt')
        >>> m.get_total_duration()
        15.5
        >>> m = Melody('fur_elise.txt')
        >>> m.get_total_duration()
        25.799999999999944
        '''
        total_d = 0
        
        for n in self.notes:
            total_d += n.duration
        
        return total_d
    
    
    def helper_octave(self, num):
        '''
        (int) -> bool
        Returns a bool of wheather the melody can be lowered
        or raised by an octave. Raises the octave of each note
        in the melody by num.
        
        >>> m = Melody('birthday.txt')
        >>> m.helper_octave(1)
        True
        >>> m.helper_octave(-1)
        True
        >>> m.helper_octave(2)
        True
        '''
        for n in self.notes:
            if n.octave == 'R':
                continue
            elif n.octave + num <= note.Note.OCTAVE_MIN and n.octave + num >= note.Note.OCTAVE_MAX:
                return False
            else:
                n.octave += num
        return True
    
    
    def lower_octave(self):
        ''' () -> bool
        Retuns True if every note of the melody can be have the octave
        lowered by one, returns false otherwise.
        
        >>> m = Melody('birthday.txt')
        >>> m.lower_octave()
        True
        >>> m = Melody('tetris.txt')
        >>> m.lower_octave()
        True
        >>> m = Melody('fur_elise.txt')
        >>> m.lower_octave()
        True
        '''
        return self.helper_octave(-1)
    
    
    def upper_octave(self):
        ''' () -> bool
        Retuns True if every note of the melody can be have the octave
        lowered by one, returns false otherwise.
        
        >>> m = Melody('birthday.txt')
        >>> m.upper_octave()
        True
        >>> m = Melody('hotcrossbuns.txt')
        >>> m.upper_octave()
        True
        >>> m = Melody('tetris.txt')
        >>> m.upper_octave()
        True
        '''
        return self.helper_octave(1)
            
            
    def change_tempo(self, tempo):
        ''' (float) -> NoneType
        Returns void, multiplies the duration of each note by
        a factor of tempo.
        
        >>> m = Melody('birthday.txt')
        >>> m.change_tempo(0.5)
        >>> m.get_total_duration()
        6.5
        >>> m = Melody('fur_elise.txt')
        >>> m.change_tempo(0.5)
        >>> m.get_total_duration()
        12.899999999999972
        >>> m = Melody('tetris.txt')
        >>> m.change_tempo(0.5)
        >>> m.get_total_duration()
        7.75
        '''
        for n in self.notes:
            n.duration *= tempo