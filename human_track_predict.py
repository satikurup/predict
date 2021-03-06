import json
import os
from argparse import Namespace, ArgumentParser

from read_and_show import plt_show_predict,id_generator
import matplotlib.pyplot as plt
import numpy as np
import time


import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str,required=False,default='./path2your_video',
        help = "Video input path"
    )

    parser.add_argument(
        "--output", type=str, default="/home/leonard/skk/yolov3-track/keras-yolo3-master/cuc1.mp4",
       
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)))
    elif "input" in FLAGS:
        #print(YOLO(**vars(FLAGS)))
        detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
    os.system("python3.6 evaluate_social_my_model.py  --trained_model_config  /home/leonard/skk/social_lstm_keras_tf-master/data/configs/other.json --trained_model_file   /home/leonard/skk/social_lstm_keras_tf-master/data/results/20190527/test=ucy/social_train_model_e0010.h5")
    
    # print(FLAGS.input) --input 0.mp4
    avi_path = '/home/leonard/skk/yolov3-track/??????/'
    view_path = '/home/leonard/skk/yolov3-track/??????/'
    
    num = FLAGS.input.split('.')[0]
    print(num) 
    plt_show_predict(avi_path,view_path,int(num))




