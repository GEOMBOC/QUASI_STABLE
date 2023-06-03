from dataclasses import dataclass, astuple
from pathlib import Path
import ffmpeg
import csv
import shutil
from ultralytics import YOLO


HEADER = ["ID", "OBJECT_TYPE", "TIME", "COORDINATES_TEXT"]


@dataclass
class VideoRecord:
    id: int
    object_type: str
    time: int
    coordinates_text: str

    @property
    def csv(self):
        return astuple(self)


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

    toimage_stream = ffmpeg.input(str(video))
    toimage_stream = ffmpeg.filter(toimage_stream, "fps", fps=1)
    toimage_stream = ffmpeg.output(toimage_stream, f"{internal}/%04d.png")
    ffmpeg.run(toimage_stream)


def detect_objects_in_video(video: Path, output: Path, overwrite: bool = True) -> None:
    if not overwrite and output.exists():
        raise Exception(f"{output} already exists!")

    if output.exists():
        shutil.rmtree(output)

    output.mkdir()

    # make computation
    preprocess_video(video, output, overwrite)

    result = Path("result.csv")
    result_path = output.joinpath(result)

    with open(result_path, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(HEADER)
        # fill csv file
        # HEADER:
        # <ID>, <OBJECT_TYPE>, <TIME>, <COORDINATES_TEXT>
        sample_video_record_erase = VideoRecord(1, "a", 2, "b")
        writer.writerow(sample_video_record_erase.csv)

    IMG = Path("IMG")
    IMG_path = output.joinpath(IMG)

    IMG_path.mkdir()
    # fill IMG_path with images
    # each image has as name the id of the reported object
