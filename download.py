import requests
import json
import os
from qbittorrent import Client

keyword = 'sunshine'
download_uri = 'https://torrents.ohys.net/download/'
uri = '{0}/json.php?dir=new&q={1}'.format(download_uri, keyword)
req = requests.get(uri)

d = json.loads(req.text[req.text.index('['):])

torrent_path = 'torrent/' + d[0]['t']

if not os.path.exists(torrent_path):
    torrent_req = requests.get(download_uri+d[0]['a'], stream=True)

    with open(torrent_path, 'wb') as torrent:
        for chunk in torrent_req.iter_content(chunk_size=128):
            torrent.write(chunk)

    qb = Client('http://127.0.0.1:8080/')
    # not required when 'Bypass from localhost' setting is active.
    # defaults to admin:admin.
    # to use defaults, just do qb.login()
    dl_path = 'D:\\maxto\\Videos\\러브라이브\\Aqours\\2기'

    with open(torrent_path, 'rb') as torrent:
        qb.download_from_file(torrent, savepath=dl_path)
