import numpy as np
import cv2
import domi_expansion as de
import domi_box_count as dbc
import domi_draw_box as ddb
import domi_equalization as deq

#=======================input=========================
img = cv2.imread('Original_picture\\images3.jpg')
#=====================================================

#======================output=========================
black_photo_locate = 'gray\\Gray_picture\\images3_black.jpg'
box_locate_before = 'gray\\_before_box\\images3_box.jpg'
photo_locate = 'gray\\_equalization_photo\\new_images3.jpg'
box_locate_after  = 'gray\\_after_box\\images3_box.jpg'
#=====================================================

#======================轉灰階並重新編碼=================
bimg = de.dm_rgb_to_gray(img)
bimg = np.array(bimg, dtype=np.uint8)
cv2.imwrite(black_photo_locate,bimg)
#=====================================================

counter_normal = dbc.scale_counter(bimg)
counter_Accumulate = dbc.scale_counter_Accumulate(counter_normal)

ddb.draw_box(range(256),counter_normal,'gray','灰階(0~255)','像素數','像素分布圖',box_locate_before)

bimg = deq.do_equalization(bimg,counter_Accumulate)

newimg = np.array(bimg, dtype=np.uint8)
cv2.imwrite(photo_locate,newimg)

counter_newimg = dbc.scale_counter(newimg)
ddb.draw_box(range(256),counter_newimg,'gray','灰階(0~255)','像素數','像素分布圖',box_locate_after)