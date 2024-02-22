# This file is part of the linuxpy project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

# This file has been generated by linuxpy.codegen.usbids
# Date: 2024-02-22 14:09:53.893563
# System: Linux
# Release: 6.5.13-1rodete2-amd64
# Version: #1 SMP PREEMPT_DYNAMIC Debian 6.5.13-1rodete2 (2024-01-11)

klass = {
    0: {"name": "(Defined at Interface level)"},
    1: {
        "children": {
            1: {"name": "Control Device"},
            2: {"name": "Streaming"},
            3: {"name": "MIDI Streaming"},
        },
        "name": "Audio",
    },
    2: {
        "children": {
            1: {"name": "Direct Line"},
            2: {
                "children": {
                    0: {"name": "None"},
                    1: {"name": "AT-commands (v.25ter)"},
                    2: {"name": "AT-commands (PCCA101)"},
                    3: {"name": "AT-commands (PCCA101 + " "wakeup)"},
                    4: {"name": "AT-commands (GSM)"},
                    5: {"name": "AT-commands (3G)"},
                    6: {"name": "AT-commands (CDMA)"},
                    254: {"name": "Defined by command set " "descriptor"},
                    255: {"name": "Vendor Specific (MSFT " "RNDIS?)"},
                },
                "name": "Abstract (modem)",
            },
            3: {"name": "Telephone"},
            4: {"name": "Multi-Channel"},
            5: {"name": "CAPI Control"},
            6: {"name": "Ethernet Networking"},
            7: {"name": "ATM Networking"},
            8: {"name": "Wireless Handset Control"},
            9: {"name": "Device Management"},
            10: {"name": "Mobile Direct Line"},
            11: {"name": "OBEX"},
            12: {
                "children": {7: {"name": "Ethernet Emulation (EEM)"}},
                "name": "Ethernet Emulation",
            },
        },
        "name": "Communications",
    },
    3: {
        "children": {
            0: {
                "children": {
                    0: {"name": "None"},
                    1: {"name": "Keyboard"},
                    2: {"name": "Mouse"},
                },
                "name": "No Subclass",
            },
            1: {
                "children": {
                    0: {"name": "None"},
                    1: {"name": "Keyboard"},
                    2: {"name": "Mouse"},
                },
                "name": "Boot Interface Subclass",
            },
        },
        "name": "Human Interface Device",
    },
    5: {"name": "Physical Interface Device"},
    6: {
        "children": {
            1: {
                "children": {1: {"name": "Picture Transfer Protocol " "(PIMA 15470)"}},
                "name": "Still Image Capture",
            }
        },
        "name": "Imaging",
    },
    7: {
        "children": {
            1: {
                "children": {
                    0: {"name": "Reserved/Undefined"},
                    1: {"name": "Unidirectional"},
                    2: {"name": "Bidirectional"},
                    3: {"name": "IEEE 1284.4 compatible " "bidirectional"},
                    255: {"name": "Vendor Specific"},
                },
                "name": "Printer",
            }
        },
        "name": "Printer",
    },
    8: {
        "children": {
            1: {
                "children": {
                    0: {"name": "Control/Bulk/Interrupt"},
                    1: {"name": "Control/Bulk"},
                    80: {"name": "Bulk-Only"},
                },
                "name": "RBC (typically Flash)",
            },
            2: {"name": "SFF-8020i, MMC-2 (ATAPI)"},
            3: {"name": "QIC-157"},
            4: {
                "children": {
                    0: {"name": "Control/Bulk/Interrupt"},
                    1: {"name": "Control/Bulk"},
                    80: {"name": "Bulk-Only"},
                },
                "name": "Floppy (UFI)",
            },
            5: {"name": "SFF-8070i"},
            6: {
                "children": {
                    0: {"name": "Control/Bulk/Interrupt"},
                    1: {"name": "Control/Bulk"},
                    80: {"name": "Bulk-Only"},
                },
                "name": "SCSI",
            },
        },
        "name": "Mass Storage",
    },
    9: {
        "children": {
            0: {
                "children": {
                    0: {"name": "Full speed (or root) hub"},
                    1: {"name": "Single TT"},
                    2: {"name": "TT per port"},
                },
                "name": "Unused",
            }
        },
        "name": "Hub",
    },
    10: {
        "children": {
            0: {
                "children": {
                    48: {"name": "I.430 ISDN BRI"},
                    49: {"name": "HDLC"},
                    50: {"name": "Transparent"},
                    80: {"name": "Q.921M"},
                    81: {"name": "Q.921"},
                    82: {"name": "Q.921TM"},
                    144: {"name": "V.42bis"},
                    145: {"name": "Q.932 EuroISDN"},
                    146: {"name": "V.120 V.24 rate ISDN"},
                    147: {"name": "CAPI 2.0"},
                    253: {"name": "Host Based Driver"},
                    254: {"name": "CDC PUF"},
                    255: {"name": "Vendor specific"},
                },
                "name": "Unused",
            }
        },
        "name": "CDC Data",
    },
    11: {"name": "Chip/SmartCard"},
    13: {"name": "Content Security"},
    14: {
        "children": {
            0: {"name": "Undefined"},
            1: {"name": "Video Control"},
            2: {"name": "Video Streaming"},
            3: {"name": "Video Interface Collection"},
        },
        "name": "Video",
    },
    15: {"name": "Personal Healthcare"},
    16: {
        "children": {
            1: {"name": "AVData Control"},
            2: {"name": "AVData Video Stream"},
            3: {"name": "AVData Audio Stream"},
        },
        "name": "Audio/Video",
    },
    17: {"name": "Billboard"},
    18: {"name": "Type-C Bridge"},
    19: {"name": "Bulk Display"},
    20: {
        "children": {
            0: {
                "children": {1: {"name": "MCTCP 1.x"}, 2: {"name": "MCTCP 2.x"}},
                "name": "MCTCP Management",
            },
            1: {
                "children": {1: {"name": "MCTCP 1.x"}, 2: {"name": "MCTCP 2.x"}},
                "name": "MCTCP Host",
            },
        },
        "name": "MCTCP over USB",
    },
    60: {"name": "I3C"},
    88: {"children": {66: {"name": "Controller"}}, "name": "Xbox"},
    220: {
        "children": {
            1: {
                "children": {1: {"name": "USB2 Compliance"}},
                "name": "Reprogrammable Diagnostics",
            }
        },
        "name": "Diagnostic",
    },
    224: {
        "children": {
            1: {
                "children": {
                    1: {"name": "Bluetooth"},
                    2: {"name": "Ultra WideBand Radio " "Control"},
                    3: {"name": "RNDIS"},
                },
                "name": "Radio Frequency",
            },
            2: {
                "children": {
                    1: {"name": "Host Wire Adapter " "Control/Data Streaming"},
                    2: {"name": "Device Wire Adapter " "Control/Data Streaming"},
                    3: {"name": "Device Wire Adapter " "Isochronous Streaming"},
                },
                "name": "Wireless USB Wire Adapter",
            },
        },
        "name": "Wireless",
    },
    239: {
        "children": {
            1: {
                "children": {
                    1: {"name": "Microsoft ActiveSync"},
                    2: {"name": "Palm Sync"},
                },
                "name": "?",
            },
            2: {
                "children": {
                    1: {"name": "Interface Association"},
                    2: {"name": "Wire Adapter Multifunction " "Peripheral"},
                },
                "name": "?",
            },
            3: {"children": {1: {"name": "Cable Based Association"}}, "name": "?"},
            5: {"name": "USB3 Vision"},
        },
        "name": "Miscellaneous Device",
    },
    254: {
        "children": {
            1: {"name": "Device Firmware Update"},
            2: {"name": "IRDA Bridge"},
            3: {
                "children": {1: {"name": "TMC"}, 2: {"name": "USB488"}},
                "name": "Test and Measurement",
            },
        },
        "name": "Application Specific Interface",
    },
    255: {
        "children": {
            255: {
                "children": {255: {"name": "Vendor Specific " "Protocol"}},
                "name": "Vendor Specific Subclass",
            }
        },
        "name": "Vendor Specific Class",
    },
}

