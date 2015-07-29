###########################
#dr.mark.schultz@gmail.com#
#220715####################
###########################
import os
import glob
from pydub import AudioSegment
import argparse
import audioread


"""
Dependencies:
1. gcc
2. pydub (sudo pip install pydub), see https://github.com/jiaaro/pydub
3. ffmpeg (brew install libav --with-libvorbis --with-sdl --with-theora)
4. audioread (sudo pip install audioread)
Default will spit out wav file slices of 2 second duration, in 16bit/mono/44.1kHz sample rate (Useful for the
Analog Elektron Rytm drum machine).
Will chop up the input file and spit out slices along its length until it reaches the end of the file.
Can input/output in any format that ffmpeg supports.

example usage:
python SliceAudio.py -i xyz.m4a -f m4a -b 2 -s 11025 -l 10000
python SliceAudio.py -h
"""

#parse command line input
PARSER = argparse.ArgumentParser(description=
								"""
								Generates one-shot samples from long audio files in batch.\n
								Email: dr.mark.schultz@gmail.com for questions/feedback.
								""")
PARSER.add_argument('-i', '--infiles', help=
					"""
					Name of input files. Can use e.g., '*.mp3' to bring up all mp3 files in a path.
					"""
					, nargs='+', required=True)
PARSER.add_argument('-c', '--channels', help=
					"""
					Number of output channels per file. '1', mono (default); '2', stereo.
					""", default = 1, required=False)
PARSER.add_argument('-f', '--format_out', help=
					"""
					Output format of files. 'wav' .wav (default); 'mp3', .mp3 etc.
					""", default = 'wav', required=False)
PARSER.add_argument('-b', '--sample_width', help=
					"""
					Number of bytes in each sample. Options are: '1'=8-bit; '2'=16-bit (default); '4'=32-bit.  Note program will exit with a 'key error' if an option other than 1, 2 or 4 is selected.
					""", default = 2, required=False)
PARSER.add_argument('-s', '--sample_rate', help=
					"""
					Sample rate of slices. '44100' (44.1kHz, CD quality); '48000' (default, DVD quality). Other common rates are '22050', '24000', '12000' and '11025'.
					""", default = 48000, required=False)
PARSER.add_argument('-l', '--sample_slice_length_ms', help=
					"""
					Length of sample slices in milliseconds. '2000' (default, 2 seconds).
					""", default = 2000, required=False)
PARSER.add_argument('-o', '--slice_overlap_slide_ms', help=
					"""
					Move the slice window this many milliseconds along to make the next slice (a 'sliding window'). '2000' (default, 2 seconds).
					""", default = 2000, required=False)


ARGS = PARSER.parse_args()

#Function to slice up the audio.
def slice_audio(files, channels, outformat, width, rate, slice_length, overlap):
	outformat = outformat.replace('.','').lower()
	#Allow the user to see their x-bit selection with this dictionary.
	width_translator = {1:'8-bit', 2:'16-bit', 4:'32-bit'}
	#For every file in the input list do processing.
	for file in files:
		fileName, fileExtension = os.path.splitext(file)
		#Print to screen the processing parameters.
		with audioread.audio_open(file) as f:
			print '\nConverting '+fileName+' from:'
			print fileExtension+' to .'+outformat+';'
			print str(f.channels)+' channel(s) to '+str(channels)+' channel(s);'
			print str(f.samplerate)+'Hz to '+str(rate)+' Hz;'
			print 'Slicing '+str(f.duration*1000)+' ms file into '+str(slice_length)+' ms slices with a slice overlap of '+str(overlap)+' ms;'
		#Store the file in RAM.
		sound = AudioSegment.from_file(file, fileExtension.replace('.','').lower())
		#Print the 'x-bit' conversion parameters.
		print width_translator[sound.sample_width]+' to '+width_translator[int(width)]+'.\n'
		#Implement the user-selected or default (if nothing selected) parameters for processing.
		sound = sound.set_frame_rate(int(rate))
		sound = sound.set_sample_width(int(width))
		sound = sound.set_channels(int(channels))
		length_sound_ms = len(sound)
		length_slice_ms = int(slice_length)
		slice_start = 0
		#Begin slicing at the start of the file.
		while slice_start + length_slice_ms < length_sound_ms:
			sound_slice = sound[slice_start:slice_start+length_slice_ms]
			sound_slice.export(fileName+'.slice'+str(slice_start/1000)+'SecsTo'+str((slice_start+length_slice_ms)/1000)+'Secs.'+outformat, format=outformat)
			slice_start += int(overlap)
		#When the slice is abutting the end of the file, output that slice too.'
		if slice_start + length_slice_ms >= length_sound_ms:
			sound_slice = sound[slice_start:length_sound_ms]
			sound_slice.export(fileName+'.slice'+str(slice_start/1000)+'SecsToEndFileAt'+str((length_sound_ms)/1000)+'Secs.'+outformat, format=outformat)

#Execute the slice_audio function.
slice_audio(ARGS.infiles, ARGS.channels, ARGS.format_out, ARGS.sample_width, ARGS.sample_rate, ARGS.sample_slice_length_ms, ARGS.slice_overlap_slide_ms)
print 'Processing completed.  Have fun with your one-shots!\n'
