from assets.downloader import Downloader
import typer
import requests
from typing import Optional
app = typer.Typer()
Youtube = Downloader(host='host', host_password='''Host_password''', download_path='~/Downloads')

@app.command()
def audio(
  urls:Optional[list[str]] = typer.Option(None, '-l', '--link', help='Url to youtube video/playlist'),
  server:Optional[bool] = typer.Option(False, '-s', '--server', help='Send a web request to pre-configured url using urls as request')
):
  print(server)
  if not server:
    Youtube.download(urls=urls)
  else:
    response = requests.get('http://127.0.0.1:5000/download/nxUpdlgtUzA')
    if response.status_code == 200:
      print(response.json())
    else:
      print(f'Failure: {response.status_code}')
    # print(r.status_code)
    # Send web request to web server
    
    pass

if __name__ == "__main__":
  app()