#!/bin/bash

MYIPADDRESS=`ifconfig en0 | grep 'inet ' | awk '{print $2}'`
VERSION=latest

# allow network connections in Xquartz Security settings
xhost +

# Allow your local user access via xhost: xhost +SI:localuser:picachooser and create a similar user with docker run option: --user=$(id -u):$(id -g)
docker pull fredericklab/picachooser:${VERSION}
docker run \
    --network host\
    --volume=/Users/frederic:/Users/frederic \
    -it \
    -e DISPLAY=${MYIPADDRESS}:0 \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -u picachooser fredericklab/picachooser:${VERSION} \
    PICAchooser \
        fix \
        --featdir /Users/frederic/Dropbox_PHC/MR_data/gradertest/079N_resting_visit1.feat \
        --melodicdir /Users/frederic/Dropbox_PHC/MR_data/gradertest/079N_resting_visit1.feat/filtered_func_data.ica \
        --scalemotiontodata
