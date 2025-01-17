#
# This file is part of the linuxpy project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

import pathlib

from .base import CEnum, run

HEADERS = [
    "/usr/include/linux/usbdevice_fs.h",
    "/usr/include/linux/usbip.h",
    "/usr/include/linux/usb/ch9.h",
    "/usr/include/linux/usb/ch11.h",
    "/usr/include/linux/usb/video.h",
]


TEMPLATE = """\
#
# This file is part of the linuxpy project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

# This file has been generated by {name}
# Date: {date}
# System: {system}
# Release: {release}
# Version: {version}

import enum

from linuxpy.ioctl import IO as _IO, IOR as _IOR, IOW as _IOW, IOWR as _IOWR
from linuxpy.ctypes import u8, i8, u16, i16, u32, i32, u64, i64, cuint, cint, cchar, cvoidp
from linuxpy.ctypes import Struct, Union, POINTER

{enums_body}


{structs_body}


# Extra structs not found on header files

class usb_hid_descriptor(Struct):
    _fields_ = [
        ("bLength", u8),
        ("bDescriptorType", u8),
        ("bcdHID", u16),
        ("bCountryCode", u8),
        ("bNumDescriptors", u8),
        ("bClassDescriptorType", u8),
        ("wClassDescriptorLength", u16),
    ]


{iocs_body}"""

this_dir = pathlib.Path(__file__).parent

# macros from #define statements
MACRO_ENUMS = [
    CEnum("URBType", "USBDEVFS_URB_TYPE_"),
    CEnum(
        "URB",
        "USBDEVFS_URB_",
        "IntFlag",
        filter=lambda name, _: not name.startswith("USBDEVFS_USB_TYPE_"),
    ),
    CEnum("Capability", "USBDEVFS_CAP_", "IntFlag"),
    CEnum("DisconnectClaim", "USBDEVFS_DISCONNECT_CLAIM_", "IntFlag"),
    CEnum(
        "IOC",
        "USBDEVFS_",
        filter=lambda name, value: "_IO" in value and not name.endswith("32"),
    ),
    CEnum("Direction", "USB_DIR_"),
    CEnum("RequestType", "USB_TYPE_"),
    CEnum("Recipient", "USB_RECIP_"),
    CEnum("Request", "USB_REQ_"),
    CEnum("Device", "USB_DEVICE_"),
    CEnum("Class", "USB_CLASS_"),
    CEnum("Test", "USB_TEST_"),
    CEnum("StatusType", "USB_STATUS_TYPE_"),
    CEnum("EndpointTransferType", "USB_ENDPOINT_XFER_"),
    CEnum("VideoSubClass", "UVC_SC_"),
    CEnum("VideoProtocol", "UVC_PC_PROTOCOL_"),
    CEnum("VideoControl", "UVC_VC_"),
    CEnum("VideoStreaming", "UVC_VS_"),
    CEnum("VideoEndPoint", "UVC_EP_"),
]


this_dir = pathlib.Path(__file__).parent


def main(output=this_dir.parent / "usb" / "raw.py"):
    run(__name__, HEADERS, TEMPLATE, MACRO_ENUMS, output=output)


if __name__ == "__main__":
    main()
