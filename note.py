# Name: Finnley Howald
# Student ID: 261099492


import musicalbeeps


class Note:
    ''' A class representing a musical note.
    Instance Attributes:
    * duration: float
    * pitch: str
    * octave: int
    * accidental: str
    Class Attributes:
    * OCTAVE_MIN: int
    * OCTAVE_MAX: int
    '''
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self, dur, pitch, octave = 1, acc = 'natural'):
        ''' (float, str, int, str) -> NoneType
        Creates an object of Note type.
        
        >>> note = Note(1.0, "A", 3, 'natural')
        >>> note.duration
        1.0
        >>> note.pitch
        'A'
        >>> note.octave
        3
        >>> note.accidental
        'natural'
        >>> note = Note(10.0, "Z", 1, 'sharp')
        Traceback (most recent call last):
        AssertionError: Incorrect Arguments
        '''
        if type(dur) != float or type(pitch) != str or type(octave) != int or type(acc) != str:
            raise AssertionError('Incorrect Arguments')
        
        if dur < 0 or octave < Note.OCTAVE_MIN or octave > Note.OCTAVE_MAX:
            raise AssertionError('Incorrect Arguments')
        
        if len(pitch) != 1 or pitch not in 'ABCDEFGR':
            raise AssertionError('Incorrect Arguments')
        
        if acc != 'sharp' and acc != 'flat' and acc != 'natural':
            raise AssertionError('Incorrect Arguments')
        
        self.duration = dur
        self.pitch = pitch
        self.octave = octave
        self.accidental = acc
        
    
    def __str__(self):
        ''' () -> str
        Returns a string of a description of a Note object.
        
        >>> note = Note(1.0, "A", 3, 'natural')
        >>> print(note)
        1.0 A 3 natural
        >>> note = Note(1.0, "B", 3, 'natural')
        >>> print(note)
        1.0 B 3 natural
        >>> note = Note(10.0, "D", 1, 'sharp')
        >>> print(note)
        10.0 D 1 sharp
        '''
        return str(self.duration) + ' ' + self.pitch + ' ' + str(self.octave) + ' ' + self.accidental
    
    
    def play(self, player):
        ''' (player) -> NoneType

        Returns void, plays the Note object so it is audible.
        '''
        accidental = ''
        if self.accidental == 'flat':
            accidental = 'b'
        elif self.accidental == 'sharp':
            accidental = '#'
         
        note_str = self.pitch + str(self.octave) + accidental
        
        if self.pitch == 'R':
            note_str = 'pause'
        
        player.play_note(note_str, self.duration)