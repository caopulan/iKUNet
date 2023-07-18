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



因为答主近期没有很多时间来做这个项目，打算依靠集体的力量了。我先大致对这个任务进行拆分，大家有任何建议都可以提issue/知乎评论/群里讨论，拆解好基础模块后，想要动手做的朋友可以来认领~

| 任务模块       | 任务设定                                       | 参考流程                                                    | 输入                      | 输出                      |
| -------------- | ---------------------------------------------- | ----------------------------------------------------------- | ------------------------- | ------------------------- |
| 元素检测       | 分割某个指定ID的人物                           | 人脸识别/re-id + Human Parsing/SAM [+ Tracking]             | 一段视频 + 参考人脸       | 每帧的人物mask            |
|                | 分割某个[类别]的物体                           | Prompt + SAM / Instance Segmentation [+ Tracking]           | 一段视频 + 物品类别       | 每帧的物体mask            |
|                | 分割某个[参考]物体                             | Prompt + SAM  [+ Tracking]                                  | 一段视频 + 参考点/框      | 每帧的物体mask            |
|                | 分割某个[含少量标注数据]的物体                 | Few-shot Segmentation  [+ Tracking]                         | 一段视频 + 少量分割标注   | 每帧的物体mask            |
| 元素移除       | 移除画面中的某个元素                           | Video Inpainting / Image Inpainting                         | 一段视频 + 元素每帧的mask | 移除元素后的视频          |
| 逻辑一致性检测 | 字幕识别                                       | OCR                                                         | 一段视频                  | 带时间戳的字幕            |
|                | 语音识别                                       | ASR + 说话人识别                                            | 一段视频                  | 带时间戳+说话人的语音文本 |
|                | 画面内容转文本                                 | Caption / VQA / Detection                                   | 一段视频                  | 时间戳 + 画面内容文本     |
|                | 判断元素移除任务下字幕、语音、画面是否逻辑一致 | 任务设定（如角色A被移除）+字幕+语音+画面内容构建prompt，LLM | 字幕、语音、画面内容      | 逻辑不一致的部分          |

一些建议：

1. 尽量保证完全自动化。
2. 使用封装较成熟、使用方便、少依赖的其他组件，如通过huggingface调用模型。
3. 元素检测需考虑变化场景（尤其是使用tracking方法的时候）。
4. 前两个可以参考Inpaint Anything，需要进行一些优化，如多场景、多人物。



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
