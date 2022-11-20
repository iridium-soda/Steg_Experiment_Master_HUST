# Steg_Experiment_Master_HUST
课程名称: 信息隐藏

课程时间: 2022

## Description

基于Python实现BMP灰度图像的LSB隐写、卡方分析和RS检测

1.   LSB隐写
2.   卡方分布
3.   RS分布

## Usage

Install dependency

```bash
pip install -r requirements.txt
```

Usage

```shell
usage: main.py [-h] [ -e | -c | -r] path

Process some images. Embed, chi-square analysis and LS analysis.

positional arguments:
  path         Input or output path

options:
  -h, --help   show this help message and exit
  -e, --embed  Steg image by LSB
  -c, --chi    Analysis image by chi-square
  -r, --rs     Analysis image by RS

```

## Tips

更大的嵌入率可以得到更显著的结果

仅限灰度图像

处于简便考虑，秘文为随机生成的01流，可控嵌入率。

Chi-square分析对于程序中的随机嵌入效果不好。
