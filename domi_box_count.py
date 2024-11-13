import domi_tool as dt

def scale_counter(img):
    counter = [0] * 255
    for i in range(0, dt.dm_size(img)):  
        for j in range(0, dt.dm_size(img[i])):
            counter[img[i][j]-1]+=1
    return counter

def scale_counter_Accumulate(arr):
    counter = [0]*255
    addr_counter = 0
    while (addr_counter < 255):
        addr_counter_2 = addr_counter
        while (addr_counter_2>=0):
            counter[addr_counter] += arr[addr_counter_2]
            addr_counter_2-=1
        addr_counter+=1
    
    return counter
