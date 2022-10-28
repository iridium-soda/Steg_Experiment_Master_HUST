# Steg_Experiment_Master_HUST
课程名称: 信息隐藏

课程时间: 2022

## Description

基于Python实现BMP灰度图像的LSB隐写、卡方分析和RS检测

1.   LSB隐写
2.   卡方分布
3.   RS分布

## References

[LSB信息隐藏的卡方分析_星辞归野的博客-CSDN博客_lsb卡方分析](https://blog.csdn.net/weixin_43916678/article/details/109825559)

[信息隐藏实验一 LSB隐写和RS分析实现_red1y的博客-CSDN博客_lsb图像信息隐藏实验](https://blog.csdn.net/weixin_39578432/article/details/123804937)

[实验:基于奇偶校验的LSB算法及卡方分析 | 烏巢 (hejueyun.github.io)](https://hejueyun.github.io/posts/42a865c0/)

[RS（Regular Singular）隐写分析及实现_咸鱼.m的博客-CSDN博客_rs隐写分析](https://blog.csdn.net/qq_37207042/article/details/106166181)

## Target

图片使用LSB进行隐写，尝试使用卡方分析和RS分析检测。



## Usage

>   在venv下开发和执行。

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



## Dependency



## Tips

更大的嵌入率可以得到更显著的结果

仅限灰度图像

处于简便考虑，秘文为随机生成的01流，可控嵌入率。

Chi-square分析对于程序中的随机嵌入效果不好。
