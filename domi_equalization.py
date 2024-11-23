import domi_tool as dt

def do_equalization(bimg,counter_Accumulate):

    _get_cdf_max = dt.find_range_max(counter_Accumulate)
    _get_cdf_min = dt.find_range_min(counter_Accumulate)
    _get_cdf_range = _get_cdf_max - _get_cdf_min
    
    for i in range(0, dt.dm_size(bimg)):  
        for j in range(0, dt.dm_size(bimg[i])):
            bimg[i][j] = ((counter_Accumulate[bimg[i][j]]-_get_cdf_min)/_get_cdf_range) * 255
            
            if (bimg[i][j]>255):
                print('fuck',bimg[i][j])
            
    return bimg