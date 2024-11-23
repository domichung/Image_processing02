import domi_tool as dt
def check_img(img):
    for i in range(0, dt.dm_size(img)):  
        for j in range(0, dt.dm_size(img[i])):
            if (img[i][j]>255):
                print('error',img[i][j])
                
def check_array_1d(img):
    for i in range(0,dt.dm_size(img)):
        if (i>255):
            print("error")