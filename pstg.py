import librosa
import essentia.standard as es
import numpy as np
import datetime

# original filename
file_path = "ff7-1-05-tifa's_theme _2_.wav"

# generate a timestamp
timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')

# create a new filename with timestamp
new_file_path = f'{file_path.split(".")[0]}_{timestamp}.wav'

print(new_file_path)

# Load the audio file
audio_file_path = "ff7-1-05-tifa's_theme _2_.wav"
audio, sr = librosa.load(audio_file_path, sr=None)

# define the path to your classifier model file
model_path = 'my_classifier.pkl'
# create a music extractor instance and set its model parameter
music_extractor = es.MusicExtractor(lowlevelStats=['mean', 'stdev'])
music_extractor = es.MusicExtractor(lowlevelStats=['mean', 'stdev'])
music_extractor = es.MusicExtractor(lowlevelStats=['mean', 'stdev'])
# extract features from an audio file
features, _ = music_extractor(audio_file_path)

# define some parameters
hop_length = 104
frame_length = 208
bass_note_range = ['C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1',                    'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2',                    'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3',                    'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4']

# Load the audio file
y, sr = librosa.load("ff7-1-05-tifa's_theme _2_.wav", sr=None)

# Determine the optimal value of n_fft based on the length of the input signal
n_fft = len(y) // 8

# Compute the STFT with the optimal value of n_fft
stft = librosa.stft(y, n_fft=n_fft)

# separate the bass and non-bass components of the signal
y_nonbass = librosa.effects.trim(librosa.resample(y, orig_sr=sr, target_sr=22050), top_db=30)[0] # assume non-bass is above 200 Hz
y, sr = librosa.load("ff7-1-05-tifa's_theme _2_.wav", sr=22050)

# Step 1: Verify that y is a numpy array and not a list
if not isinstance(y, np.ndarray):
    y = np.array(y)

# Step 2: Reshape y to a two-dimensional array if it is one-dimensional
if len(y.shape) == 1:
    y = y.reshape(-1, 1)

# Load the audio file
y, sr = librosa.load("ff7-1-05-tifa's_theme _2_.wav", sr=22050)

padded_signal = np.pad(y, (len(y), len(y)), 'constant', constant_values=0)

S_full, phase = librosa.magphase(librosa.stft(padded_signal, n_fft=208, hop_length=hop_length, win_length=208))

# calculate the magnitude spectrogram of the non-bass signal
n_fft = 512
S_full, phase = librosa.magphase(librosa.stft(y_nonbass, n_fft=n_fft, hop_length=hop_length, win_length=n_fft))

# extract the low-frequency noise floor using MFCCs
mfcc = librosa.feature.mfcc(y=y_nonbass, sr=sr, n_mfcc=1, dct_type=2, norm='ortho')
noise_floor = np.median(mfcc)

# identify the foreground components of the non-bass signal
S_foreground = S_full * (S_full > noise_floor)

# extract the chroma and spectral complexity features of the non-bass signal
chroma = librosa.feature.chroma_stft(S=S_foreground**2, sr=sr, hop_length=hop_length, n_chroma=12)
spectral_complexity = es.SpectralComplexity()(y_nonbass)

# extract the low-frequency noise floor using MFCCs
mfcc = librosa.feature.mfcc(y=y_nonbass, sr=sr, n_mfcc=1, dct_type=2, norm='ortho')
noise_floor = np.median(mfcc)

# identify the foreground components of the non-bass signal
S_foreground = S_full * (S_full > noise_floor)

# extract the chroma and spectral complexity features of the non-bass signal
chroma = librosa.feature.chroma_stft(S=S_foreground**2, sr=sr, hop_length=hop_length, n_chroma=12)
spectral_complexity = es.SpectralComplexity()(y_nonbass)

# Detect non-bass notes from the chroma features and transpose to bass guitar range
bass_notes = []
for i, frame in enumerate(chroma):
    note_idx = np.argmax(chroma[i])
    if note_idx >= len(bass_note_range):
      continue
    note = bass_note_range[note_idx]

    bass_note = note if note is not None else '-'
    semitones = note_idx - bass_note_range.index(note)

  # shift the pitch down by a number of semitones to bring it within the bass guitar range
    semitones = note_idx - bass_note_range.index(note)
    y_frame = y_nonbass[i*hop_length:(i+1)*hop_length]
    y_frame_shifted = librosa.effects.pitch_shift(y_frame, sr=sr, n_steps=semitones)
