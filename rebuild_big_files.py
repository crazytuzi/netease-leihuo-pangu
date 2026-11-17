# -*- coding: utf-8 -*-
"""按序拼接分片并自校验（大小 + SHA-256），只写标准库。"""
import hashlib
import os
import sys

TARGETS = [
    {
        "name": '倩女幽魂OL残缺服务端.zip',
        "dir": 'OriginalServerNndClient',
        "parts": 11,
        "size": 905315034,
        "sha256": 'd89e052667363122d46b08323278f4b30be5afab08ab3e07275b8375d268815d',
        "md5": '9228273e3a259f20209e2fabe9229320',
    },
    {
        "name": '倩女幽魂二测客户端安装包-0.9.13.exe',
        "dir": 'OriginalServerNndClient',
        "parts": 10,
        "size": 789100186,
        "sha256": '65efdc9f551c4db44ce58e29ef094f6dfce0b26412bb0c07e4e0db5719b3fe14',
        "md5": '7ecc0223725d1ca55a88c8ba96342b3e',
    },
]

HERE = os.path.dirname(os.path.abspath(__file__))


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    failed = 0
    for t in TARGETS:
        d = os.path.join(HERE, t["dir"])
        out = os.path.join(d, t["name"])
        parts = [os.path.join(d, "%s.part%02d" % (t["name"], i + 1))
                 for i in range(t["parts"])]
        missing = [p for p in parts if not os.path.isfile(p)]
        if missing:
            print("[x] 缺分片: " + missing[0])
            failed += 1
            continue
        tmp = out + ".rebuild"
        with open(tmp, "wb") as w:
            for p in parts:
                with open(p, "rb") as r:
                    for chunk in iter(lambda: r.read(4 * 1024 * 1024), b""):
                        w.write(chunk)
        size_ok = os.path.getsize(tmp) == t["size"]
        sha_ok = sha256_of(tmp) == t["sha256"]
        if size_ok and sha_ok:
            os.replace(tmp, out)
            print("[v] " + t["name"] + " 还原成功，SHA-256 一致")
        else:
            os.remove(tmp)
            print("[x] " + t["name"] + " 校验失败 size_ok=%s sha_ok=%s" % (size_ok, sha_ok))
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
