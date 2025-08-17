# 17175316 - Cavernous Maw

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Meriphataud Mountains [S] (ID: 97) |
| Block Size       | 960 bytes                          |
| Total Events     | 4                                  |
| References Count | 15                                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [102](#event-102)     | 0x0001       |    221 |             33 |
| [103](#event-103)     | 0x00DE       |    218 |             32 |
| [109](#event-109)     | 0x01B8       |    426 |             58 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1B9D      |        7069 |
|       1 | 0x038E      |         910 |
|       2 | 0x1BA0      |        7072 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C8      |         200 |
|       6 | 0x003C      |          60 |
|       7 | 0x0013      |          19 |
|       8 | 0x0155      |         341 |
|       9 | 0x1B9F      |        7071 |
|      10 | 0x00C9      |         201 |
|      11 | 0x1B9E      |        7070 |
|      12 | 0x0B1B      |        2843 |
|      13 | 0x1BAF      |        7087 |
|      14 | 0x0002      |           2 |

## String References

- **7069**: You can feel the warm, moist breath of the maw on your skin.
- **7070**: An unseen force is drawing you towards the maw.
- **7071**: A portal has opened within the depths of the maw.
- **7072**: Raise your $3? [Yes./No.]
- **7087**: To where will you head? [[The past/The present]./Walk of Echoes./Nowhere for now.]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 102

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 221 bytes |
| Instructions | 33        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 48 00 80 23 03  02 10 01 80 24 02 80 03    .H..#.....$...
0010: 80 04 80 25 02 00 10 04  80 00 CF 00 43 00 43 01  ...%........C.C.
0020: 42 46 01 03 01 10 03 80  45 05 80 F0 FF FF 7F F0  BF......E.......
0030: FF FF 7F 66 64 6F 31 04  80 1C 06 80 38 07 80 29  ...fdo1.....8..)
0040: 01 F0 FF FF 7F 03 45 08  80 F0 FF FF 7F F0 FF FF  ......E.........
0050: 7F 61 74 31 36 04 80 45  05 80 F0 FF FF 7F F0 FF  .at16..E........
0060: FF 7F 66 64 69 31 04 80  48 09 80 1C 06 80 45 05  ..fdi1..H.....E.
0070: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 6E 04 80 45  .........blon..E
0080: 0A 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 04 80  ..........blon..
0090: 45 05 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 04  E..........ovl1.
00A0: 80 45 08 80 F0 FF FF 7F  F0 FF FF 7F 77 61 72 70  .E..........warp
00B0: 04 80 29 01 F0 FF FF 7F  04 45 05 80 F0 FF FF 7F  ..)......E......
00C0: F0 FF FF 7F 62 6C 6F 66  04 80 46 00 01 DA 00 02  ....blof..F.....
00D0: 00 10 03 80 00 DA 00 01  DA 00 20 00 21 00        .......... .!.  
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x48] [System] [7069*]:
    → "You can feel the warm, moist breath of the maw on your skin."
  2: 0x0006 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0007 [0x03] Work_Zone[2] = 910*
  4: 0x000C [0x24] CREATE_DIALOG(message_id=7072*, default_option=1*, option_flags=0*)
    → "Raise your $3? [Yes./No.]"
  5: 0x0013 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0014 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00CF
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0020 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0021 [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0023 [0x03] Work_Zone[1] = 1*
 12: 0x0028 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0039 [0x1C] WAIT(60* ticks)
 14: 0x003C [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 15: 0x003F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 16: 0x0046 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at16" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 17: 0x0057 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0068 [0x48] [System] [7071*]:
    → "A portal has opened within the depths of the maw."
 19: 0x006B [0x1C] WAIT(60* ticks)
 20: 0x006E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x007F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 22: 0x0090 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x00A1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 24: 0x00B2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 25: 0x00B9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x00CA [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x00CC [0x01] GOTO 0x00DA
 28: 0x00CF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00DA
 29: 0x00D7 [0x01] GOTO 0x00DA

SUBROUTINE_00DA:
 30: 0x00DA [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 31: 0x00DC [0x21] END_EVENT
 32: 0x00DD [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00DE    |
| Data Size    | 218 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                            20 01                 .
00E0: 48 0B 80 23 03 02 10 01  80 24 02 80 03 80 04 80  H..#.....$......
00F0: 25 02 00 10 04 80 00 A9  01 43 00 43 01 42 46 01  %........C.C.BF.
0100: 03 01 10 03 80 45 05 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0110: 66 64 6F 31 04 80 1C 06  80 38 07 80 29 01 F0 FF  fdo1.....8..)...
0120: FF 7F 03 45 08 80 F0 FF  FF 7F F0 FF FF 7F 61 74  ...E..........at
0130: 31 36 04 80 45 05 80 F0  FF FF 7F F0 FF FF 7F 66  16..E..........f
0140: 64 69 31 04 80 1C 06 80  45 05 80 F0 FF FF 7F F0  di1.....E.......
0150: FF FF 7F 62 6C 6F 6E 04  80 45 0A 80 F0 FF FF 7F  ...blon..E......
0160: F0 FF FF 7F 62 6C 6F 6E  04 80 45 05 80 F0 FF FF  ....blon..E.....
0170: 7F F0 FF FF 7F 6F 76 6C  31 04 80 45 08 80 F0 FF  .....ovl1..E....
0180: FF 7F F0 FF FF 7F 77 61  72 70 04 80 29 01 F0 FF  ......warp..)...
0190: FF 7F 04 45 05 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  ...E..........bl
01A0: 6F 66 04 80 46 00 01 B4  01 02 00 10 03 80 00 B4  of..F...........
01B0: 01 01 B4 01 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x00DE [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00E0 [0x48] [System] [7070*]:
    → "An unseen force is drawing you towards the maw."
  2: 0x00E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00E4 [0x03] Work_Zone[2] = 910*
  4: 0x00E9 [0x24] CREATE_DIALOG(message_id=7072*, default_option=1*, option_flags=0*)
    → "Raise your $3? [Yes./No.]"
  5: 0x00F0 [0x25] WAIT_DIALOG_SELECT()
  6: 0x00F1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01A9
  7: 0x00F9 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x00FB [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x00FD [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x00FE [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0100 [0x03] Work_Zone[1] = 1*
 12: 0x0105 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0116 [0x1C] WAIT(60* ticks)
 14: 0x0119 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 15: 0x011C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 16: 0x0123 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at16" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 17: 0x0134 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0145 [0x1C] WAIT(60* ticks)
 19: 0x0148 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0159 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x016A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x017B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 23: 0x018C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 24: 0x0193 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x01A4 [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x01A6 [0x01] GOTO 0x01B4
 27: 0x01A9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01B4
 28: 0x01B1 [0x01] GOTO 0x01B4

SUBROUTINE_01B4:
 29: 0x01B4 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 30: 0x01B6 [0x21] END_EVENT
 31: 0x01B7 [0x00] END_REQSTACK()
```

### Event 109

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01B8    |
| Data Size    | 426 bytes |
| Instructions | 58        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                          20 01 48 0B 80 23 03 02           .H..#..
01C0: 10 0C 80 24 02 80 03 80  04 80 25 02 00 10 04 80  ...$......%.....
01D0: 00 5E 03 03 02 10 03 80  24 0D 80 0E 80 04 80 25  .^......$......%
01E0: 02 00 10 04 80 00 98 02  43 00 43 01 42 46 01 03  ........C.C.BF..
01F0: 01 10 03 80 45 05 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0200: 64 6F 31 04 80 1C 06 80  38 07 80 29 01 F0 FF FF  do1.....8..)....
0210: 7F 03 45 08 80 F0 FF FF  7F F0 FF FF 7F 61 74 31  ..E..........at1
0220: 36 04 80 45 05 80 F0 FF  FF 7F F0 FF FF 7F 66 64  6..E..........fd
0230: 69 31 04 80 1C 06 80 45  05 80 F0 FF FF 7F F0 FF  i1.....E........
0240: FF 7F 62 6C 6F 6E 04 80  45 0A 80 F0 FF FF 7F F0  ..blon..E.......
0250: FF FF 7F 62 6C 6F 6E 04  80 45 05 80 F0 FF FF 7F  ...blon..E......
0260: F0 FF FF 7F 6F 76 6C 31  04 80 45 08 80 F0 FF FF  ....ovl1..E.....
0270: 7F F0 FF FF 7F 77 61 72  70 04 80 29 01 F0 FF FF  .....warp..)....
0280: 7F 04 45 05 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  ..E..........blo
0290: 66 04 80 46 00 01 5B 03  02 00 10 03 80 00 50 03  f..F..[.......P.
02A0: 43 00 43 01 42 46 01 03  01 10 0E 80 45 05 80 F0  C.C.BF......E...
02B0: FF FF 7F F0 FF FF 7F 66  64 6F 31 04 80 1C 06 80  .......fdo1.....
02C0: 38 07 80 29 01 F0 FF FF  7F 03 45 08 80 F0 FF FF  8..)......E.....
02D0: 7F F0 FF FF 7F 61 74 31  36 04 80 45 05 80 F0 FF  .....at16..E....
02E0: FF 7F F0 FF FF 7F 66 64  69 31 04 80 1C 06 80 45  ......fdi1.....E
02F0: 05 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 04 80  ..........blon..
0300: 45 0A 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 04  E..........blon.
0310: 80 45 05 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  .E..........ovl1
0320: 04 80 45 08 80 F0 FF FF  7F F0 FF FF 7F 77 61 72  ..E..........war
0330: 70 04 80 29 01 F0 FF FF  7F 04 45 05 80 F0 FF FF  p..)......E.....
0340: 7F F0 FF FF 7F 62 6C 6F  66 04 80 46 00 01 5B 03  .....blof..F..[.
0350: 02 00 10 03 80 00 5B 03  01 5B 03 01 5E 03 20 00  ......[..[..^. .
0360: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x01B8 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x01BA [0x48] [System] [7070*]:
    → "An unseen force is drawing you towards the maw."
  2: 0x01BD [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01BE [0x03] Work_Zone[2] = 2843*
  4: 0x01C3 [0x24] CREATE_DIALOG(message_id=7072*, default_option=1*, option_flags=0*)
    → "Raise your $3? [Yes./No.]"
  5: 0x01CA [0x25] WAIT_DIALOG_SELECT()
  6: 0x01CB [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x035E
  7: 0x01D3 [0x03] Work_Zone[2] = 1*
  8: 0x01D8 [0x24] CREATE_DIALOG(message_id=7087*, default_option=2*, option_flags=0*)
    → "To where will you head? [[The past/The present]./Walk of Echoes./Nowhere for now.]"
  9: 0x01DF [0x25] WAIT_DIALOG_SELECT()
 10: 0x01E0 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0298
 11: 0x01E8 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x01EA [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x01EC [0x42] SET_CLI_EVENT_CANCEL_DATA()
 14: 0x01ED [0x46] CAMERA_CONTROL: Disable user control
 15: 0x01EF [0x03] Work_Zone[1] = 1*
 16: 0x01F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x0205 [0x1C] WAIT(60* ticks)
 18: 0x0208 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 19: 0x020B [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 20: 0x0212 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at16" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 21: 0x0223 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0234 [0x1C] WAIT(60* ticks)
 23: 0x0237 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x0248 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 25: 0x0259 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x026A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 27: 0x027B [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 28: 0x0282 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 29: 0x0293 [0x46] CAMERA_CONTROL: Restore default settings
 30: 0x0295 [0x01] GOTO 0x035B
 31: 0x0298 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0350
 32: 0x02A0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 33: 0x02A2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 34: 0x02A4 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 35: 0x02A5 [0x46] CAMERA_CONTROL: Disable user control
 36: 0x02A7 [0x03] Work_Zone[1] = 2*
 37: 0x02AC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 38: 0x02BD [0x1C] WAIT(60* ticks)
 39: 0x02C0 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 40: 0x02C3 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 41: 0x02CA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at16" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 42: 0x02DB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 43: 0x02EC [0x1C] WAIT(60* ticks)
 44: 0x02EF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 45: 0x0300 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 46: 0x0311 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 47: 0x0322 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 48: 0x0333 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 49: 0x033A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x034B [0x46] CAMERA_CONTROL: Restore default settings
 51: 0x034D [0x01] GOTO 0x035B
 52: 0x0350 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x035B
 53: 0x0358 [0x01] GOTO 0x035B

SUBROUTINE_035B:
 54: 0x035B [0x01] GOTO 0x035E

SUBROUTINE_035E:
 55: 0x035E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 56: 0x0360 [0x21] END_EVENT
 57: 0x0361 [0x00] END_REQSTACK()
```
