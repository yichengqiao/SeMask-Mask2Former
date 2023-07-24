# English Version:
# SeMask-Mask2Former：A Semantic Segmentation Model for High Resolution Remote Sensing Images


This project presents a semantic segmentation model for high-resolution remote sensing images called SeMask-Mask2Former, based on the potsdam dataset. Below is the directory structure and a brief description of the project.


## File and Folder Descriptions

- `.ipynb_checkpoints`: Jupyter Notebook checkpoint folder.
- `configs`: Contains model configuration files.
- `data`: Contains dataset and preprocessing-related files.
- `datasets`: Contains code related to dataset processing.
- `demo`: Contains demo files.
- `output`: Contains output results from training and testing.
- `tools`: Contains auxiliary tools.
- `eval.sh`: Evaluation script.
- `GETTING_STARTED.md`: Getting started guide.
- `INSTALL.md`: Installation guide.
- `kill_inpynb.checkpoint.py`: Jupyter Notebook processing file.
- `mmcv.ipynb`: MMCV library usage example.
- `MODEL_ZOO.md`: Model zoo description.
- `README.md`: Project readme file.
- `register_data.ipynb`: Dataset registration file.
- `requirements.txt`: List of Python packages required for the project.
- `test_vaihingen.ipynb`: Test file for the Vaihingen dataset.
- `train.ipynb`: Jupyter Notebook file for training.
- `train.sh`: Training script.
- `train_ipynb.txt`: Training text file.
- `train_net.py`: Main code for network training.
- `train_potsdam-old.ipynb`: Training file for the old version of the Potsdam dataset.
- `train_vaihingen.ipynb`: Training file for the Vaihingen dataset.

## Quick Start

Please refer to `INSTALL.md` and `GETTING_STARTED.md` for project installation and configuration.

## Model Training and Testing

Use `train.ipynb`, `train_vaihingen.ipynb`, and `train_potsdam-old.ipynb` for model training. For testing, refer to `test_vaihingen.ipynb`.

Enjoy using the project!
## citation
If you find this project helpful for your research, please consider citing the report and giving a ⭐.
```BibTex
@INPROCEEDINGS{10115761,
  author={Qiao, Yicheng and Liu, Wei and Liang, Bin and Wang, Pengyun and Zhang, Haopeng and Yang, Junli},
  booktitle={2023 IEEE Aerospace Conference}, 
  title={SeMask-Mask2Former: A Semantic Segmentation Model for High Resolution Remote Sensing Images}, 
  year={2023},
  volume={},
  number={},
  pages={1-6},
  doi={10.1109/AERO55745.2023.10115761}
}
```
# 中文版本：
# SeMask-Mask2Former：A Semantic Segmentation Model for High Resolution Remote Sensing Images
这个项目是一个基于potsdam数据集的遥感图像语义分割模型，名为SeMask-Mask2Former。以下是项目的目录结构和简要说明。

*《SeMask-Mask2Former：A Semantic Segmentation Model for High Resolution Remote Sensing Images》发表在2023 IEEE Aerospace Conference At the Yellowstone Conference Center in Big Sky, Montana,March 04 - 11
.

├─ .ipynb_checkpoints

├─ configs

├─ data

├─ datasets

├─ demo

├─ output

├─ tools

├─ eval.sh

├─ GETTING_STARTED.md

├─ INSTALL.md

├─ kill_inpynb.checkpoint.py

├─ mmcv.ipynb

├─ MODEL_ZOO.md

├─ README.md

├─ register_data.ipynb

├─ requirements.txt

├─ test_vaihingen.ipynb

├─ train.ipynb

├─ train.sh

├─ train_ipynb.txt

├─ train_net.py

├─ train_potsdam-old.ipynb

└─ train_vaihingen.ipynb


## 文件及文件夹说明

- `.ipynb_checkpoints`: Jupyter Notebook的检查点文件夹。
- `configs`: 存放模型配置文件。
- `data`: 存放数据集和预处理过程的相关文件。
- `datasets`: 包含数据集处理的相关代码。
- `demo`: 存放演示文件。
- `output`: 存放训练和测试的输出结果。
- `tools`: 一些辅助工具。
- `eval.sh`: 评估脚本。
- `GETTING_STARTED.md`: 入门指南。
- `INSTALL.md`: 安装指南。
- `kill_inpynb.checkpoint.py`: Jupyter Notebook处理文件。
- `mmcv.ipynb`: MMCV库的使用示例。
- `MODEL_ZOO.md`: 模型库说明。
- `README.md`: 项目的自述文件。
- `register_data.ipynb`: 数据集注册文件。
- `requirements.txt`: 项目依赖的Python包列表。
- `test_vaihingen.ipynb`: Vaihingen数据集的测试文件。
- `train.ipynb`: 训练的Jupyter Notebook文件。
- `train.sh`: 训练脚本。
- `train_ipynb.txt`: 训练文本文件。
- `train_net.py`: 训练网络的主要代码。
- `train_potsdam-old.ipynb`: 旧版Potsdam数据集的训练文件。
- `train_vaihingen.ipynb`: Vaihingen数据集的训练文件。

## 快速开始

请参照`INSTALL.md`和`GETTING_STARTED.md`进行项目的安装和配置。

## 安装

```
git clone https://github.com/Joeyicheng/SeMask-Mask2Former.git
```

```
pip install -r requirements.txt
```


## 模型训练与测试

使用`train.ipynb`、`train_vaihingen.ipynb`和`train_potsdam-old.ipynb`进行模型的训练。测试过程可参考`test_vaihingen.ipynb`。

祝您使用愉快！
