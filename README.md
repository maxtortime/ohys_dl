# Ohys-Raws 자동 다운로드 프로그램

**본 프로그램을 사용하여 발생하는 모든 문제는 저작자가 책임지지 않습니다.**

ohys 토렌트와 파일을 qbittorent를 이용해 애니메이션의 최신화를 다운로드하는 파이썬 스크립트입니다.

## 사용법
- Python 3.5+, qbittorrent 설치
- pip를 이용해 `requests`, `python-qbittorrent` 설치
- `download.py`의 `keyword` 변수에 자신이 주기적으로 다운로드할 애니메이션만 검색할 단어를 적절히 넣는다.
- `dl_path`에 애니가 다운로드될 경로를 넣는다.
- `download.py`가 있는 디렉토리에 `torrent` 디렉토리 만들기.
- `download.py`가 실행되기 전 반드시 qbittorent가 켜져 있어야 함.
- 이미 최신 화의 토렌트가 `torrent` 파일에 있으면 아무 일도 하지 않음
- 따라서 자신이 볼 애니메이션의 최신화가 올라올 적절한 시간에 맞추어 `download.py`를 실행할 것.
