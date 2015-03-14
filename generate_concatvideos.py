import sys
import glob

all_args = []

for arg in sys.argv:
    all_args.append(arg)

output_dir = all_args[1]

# create a textfile that serves as input for ffmpeg to join all the individual videos
with open("concatvideos",'w') as the_file:
    for videofile_name in sorted(glob.glob(output_dir+"*.mp4"), key=lambda name:int(name[len(output_dir):-4])):
        the_file.write("file '%s'\n" % videofile_name)
