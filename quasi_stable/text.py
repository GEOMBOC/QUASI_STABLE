from dataclasses import dataclass, asdict
from pathlib import Path
from json import dumps
import spacy
import requests
import shutil

MODEL = spacy.load("models/text-model")


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


def named_entity_recognition(text: str, model) -> TextRecord:
    result = model(text)

    organizations = [str(ent) for ent in result.ents if ent.label_ == "ORG"]
    locations = [str(ent) for ent in result.ents if ent.label_ == "LOC"]
    people = [str(ent) for ent in result.ents if ent.label_ == "PER"]
    dates = [str(ent) for ent in result.ents if ent.label_ == "DATE"]
    misc = [
        str(ent)
        for ent in result.ents
        if ent.label_ in ("MISC", "CIFRA VICTIMAS", "TIPO DAMNIFICADOS")
    ]
    impact = [str(ent) for ent in result.ents if ent.label_ == "IMPACT"]
    return TextRecord(text, organizations, locations, people, dates, misc, impact)


def ner_from_str(text: str, output: Path, overwrite: bool = True) -> None:
    if not overwrite and output.exists():
        raise Exception(f"{output} already exists!")

    if output.exists():
        shutil.rmtree(output)

    output.mkdir()

    text_record = named_entity_recognition(text, MODEL)

    result = "result.json"
    result_path = output.joinpath(result)

    with open(result_path, "w") as f:
        f.write(text_record.json)


def ner_from_file(text: Path, output: Path, overwrite: bool = True) -> None:
    with open(text, "r") as file:
        ner_from_str(file.read(), output, overwrite)


def ner_from_url(url: str, output: Path, overwrite: bool = True) -> None:
    with requests.get(url) as r:
        ner_from_str(r.text, output, overwrite)
