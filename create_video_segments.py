import sys
import subprocess
import glob

all_args = []

for arg in sys.argv:
    all_args.append(arg)

# remove the first part which is the filename of the script
all_args = all_args[1:]

# get the images directory
images_dir = all_args[0]

# set the output directory 
output_dir = all_args[1]

# get the timstamps to split at
time_parts = all_args[2:]

outfile_name_iterator = -1

# TODO convert start and end time to a duration, this speeds up the process, 
# pool the processes, they can run independently
for (start_time, end_time, imagefile_name) in zip(time_parts, time_parts[1:], sorted(glob.glob(images_dir+"*.png"),key=lambda name:int(name[len(images_dir):-4]))):
    outfile_name_iterator = outfile_name_iterator + 1
    outfile_name = output_dir + str(outfile_name_iterator) + ".mp4"

    ret_val = subprocess.call(["ffmpeg",
      "-loglevel",
      "error",
      "-y",
      "-loop",
      "1",
      "-i",
      imagefile_name,
      "-ss",
      start_time,
      "-to",
      end_time,
      "-preset",
      "ultrafast",
      "-qp",
      "0",
      outfile_name])

    print ret_val

