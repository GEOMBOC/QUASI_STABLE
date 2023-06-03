from dataclasses import dataclass, asdict
from pathlib import Path
from json import dumps
from unidecode import unidecode
from joblib import load
import pandas as pd
import spacy
import requests

segmenter = spacy.load('models/model-best')

@dataclass
class TextRecord:
    text: str
    org: list[str]
    loc: list[str]
    per: list[str]
    dates: list[str]
    misc: list[str]
    impact: str

    @property
    def __dict__(self):
        return asdict(self)

    @property
    def json(self):
        return dumps(self.__dict__)


def ner_from_str(text: str, output_path: Path, overwrite: bool = True) -> None:
    # do computation

    if not overwrite and output_path.exists():
        raise Exception(f"{output_path} already exists!")

    output_path.mkdir()

    # create data class
    erase_test_dataclass = extract_tokens(text,segmenter)

    result = "result.json"
    result_path = output_path.joinpath(result)

    with open(result_path, "w") as f:
        f.write(erase_test_dataclass.json)


def ner_from_file(text_path: Path, output_path: Path, overwrite: bool = True) -> None:
    with open(text_path,'r') as file:
        ner_from_str(file.read(),output_path,overwrite)


def ner_from_url(url: str, output_path: Path, overwrite: bool = True) -> None:
    with requests.get(url) as req:
        ner_from_str(req.text,output_path,overwrite)
    
def classify_text(texto):
    return "DEFORESTACIÓN"

def extract_tokens(texto, model):
    doc = model(texto)
    personas = [str(ent) for ent in doc.ents if ent.label_ == "PER"]
    lugares = [str(ent) for ent in doc.ents if ent.label_ == "LOC"]
    fechas = [str(ent) for ent in doc.ents if ent.label_ == "DATE"]
    cifras = [str(ent) for ent in doc.ents if ent.label_ == "CIFRA"]
    damnificados = [str(ent) for ent in doc.ents if ent.label_ == "TIPO DAMNIFICADO"]
    impacto = [str(ent) for ent in doc.ents if ent.label_ == "IMPACT"]
    organizaciones = [str(ent) for ent in doc.ents if ent.label_ == "ORG"]
    classification = classify_text(texto)
    return TextRecord(
        texto,
        organizaciones,
        lugares,
        personas,
        fechas,
        damnificados + impacto,
        classification
    )