#!/bin/bash



# SCRIPT_DIR=$(dirname "$(realpath "$0")")

python mytools/i2v.py /mnt/nas/datasets_tmp/ffhq/images1024x1024/04000/04033.png \
                            /mnt/nas/share2/home/cby/Light-A-Video/input_wan/04033.mp4 \
                            --resolution 512 512 \
                            --frame_count 13 \
                            --fps 8
