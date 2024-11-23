import numpy as np
import cv2
import domi_expansion as de
import domi_box_count as dbc
import domi_draw_box as ddb
import domi_equalization as deq
import domi_tool as dt
import _addpoint_rgb2hsl as ahsl

#
#=======================input=========================
img = cv2.imread('Original_picture\\images3.jpg')
#=====================================================

#======================output=========================
box_locate_before_L = 'add_point\\_before_box\\L_channel\\images3_box.jpg'

photo_locate = 'add_point\\_equalization_photo\\new_images3.jpg'

box_locate_after_L  = 'add_point\\_after_box\\L_channel\\images3_box.jpg'
#=====================================================

#hsl_img = ahsl.rgbimg2hsl(img)
hsl_img = cv2.cvtColor(img,cv2.COLOR_BGR2Lab)

channel_h = dt.index2channel(hsl_img,2)
channel_s = dt.index2channel(hsl_img,1)
channel_l = dt.index2channel(hsl_img,0)

counter_normal_l = dbc.scale_counter(channel_l)
counter_Accumulate_l = dbc.scale_counter_Accumulate(counter_normal_l)

ddb.draw_box(range(256),counter_normal_l,'gray','灰階(0~255)','像素數','亮度分布圖',box_locate_before_L)
channel_l = deq.do_equalization(channel_l,counter_Accumulate_l)

final_hsl_img = dt.channel2rgb_arr(channel_l,channel_s,channel_h)
final_hsl_img = np.array(final_hsl_img, dtype=np.uint8)
#final_img = ahsl.hsl2rgbimg(final_hsl_img)
final_img = cv2.cvtColor(final_hsl_img,cv2.COLOR_Lab2BGR)

final_img = np.array(final_img, dtype=np.uint8)
cv2.imwrite(photo_locate,final_img)

new_channel_h = dt.index2channel(hsl_img,2)
new_channel_s = dt.index2channel(hsl_img,1)
new_channel_l = dt.index2channel(hsl_img,0)

new_counter_normal_l = dbc.scale_counter(new_channel_l)

ddb.draw_box(range(256),new_counter_normal_l,'gray','灰階(0~255)','像素數','藍色像素分布圖',box_locate_after_L)