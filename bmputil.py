import collections
import itertools

import cv2

import logger


class BmpUtil:
    """
    To operate bmp file. See http://exasic.com/article/index.php?md=py-bmp2
    """

    def __init__(self, path):
        logger.logger.debug("Now loading image {}".format(path))
        self.image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # self.image is pixels group
        self.depth = 256  # Greyscale maximum pixel is 255
        self.rows, self.cols = self.image.shape  # size should be like (512,512)
        self.pixels = self.rows * self.cols

        logger.logger.debug("Image {} size is {}*{}".format(path, self.rows, self.cols))

    def write_image(self, path):
        """
        Write image to file. Must be bmp greyscale.
        """

        cv2.imwrite(path, self.image)

    def count_greyscale(self) -> dict:
        """
        To collect and count grey value; return Counter_dict
        """
        tmp = list(
            itertools.chain.from_iterable(self.image))  # Convert 2-dimension array to 1-dimension array by merging them
        collection = collections.Counter(tmp)
        logger.logger.debug("STAT and collect pixels: {}".format(collection))

        return [collection[i] for i in range(self.depth)]  # Convert dict to ordered list


def flip(pixel_group, mode) :
    """
    Flip pixel groups by mode, return flipped group
    mode:
    0 = Keep
    1 = 0<->1
    -1 = 0<-> -1
    """
    pix_group = pixel_group[:]  # Deep copy to prevent pollute original matrix
    tmp = pix_group[:]

    assert (len(pix_group) == len(mode))
    for index, pix in enumerate(pix_group):
        if mode[index] == 1:
            if pix % 2:
                pix_group[index] -= 1
            else:
                pix_group[index] += 1
        elif mode[index] == -1:
            if pix % 2:
                pix_group[index] += 1
            else:
                pix_group[index] -= 1
        else:  # Should be 0 here
            pass
        # logger.logger.debug("Pix {} was replaced to {} by mode {}".format(pix, pix_group[index], mode[index]))
    logger.logger.debug("Pixel group {} was replaced to {} by mode {}".format(tmp, pix_group, mode))
    return pix_group


def cal_smoothness(pixel_group) -> int:
    """
    To calculate smoothness by formula:
    f({x_i})=\sum_{i=1}^{n-1} |x_{i+1}-x_i|
    """
    acc_smoothness = 0
    for i in range(len(pixel_group) - 1):
        acc_smoothness += abs(pixel_group[i + 1] - pixel_group[i])
    return acc_smoothness
