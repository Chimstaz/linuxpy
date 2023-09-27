#
# This file is part of the python-linux project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

import collections
import ctypes
import struct


i8 = ctypes.c_int8
i16 = ctypes.c_int16
i32 = ctypes.c_int32
i64 = ctypes.c_int64

u8 = ctypes.c_uint8
u16 = ctypes.c_uint16
u32 = ctypes.c_uint32
u64 = ctypes.c_uint64


cint = ctypes.c_int
cuint = ctypes.c_uint
cchar = ctypes.c_char

cenum = cuint
cvoidp = ctypes.c_void_p

sizeof = ctypes.sizeof

calcsize = struct.calcsize

Union = ctypes.Union

POINTER = ctypes.POINTER

create_string_buffer = ctypes.create_string_buffer
cast = ctypes.cast


class Struct(ctypes.Structure):
    def __repr__(self):
        name = type(self).__name__
        fields = ", ".join(
            (
                "{}={}".format(field[0], getattr(self, field[0]))
                for field in self._fields_
            )
        )
        return f"{name}()"

    def __iter__(self):
        for fname, _ in self._fields_:
            yield getattr(self, fname)

    def asdict(self):
        r = collections.OrderedDict()
        for field_name, _ in self._fields_:
            r[field_name] = getattr(self, field_name)
        return r


class timeval(Struct):
    _fields_ = [
        ("secs", ctypes.c_long),
        ("usecs", ctypes.c_long),
    ]


class timespec(Struct):
    _fields_ = [
        ("secs", ctypes.c_long),
        ("nsecs", ctypes.c_long),
    ]