# calculate the magnitude spectrogram of the non-bass signal
S_full, phase = librosa.magphase(librosa.stft(y_nonbass, n_fft=512, hop_length=hop_length, win_length=512))

# extract the low-frequency noise floor using MFCCs
mfcc = librosa.feature.mfcc(y=y_nonbass, sr=sr, n_mfcc=1, dct_type=2, norm='ortho')
noise_floor = np.median(mfcc)

# identify the foreground components of the non-bass signal
S_foreground = S_full * (S_full > noise_floor)

# extract the chroma and spectral complexity features of the non-bass signal
chroma = librosa.feature.chroma_stft(S=S_foreground**2, sr=sr, hop_length=hop_length, n_chroma=12)
spectral_complexity = es.SpectralComplexity()(y_nonbass)

# Detect non-bass notes from the chroma features and transpose to bass guitar range
bass_notes = []
for i, frame in enumerate(chroma):
    note_idx = np.argmax(chroma[i])
    if note_idx >= len(bass_note_range):
      continue
    note = bass_note_range[note_idx]

    bass_note = note if note is not None else '-'
    semitones = note_idx - bass_note_range.index(note)

  # shift the pitch down by a number of semitones to bring it within the bass guitar range
    semitones = note_idx - bass_note_range.index(note)
    y_frame = y_nonbass[i*hop_length:(i+1)*hop_length]
    y_frame_shifted = librosa.effects.pitch_shift(y_frame, sr=sr, n_steps=semitones)
    y_nonbass[i*hop_length:(i+1)*hop_length] = y_frame_shifted
    bass_notes.append(note)

    # shift the pitch down by a number of semitones to bring it within the bass guitar range
    semitones = note_idx - bass_note_range.index(note)
    y_frame = y_nonbass[i*hop_length:(i+1)*hop_length]
    y_frame_shifted = librosa.effects.pitch_shift(y_frame, sr=sr, n_steps=semitones)
    y_nonbass[i*hop_length:(i+1)*hop_length] = y_frame_shifted
    bass_notes.append(note)

# create a text file to store the bass tab
f = open('bass_tab.txt', 'w')
f.write('Bass Tab of Audio File\n\n')
f.write('Time\t\tNote\n')

# loop through each frame and write the bass notes to the text file
for i in range(len(bass_notes)):
    time = librosa.frames_to_time(i, sr=sr, hop_length=hop_length)
    note = bass_notes[i]
    if note == None:
        bass_note = '-'
    else:
        bass_note = note

    f.write('{:.2f}-{:02.0f}\t\t{}\n'.format(np.floor(time), np.round((time % 1) * 100), bass_note))

# separate the bass and non-bass components of the signal
y_nonbass = librosa.effects.trim(librosa.resample(y, orig_sr=sr, target_sr=22050), top_db=30)[0] # assume non-bass is above 200 Hz
y, sr = librosa.load("ff7-1-05-tifa's_theme _2_.wav", sr=22050)




S_full, phase = librosa.magphase(librosa.stft(padded_signal, n_fft=200, hop_length=hop_length, win_length=200))

# calculate the magnitude spectrogram of the non-bass signal
n_fft = 512
S_full, phase = librosa.magphase(librosa.stft(y_nonbass, n_fft=n_fft, hop_length=hop_length, win_length=n_fft))

# extract the low-frequency noise floor using MFCCs
mfcc = librosa.feature.mfcc(y=y_nonbass, sr=sr, n_mfcc=1, dct_type=2, norm='ortho')
noise_floor = np.median(mfcc)

# identify the foreground components of the non-bass signal
S_foreground = S_full * (S_full > noise_floor)

# extract the chroma and spectral complexity features of the non-bass signal
chroma = librosa.feature.chroma_stft(S=S_foreground**2, sr=sr, hop_length=hop_length, n_chroma=12)
spectral_complexity = es.SpectralComplexity()(y_nonbass)


# extract the low-frequency noise floor using MFCCs
mfcc = librosa.feature.mfcc(y=y_nonbass, sr=sr, n_mfcc=1, dct_type=2, norm='ortho')
noise_floor = np.median(mfcc)

