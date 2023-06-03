from dataclasses import dataclass, asdict
from pathlib import Path
from json import dumps


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
    erase_test_dataclass = TextRecord(
        "aa", ["-"], ["--"], ["*"], ["**"], ["11"], "lala"
    )

    result = "result.json"
    result_path = output_path.joinpath(result)

    with open(result_path, "w") as f:
        f.write(erase_test_dataclass.json)


def ner_from_file(text_path: Path, output_path: Path, overwrite: bool = True) -> None:
    # do computation

    if not overwrite and output_path.exists():
        raise Exception(f"{output_path} already exists!")

    output_path.mkdir()

    # create data class
    erase_test_dataclass = TextRecord(
        "aa", ["-"], ["--"], ["*"], ["**"], ["11"], "lala"
    )

    result = "result.json"
    result_path = output_path.joinpath(result)

    with open(result_path, "w") as f:
        f.write(erase_test_dataclass.json)


def ner_from_url(url: str, output_path: Path, overwrite: bool = True) -> None:
    # do computation

    if not overwrite and output_path.exists():
        raise Exception(f"{output_path} already exists!")

    output_path.mkdir()

    # create data class
    erase_test_dataclass = TextRecord(
        "aa", ["-"], ["--"], ["*"], ["**"], ["11"], "lala"
    )

    result = "result.json"
    result_path = output_path.joinpath(result)

    with open(result_path, "w") as f:
        f.write(erase_test_dataclass.json)
