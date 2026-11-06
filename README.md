### Run anime face detection from repo root

Source: https://github.com/shitagaki-lab/see-through/blob/main/annotators/README.md

Execute the parse_live2d.py script with the facedet subcommand inside the ann_mmpose environment. The --exec_list flag points to an execution list file under workspace/datasets.

```bash
conda run --no-capture-output -n ann_mmpose \
  python inference/scripts/parse_live2d.py facedet \
  --exec_list workspace/datasets/.../exec_list.txt
```

--------------------------------

### Prepare background images for training data

Source: https://github.com/shitagaki-lab/see-through/blob/main/README_datapipeline.md

Download the anime segmentation background dataset using hf and extract it with 7z. The commands assume you are in the workspace/datasets directory.

```bash
cd workspace/datasets
```

```bash
hf download 24yearsold/anime_segmentation_bg --local-dir ./ --repo-type dataset
```

```bash
7z x anime_segmentation_bg.zip.001
```

```bash
rm -rf ./anime_segmentation_bg.zip.*
```

--------------------------------

### Setup commands for anime_face_detector environment

Source: https://github.com/shitagaki-lab/see-through/blob/main/annotators/anime_face_detector/README.md

Creates and activates the Conda environment `live2d_ann_mmpose` with Python 3.10, installs PyTorch 1.13.1 with CUDA 11.7, and installs OpenMMLab packages (mmcv-full, mmdet, mmpose) via MIM. Note: environment compatibility with `common/` is not verified; see `../../ISSUES.md`.

```bash
conda create -n live2d_ann_mmpose python=3.10 -c conda-forge
conda activate live2d_ann_mmpose
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 \
  --extra-index-url https://download.pytorch.org/whl/cu117
pip install openmim==0.3.6 numpy==1.26.4 opencv-python==4.10.0.84
mim install mmcv-full==1.7.0
mim install mmdet==2.28.2
mim install mmpose==0.29.0
```

--------------------------------

### Installation command for animeinsseg dependencies

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements-inference-mmdet.txt

Install the required packages for anime instance segmentation using mmcv and mmdet. Requires CUDA toolkit.

```bash
pip install -r requirements-inference-mmdet.txt
```

--------------------------------

### requirements-inference-mmdet.txt

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements-inference-mmdet.txt

Lists the exact package versions needed for anime instance segmentation with mmcv and mmdet.

```text
mmcv==2.1.0
mmdet==3.3.0
mmengine==0.10.7
```

--------------------------------

### ML utilities dependencies

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements.txt

Machine learning utility packages including kornia, omegaconf, pycocotools, and grad-cam.

```text
kornia==0.8.2
omegaconf==2.3.0
pycocotools==2.0.11
grad-cam==1.5.5
```

--------------------------------

### Set up dedicated conda environment for anime_face_detector

Source: https://github.com/shitagaki-lab/see-through/blob/main/annotators/README.md

Create a separate conda environment named ann_mmpose with Python 3.10 for the legacy anime_face_detector, which requires PyTorch 1.13, mmcv-full 1.7, and other incompatible dependencies. Install the required packages and the common package from the repo root.

```bash
conda create -n ann_mmpose python=3.10
conda activate ann_mmpose
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 \
  --extra-index-url https://download.pytorch.org/whl/cu117
pip install openmim==0.3.6 numpy==1.26.4 opencv-python==4.10.0.84
mim install mmcv-full==1.7.0
mim install mmdet==2.28.2
mim install mmpose==0.29.0
pip install -e ./common
```

--------------------------------

### Environment Setup Commands

Source: https://github.com/shitagaki-lab/see-through/blob/main/README.md

Commands to create a conda environment, install PyTorch with CUDA 12.8, install dependencies, and create an assets symlink. Note: aarch64 users may need torch>=2.9.0; AMD ROCm users should install the matching ROCm wheel set. Always run scripts from the repository root.

