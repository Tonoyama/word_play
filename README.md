# 聞き返しボット
## インストール

```shell
pip3 install -r requirements.txt
```

### Windows(Python 3.7の場合)

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio で`PyAudio-0.2.11-cp37-cp37m-win_amd64.whl`をダウンロードし、以下を実行すると`PyAudio`がインストールされる。

```shell
python -m pip install .\PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
```

## 実行

Linux:

```shell
python3 main.py
```

Windows:

```shell
python3 -X utf-8 main.py
```