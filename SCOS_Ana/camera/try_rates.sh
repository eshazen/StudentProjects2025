#!/bin/bash

for fps in 10 20 30 40 50 60 70 80 90 100
do
  echo "trying " $fps
  rm -f video.raw
  ./capture_raw $fps 1000 video.raw 2>1 >/dev/null
  echo $fps `./frame_count.sh video.raw`
done