```bash
# 1. Create environment
conda create -n see_through python=3.12 -y
conda activate see_through

# 2. Install PyTorch (CUDA 12.8)
# aarch64 users: the pinned versions below may not be available; use torch>=2.9.0 instead
pip install torch==2.8.0+cu128 torchvision==0.23.0+cu128 torchaudio==2.8.0+cu128 \
  --index-url https://download.pytorch.org/whl/cu128

# AMD ROCm users: install the ROCm wheel set that matches your local ROCm runtime instead.
# For example, on ROCm 7.2:
# pip install torch torchvision torchaudio \
#   --index-url https://download.pytorch.org/whl/rocm7.2

# 3. Install dependencies (includes common utilities and annotators)
pip install -r requirements.txt

# 4. Create assets symlink (you can also copy assets to the root if you prefer)
ln -sf common/assets assets
```

--------------------------------

### Create and activate conda environment, install detectron2

Source: https://github.com/shitagaki-lab/see-through/blob/main/annotators/bizarre_tagger/README.md

Sets up a conda environment named `live2d_ann_detectron2` with Python 3.10, activates it, and installs detectron2 from the main branch on GitHub without build isolation.

```bash
conda create -n live2d_ann_detectron2 python=3.10
conda activate live2d_ann_detectron2
pip install git+https://github.com/facebookresearch/detectron2@main#egg=detectron2 \
  --no-build-isolation
```

--------------------------------

### Setup commands for animeinsseg conda environment

Source: https://github.com/shitagaki-lab/see-through/blob/main/annotators/animeinsseg/README.md

Commands to create and activate the `live2d_ann_mmdet3` conda environment and install required packages. Includes PyTorch, mmcv, numpy, accelerate, opencv, openmim, ipykernel, einops, setuptools, and a custom mmdetection build. Note: dependency hell prevents a single conda YAML; see ISSUES.md.

```bash
conda create -n live2d_ann_mmdet3 python=3.12 -c conda-forge
conda activate live2d_ann_mmdet3
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 \
  --index-url https://download.pytorch.org/whl/cu121
pip install mmcv==2.2.0 -f https://download.openmmlab.com/mmcv/dist/cu121/torch2.4/index.html
pip install numpy==1.26.4 accelerate==1.7.0 pillow-jxl-plugin opencv-python==4.10.0.84 \
  openmim==0.3.9 ipykernel einops
pip install setuptools==80.9.0
pip install git+https://github.com/dmMaze/mmdetection@dev-3.x#egg=mmdet
```

--------------------------------

### Setup commands for see_through_dev environment

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements.txt

Commands to create and activate a conda environment named see_through_dev with Python 3.12, install PyTorch with CUDA 12.8, and install the requirements file. Optional tier files can be installed separately as needed.

```bash
conda create -n see_through_dev python=3.12 -y
conda activate see_through_dev
pip install torch==2.8.0+cu128 torchvision==0.23.0+cu128 torchaudio==2.8.0+cu128 \
  --index-url https://download.pytorch.org/whl/cu128
pip install -r requirements.txt
```

```bash
pip install -r requirements-training-deepspeed.txt
pip install -r requirements-inference-annotators.txt
pip install -r requirements-inference-mmdet.txt
```

--------------------------------

### Initialize SemanticSam model from pretrained checkpoint

Source: https://github.com/shitagaki-lab/see-through/blob/main/inference/demo/bodypartseg_sam.ipynb

Loads the SemanticSam model from Hugging Face with 19 classes and moves it to CUDA.

```python
model: SemanticSam = init_model_from_pretrained(
    pretrained_model_name_or_path='24yearsold/l2d_sam_iter2',
    weights_name='checkpoint-18000.pt',
    module_cls=SemanticSam,
    download_from_hf=True,
    model_args=dict(class_num=19)
).to(device='cuda')
```

--------------------------------

### Run Heuristic Part Segmentation (heuristic_partseg.py)

Source: https://github.com/shitagaki-lab/see-through/blob/main/README.md

Further processes a PSD after layer splitting for depth-based or left-right stratification. The depth split uses seg_wdepth and the left-right split uses seg_wlr, each with a --target_tags argument.

```bash
# Split based on depth
python inference/scripts/heuristic_partseg.py seg_wdepth --srcp workspace/test_samples_output/PV_0047_A0020.psd --target_tags handwear
```

```bash
#Left-right split
python inference/scripts/heuristic_partseg.py seg_wlr --srcp workspace/test_samples_output/PV_0047_A0020_wdepth.psd --target_tags handwear-1
```

--------------------------------

### Run inference on test image

