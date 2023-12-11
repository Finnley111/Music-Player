# Music-Player

## Overview
This Python project creates a simple music player that reads musical notes from a text file and plays them using the musicalbeeps library. The text file contains the musical sheet in a structured format, including the song's metadata, notes, octaves, accidentals, and durations. Repeated sequences of notes are also supported.

## Requirements
Python 3.x
musicalbeeps library

## Installation
Before running the script, you need to install the musicalbeeps library. You can install it using pip:
pip install musicalbeeps

## Usage
To use the music player, you need a text file (song.txt) containing the song's data in the specified format.

## Text File Format
The text file should have the following structure:

The first line contains the song's title.

The second line contains the author's name or "Traditional" if it's a traditional song.

Subsequent lines each represent a single note in the following format: <duration> <pitch> <octave> <accidental> <repeat>

<duration> is a float representing the note's duration.

<pitch> is a single character (A-G) representing the note's pitch, or R for a rest.

<octave> is an integer indicating the octave number.

<accidental> is one of the following: SHARP, FLAT, or NATURAL.

<repeat> is a boolean (true or false). If true, the sequence that the note is part of will be repeated.

## Example of a text file content:

Hot Cross Buns
Traditional
0.5 B 4 NATURAL true
0.5 A 4 NATURAL false
1 G 4 NATURAL true
0.5 R false
.25 G 4 NATURAL true
.25 G 4 NATURAL true
.25 A 4 NATURAL true
.25 A 4 NATURAL true
0.5 R false
0.5 B 4 NATURAL false
0.5 A 4 NATURAL false
1 G 4 NATURAL false


## Running the Music Player
Execute play_melody.py with the text file as an argument for Melody:

melody = Melody("hotcrossbuns.txt")
The script will read the song data from the file and play it back using musical tones.

## Acknowledgements
Thanks to the creators of the musicalbeeps library for providing the means to play musical notes in Python.
This project was inspired by the traditional methods of representing and playing music programmatically.

## Enjoy making music with Python!





