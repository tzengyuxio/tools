#!/bin/bash
#
# Take Time Lapsed Screen Shots From Terminal
# http://www.mactricksandtips.com/2009/12/take-timed-lapsed-screen-shots-from-terminal.html

# script #1
#while [ 1 ];
#do vardate=$(date +%Y\-%m\-%d\_%H.%M.%S);
    #screencapture -t jpg -x ~/Desktop/screencapture/$vardate.jpg;
    #sleep 5;
#done

# script #2
i=1;
while [ 1 ];
do screencapture -t jpg -x ~/Desktop/screencapture/$i.jpg;
    let i++;
    sleep 5;
done

# script to convert sequence of images into time-lapse video.
#ffmpeg -f image2 -i %d.jpg -vcodec mpeg4 -b 800k newvid.mp4