Source: https://github.com/shitagaki-lab/see-through/blob/main/inference/demo/bodypartseg_sam.ipynb

Loads a test image, runs model inference, and converts predictions to a boolean mask array.

```python
p = '../../assets/test_image1.png'

img = np.array(Image.open(p).convert('RGB'))
with torch.inference_mode():
    preds = model.inference(img)[0]
    masks_np = (preds > 0).to(device='cpu', dtype=torch.bool).numpy()
```

--------------------------------

### Run Layer Decomposition Pipeline (inference_psd.py)

Source: https://github.com/shitagaki-lab/see-through/blob/main/README.md

Runs the full See-through pipeline: LayerDiff 3D for transparent layers, fine-tuned Marigold for pseudo-depth, and stratification into up to 23 semantic layers, exporting a layered PSD. Output is saved to workspace/layerdiff_output/ by default. Head and body separation are in two continuous stages, which may take longer than the original model.

```bash
# Decompose a single image into a layered PSD
python inference/scripts/inference_psd.py \
  --srcp assets/test_image.png \
  --save_to_psd
```

```bash
# Process a directory of images
python inference/scripts/inference_psd.py \
  --srcp path/to/image_folder/ \
  --save_to_psd
```

--------------------------------

### Launch UI with a specific project

Source: https://github.com/shitagaki-lab/see-through/blob/main/ui/README.md

Open a project directly by passing its path to the `--proj` flag. The path is relative to the repo root.

```bash
python ui/ui/launch.py --proj workspace/datasets/<project_name>
```

--------------------------------

### Install optional dependencies for training

Source: https://github.com/shitagaki-lab/see-through/blob/main/training/README.md

Install DeepSpeed ZeRO for multi-GPU training (required for LayerDiff), wandb for experiment tracking, bitsandbytes for 8-bit Adam optimizer (used with --use_8bit_adam in config), and torchmetrics for FID/LPIPS/PSNR benchmarks (required by scripts/benchmark.py).

```bash
# DeepSpeed ZeRO for multi-GPU training (required for LayerDiff)
pip install -r requirements-training-deepspeed.txt

# Experiment tracking
pip install wandb

# 8-bit Adam optimizer (used with --use_8bit_adam in config)
pip install bitsandbytes

# FID / LPIPS / PSNR benchmarks (required by scripts/benchmark.py)
pip install torchmetrics
```

--------------------------------

### Multi-GPU training with DeepSpeed (LayerDiff example)

Source: https://github.com/shitagaki-lab/see-through/blob/main/training/README.md

Run from repository root. Activates conda environment and launches multi-GPU training with Accelerate using a config file. Adjust num_processes to match GPU count.

```bash
cd /path/to/see-through
conda activate see_through

# Multi-GPU training with DeepSpeed (LayerDiff example)
accelerate launch --config_file training/configs/test_ddp_4gpu.json \
  training/train/train_layerdiff.py \
  --config training/configs/test_layerdiff.yaml
```

--------------------------------

### Marigold depth training pipeline (2D to 3D)

Source: https://github.com/shitagaki-lab/see-through/blob/main/training/README.md

Three-stage pipeline for Marigold depth: train 2D depth model, convert UNet weights to 3D, then fine-tune 3D model. Requires multi-GPU training with DeepSpeed ZeRO-2.

```text
train_marigold_depth.py  -->  cvt_marigold2d_to_3d.py  -->  train_marigold3d.py
    (2D depth model)          (UNet weight conversion)       (3D depth model)
```

--------------------------------

### Generate pseudo labels with parse_live2d.py

Source: https://github.com/shitagaki-lab/see-through/blob/main/README_datapipeline.md

Run three commands to build an execution list, perform SAM inference, and label Live2D parts with SAM segments. The exec_list.txt file is used by the UI for manual label correction.

```bash
python inference/scripts/parse_live2d.py build_live2d_exec_list --srcd workspace/datasets/partextr_output
```

```bash
python inference/scripts/parse_live2d.py sam_infer_l2d --exec_list workspace/datasets/partextr_output/exec_list.txt
```

```bash
python inference/scripts/parse_live2d.py label_l2d_wsamsegs --exec_list workspace/datasets/partextr_output/exec_list.txt --extr_more
```

--------------------------------

### Workspace directory structure for project data

