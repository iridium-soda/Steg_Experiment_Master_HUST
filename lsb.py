import random
import time

import bmputil
import logger


def embed(path: str):
    logger.logger.debug("Running embed")
    img = bmputil.BmpUtil(path)
    embed_rate = 1
    '''
    Generate random secret according to embed_rate
    '''
    random.seed(1024)  # Set seed as 1024
    secret_flow = "".join([str(random.randint(0, 1)) for _ in range(int(img.pixels * embed_rate))])

    '''
    Generate random flow of index
    '''
    embed_flow = [i for i in range(img.pixels)]
    random.shuffle(embed_flow)

    assert (len(secret_flow) <= img.pixels)  # To ensure secret can be embedded into the image
    '''
    Ready to embed
    '''
    for index, b in enumerate(secret_flow):
        '''
        Resolve row and colum by index
        '''
        img_index = embed_flow[index]
        img_index_row = img_index // img.cols
        img_index_col = img_index % img.cols
        assert (img_index_row < img.rows and img_index_col < img.cols)
        # logger.logger.debug("Index {} is resolved by {} row and {} column".format(img_index, img_index_row,
        # img_index_col))

        '''
        Embed
        '''
        # tmp = img.image[img_index_row, img_index_col]
        img.image[img_index_row, img_index_col] = img.image[img_index_row, img_index_col] >> 1 << 1 | int(
            b)  # >>1<<1 means set the lowest bit to 0
        # logger.logger.debug("Embed: {} to {}\t->\t{}".format(b, tmp, img.image[img_index_row, img_index_col]))

    '''
    Write image
    '''
    filename = "./embed_" + str(embed_rate) + "_" + str(int(time.time())) + ".bmp"
    img.write_image(filename)
    logger.logger.info("Embed finished:{}".format(filename))
