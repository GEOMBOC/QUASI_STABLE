import click
from video import detect_objects_in_video
from text import ner_from_str, ner_from_file, ner_from_url
from pathlib import Path


@click.group()
def cli():
    pass


@click.command()
@click.option("-f", "overwrite", flag_value=True, help="Overwrite")
def process_video(overwrite):
    video_path = click.prompt("Enter video path", type=str)
    v = Path(video_path)
    output_path = click.prompt("Enter output path", type=str)
    o = Path(output_path)

    detect_objects_in_video(v, o, overwrite)


@click.command()
@click.argument("mode")
@click.option("-f", "overwrite", flag_value=True, help="Overwrite")
def process_text(mode: str, overwrite) -> None:
    if mode == "str":
        s = click.prompt("Enter string", type=str)
        output_path = click.prompt("Enter output path", type=str)
        o = Path(output_path)
        ner_from_str(str, o, overwrite)
    elif mode == "file":
        file_path = click.prompt("Enter file path", type=str)
        f = Path(file_path)
        output_path = click.prompt("Enter output path", type=str)
        o = Path(output_path)
        ner_from_file(f, o, overwrite)
    elif mode == "url":
        url = click.prompt("Enter url", type=str)
        output_path = click.prompt("Enter output path", type=str)
        o = Path(output_path)
        ner_from_url(str, o, overwrite)
    else:
        raise click.ClickException("Mode can be -> str|file|url")


cli.add_command(process_video)
cli.add_command(process_text)

if __name__ == "__main__":
    cli()