Source: https://github.com/shitagaki-lab/see-through/blob/main/ui/README.md

Expected layout under `workspace/datasets/`. Each project directory contains `exec_list.txt` (model paths, one per line) and model folders with `final.jxl`, `final.json` (auto-created), `instances.json`, and `*_masks.json` (from inference).

```text
workspace/
└── datasets/
    └── <project_name>/
        ├── exec_list.txt              # List of model paths (one per line)
        └── <model_name>/
            ├── final.jxl              # Source image (JXL format)
            ├── final.json             # Project metadata (auto-created by UI)
            ├── instances.json         # Instance annotations
            └── *_masks.json           # Segmentation masks (from inference)
```

--------------------------------

### Launch UI from repo root with conda env

Source: https://github.com/shitagaki-lab/see-through/blob/main/ui/README.md

Run the Qt6 UI from the repository root. Requires the `see_through` conda environment and the `assets` symlink at repo root, otherwise the UI crashes on startup with `FileNotFoundError`.

```bash
cd /path/to/see-through
conda activate see_through
python ui/ui/launch.py
```

--------------------------------

### Run synthesize script to generate training data

Source: https://github.com/shitagaki-lab/see-through/blob/main/README_datapipeline.md

Render body samples using the execution list and background list, then generate a target list. The output is saved to workspace/datasets/test_bodysamples.

```bash
python inference/scripts/syn_data.py render_body_samples --exec_list workspace/datasets/partextr_output/exec_list.txt --bg_list workspace/datasets/anime_segmentation_bg/exec_list.txt \
--save_dir workspace/datasets/test_bodysamples
```

```bash
python inference/scripts/syn_data.py get_tgt_list --src_dir workspace/datasets/partextr_bodysamples
```

--------------------------------

### Run Block Swap Pipeline (8 GB GPUs)

Source: https://github.com/shitagaki-lab/see-through/blob/main/README.md

Achieves ~8 GB peak VRAM at 1280 resolution with bf16 precision using block swap. Note: the command includes a trailing backslash.

```bash
python inference/scripts/inference_psd_blockswap.py \
  --srcp assets/test_image.png \
  --save_to_psd \
```

--------------------------------

### Visualize segmentation masks

Source: https://github.com/shitagaki-lab/see-through/blob/main/inference/demo/bodypartseg_sam.ipynb

Displays the segmentation masks overlaid on the original image using the V2 body part labels.

```python
Image.fromarray(visualize_segs_with_labels(masks_np, img, VALID_BODY_PARTS_V2))
```

--------------------------------

### LayerDiff training pipeline (2D to 3D)

Source: https://github.com/shitagaki-lab/see-through/blob/main/training/README.md

Three-stage pipeline for LayerDiff: train 2D layer model, convert UNet weights to 3D, then fine-tune 3D model. Requires multi-GPU training with DeepSpeed ZeRO-2.

```text
train_layerdiff.py  -->  cvt_layerdiff2d_to_3d.py  -->  train_layerdiff3d.py
   (2D layer model)       (UNet weight conversion)       (3D layer model)
```

--------------------------------

### Import dependencies for body part segmentation

Source: https://github.com/shitagaki-lab/see-through/blob/main/inference/demo/bodypartseg_sam.ipynb

Imports required libraries and modules for the body part segmentation demo, including SemanticSam and utility functions.

```python
import argparse
from omegaconf import OmegaConf
import os
import os.path as osp
import numpy as np
from  tqdm import tqdm
from einops import reduce
from PIL import Image
import click
import cv2
import sys


from live2d.scrap_model import animal_ear_detected, Drawable, VALID_BODY_PARTS_V2
from utils.cv import fgbg_hist_matching, quantize_image, random_crop, rle2mask, mask2rle, img_alpha_blending, resize_short_side_to, batch_save_masks, batch_load_masks
from utils.torch_utils import seed_everything, init_model_from_pretrained
from utils.visualize import visualize_segs_with_labels
from modules.semanticsam import SemanticSam, Sam
import torch
```

--------------------------------

### HuggingFace stack dependencies

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements.txt

HuggingFace-related packages including transformers, diffusers, huggingface-hub, tokenizers, accelerate, safetensors, timm (from GitHub), and simple-parsing.

