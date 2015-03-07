1. install ffmpeg, sox, imagemagick, ghostscript

1. convert the audio to a wav (wav files are faster to process, and easier to manipulate using sox)
```
ffmpeg -i bigdata_audio.m4a audio.wav
```

1. remove noise from audio
```
sox audio.wav -n trim 0 1.5 noiseprof noise.profile
sox audio.wav cleaned.wav noisered noise.profile 0
```

1. convert the pdf to individual images using
```
> convert -density 150 -resize 1920x1080 bigbigdata.pdf[0-20] individual_images\%d.png 
```

1. notedown audio for timestamps at which slide is to be changed

1. generate segments of video for those times
```
> python create_video_segments.py individual_images\ individual_video\ 00:02 00:40 1:25 2:10 3:35 3:50 5:30 7:22 7:42 8:02 10:03 12:10 13:10 15:12 16:00 17:25 18:30 20:00 21:18 21:23
```

1. trim the audio if required
```
sox cleaned.wav final.wav trim 00:02 =21:20 
```

1. generate a `concatvideos` file to be used by ffmpeg to join the videos to form a single one
```
> generate_concatvideos.py individual_video\
```

1. run the ffmpeg script to create the joined video
```
ffmpeg -f concat -i concatvideos -c copy joined.mp4
```

1. join the generated video with the final audio
```
ffmpeg -i joined.mp4 -i final.wav -shortest -preset ultrafast -q 0 final.mp4
```
