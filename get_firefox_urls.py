import os
import json
import sys

import lz4.block

__version__ = "0.1.0"


def get_firefox_urls(mozziladir="~/.mozilla"):
    for parentdir, dirs, files in os.walk(os.path.expanduser(mozziladir)):
        if "recovery.jsonlz4" in files:
            break
    else:
        print("Could not find recovery.jsonlz4 in ~/.mozilla")

    filename = os.path.join(parentdir, "recovery.jsonlz4")

    with open(filename, "rb") as f:
        # the first 8 bytes in recovery.jsonlz4 should contain
        # the string mozLz40
        assert f.read(8) == b"mozLz40\0"
        # after these 8 bytes the file is a lz4 stream
        compressed_data = f.read()

    data = lz4.block.decompress(compressed_data)
    root = json.loads(data.decode("utf-8"))

    for w, window in enumerate(root["windows"]):
        for t, tab in enumerate(window["tabs"]):
            yield w, t, tab["entries"][tab["index"]-1]["url"]


def main():
    for w, t, url in get_firefox_urls():
        print("window %d tab %d: %s" % (w, t, url))