```text
transformers==5.0.0
diffusers==0.37.0
huggingface-hub==1.7.2
tokenizers==0.22.2
accelerate==1.13.0
safetensors==0.7.0
timm @ git+https://github.com/huggingface/pytorch-image-models@6e3fdda39508db30766f9d9e6ec32380ebee8b8c
simple-parsing==0.1.8
```

--------------------------------

### Run NF4 Quantized Pipeline (8 GB GPUs)

Source: https://github.com/shitagaki-lab/see-through/blob/main/README.md

Uses 4-bit quantized model weights to achieve ~8 GB peak VRAM at 1280 resolution. Requires installing bitsandbytes first. Default settings: group_offload on, depth resolution 720. Quality is close to full-precision (PSNR ~30 dB, SSIM ~0.96 vs bf16 baseline).

```bash
# Install bitsandbytes (one-time)
pip install -r requirements-inference-bnb.txt
```

```bash
# Run with NF4 quantization (default: group_offload on, depth resolution 720)
python inference/scripts/inference_psd_quantized.py \
  --srcp assets/test_image.png \
  --save_to_psd
```

```bash
# For even lower VRAM, reduce layerdiff resolution to 1024
python inference/scripts/inference_psd_quantized.py \
  --srcp assets/test_image.png \
  --save_to_psd \
  --resolution 1024
```

--------------------------------

### Headless testing with Xvfb

Source: https://github.com/shitagaki-lab/see-through/blob/main/ui/README.md

For visual testing on headless Linux. Installs system dependencies, starts Xvfb on display :99, and runs the UI with that display.

```bash
sudo bash ui/install_system_deps.sh
Xvfb :99 -screen 0 1920x1080x24 &
DISPLAY=:99 python ui/ui/launch.py
```

--------------------------------

### Run Layer Decomposition with Group Offload (12 GB GPUs)

Source: https://github.com/shitagaki-lab/see-through/blob/main/README.md

Enables group offload to reduce peak VRAM to ~10 GB at 1280 resolution for 12 GB GPUs. The default pipeline runs at bf16 precision and requires approximately 12-16 GB of VRAM at 1280 resolution.

```bash
python inference/scripts/inference_psd.py \
  --srcp assets/test_image.png \
  --save_to_psd \
  --group_offload
```

--------------------------------

### Core scientific dependencies

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements.txt

Core scientific Python packages pinned for the see_through_dev environment, including numpy, opencv-python, pillow, matplotlib, pandas, scikit-learn, scipy, scikit-image, einops, and pillow-jxl-plugin.

```text
numpy==2.2.6
opencv-python==4.13.0.92
pillow==12.1.1
pillow-jxl-plugin==1.3.7
matplotlib==3.9.4
pandas==2.3.3
scikit-learn==1.7.2
scipy==1.15.3
scikit-image==0.25.2
einops==0.8.2
```

--------------------------------

### Install optional annotator extras

Source: https://github.com/shitagaki-lab/see-through/blob/main/annotators/README.md

Install heavier annotator extras like bizarre_tagger, lang_sam, and animeinsseg. The bizarre_tagger and lang_sam extras require a C++ compiler and take about 10 minutes. The animeinsseg extra needs the CUDA toolkit for mmcv build. Use the pre-configured tier file or install everything with [all].

```bash
# Body parsing + language SAM (~10 min, needs C++ compiler)
pip install -e annotators[bizarre_tagger,lang_sam]

# Instance segmentation (needs CUDA toolkit for mmcv build)
pip install -e annotators[animeinsseg]

# Or use the pre-configured tier file:
pip install -r requirements-inference-mmdet.txt

# Everything
pip install -e annotators[all]
```

--------------------------------

### UI-specific dependencies

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements.txt

UI-specific packages: natsort, py7zr, termcolor, colorama, and pyyaml.

```text
natsort==8.4.0
py7zr==1.1.0
termcolor==3.3.0
colorama==0.4.6
pyyaml==6.0.3
```

--------------------------------

### Install annotator extras (detectron2 + SAM2)

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements-inference-annotators.txt

Two-step installation for detectron2 (bizarre_tagger) and SAM2 (lang_sam). Requires a C++ compiler and torch already installed. Use --no-build-isolation because detectron2's setup.py imports torch; order matters for iopath compatibility.

