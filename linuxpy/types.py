#
# This file is part of the linuxpy project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

import collections.abc
import os
import pathlib
import typing

if hasattr(typing, "Self"):  # 3.11+
    Self = typing.Self
else:
    import typing_extensions

    Self = typing_extensions.Self

if hasattr(collections.abc, "Buffer"):  # 3.12+
    Buffer = collections.abc.Buffer
else:
    import typing_extensions

    Buffer = typing_extensions.Buffer


Union = typing.Union
PathLike = Union[str, pathlib.Path, os.PathLike]

Iterable = collections.abc.Iterable
Iterator = collections.abc.Iterator
AsyncIterable = collections.abc.AsyncIterable
AsyncIterator = collections.abc.AsyncIterator