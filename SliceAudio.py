###########################
#dr.mark.schultz@gmail.com#
#220715####################
###########################
import os
import glob
from pydub import AudioSegment
import argparse

"""
Dependencies:
1. gcc
2. pydub (sudo pip install pydub), see https://github.com/jiaaro/pydub
3. ffmpeg (brew install libav --with-libvorbis --with-sdl --with-theora)

Default will spit out wav file slices of 2 second duration, in 16bit/mono/44.1kHz sample rate (Useful for the
Analog Elektron Rytm drum machine).
Will chop up the input file and spit out slices along its length until it reaches the end of the file.
Can input/output in any format that ffmpeg supports.

example usage:
python SliceAudio.py -i xyz.m4a -f m4a -b 2 -s 11025 -l 10000

"""

#parse command line input
PARSER = argparse.ArgumentParser(description=
								"""
								Generates one-shot samples from long audio files in batch.
								""")
PARSER.add_argument('-i', '--infiles', help=
					"""
					Name of input files. Can use e.g., '*.mp3' to bring up all mp3 files in a path.
					"""
					, nargs='+', required=True)
PARSER.add_argument('-o', '--outchannels', help=
					"""
					Number of output channels per file. '1', mono (default); '2', stereo.
					""", default = 1, required=False)
PARSER.add_argument('-f', '--format_out', help=
					"""
					Output format of files. 'wav' .wav (default); 'mp3', .mp3 etc.
					""", default = 'wav', required=False)
PARSER.add_argument('-b', '--sample_width', help=
					"""
					Number of bytes in each sample. '1' 8 bit, '2' 16 bit (default).
					""", default = 2, required=False)
PARSER.add_argument('-s', '--sample_rate', help=
					"""
					Sample rate of slices. '44100' (44.1kHz, default, CD quality); '48000' (DVD). Other common rates are '22050', '24000', '12000' and '11025'.
					""", default = 44100, required=False)
PARSER.add_argument('-l', '--sample_slice_length_ms', help=
					"""
					Length of sample slices in milliseconds. '2000' (default, 2 seconds).
					""", default = 2000, required=False)

ARGS = PARSER.parse_args()


def slice_audio(files, channels, outformat, width, rate, slice_length):
	for file in files:
		file_parameters = []
		fileName, fileExtension = os.path.splitext(file)
		sound = AudioSegment.from_file(file, fileExtension.replace('.',''))
		sound = sound.set_frame_rate(int(rate))
		sound = sound.set_sample_width(int(width))
		sound = sound.set_channels(int(channels))
		length_sound_ms = len(sound)
		length_slice_ms = int(slice_length)
		slice_start = 0
		while slice_start + length_slice_ms < length_sound_ms:
			sound_slice = sound[slice_start:slice_start+length_slice_ms]
			sound_slice.export(fileName+'.slice'+str(slice_start/1000)+'SecsTo'+str((slice_start+length_slice_ms)/1000)+'Secs.'+outformat, format=outformat)
			slice_start += length_slice_ms

slice_audio(ARGS.infiles, ARGS.outchannels, ARGS.format_out, ARGS.sample_width, ARGS.sample_rate, ARGS.sample_slice_length_ms)
