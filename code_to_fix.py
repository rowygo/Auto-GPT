import mido
import re


def generate_midi(beats, bpm, spacing, notes):
    midi = mido.MidiFile()
    midi.add_track()
    time_per_beat = 60 / bpm
    seconds_per_beat = time_per_beat * 1000
    tempo = mido.MetaMessage('set_tempo', tempo=round(seconds_per_beat), time=0)
    midi.tracks[0].append(tempo)
    
    time = 0
    for i, measure in enumerate(notes):
        for j, note in enumerate(measure):
            if note not in ['x', '\\', '', 'h', 'p']:
          midi.tracks[0].append(mido.Message('note_on', note=note, velocity=100, time=int(time*480), channel=0))
            midi.tracks[0].append(mido.Message('note_off', note=note, velocity=100, time=int((time+spacing)*480)))
            time += beats / len(measure)

    with open('tab_to_midi.mid', 'wb') as out_file:
        midi.writeFile(out_file)

bass_tab = """
G|--------------------------------------------------------
D|--------------------------------------------------------
A|-------0-2-3---0-2-0-------------------------------------
E|---0-3-----------------3-0--3-2--0-----------------------
      Am               C             D              F
"""
notes = [['A', '', '', 'C'], ['', '', 'D', ''], ['E', '', '', 'F'], ['G', '', '', '']]
notes = bass_tab
beats = 4
spacing = 0.125
bpm = 120 #define bpm here
generate_midi(beats, bpm, spacing, notes)

# read in tab data from input file
with open('input.txt', 'r') as file:
    tab_data = file.read()

# clean up tab data
tab_data = tab_data.replace('-', '0').replace('\n', '').replace('\r', '').replace('h', 'p').replace('p', '.')

# convert tab data to list of notes
note_list = []
for note_str in re.findall('Note: (\d+) Velocity: (\d+) Time: ([\d.]+)', tab_data):
    note, velocity, time = map(float, note_str)
    note_list.append({'note': int(note), 'velocity': velocity, 'time': time})

# create MIDI file and track
mid = mido.MidiFile(type=1)
track = mido.MidiTrack()
mid.tracks.append(track)

# add notes to track
time = 0
track.append(mido.Message('program_change', program=32, time=time))
for note in note_list:
    time += note['time']
    track.append(mido.Message('note_on', note=note['note'], velocity=int(note['velocity']), time=int(time*480)))
    track.append(mido.Message('note_off', note=note['note'], velocity=int(note['velocity']), time=int(time*480)))

# write MIDI file to output file
mid.save('output.mid')
