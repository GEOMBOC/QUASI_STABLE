from dataclasses import dataclass, astuple
from pathlib import Path
import ffmpeg
import csv
import shutil
import numpy as np
import pandas as pd
import cv2
import re
from ultralytics import YOLO


HEADER = ["ID", "OBJECT_TYPE", "TIME", "COORDINATES_TEXT"]
MODEL = YOLO("yolov8x.pt")


@dataclass
class VideoRecord:
    id: int
    object_type: str
    time: int
    coordinates_text: str

    @property
    def csv(self):
        return astuple(self)


def extract_time(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def preprocess_video(video: Path, output: Path, overwrite: bool = True):
    """
    transcode to h.264
    and then pass to images

    this takes a loong time
    """
    t = "transcode"

    transcode = output.joinpath(t)

    transcode.mkdir()

    transcode_stream = ffmpeg.input(str(video), an=None)
    transcode_stream = ffmpeg.output(
        transcode_stream, f"{transcode}/out.mp4", vcodec="libx264", vsync="vfr"
    )
    ffmpeg.run(transcode_stream)

    d = "internal"

    internal = output.joinpath(d)

    internal.mkdir()

    toimage_stream = ffmpeg.input(f"{transcode}/out.mp4")
    toimage_stream = ffmpeg.filter(toimage_stream, "fps", fps=1)
    toimage_stream = ffmpeg.output(toimage_stream, f"{internal}/%d.png")
    ffmpeg.run(toimage_stream)

    return {transcode: "short description", internal: "short description"}


def collect_data(file: Path) -> VideoRecord:
    model.train("dataset/video
    results = MODEL(file)
    id = seconds = int(file.stem)

    t = extract_time(seconds)

    image_array = np.array(cv2.imread(str(file)))
    for result in results:
        for box in result.boxes:
            for type, coordinates in zip(box.cls, box.xyxy):
                coordinates = coordinates.detach().cpu().numpy().astype(int)
                sub_image = image_array[
                    coordinates[0] : coordinates[2], coordinates[1] : coordinates[3]
                ]
                
                if (len(sub_image) != 0):
                    cv2.imwrite(f"IMG/{id}.jpg", sub_image)

                return VideoRecord(id, result.names[type.item()], t, 0)


def detect_objects_in_video(video: Path, output: Path, overwrite: bool = True) -> None:
    if not overwrite and output.exists():
        raise Exception(f"{output} already exists!")

    if output.exists():
        shutil.rmtree(output)

    output.mkdir()

    # make computation
    _, internal = preprocess_video(video, output, overwrite)

    result = Path("result.csv")
    result_path = output.joinpath(result)

    IMG = Path("IMG")
    IMG_path = output.joinpath(IMG)

    IMG_path.mkdir()
    # fill IMG_path with images
    # each image has as name the id of the reported object

    with open(result_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        # fill csv file
        # HEADER:
        # <ID>, <OBJECT_TYPE>, <TIME>, <COORDINATES_TEXT>
        for f in internal.iterdir():
            record = collect_data(f)
            writer.writerow(record.csv)
