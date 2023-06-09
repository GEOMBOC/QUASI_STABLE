# QUASI_STABLE

CODEFEST AD ASTRA 2023 library for object detection from aerial images and NER from news cycles and other sources.  

## Members

- DIEGO RAMIREZ GARRIDO
- ISAAC DAVID BERMUDEZ LARA
- JUAN JOSE MEJIA ALVAREZ
- SANTIAGO MORALES DUARTE
- CD. STIVEN VIVIESCAS

## Object detection

We used the [mmrotate](https://github.com/open-mmlab/mmrotate/) state-of-the-art library for rotated object recognition. Here's a [mmrotate](https://github.com/open-mmlab/mmrotate/) recognition sample:

https://user-images.githubusercontent.com/10410257/154433305-416d129b-60c8-44c7-9ebb-5ba106d3e9d5.MP4

The master branch works with **PyTorch 1.8**.

We trained a model with 4 videos of aerial data provided by the Colombian Air Force. We expanded the video dataset with [aerial-cars-dataset](https://github.com/jekhor/aerial-cars-dataset) to detect vehicles and we finetuned a detector using a pre-trained [model](https://github.com/open-mmlab/mmrotate/blob/main/configs/oriented_rcnn/oriented_rcnn_r50_fpn_1x_dota_le90.py). We upload a trained model which detects vehicles and constructions, we provide the config and checkpoint files. Here's a sample of the model recognition capabilities: 

![sample](https://github.com/GEOMBOC/QUASI_STABLE/blob/main/sample.png)

### EasyOCR

We implement easyocr library to extract dates, times and coordinates shown in the surveillance video. We have applied a pre-processing to the frame that acts as argument to the functions, thereby reducing the computational complexity of the model. 

NOTE: Class-based approach, do not forget to call the proper instance functions before obtaining relevant parameters. 

### Usage

```python
def detect_objects_in_video(
    video_path: Path, output_path: Path, overwrite: bool = True
) -> None:
```
This method generates a csv file with the following structure:

El método debe generar un archivo con el resultado del análisis, en la ruta dada. El formato de este archivo debe ser CSV. Cada fila debe tener la siguiente estructura:
ID, OBJECT_TYPE, TIME, COORDINATES_TEXT
- ID := “ID of the object found”
- OBJECT_TYPE := “Type of object found: VEHICULO, CONSTRUCCIÓN, VIA, OTROS“
- TIME := ”Time of object found: HH:MM:SS (hora militar)”
- COORDINATES_TEXT := ”Coordinate text found in the video when the object was found”
    
## NER

We used the pre-configured spacy library in order to obtain an effective NER model. In order to train the model, we labelled adequate and clean news samples containing relevant entities that are then shown to the user via a JSON file. 

TO ACCESS TRAINED MODEL, GO TO https://drive.google.com/file/d/1egavB44AwGe9ZrpDBaugvuqFTUebaNXD/view?usp=sharing, DOWNLOAD, DECOMPRESS AND POSITION THE FOLDER IN THE PATH SELECTED AT THE BEGGINING OF text.py.

The file has to be decompressed on models/text-model/

### Usage
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


### Library

You can import video.py and ```text.py``` files. This can be used as a library or can be used as an python library or as an CLI. Unzip all files before using. 

### CLI

```bash
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  process-text
  process-vide
```
