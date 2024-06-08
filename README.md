# VideoReTalking-HQ
VideoReTalking-HQ is an imptuve high-quality video retalking tool for enhancing and synchronizing video frames with audio inputs using advanced face enhancement techniques, including GFPGAN, and expression control.

## About

VideoReTalking-HQ, an enhaced system to edit the faces of a real-world talking head video according to input audio, producing a high-quality and lip-syncing output video.  The system disentangles this objective into three sequential tasks: face video generation with a canonical expression; audio-driven lip-sync; and face enhancement for improving photo-realism. Given a talking-head video, we first modify the expression of each frame according to the same expression template using the expression editing network, resulting in a video with the canonical expression. This video, together with the given audio, is then fed into the lip-sync network to generate a lip-syncing video. Finally, we improve the photo-realism of the synthesized faces through an identity-aware face enhancement network and post-processing. We use learning-based approaches for all three steps and all our modules can be tackled in a sequential pipeline without any user intervention.

![video-retalking1](https://github.com/ShmuelRonen/VideoReTalking-HQ/assets/80190186/82bc97ed-c0a0-4d53-8b5f-93d2b18683d2)

## Installation steps
```
https://github.com/ShmuelRonen/VideoReTalking-HQ.git
cd VideoReTalking-HQ
conda create -n video_retalking python=3.8
conda activate video_retalking
pip install ffmpeg

# For your CUDA version please follow the instructions from https://pytorch.org/get-started/previous-versions/
# This installation suggestion command only works on CUDA 11.1
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html

pip install -r requirements.txt
pip install ffmpeg-python
pip install gradio
pip install gfpgan

```
https://drive.google.com/file/d/12_3Df9LMTweNZHxlbjM851UCguRfjpru/view?usp=drive_link

1. Download the archive from Google Drive to your computer.

2. Extract the compressed checkpoints folder with 7zip. 

3. copy the checkpoints folder  into the main VideoReTalking-HQ folder.

4. Click on start.bat to launch

_____________



## Acknowledgement
Thanks to
[Wav2Lip](https://github.com/Rudrabha/Wav2Lip),
[PIRenderer](https://github.com/RenYurui/PIRender), 
[GFP-GAN](https://github.com/TencentARC/GFPGAN), 
[GPEN](https://github.com/yangxy/GPEN),
[ganimation_replicate](https://github.com/donydchen/ganimation_replicate),
[STIT](https://github.com/rotemtzaban/STIT)
for sharing their code.


## Related Work
- [StyleHEAT: One-Shot High-Resolution Editable Talking Face Generation via Pre-trained StyleGAN (ECCV 2022)](https://github.com/FeiiYin/StyleHEAT)
- [CodeTalker: Speech-Driven 3D Facial Animation with Discrete Motion Prior (CVPR 2023)](https://github.com/Doubiiu/CodeTalker)
- [SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation (CVPR 2023)](https://github.com/Winfredy/SadTalker)
- [DPE: Disentanglement of Pose and Expression for General Video Portrait Editing (CVPR 2023)](https://github.com/Carlyx/DPE)
- [3D GAN Inversion with Facial Symmetry Prior (CVPR 2023)](https://github.com/FeiiYin/SPI/)
- [T2M-GPT: Generating Human Motion from Textual Descriptions with Discrete Representations (CVPR 2023)](https://github.com/Mael-zys/T2M-GPT)

##  Disclaimer

This is not an official product of Tencent. 

```
1. Please carefully read and comply with the open-source license applicable to this code before using it. 
2. Please carefully read and comply with the intellectual property declaration applicable to this code before using it.
3. This open-source code runs completely offline and does not collect any personal information or other data. If you use this code to provide services to end-users and collect related data, please take necessary compliance measures according to applicable laws and regulations (such as publishing privacy policies, adopting necessary data security strategies, etc.). If the collected data involves personal information, user consent must be obtained (if applicable). Any legal liabilities arising from this are unrelated to Tencent.
4. Without Tencent's written permission, you are not authorized to use the names or logos legally owned by Tencent, such as "Tencent." Otherwise, you may be liable for legal responsibilities.
5. This open-source code does not have the ability to directly provide services to end-users. If you need to use this code for further model training or demos, as part of your product to provide services to end-users, or for similar use, please comply with applicable laws and regulations for your product or service. Any legal liabilities arising from this are unrelated to Tencent.
6. It is prohibited to use this open-source code for activities that harm the legitimate rights and interests of others (including but not limited to fraud, deception, infringement of others' portrait rights, reputation rights, etc.), or other behaviors that violate applicable laws and regulations or go against social ethics and good customs (including providing incorrect or false information, spreading pornographic, terrorist, and violent information, etc.). Otherwise, you may be liable for legal responsibilities.

```
