def dm_size(arr):
    x = 0
    for w in arr:
        x += 1
    return x

def dm_cpy(arr):
    rows = dm_size(arr)  
    cols = dm_size(arr[0]) if rows > 0 else 0  
    cpy = [[0] * cols for _ in range(rows)]  

    for i in range(rows):
        for j in range(cols):
            cpy[i][j] = arr[i][j]  

    return cpy

def dm_small_arr(arr):
    rows = dm_size(arr)  
    cols = dm_size(arr[0]) if rows > 0 else 0  
    
    new_rows = rows - 2
    new_cols = cols - 2

    if new_rows > 0 and new_cols > 0:
        cpy = [[0] * new_cols for _ in range(new_rows)]
        
        for i in range(1, rows - 1):  
            for j in range(1, cols - 1):  
                cpy[i - 1][j - 1] = arr[i][j]  
    else:
        cpy = []  

    return cpy

#======================================第二次作業新增小工具
def find_range_max(arr):
    max = 0
    count = 0
    while (count<256):
        if (arr[count]>max):
            max = arr[count]
        count+=1

    return max

def find_range_min(arr):
    min = 0
    count = 0
    while (count<256):
        if (arr[count]<min):
            min = arr[count]
        count+=1
    
    return min

#============三色拆分工具

def index2channel(arr, k_index):
    newarr = []
    for i in range(dm_size(arr)):
        new_row = []
        for j in range(dm_size(arr[i])):
            
            new_row_value = arr[i][j][k_index]
            new_row += [new_row_value]  
        
        newarr += [new_row]
    #print(newarr)
    return newarr

def channel2rgb_arr(arr1, arr2, arr3):

    newarr = [[None] * dm_size(arr1[0]) for _ in range(dm_size(arr1))]
    
    for i in range(dm_size(arr1)):
        
        row_3d = [None] * dm_size(arr1[i])
        
        for j in range(dm_size(arr1[i])):
            row_3d[j] = [int(arr1[i][j]), int(arr2[i][j]), int(arr3[i][j])]
            #if (arr1[i][j]>255):
            #    print('fuck1',row_3d[j])
            #if (arr2[i][j]>255):
            #    print('fuck2')
            #if (arr3[i][j]>255):
            #    print('fuck3')

        newarr[i] = row_3d
    
    return newarr

#============加分題新增小工具
def getmax_3channel(r,g,b):
    
    rnum = r
    
    if (rnum < g):
        rnum = g
    if (rnum < b):
        rnum = b
    
    return rnum

def getmin_3channel(r,g,b):
    
    rnum = r
    
    if (rnum > g):
        rnum = g
    if (rnum > b):
        rnum = b
        
    return rnum