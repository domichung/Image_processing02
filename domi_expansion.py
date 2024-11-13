import domi_tool as dt

def dm_rgb_to_gray(img):
    
    height = dt.dm_size(img)
    width = dt.dm_size(img[0])
    
    gray_img = [[0] * width for _ in range(height)]

    for i in range(height):
        for j in range(width):

            r = img[i][j][2]
            g = img[i][j][1]
            b = img[i][j][0]

            gray_value = (r * 299 // 1000 + g * 587 // 1000 + b * 114 // 1000)  
            # 參考 https://medium.com/電腦視覺/邊緣偵測-索伯算子-sobel-operator-95ca51c8d78a
            gray_img[i][j] = gray_value

    return gray_img