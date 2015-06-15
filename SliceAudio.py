import os
import glob
from pydub import AudioSegment
import argparse
import os

#parse command line input
PARSER = argparse.ArgumentParser(description=
                                 """
                                 reads in and 
                                 """)
PARSER.add_argument('-f', '--filename', help=
                    """
                    Name of input file.
                    """
                    , required=True)
PARSER.add_argument('-n', '--names_file', help=
                    """
                    Names file containing original names (col 1),
                    translated names in col 2.
                    """
                    , required=True)
PARSER.add_argument('-i', '--informat', help=
                    """
                    File format of input. e.g., genbank, fasta, phylip, nexus.
                    """
                    , required=True)
PARSER.add_argument('-o', '--outformat', help=
                    """
                    File format of output. e.g., genbank, fasta, phylip,
                    nexus.
                    """
                    , required=True)

ARGS = PARSER.parse_args()






audio_dir="/Documents/AudioLibraries/AbletonStuff/Library/Samples/iPhoneRecordings/Do_Not_Modify_This_Folder/"
# ext_list=("*/*.caf")
os.chdir(audio_dir)

#       mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
 #       AudioSegment.from_file(video).export(mp3_filename, format='mp3')

ext_list=("*/*/*/*.caf")
for ext in ext_list:
    for caf in glob.glob(ext):
        if ".caf" in caf:
            print caf
            
import os

files = os.listdir(DIRNAME)
for f in files:
    if '.3gp~' in f:
        newname = f.split('~')[0]
        os.rename(f, newname)
