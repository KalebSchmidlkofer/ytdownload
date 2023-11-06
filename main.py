#!/usr/bin/python3.10
from ytdl.variables import youtube, VIDEO, AUDIO
import typer
from typing import Optional

# class NaturalOrderGroup(click.Group):
  # def list_commands(self, ctx):
    # return self.commands.keys()

app = typer.Typer()

AUDIO_QUALITY = [64, 128, 256, 320]
VIDEO_QUALITY = [144, 240, 360, 480, 720, 1080]

# AUDIO DOWNLOADER
  

@app.command()
def audio(
  link: Optional[list[str]] = typer.Option(None, '-l', '--link', help='Url to a youtube video'),
  incognito: bool = typer.Option(False, '-i', '--incognito', help="Doesn't write to archive file"),
  quality: Optional[int] = typer.Option(None, '-q', '--quality', help='Choose the quality of the audio(Defaults to best)')
  ):
  youtube.quality_check(quality, AUDIO_QUALITY)
  if not incognito:
    youtube.download(AUDIO.DEFAULT, link, quality)
  else:
    print('Running incognito')
    youtube.download(AUDIO.INCOGNITO, link, quality)


# VIDEO DOWNLOADER
@app.command()
def video(
  link: Optional[list[str]] = typer.Option(None, '-l', '--link', help='Url to a youtube video'),
  incognito: bool = typer.Option(False, '-i', '--incognito', help="Doesn't write to archive file"),
  quality: Optional[int] = typer.Option(None, '-q', '--quality', help='Choose the quality of the Video(Defaults to best)')
):
  youtube.quality_check(quality, VIDEO_QUALITY)
  if not incognito:
    youtube.download(VIDEO.DEFAULT, link, quality)
  else:
    print('Running incognito')
    youtube.download(VIDEO.INCOGNITO, link, quality)


if __name__ == "__main__":
  app()