#!/usr/bin/python3.10
import yt_dlp
from ytdl.variables import *
import typer, rich, click
from typing import Optional, List, Tuple
import sys
import json
class NaturalOrderGroup(click.Group):
    def list_commands(self, ctx):
        return self.commands.keys()        

workingpath = getcwd()
app = typer.Typer(cls=NaturalOrderGroup, add_completion=False)

#######! AUDIO DOWNLOADER
def download(ydlopts, links):
  for x in links:

    with yt_dlp.YoutubeDL(ydlopts) as ydl:
      # * Set up so that if playlist = NA change download path 
        # info = ydl.extract_info(x, download = False)
        # info = json.dumps(ydl.sanitize_info(info))
        # json_dict = json.loads(info)
        # title = json_dict['title']
        # print(title)
        ydl.download(x)

@app.command()
def audio(
  ytlink: Optional[list[str]] = typer.Option(None, '-l', '--link'),
  incognito: bool = typer.Option(False, '-i', '--incognito'),
  ):
  if incognito:
    print('Running incognito')
    download(ydl_optsIAA, ytlink)
  else:
    download(ydl_optsA, ytlink)

#######! VIDEO DOWNLOADER
@app.command()
def video(
  ytlink: Optional[list[str]] = typer.Option(None, '-l', '--link'),
  incognito: bool = typer.Option(False, '-i', '--incognito')
):
  if incognito:
    print('Running incognito')
    download(ydl_optsIVA, ytlink)
  else:
    download(ydl_optsV, ytlink)

if __name__ == "__main__":
  app()