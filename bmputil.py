import collections
import itertools

import cv2

import logger


class BmpController:
    """
    To operate bmp file. See http://exasic.com/article/index.php?md=py-bmp2
    """

    def __init__(self, path):
        logger.logger.debug("Now loading image {}".format(path))
        self.image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
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
