# QUASI_STABLE

CODEFEST AD ASTRA 2023 library for object detection from aerial images and NER f. 

## Members

- DIEGO RAMIREZ GARRIDO
- ISAAC DAVID BERMUDEZ LARA
- JUAN JOSE MEJIA ALVAREZ
- SANTIAGO MORALES DUARTE

## Object detection

We used the [mmrotate](https://github.com/open-mmlab/mmrotate/) state-of-the-art library for rotated object recognition. Here's a [mmrotate](https://github.com/open-mmlab/mmrotate/) recognition sample:

https://user-images.githubusercontent.com/10410257/154433305-416d129b-60c8-44c7-9ebb-5ba106d3e9d5.MP4

The master branch works with **PyTorch 1.8**.

We trained a model with 4 videos of aerial data provided by the Colombian Air Force. We expanded the video dataset with [aerial-cars-dataset](https://github.com/jekhor/aerial-cars-dataset) to detect vehicles and we finetuned a detector using a pre-trained [model](https://github.com/open-mmlab/mmrotate/blob/main/configs/oriented_rcnn/oriented_rcnn_r50_fpn_1x_dota_le90.py). We upload a trained model which detects vehicles and constructions, we provide the config and checkpoint files. Here's a sample of the model recognition capabilities: 

## EasyOCR

## NER

## Usage

This can be used as a library or can be used as an python library or as an CLI.

### Library

You can import video.py and text.py files.

### Video

Available functions

TODO: give a short description of available functions

```python
def detect_objects_in_video(
    video_path: Path, output_path: Path, overwrite: bool = True
) -> None:
```

### Text
Decompress models.zip BEFORE USING THIS PART. Put result inside QUASI_STABLE root folder.
Available functions

TODO: give a short description of available functions

```python
def ner_from_str(text: str, output_path: Path, overwrite: bool = True) -> None:
```

```python
def ner_from_file(text_path: Path, output_path: Path, overwrite: bool = True) -> None:
```

```python
def ner_from_url(url: str, output_path: Path, overwrite: bool = True) -> None:
```

### CLI

```bash
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  process-text
  process-vide
```
