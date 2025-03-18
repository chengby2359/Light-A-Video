#!/bin/bash



# SCRIPT_DIR=$(dirname "$(realpath "$0")")

python mytools/i2v.py /inspire/hdd/ws-f4d69b29-e0a5-44e6-bd92-acf4de9990f0/public-project/zhoujianjun-240108120125/chengby/datasets/ffhq-dataset/images1024x1024/01000/01059.png \
                            /inspire/hdd/ws-f4d69b29-e0a5-44e6-bd92-acf4de9990f0/public-project/zhoujianjun-240108120125/chengby/codes/Light-A-Video/input_wan/ffhq \
                            --resolution 832 480 \
                            --frame_count 9 \
                            --fps 14
