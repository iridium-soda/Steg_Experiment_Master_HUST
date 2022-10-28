import cv2
from scipy import stats


def grayHist(img):
    grayDict = {}
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for key in range(256):
        grayDict[key] = 0
    for i in range(img_gray.shape[0]):
        for j in range(img_gray.shape[1]):
            grayDict[img_gray[i][j]] += 1
    '''
    grayDict=cv2.calcHist([img],[0],None,[256],[0,256])
    '''
    return grayDict


def as_num(x):
    y = '{:.10f}'.format(x)  # .10f 保留10位小数
    return y


if __name__ == "__main__":
    rpath = "embed_1666922117.bmp"
    rim = cv2.imread(rpath)
    rim_grey = grayHist(rim)
    tp = []
    for i in range(256):
        tp.append(rim_grey[i])
    i = 0
    exp = []
    obs = []
    while (i <= 127):
        if (((tp[2 * i] + tp[2 * i + 1]) // 2) == 0):
            i += 1
            continue
        exp.append((tp[2 * i] + tp[2 * i + 1]) / 2)
        obs.append(tp[2 * i])
        i += 1
    x = stats.chisquare(obs, f_exp=exp)
    print(as_num(x[1]))
    print(as_num(x[1]))