# identify the foreground components of the non-bass signal
S_foreground = S_full * (S_full > noise_floor)

# extract the chroma and spectral complexity features of the non-bass signal
chroma = librosa.feature.chroma_stft(S=S_foreground**2, sr=sr, hop_length=hop_length, n_chroma=12)

# Detect non-bass notes from the chroma features and transpose to bass guitar range
bass_notes = []
for i, frame in enumerate(chroma):
    note_idx = np.argmax(chroma[i])
    if note_idx >= len(bass_note_range):
      continue
    note = bass_note_range[note_idx]

    bass_note = note if note is not None else '-'
    semitones = note_idx - bass_note_range.index(note)

  # shift the pitch down by a number of semitones to bring it within the bass guitar range
    semitones = note_idx - bass_note_range.index(note)
    y_frame = y_nonbass[i*hop_length:(i+1)*hop_length]
    y_frame_shifted = librosa.effects.pitch_shift(y_frame, sr=sr, n_steps=semitones)
    y_nonbass[i*hop_length:(i+1)*hop_length] = y_frame_shifted
    bass_notes.append(note)

    # shift the pitch down by a number of semitones to bring it within the bass guitar range
    semitones = note_idx - bass_note_range.index(note)
    y_frame = y_nonbass[i*hop_length:(i+1)*hop_length]
    y_frame_shifted = librosa.effects.pitch_shift(y_frame, sr=sr, n_steps=semitones)
    # separate the bass and non-bass components of the signal
y_nonbass = librosa.effects.trim(librosa.resample(y, orig_sr=sr, target_sr=22050), top_db=30)[0] # assume non-bass is above 200 Hz
y, sr = librosa.load("ff7-1-05-tifa's_theme _2_.wav", sr=22050)

padded_signal = librosa.util.pad_center(y, len(y)*2, mode='constant')

S_full, phase = librosa.magphase(librosa.stft(padded_signal, n_fft=208, hop_length=hop_length, win_length=208))

# calculate the magnitude spectrogram of the non-bass signal
n_fft = 512
S_full, phase = librosa.magphase(librosa.stft(y_nonbass, n_fft=n_fft, hop_length=hop_length, win_length=n_fft))

# extract the low-frequency noise floor using MFCCs
mfcc = librosa.feature.mfcc(y=y_nonbass, sr=sr, n_mfcc=1, dct_type=2, norm='ortho')
noise_floor = np.median(mfcc)

# identify the foreground components of the non-bass signal
S_foreground = S_full * (S_full > noise_floor)

# extract the chroma and spectral complexity features of the non-bass signal
chroma = librosa.feature.chroma_stft(S=S_foreground**2, sr=sr, hop_length=hop_length, n_chroma=12)
spectral_complexity = es.SpectralComplexity()(y_nonbass)

# Detect non-bass notes from the chroma features and transpose to bass guitar range
bass_notes = []
for i, frame in enumerate(chroma):
    note_idx = np.argmax(chroma[i])
    if note_idx >= len(bass_note_range):
      continue
    note = bass_note_range[note_idx]

    bass_note = note if note is not None else '-'
    semitones = note_idx - bass_note_range.index(note)

  # shift the pitch down by a number of semitones to bring it within the bass guitar range
    semitones = note_idx - bass_note_range.index(note)
    y_frame = y_nonbass[i*hop_length:(i+1)*hop_length]
    y_frame_shifted = librosa.effects.pitch_shift(y_frame, sr=sr, n_steps=semitones)

    y_nonbass[i*hop_length:(i+1)*hop_length] = y_frame_shifted
    bass_notes.append(note)

# create a text file to store the bass tab
f = open('bass_tab.txt', 'w')
f.write('Bass Tab of Audio File\n\n')
f.write('Time\t\tNote\n')

# loop through each frame and write the bass notes to the text file
for i in range(len(bass_notes)):
    time = librosa.frames_to_time(i, sr=sr, hop_length=hop_length)
    note = bass_notes[i]
    if note == None:
        bass_note = '-'
    else:
        bass_note = note

    f.write('{:.2f}-{:02.0f}\t\t{}\n'.format(np.floor(time), np.round((time % 1) * 100), bass_note))

f.close()
