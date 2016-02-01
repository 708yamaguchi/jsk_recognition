#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

import cv2
import numpy as np
import PIL

from std_msgs.msg import ColorRGBA

def get_tile_image(imgs, tile_shape=None):
    # import should be here to avoid import error on server
    # caused by matplotlib's backend
    import matplotlib.pyplot as plt  # noqa

    def get_tile_shape(img_num):
        x_num = 0
        y_num = int(math.sqrt(img_num))
        while x_num * y_num < img_num:
            x_num += 1
        return x_num, y_num

    if tile_shape is None:
        tile_shape = get_tile_shape(len(imgs))

    img_rgb_list = []
    for img in imgs:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_rgb_list.append(img_rgb)
    # check if all the resolution is same
    x_num, y_num = tile_shape
    if all(img.shape == imgs[0].shape for img in imgs[1:]):
        #rospy.loginfo("all the size same images")
        concatenated_image = None
        for y in range(y_num):
            row_image = None
            for x in range(x_num):
                i = x + y * x_num
                if i >= len(imgs):
                    img = np.zeros(imgs[0].shape, dtype=np.uint8)
                else:
                    img = imgs[i]
                if row_image is None:
                    row_image = img
                else:
                    row_image = cv2.hconcat([row_image, img])
            if concatenated_image is None:
                concatenated_image = row_image
            else:
                concatenated_image = cv2.vconcat([concatenated_image, row_image])
        return concatenated_image
    else:
        for i, img_rgb in enumerate(img_rgb_list):
            plt.subplot(y_num, x_num, i+1)
            plt.axis('off')
            plt.imshow(img_rgb)
        canvas = plt.get_current_fig_manager().canvas
        canvas.draw()
        pil_img = PIL.Image.frombytes('RGB',
            canvas.get_width_height(), canvas.tostring_rgb())
        out_rgb = np.array(pil_img)
        out_bgr = cv2.cvtColor(out_rgb, cv2.COLOR_RGB2BGR)
        plt.close()
        return out_bgr

def color_category20(i):
    colors = (0x1f77b4,
              0xaec7e8,
              0xff7f0e,
              0xffbb78,
              0x2ca02c,
              0x98df8a,
              0xd62728,
              0xff9896,
              0x9467bd,
              0xc5b0d5,
              0x8c564b,
              0xc49c94,
              0xe377c2,
              0xf7b6d2,
              0x7f7f7f,
              0xc7c7c7,
              0xbcbd22,
              0xdbdb8d,
              0x17becf,
              0x9edae5)
    c = colors[i % 20]
    return ColorRGBA(r=(c >> 16) / 255.0, g=((c >> 8) & 255) / 255.0, b=(c & 255) / 255.0, a=1.0)

def color_category10(i):
    colors = (0x1f77b4,
              0xff7f0e,
              0x2ca02c,
              0xd62728,
              0x9467bd,
              0x8c564b,
              0xe377c2,
              0x7f7f7f,
              0xbcbd22,
              0x17becf)
    c = colors[i % 10]
    return ColorRGBA(r=(c >> 16) / 255.0, g=((c >> 8) & 255) / 255.0, b=(c & 255) / 255.0, a=1.0)

    
