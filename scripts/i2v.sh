#!/bin/bash



# SCRIPT_DIR=$(dirname "$(realpath "$0")")

# python mytools/i2v.py /inspire/hdd/ws-f4d69b29-e0a5-44e6-bd92-acf4de9990f0/public-project/zhoujianjun-240108120125/chengby/datasets/PPR10K/converted_cby/1024/221_8.png \
#                             /inspire/hdd/ws-f4d69b29-e0a5-44e6-bd92-acf4de9990f0/public-project/zhoujianjun-240108120125/chengby/codes/Light-A-Video/input_cog/PPR10K \
#                             --resolution 720 480 \
#                             --frame_count 9 \
#                             --fps 14

# /inspire/hdd/ws-f4d69b29-e0a5-44e6-bd92-acf4de9990f0/public-project/zhoujianjun-240108120125/chengby/datasets/PPR10K/converted_cby/train/input/221_8_0.png

python mytools/i2v.py /inspire/hdd/ws-f4d69b29-e0a5-44e6-bd92-acf4de9990f0/public-project/zhoujianjun-240108120125/chengby/2023-05-06_18.png \
                            /inspire/hdd/ws-f4d69b29-e0a5-44e6-bd92-acf4de9990f0/public-project/zhoujianjun-240108120125/chengby/codes/Light-A-Video/input_cog/ \
                            --resolution 720 480 \
                            --frame_count 9 \
                            --fps 14