import domi_tool as dt


def rgb2hsl(r, g, b):
    r =  r / 255
    g =  g / 255
    b =  b / 255  

    max_val = dt.getmax_3channel(r, g, b)
    min_val = dt.getmin_3channel(r, g, b)
    get_range = max_val - min_val

    h = 0
    if get_range == 0:
        h = 0  
    elif max_val == r:
        h = (60 * ((g - b) / get_range) + 360) % 360
    elif max_val == g:
        h = (60 * ((b - r) / get_range) + 120) % 360
    elif max_val == b:
        h = (60 * ((r - g) / get_range) + 240) % 360

    if max_val == 0:
        s = 0
    else:
        check = 2 * (max_val + min_val) - 1
        
        if (check < 1):
            s = get_range / (1 - check)
        else:
            s = 1  

    l = (max_val + min_val) / 2

    #print(l)

    return h, s, l

#=================================

def hsl2rgb(h, s, l):
    h = h % 360

    c = (1 - abs(2 * l - 1)) * s

    temp_h = h / 60
    x = c * (1 - abs(temp_h % 2 - 1))

    m = l - c / 2

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    elif 300 <= h <= 360:
        r, g, b = c, 0, x
    else:
        raise ValueError("Hue value out of range")

    r = int((r + m) * 255 + 0.5)
    g = int((g + m) * 255 + 0.5)
    b = int((b + m) * 255 + 0.5)

    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    return r, g, b


def rgbimg2hsl(img):
    
    height = dt.dm_size(img)
    width = dt.dm_size(img[0])

    hsl_img = [[[0.0, 0.0, 0.0] for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            
            r = img[i][j][0]
            g = img[i][j][1]
            b = img[i][j][2]

            h,s,l = rgb2hsl(r,g,b)
            
            hsl_img[i][j][0],hsl_img[i][j][1],hsl_img[i][j][2] = float(h),float(s),int(l*255)

    return hsl_img

def hsl2rgbimg(arr):
    height = dt.dm_size(arr)
    width = dt.dm_size(arr[0])

    rgb_img = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            
            l = arr[i][j][0]/255
            s = arr[i][j][1]
            h = arr[i][j][2]

            r,g,b = hsl2rgb(h,s,l)

            rgb_img[i][j][0],rgb_img[i][j][1],rgb_img[i][j][2] = r,g,b

            #print(r,g,b)

    return rgb_img

#r = 100
#g = 200
#b = 255

#x, y, z = rgb2hsl(r, g, b)
#print(f"HSL: {x}, {y}, {z}")

#r2, g2, b2 = hsl2rgb(x, y, z)
#print(f"RGB after conversion: {r2}, {g2}, {b2}")
