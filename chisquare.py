import numpy as np
from scipy import stats

import bmputil
import logger


def chi(path: str):
    """
    Run chi-square analysis. Return p.
    """
    logger.logger.debug("Running chi")
    img = bmputil.BmpUtil(path)
    pixel_counter = np.zeros(256, dtype=int)
    for i in range(len(img.image)):
        for j in range(len(img.image[0])):
            pixel_counter[img.image[i][j]] += 1
    h2i = pixel_counter[2:255:2]  # h_(2i)
    h2is = (h2i + pixel_counter[3:256:2]) / 2  # h*_(2i)
    fil = (h2is != 0)
    k = sum(fil)
    idx = np.zeros(k, dtype=int)
    for i in range(127):
        if fil[i]:
            idx[sum(fil[1:i])] = i
    r = sum(((h2i[idx] - h2is[idx]) ** 2) / (h2is[idx]))
    p = 1 - stats.chi2.cdf(r, k - 1)
    logger.logger.info("Calculated p value is {}".format(p))
