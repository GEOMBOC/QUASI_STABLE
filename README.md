# QUASI_STABLE

CODEFEST AD ASTRA 2023 library for object detection from aerial images and NER f. 

## Members

- DIEGO RAMIREZ GARRIDO
- ISAAC DAVID BERMUDEZ LARA
- JUAN JOSE MEJIA ALVAREZ
- SANTIAGO MORALES DUARTE

## Object detection

We implemented the [mmrotate](https://github.com/mmrotate) library for rotated object recognition.

https://user-images.githubusercontent.com/10410257/154433305-416d129b-60c8-44c7-9ebb-5ba106d3e9d5.MP4

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