```bash
pip install --no-build-isolation -r requirements-inference-annotators.txt
```

```bash
pip install --no-build-isolation "sam-2 @ git+https://github.com/facebookresearch/segment-anything-2@c2ec8e14a185632b0a5d8b161928ceb50197eddc"
```

--------------------------------

### Dev tools dependencies

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements.txt

Development tools: ipykernel, Cython, wheel, and pytest.

```text
ipykernel==7.2.0
Cython==3.2.4
wheel==0.45.1
pytest==8.4.1
```

--------------------------------

### DeepSpeed installation requirements

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements-training-deepspeed.txt

Install DeepSpeed 0.15.4 for multi-GPU distributed training. Requires a C++ compiler and CUDA toolkit. Optional extras are commented out: wandb for experiment tracking, bitsandbytes for 8-bit Adam optimizer (--use_8bit_adam flag), and torchmetrics for FID/LPIPS/PSNR benchmarks (scripts/benchmark.py).

```text
# DeepSpeed for multi-GPU distributed training (requires C++ compiler + CUDA toolkit)
# Install: pip install -r requirements-training-deepspeed.txt
deepspeed==0.15.4

# Optional extras (uncomment as needed):
# wandb          — experiment tracking
# bitsandbytes   — 8-bit Adam optimizer (--use_8bit_adam flag)
# torchmetrics   — FID/LPIPS/PSNR benchmarks (scripts/benchmark.py)
```

--------------------------------

### VAE training dependencies (lpips + convnext)

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements.txt

Packages for VAE training: lpips and convnext_perceptual_loss from GitHub. Included in base per decision to avoid separate tier friction.

```text
lpips==0.1.4
convnext_perceptual_loss @ git+https://github.com/sypsyp97/convnext_perceptual_loss.git@967cd172dfcc6407f6b8e5ea489cfd2f4fba51ba
```

--------------------------------

### Windows Installation Commands

Source: https://github.com/shitagaki-lab/see-through/blob/main/ui/ui/readme.md

Install dependencies for Windows with Python 3.10. Note that Python >3.11 might break mmcv, and torch >2.1 might not work for mmcv.

```shell
pip install -r requirements.txt
pip install -U openmim
# torch > 2.1 might not work for mmcv
pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu118 
pip install numpy==1.26.4
mim install mmcv==2.1.0
mim install mmdet==3.3.0
python launch.py
```

--------------------------------

### Install UI requirements from ui/ directory

Source: https://github.com/shitagaki-lab/see-through/blob/main/ui/requirements-legacy-3.10.txt

Install the legacy Python 3.10 requirements for the UI shell. Run from the ui/ directory so that the editable install of ../common resolves. Ensure the assets -> common/assets symlink exists at repo root for cwd-relative paths.

```bash
cd ui && pip install -r requirements.txt
```

--------------------------------

### Optional Annotator Tiers Installation Commands

Source: https://github.com/shitagaki-lab/see-through/blob/main/README.md

Commands to install optional annotator tiers: body parsing (detectron2), SAM2, and instance segmentation (mmcv/mmdet). Install as needed.

```bash
pip install --no-build-isolation -r requirements-inference-annotators.txt
```

```bash
pip install --no-build-isolation -r requirements-inference-sam2.txt
```

```bash
pip install -r requirements-inference-mmdet.txt
```

--------------------------------

### Data & IO dependencies

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements.txt

Data and I/O packages: click, psd-tools with composite extra, and tqdm.

```text
click==8.3.1
psd-tools[composite]==1.14.2
tqdm==4.67.3
```

--------------------------------

### Qt UI dependencies

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements.txt

Qt-based UI packages: PyQt6, PyQt6-Qt6, and qtpy.

```text
PyQt6==6.9.1
PyQt6-Qt6==6.9.1
qtpy==2.4.3
```

--------------------------------

### macOS Installation Commands

Source: https://github.com/shitagaki-lab/see-through/blob/main/ui/ui/readme.md

Install dependencies for macOS with Python 3.11. Note that torch != 2.1.0 might not work for mmcv.

