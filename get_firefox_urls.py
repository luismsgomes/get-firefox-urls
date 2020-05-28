import os
import json
import sys

import lz4.block

__version__ = "0.1.2"


def get_firefox_urls(firefoxdir=os.path.expanduser("~/.mozilla/firefox")):
    with os.scandir(firefoxdir) as entries:
        for entry in entries:
            if not entry.name.startswith('.') and entry.is_dir():
                yield from get_firefox_urls_from_profile(
                    os.path.join(firefoxdir, entry.name)
                )


def get_firefox_urls_from_profile(profiledir):
    filename = os.path.join(profiledir, "sessionstore-backups", "recovery.jsonlz4")
    if not os.path.exists(filename):
        return
    profile_hash, _, profile_name = os.path.basename(profiledir).partition(".")
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
            url = tab["entries"][tab["index"]-1]["url"]
            yield profile_name, w, t, url


def main():
    for p, w, t, url in get_firefox_urls():
        print("profile %s; window %d; tab %d: %s" % (p, w, t, url))
