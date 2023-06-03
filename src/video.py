from dataclasses import dataclass, astuple
from pathlib import Path
import csv


HEADER = ["ID", "OBJECT_TYPE", "TIME", "COORDINATES_TEXT"]


@dataclass
class VideoRecord:
    id: int
    object_type: str
    time: int
    coordinates_text: str

    @property
    def csv(self):
        return astuple(self.__dict__)


def detect_objects_in_video(
    video_path: Path, output_path: Path, overwrite: bool = True
) -> None:
    # make computation

    if not overwrite and output_path.exists():
        raise Exception(f"{output_path} already exists!")

    output_path.mkdir()

    result = Path("result.csv")
    result_path = output_path.joinpath(result)

    with open(result_path, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(HEADER)
        # fill csv file
        # HEADER:
        # <ID>, <OBJECT_TYPE>, <TIME>, <COORDINATES_TEXT>
        sample_video_record_erase = VideoRecord(1, "a", 2, "b")
        writer.writerow(sample_video_record_erase.csv)

    IMG = Path("IMG")
    IMG_path = output_path.joinpath(IMG)

    IMG_path.mkdir()
    # fill IMG_path with images
    # each image has as name the id of the reported object
