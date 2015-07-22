# SliceAudio.py
I have written a python script to slice up audio files (*in batch if so desired*) for the Analog Elektron Rytm (or any other thing that can play audio files). 

It is available for free download here:
https://github.com/schultzm/SliceAudio.py

By default it will slice a file into 2-second blocks, with each block starting at the end of the next block, and each block output as a separate file (into the folder containing the input file; file output names as per input but with the position in the original file added to the output file name).  The format of the output slices is by default that which the Elektron Analog Rytm likes as input (i.e., 16-bit, 48kHz, mono).  If so desired, the user can crush the sample to 8-bit width or have it in medium (16-bit) or high-quality (32-bit).  Sample rate can be anywhere from low quality (11025 Hz) to high quality (48000 Hz) – in fact, sample rate can be whatever you want, but your computer may not know how to deal those non-standard rates (e.g., I tested it with 1 Hz, and iTunes died when trying to play it – see the help menu for standard/accepted options [python SliceAudio.py -h] ).   The user can also alter the sample slice length and the overlap slide on the previous slice (e.g., you could slice into 10 second windows with each subsequent window overlapping the previous window by 1 second.  NB. time is measured in milliseconds, so multiply x-seconds by 1000 to get the desired slice length).  There is an option for stereo output.  The script can input and output any format that is supported by ffmpeg**.    

It is a command line script so you will need to run it in terminal (or other command line window).  Requires python, 


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


**ffmpeg formats: https://trac.ffmpeg.org/wiki/audio%20types
