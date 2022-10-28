import argparse

import chisquare
import logger
import lsb

parser = argparse.ArgumentParser(description='Process some images. Embed, chi-square analysis and LS analysis.')
parser.add_argument('path', type=str,
                    help='Input or output path')
exGroup = parser.add_mutually_exclusive_group()
exGroup.add_argument('-e', '--embed', action="store_true", default=True, help="Steg image by LSB")
exGroup.add_argument('-c', '--chi', action="store_true", help="Analysis image by chi-square")
exGroup.add_argument('-r', "--rs", action="store_true", help="Analysis image by RS")

if __name__ == "__main__":

    args = parser.parse_args()

    path, ifEmbed, ifChi, ifRS = args.path, args.embed, args.chi, args.rs

    if ifChi or ifRS:
        ifEmbed = False  # Convert ifEmbed to false manually

    logger.logger.debug("Command Status:\tPath:{}\tEmbed:{}\tChi:{}\tRS:{}\t".format(path, ifEmbed, ifChi, ifRS))

    if ifEmbed:
        lsb.embed(path)
    if ifChi:
        chisquare.chi(path)
