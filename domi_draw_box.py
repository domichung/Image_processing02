import matplotlib.pyplot as plt
#======================設圖表中文======================
def plt_chinese():
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
#=====================================================

def draw_box(gray_levels,arr,color,x_name,y_name,tittle,locate):
    plt_chinese()
    plt.figure(figsize=(10, 10))
    plt.bar(gray_levels, arr, color=color)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title(tittle)
    plt.savefig(locate)