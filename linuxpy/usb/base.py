import enum
import pathlib

from ..ctypes import cuint, pointer, cast, u8, cvoidp, u32
from .. import kernel
from .. import device
from .. import ioctl
from . import raw

USB_DEV_PATH	= pathlib.Path("/dev")
USB_DEV_TMPFS_PATH = USB_DEV_PATH / "bus" / "usb"

DT_DEVICE_SIZE = 18
DT_CONFIG_SIZE = 9
DT_INTERFACE_SIZE = 9
DT_ENDPOINT_SIZE = 7
DT_ENDPOINT_AUDIO_SIZE = 9	# Audio extension
DT_HUB_NONVAR_SIZE = 7
DT_SS_ENDPOINT_COMPANION_SIZE = 6
DT_BOS_SIZE	 = 5
DT_DEVICE_CAPABILITY_SIZE = 3

if kernel.VERSION >= (5, 2, 0):
    MAX_ISO_PACKET = 98304
elif kernel.VERSION >= (3, 10, 0):
    MAX_ISO_PACKET = 49152
else:
    MAX_ISO_PACKET = 8192


class TransferType(enum.IntEnum):
    CONTROL = 0x0
    ISOCHRONOUS = 0x1
    BULK = 0x2
    INTERRUPT = 0x3


def set_configuration(fd, n):
    n = cuint(n)
    return ioctl.ioctl(fd, raw.IOC.SETCONFIGURATION, n)


def claim_interface(fd, n):
    n = cuint(n)
    return ioctl.ioctl(fd, raw.IOC.CLAIMINTERFACE, n)
    

def active_configuration(fd):
    result = u8(0)
    ctrl = raw.usbdevfs_ctrltransfer()
    ctrl.bRequestType = raw.Direction.IN
    ctrl.bRequest = raw.Request.GET_CONFIGURATION
    ctrl.wValue = 0
    ctrl.wIndex = 0
    ctrl.wLength = 1
    ctrl.timeout = 1000
    ctrl.data = cast(pointer(result), cvoidp)
    ioctl.ioctl(fd, raw.IOC.CONTROL, ctrl)
    return result.value


def capabilities(fd):
    caps = u32()
    ioctl.ioctl(fd, raw.IOC.GET_CAPABILITIES, caps)
    return raw.Capability(caps.value)


def speed(fd):
    result = ioctl.ioctl(fd, raw.IOC.GET_SPEED)
    return raw.UsbDeviceSpeed(result)


class BaseDevice(device.BaseDevice):

    def __repr__(self):
        return f"{type(self).__name__}(bus={self.bus_number}, address={self.device_address})"

    @property
    def bus_number(self):
        raise NotImplementedError
    
    @property
    def device_address(self):
        raise NotImplementedError

    @property
    def session_id(self):
        return (self.bus_number << 8) | self.device_address

    @property
    def active_configuration(self):
        return active_configuration(self.fileno())

    @property
    def capabilities(self):
        return capabilities(self.fileno())

    @property
    def speed(self):
        return speed(self.fileno())

    def set_configuration(self, n):
        return set_configuration(self.fileno(), n)

    def claim_interface(self, n):
        return claim_interface(self.fileno(), n)
    
    @classmethod
    def from_address(cls, bus_number, device_address):
        pass