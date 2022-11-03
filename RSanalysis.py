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
            [[int(row[ex_index * n + inter_index]) for inter_index in range(n)] for ex_index in
             range(img.cols // n)])  # NOTE: The number of columns must be divisible by n
        # NOTE: Convert pixel to int to prevent overflow

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
        pixel_groups_neg.append([bmputil.flip(group, mode_neg) for group in row])

    '''
    Calculate smoothness of +1 and -1
    '''

    smoothness_pos, smoothness_neg = [], []
    for row in pixel_groups_pos:
        smoothness_pos.append([bmputil.cal_smoothness(group) for group in row])
    for row in pixel_groups_neg:
        smoothness_neg.append([bmputil.cal_smoothness(group) for group in row])

    '''
    Count and calculate R and S
    '''
    cnt_r_pos, cnt_s_pos, cnt_r_neg, cnt_s_neg = 0, 0, 0, 0
    for row_index, smoothness_row in enumerate(smoothness_original):
        for group_index, group_original in enumerate(smoothness_row):
            if group_original > smoothness_pos[row_index][group_index]:
                logger.logger.debug(
                    "Original:{}\tPos:{}, S+".format(group_original, smoothness_pos[row_index][group_index]))
                cnt_s_pos += 1
            elif group_original < smoothness_pos[row_index][group_index]:
                cnt_r_pos += 1
                logger.logger.debug(
                    "Original:{}\tPos:{}, R+".format(group_original, smoothness_pos[row_index][group_index]))
            '''
            Calculate -1 groups
            '''
            if group_original > smoothness_neg[row_index][group_index]:
                cnt_s_neg += 1
                logger.logger.debug(
                    "Original:{}\tNeg:{}, S-".format(group_original, smoothness_neg[row_index][group_index]))
            elif group_original < smoothness_neg[row_index][group_index]:
                cnt_r_neg += 1
                logger.logger.debug(
                    "Original:{}\tNeg:{}, R-".format(group_original, smoothness_neg[row_index][group_index]))
    '''
    Analysis and output
    '''
    logger.logger.info("RS Analysis:\tR+:{}\tR-:{}\tS+:{}\tS-:{}".format(cnt_r_pos, cnt_r_neg, cnt_s_pos, cnt_s_neg))
    # Judge by (R-)-(S-)>(R+)-(S+)
    if cnt_r_neg - cnt_s_neg > cnt_r_pos - cnt_s_pos:
        logger.logger.info("Analysis finished: embedding approved")
    else:
        logger.logger.info("Analysis finished: embedding disapproved")
