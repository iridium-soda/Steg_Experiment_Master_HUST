import bmputil
import logger


# See https://blog.csdn.net/qq_37207042/article/details/106166181
def rs(path: str):
    """
    Do rs analysis and return if the pic was embedded
    Set n=4 and mode matrix is [1,0,0,1]
    """
    logger.logger.debug("Running rs")
    img = bmputil.BmpUtil(path)
    logger.logger.debug("img's shape is {}*{}".format(img.rows, img.cols))
    n = 4
    mode = [1, 0, 0, 1]
    '''
    Divide pixels into 1*4 group
    '''
    pixel_groups_original = []  # 2-D matrix and each cell is the group if 1*n pixels
    for row in img.image:  # for each row
        pixel_groups_original.append(
            [[row[ex_index * n + inter_index] for inter_index in range(n)] for ex_index in
             range(img.cols // n)])  # NOTE: The number of columns must be divisible by n

    '''
    Calculate smoothness for original pixel groups
    '''
    smoothness_original = []  # 2-D matrix to store original smoothness; each group has its own value
    for row in pixel_groups_original:
        smoothness_original.append([bmputil.cal_smoothness(group) for group in row])  # each group contains 1*n pixels
    '''
    Do +1 flip by mode
    '''
    pixel_groups_pos = []
    for row in pixel_groups_original:
        pixel_groups_pos.append([bmputil.flip(group, mode) for group in row])

    '''
    Do -1 flip by mode
    '''
    mode_neg = [-a for a in mode]
    pixel_groups_neg = []
    for row in pixel_groups_original:
        pixel_groups_neg.append([bmputil.flip(group, mode) for group in row])

    '''
    Calculate smoothness of +1 and -1
    '''

    smoothness_pos, smoothness_neg = [], []
    for row in pixel_groups_pos:
        smoothness_pos.append([bmputil.cal_smoothness(group) for group in row])
    for row in pixel_groups_neg:
        smoothness_neg.append([bmputil.cal_smoothness(group) for group in row])

    '''
    TODO: Count and calculate R and S
    '''
