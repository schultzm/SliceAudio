# SliceAudio.py
Slice up audio files in batch to generate one shot samples.  

Default will spit out wav file slices of 2 second duration, in 16bit/mono/44.1kHz sample rate (standard format for the
Analog Elektron Rytm drum machine).
Will chop up the input files and spit out slices along the length of each until it reaches the end of each file.
Can input/output in any format that ffmpeg supports.

example usage:
python SliceAudio.py -i xyz.m4a -f m4a -b 2 -s 11025 -l 10000
python SliceAudio.py -h

Dependencies:
1. gcc
2. pydub (sudo pip install pydub), see https://github.com/jiaaro/pydub
3. ffmpeg (brew install libav --with-libvorbis --with-sdl --with-theora)

