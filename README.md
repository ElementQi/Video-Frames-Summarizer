# Video-Frames-Summarizer

Video Summary Using Multimodal LLM API

## INFO

The workflow of the project:

- Extract n frames from a video;

- Put n frames into the Multimodal LLM to generate summary.

A video listed in `./video` is one of the data from [Charades](https://prior.allenai.org/projects/charades) according to [SEED-Bench-2]([https://huggingface.co/datasets/AILab-CVC/SEED-Bench-2]).

Sample output:

> 视频展示了一个房间的场景，其中一个人正在整理物品。视频中可以看到一个桌子，上面放着一台笔记本电脑、一个鼠标和一个手机。这个人穿着蓝色的上衣和黑色的裤子，正在弯腰整理桌子下面的物品。随后，他站直了身体，继续整理物品。最后，他把鞋子放在了地上。整个视频给人一种温馨的感觉，展示了一个人在整理房间时的日常生活场景。

## How to Use

In root directory, change the shell script as you need, and run `extract_frames.sh` to generate frame images, and then run `llm_summary.sh` to generate summary respectively.
