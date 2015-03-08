# Chennaipy-video-helpers

This repository contains helper scripts and commands to create meetup videos for [Chennaipy](http://chennaipy.org).

## Steps

* Install `ffmpeg`, `sox`, `imagemagick`, `ghostscript`
    * On OSX, you can directly use brew for the above:
    
            brew install ffmpeg sox imagemagick ghostscript
            
    * On Ubuntu, installing [ffmpeg is a bit tricky](http://blog.pkh.me/p/13-the-ffmpeg-libav-situation.html), but these commands should get you started: 

            sudo add-apt-repository ppa:mc3man/trusty-media
            sudo apt-get update
            sudo apt-get dist-upgrade
            sudo apt-get install ffmpeg imagemagick ghostscript sox

        You can read more about the ffmpeg ppa [here](https://launchpad.net/~mc3man/+archive/ubuntu/trusty-media)
    * On Windows, you can individually download and install prebuilt binaries for the packages:
        * [ffmpeg](http://ffmpeg.zeranoe.com/builds/), 64-bit static should do
        * [sox](http://sourceforge.net/projects/sox/files/sox/)
        * [imagemagick](http://www.imagemagick.org/script/binary-releases.php#windows)
        * [ghostscript](http://www.ghostscript.com/download/gsdnld.html)
        * you might have to manually add them to `PATH` if not done automatically. 
            
* Convert the audio to a wav (wav files are faster to process, and easier to manipulate using sox)

        $ ffmpeg -i bigdata_audio.m4a audio.wav
        
* Remove noise from audio

        $ sox audio.wav -n trim 0 1.5 noiseprof noise.profile
        $ sox audio.wav cleaned.wav noisered noise.profile 0
        
* Convert the pdf to individual images using

        $ convert -density 150 -resize 1920x1080 bigbigdata.pdf[0-20] individual_images/%d.png 

* Notedown timestamps from audio at which slide is to be changed

* Generate segments of video for those times

        $ python create_video_segments.py individual_images\ individual_video\ 00:02 00:40 1:25 2:10 3:35 3:50 5:30 7:22 7:42 8:02 10:03 12:10 13:10 15:12 16:00 17:25 18:30 20:00 21:18 21:23

* Trim the audio if required

        $ sox cleaned.wav final.wav trim 00:02 =21:20 

* Generate a `concatvideos` file to be used by ffmpeg to join the videos to form a single one

        $ generate_concatvideos.py individual_video\

* Run the ffmpeg script to create the joined video

        $ ffmpeg -f concat -i concatvideos -c copy joined.mp4

* Join the generated video with the final audio

        $ ffmpeg -i joined.mp4 -i final.wav -shortest -preset ultrafast -q 0 final.mp4
