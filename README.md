# 【ZCCV2023】iKUNet: Intelligent Key-element Unlinking Network for Element Removal in Video
<p align="center">
    <a href="https://www.zhihu.com/question/612195663/answer/3120128019">
        <img alt="zhihu" src="https://img.shields.io/badge/Zhihu-知乎回答-blue">
    </a>
    <a href="https://github.com/PRIV-Creation/UniDiffusion/blob/main/LICENSE">
        <img alt="GitHub" src="https://img.shields.io/github/license/PRIV-Creation/UniDiffusion.svg?color=yellow">
    </a>
</p>

[最新一期奔跑吧将KunKun原地消失能启发哪些计算机视觉研究？ - 椿楸的回答 - 知乎](https://www.zhihu.com/question/612195663/answer/3120128019)

## Introduction
近年来，由于明星、企业频繁塌房，衍生出一个新的需求，即移除情节中的某个元素，如某个明星或某个赞助商，我们将这个任务命名为视频元素移除。
因此，我们提出了iKUNet框架，包含了**元素检测, 元素移除, 逻辑一致性检测**。我们采用了较轻量的开源代码构建iKUNet。

**本开源项目仅做娱乐使用。**

## iKUNet
关键技术：
- 元素检测
  - 人: Detection + Face Recognition + Matting
  - 物品: (zero-shot/one-shot) Segmenation
- 元素移除: Video Inpainting
- 逻辑一致性检测：
  - 字幕：OCR
  - 旁白：ASR
  - 视频：Video Caption + VQA
  - LLM

## Plan
计划先在两个demo上完成元素检测+移除

移除篮球尝试zero-shot segmentation，安慕希的分割可能精度不够，考虑采用few-shot微调一下

### Demo1: 两年半练习生
分别尝试移除人和篮球
### Demo2：跑男（截取一个几分钟片段）
分别尝试移除人和安慕希

## Getting Start
TODO

## Contribution
<img src="./ikunnet_wechat.jpg" width="240">
我们欢迎来自开源社区和知乎的开发者贡献代码，尤其是关于逻辑一致性检测模块。同时，任何想法也欢迎提交issue或知乎评论。

## Acknowledgement
https://weibo.com/caizicaixukun

## Citation
```
@inproceedings{kun2023ikunet,
  title=iKUNet: Intelligent Key-element Unlinking Network for Element Removal in Video},
  author={iKUNet's contributors},
  booktitle={Proceedings of the Zhihu Conference on Computer Vision},
  pages={question=612195663&answer=3120128019},
  year={2023}
}
```
