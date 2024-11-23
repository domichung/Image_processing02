import numpy as np
import cv2
import domi_expansion as de
import domi_box_count as dbc
import domi_draw_box as ddb
import domi_equalization as deq
import domi_tool as dt
import img_check as debu

#=======================input=========================
img = cv2.imread('Original_picture\\images3.jpg')
#=====================================================

#======================output=========================
box_locate_before_R = 'color\\_before_box\\RED\\images3_box.jpg'
box_locate_before_G = 'color\\_before_box\\GREEN\\images3_box.jpg'
box_locate_before_B = 'color\\_before_box\\BLUE\\images3_box.jpg'
photo_locate = 'color\\_equalization_photo\\new_images3.jpg'
box_locate_after_R  = 'color\\_after_box\\RED\\images3_box.jpg'
box_locate_after_G  = 'color\\_after_box\\GREEN\\images3_box.jpg'
box_locate_after_B  = 'color\\_after_box\\BLUE\\images3_box.jpg'
#=====================================================

channel_r = dt.index2channel(img,0)
channel_g = dt.index2channel(img,1)
channel_b = dt.index2channel(img,2)

counter_normal_r = dbc.scale_counter(channel_r)
counter_normal_g = dbc.scale_counter(channel_g)
counter_normal_b = dbc.scale_counter(channel_b)

counter_Accumulate_r = dbc.scale_counter_Accumulate(counter_normal_r)
counter_Accumulate_g = dbc.scale_counter_Accumulate(counter_normal_g)
counter_Accumulate_b = dbc.scale_counter_Accumulate(counter_normal_b)

ddb.draw_box(range(256),counter_normal_r,'gray','灰階(0~255)','像素數','紅色像素分布圖',box_locate_before_R)
ddb.draw_box(range(256),counter_normal_g,'gray','灰階(0~255)','像素數','綠色像素分布圖',box_locate_before_G)
ddb.draw_box(range(256),counter_normal_b,'gray','灰階(0~255)','像素數','藍色像素分布圖',box_locate_before_B)

channel_r = deq.do_equalization(channel_r,counter_Accumulate_r)
channel_g = deq.do_equalization(channel_g,counter_Accumulate_g)
channel_b = deq.do_equalization(channel_b,counter_Accumulate_b)

final_img = dt.channel2rgb_arr(channel_r,channel_g,channel_b)
final_img = np.array(final_img, dtype=np.uint8)
cv2.imwrite(photo_locate,final_img)

new_channel_r = dt.index2channel(final_img,0)
new_channel_g = dt.index2channel(final_img,1)
new_channel_b = dt.index2channel(final_img,2)

counter_new_normal_r = dbc.scale_counter(new_channel_r)
counter_new_normal_g = dbc.scale_counter(new_channel_g)
counter_new_normal_b = dbc.scale_counter(new_channel_b)

ddb.draw_box(range(256),counter_new_normal_r,'gray','灰階(0~255)','像素數','紅色像素分布圖',box_locate_after_R)
ddb.draw_box(range(256),counter_new_normal_g,'gray','灰階(0~255)','像素數','綠色像素分布圖',box_locate_after_G)
ddb.draw_box(range(256),counter_new_normal_b,'gray','灰階(0~255)','像素數','藍色像素分布圖',box_locate_after_B)