```shell
pip install -r requirements.txt
pip install -U openmim
# torch != 2.1.0 might not work for mmcv
pip install torch==2.1.0 torchvision torchaudio
pip install numpy==1.26.4
pip install mmcv==2.1.0 -f https://download.openmmlab.com/mmcv/dist/cpu/torch2.1/index.html
mim install mmdet==3.3.0
python launch.py
```

--------------------------------

### Install SAM2 after detectron2 (requirements-inference-sam2.txt)

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements-inference-sam2.txt

Install SAM2 after detectron2 to avoid iopath version conflicts. Use --no-build-isolation. The pinned commit is c2ec8e14a185632b0a5d8b161928ceb50197eddc.

```text
# SAM2 for lang_sam annotator
# Install AFTER requirements-inference-annotators.txt (detectron2 must be installed first):
#   pip install --no-build-isolation -r requirements-inference-sam2.txt
# This is separate because SAM2 and detectron2 have conflicting iopath version needs.
# Installing detectron2 first gets iopath==0.1.9 (via fvcore); SAM2 accepts it.
sam-2 @ git+https://github.com/facebookresearch/segment-anything-2@c2ec8e14a185632b0a5d8b161928ceb50197eddc
```

--------------------------------

### requirements-inference-annotators.txt

Source: https://github.com/shitagaki-lab/see-through/blob/main/requirements-inference-annotators.txt

Dependencies for the annotator extras. Step 1 installs detectron2 and its dependencies, including iopath<0.1.10 via fvcore.

```text
detectron2 @ git+https://github.com/facebookresearch/detectron2@a25898a09d6ee232767647e92c6177fb1c642369
hydra-core
pydantic>=2.9.2
uvloop
```

--------------------------------

### Legacy Python 3.10 requirements.txt content

Source: https://github.com/shitagaki-lab/see-through/blob/main/ui/requirements-legacy-3.10.txt

Deprecated legacy requirements file for Python 3.10. Use the unified requirements.txt at repo root instead. Includes base UI dependencies, Qt framework, scientific libraries, data/IO tools, and terminal/logging packages. Note that Tier 1 annotators are not installable via this file.

```text
# DEPRECATED — Legacy Python 3.10 requirements. Kept for reference only.
# Use the unified requirements.txt at repo root instead.
# See docs/superpowers/specs/2026-03-24-unified-env-design.md
#
# ── Tier 0 — Base UI ──────────────────────────────────────────────
# Everything needed to run the UI shell: project loading, canvas,
# tagging, editing. No compiler required. Installs in ~2 min.
# Pinned 2026-03-21 from fresh conda env build.
#
# NOTE: Install from the ui/ directory so that -e ../common resolves:
#   cd ui && pip install -r requirements.txt
# Also ensure assets -> common/assets symlink exists at repo root
# (the UI uses cwd-relative paths for icons and tag cluster data).

# Shared utilities (editable install from sibling directory)
-e ../common

# ── Qt framework ──
PyQt6==6.9.1
PyQt6-Qt6==6.9.1
qtpy==2.4.3

# ── Core scientific ──
numpy==1.26.4
opencv-python==4.10.0.84
pillow==12.1.1
pillow-jxl-plugin==1.3.7
matplotlib==3.9.4
pandas==2.3.3

# ── Data & IO ──
huggingface-hub==1.7.2
simple-parsing==0.1.8
pycocotools==2.0.11
pyyaml==6.0.3
natsort==8.4.0
py7zr==1.1.0
einops==0.8.2

# ── Terminal / logging ──
termcolor==3.3.0
colorama==0.4.6

# ── Tier 1 — Annotators (NOT installable via this file) ─────────
# Segmentation inference from within the UI requires:
#   - torch + torchvision (CUDA)
#   - annotators/ sub-codebase modules
#   - Pretrained model weights
#
# KNOWN ISSUE: ui/ui/run_thread.py references modules that don't
# match the current annotator module names:
#   UI expects: annotators.anime_segmentation → actual: annotators.animeinsseg
#   UI expects: annotators.sam               → actual: annotators.lang_sam.models.sam
# See UI_TEST_REPORT.md for details.
```

--------------------------------

### Install lang_sam dependencies

Source: https://github.com/shitagaki-lab/see-through/blob/main/annotators/lang_sam/README.md

Install the package's own requirements.txt, which builds SAM2 and takes several minutes.

```bash
pip install -r requirements.txt
```
