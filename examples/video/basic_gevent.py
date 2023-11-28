#
# This file is part of the linuxpy project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

import argparse
import logging
import time

import gevent

from linuxpy.io import GeventIO
from linuxpy.video.device import Device


def loop(variable):
    while True:
        gevent.sleep(0.1)
        variable[0] += 1


def run(device):
    data = [0]
    gevent.spawn(loop, data)

    with device as stream:
        start = last = time.monotonic()
        last_update = 0
        for frame in stream:
            new = time.monotonic()
            fps, last = 1 / (new - last), new
            if new - last_update > 0.1:
                elapsed = new - start
                print(
                    f"frame {frame.frame_nb:04d} {len(frame)/1000:.1f} Kb at {fps:.1f} fps ; "
                    f"data={data[0]}; {elapsed=:.2f} s;",
                    end="\r",
                )
                last_update = new


def device_text(text):
    try:
        return Device.from_id(int(text), io=GeventIO)
    except ValueError:
        return Device(text, io=GeventIO)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-level", choices=["debug", "info", "warning", "error"], default="info")
    parser.add_argument("device", type=device_text)
    return parser


def main(args=None):
    parser = cli()
    args = parser.parse_args(args=args)
    fmt = "%(threadName)-10s %(asctime)-15s %(levelname)-5s %(name)s: %(message)s"
    logging.basicConfig(level=args.log_level.upper(), format=fmt)

    try:
        run(args.device)
    except KeyboardInterrupt:
        logging.info("Ctrl-C pressed. Bailing out")


if __name__ == "__main__":
    main()
