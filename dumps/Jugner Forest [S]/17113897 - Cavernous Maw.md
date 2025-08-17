# 17113897 - Cavernous Maw

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 1188 bytes                 |
| Total Events     | 4                          |
| References Count | 17                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [101](#event-101)     | 0x0001       |    221 |             33 |
| [102](#event-102)     | 0x00DE       |    291 |             39 |
| [9](#event-9)         | 0x0201       |    572 |             72 |

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
|      12 | 0x0078      |         120 |
|      13 | 0x001E      |          30 |
|      14 | 0x0B1B      |        2843 |
|      15 | 0x1BAF      |        7087 |
|      16 | 0x0002      |           2 |

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

### Event 101

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
0050: 7F 61 74 30 34 04 80 45  05 80 F0 FF FF 7F F0 FF  .at04..E........
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
 16: 0x0046 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at04" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
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

### Event 102

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00DE    |
| Data Size    | 291 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                            20 01                 .
00E0: 48 0B 80 23 03 02 10 01  80 24 02 80 03 80 04 80  H..#.....$......
00F0: 25 02 00 10 04 80 00 F2  01 43 00 43 01 42 46 01  %........C.C.BF.
0100: 03 01 10 03 80 45 05 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0110: 66 64 6F 31 04 80 1C 06  80 38 07 80 29 01 F0 FF  fdo1.....8..)...
0120: FF 7F 03 45 08 80 F0 FF  FF 7F F0 FF FF 7F 61 74  ...E..........at
0130: 30 34 04 80 45 05 80 F0  FF FF 7F F0 FF FF 7F 66  04..E..........f
0140: 64 69 31 04 80 1C 06 80  45 05 80 F0 FF FF 7F F0  di1.....E.......
0150: FF FF 7F 62 6C 6F 6E 04  80 45 0A 80 F0 FF FF 7F  ...blon..E......
0160: F0 FF FF 7F 62 6C 6F 6E  04 80 45 05 80 F0 FF FF  ....blon..E.....
0170: 7F F0 FF FF 7F 6F 76 6C  31 04 80 45 08 80 F0 FF  .....ovl1..E....
0180: FF 7F F0 FF FF 7F 77 61  72 70 04 80 29 01 F0 FF  ......warp..)...
0190: FF 7F 04 1C 0C 80 45 0A  80 F8 FF FF 7F F8 FF FF  ......E.........
01A0: 7F 77 68 6F 31 04 80 55  0A 80 F8 FF FF 7F F8 FF  .who1..U........
01B0: FF 7F 77 68 6F 31 45 05  80 F8 FF FF 7F F8 FF FF  ..who1E.........
01C0: 7F 66 64 6F 30 04 80 1C  0D 80 30 45 0A 80 F8 FF  .fdo0.....0E....
01D0: FF 7F F8 FF FF 7F 77 68  69 31 04 80 45 05 80 F0  ......whi1..E...
01E0: FF FF 7F F0 FF FF 7F 62  6C 6F 66 04 80 46 00 01  .......blof..F..
01F0: FD 01 02 00 10 03 80 00  FD 01 01 FD 01 20 00 21  ............. .!
0200: 00                                                .               
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
  6: 0x00F1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01F2
  7: 0x00F9 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x00FB [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x00FD [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x00FE [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0100 [0x03] Work_Zone[1] = 1*
 12: 0x0105 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0116 [0x1C] WAIT(60* ticks)
 14: 0x0119 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 15: 0x011C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 16: 0x0123 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at04" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 17: 0x0134 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0145 [0x1C] WAIT(60* ticks)
 19: 0x0148 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0159 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x016A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x017B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 23: 0x018C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 24: 0x0193 [0x1C] WAIT(120* ticks)
 25: 0x0196 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 26: 0x01A7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 27: 0x01B6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 28: 0x01C7 [0x1C] WAIT(30* ticks)
 29: 0x01CA [0x30] SET_UCOFF_CONTINUE_ZERO()
 30: 0x01CB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 31: 0x01DC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x01ED [0x46] CAMERA_CONTROL: Restore default settings
 33: 0x01EF [0x01] GOTO 0x01FD
 34: 0x01F2 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01FD
 35: 0x01FA [0x01] GOTO 0x01FD

SUBROUTINE_01FD:
 36: 0x01FD [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 37: 0x01FF [0x21] END_EVENT
 38: 0x0200 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0201    |
| Data Size    | 572 bytes |
| Instructions | 72        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:    20 01 48 0B 80 23 03  02 10 0E 80 24 02 80 03    .H..#.....$...
0210: 80 04 80 25 02 00 10 04  80 00 39 04 03 02 10 03  ...%......9.....
0220: 80 24 0F 80 10 80 04 80  25 02 00 10 04 80 00 2A  .$......%......*
0230: 03 43 00 43 01 42 46 01  03 01 10 03 80 45 05 80  .C.C.BF......E..
0240: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 04 80 1C 06  ........fdo1....
0250: 80 38 07 80 29 01 F0 FF  FF 7F 03 45 08 80 F0 FF  .8..)......E....
0260: FF 7F F0 FF FF 7F 61 74  30 34 04 80 45 05 80 F0  ......at04..E...
0270: FF FF 7F F0 FF FF 7F 66  64 69 31 04 80 1C 06 80  .......fdi1.....
0280: 45 05 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 04  E..........blon.
0290: 80 45 0A 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
02A0: 04 80 45 05 80 F0 FF FF  7F F0 FF FF 7F 6F 76 6C  ..E..........ovl
02B0: 31 04 80 45 08 80 F0 FF  FF 7F F0 FF FF 7F 77 61  1..E..........wa
02C0: 72 70 04 80 29 01 F0 FF  FF 7F 04 1C 0C 80 45 0A  rp..).........E.
02D0: 80 F8 FF FF 7F F8 FF FF  7F 77 68 6F 31 04 80 55  .........who1..U
02E0: 0A 80 F8 FF FF 7F F8 FF  FF 7F 77 68 6F 31 45 05  ..........who1E.
02F0: 80 F8 FF FF 7F F8 FF FF  7F 66 64 6F 30 04 80 1C  .........fdo0...
0300: 0D 80 30 45 0A 80 F8 FF  FF 7F F8 FF FF 7F 77 68  ..0E..........wh
0310: 69 31 04 80 45 05 80 F0  FF FF 7F F0 FF FF 7F 62  i1..E..........b
0320: 6C 6F 66 04 80 46 00 01  36 04 02 00 10 03 80 00  lof..F..6.......
0330: 2B 04 43 00 43 01 42 46  01 03 01 10 10 80 45 05  +.C.C.BF......E.
0340: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 04 80 1C  .........fdo1...
0350: 06 80 38 07 80 29 01 F0  FF FF 7F 03 45 08 80 F0  ..8..)......E...
0360: FF FF 7F F0 FF FF 7F 61  74 30 34 04 80 45 05 80  .......at04..E..
0370: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 04 80 1C 06  ........fdi1....
0380: 80 45 05 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
0390: 04 80 45 0A 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  ..E..........blo
03A0: 6E 04 80 45 05 80 F0 FF  FF 7F F0 FF FF 7F 6F 76  n..E..........ov
03B0: 6C 31 04 80 45 08 80 F0  FF FF 7F F0 FF FF 7F 77  l1..E..........w
03C0: 61 72 70 04 80 29 01 F0  FF FF 7F 04 1C 0C 80 45  arp..).........E
03D0: 0A 80 F8 FF FF 7F F8 FF  FF 7F 77 68 6F 31 04 80  ..........who1..
03E0: 55 0A 80 F8 FF FF 7F F8  FF FF 7F 77 68 6F 31 45  U..........who1E
03F0: 05 80 F8 FF FF 7F F8 FF  FF 7F 66 64 6F 30 04 80  ..........fdo0..
0400: 1C 0D 80 30 45 0A 80 F8  FF FF 7F F8 FF FF 7F 77  ...0E..........w
0410: 68 69 31 04 80 45 05 80  F0 FF FF 7F F0 FF FF 7F  hi1..E..........
0420: 62 6C 6F 66 04 80 46 00  01 36 04 02 00 10 03 80  blof..F..6......
0430: 00 36 04 01 36 04 01 39  04 20 00 21 00           .6..6..9. .!.   
```

#### Opcodes

```
  0: 0x0201 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0203 [0x48] [System] [7070*]:
    → "An unseen force is drawing you towards the maw."
  2: 0x0206 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0207 [0x03] Work_Zone[2] = 2843*
  4: 0x020C [0x24] CREATE_DIALOG(message_id=7072*, default_option=1*, option_flags=0*)
    → "Raise your $3? [Yes./No.]"
  5: 0x0213 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0214 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0439
  7: 0x021C [0x03] Work_Zone[2] = 1*
  8: 0x0221 [0x24] CREATE_DIALOG(message_id=7087*, default_option=2*, option_flags=0*)
    → "To where will you head? [[The past/The present]./Walk of Echoes./Nowhere for now.]"
  9: 0x0228 [0x25] WAIT_DIALOG_SELECT()
 10: 0x0229 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x032A
 11: 0x0231 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x0233 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x0235 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 14: 0x0236 [0x46] CAMERA_CONTROL: Disable user control
 15: 0x0238 [0x03] Work_Zone[1] = 1*
 16: 0x023D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x024E [0x1C] WAIT(60* ticks)
 18: 0x0251 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 19: 0x0254 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 20: 0x025B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at04" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 21: 0x026C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x027D [0x1C] WAIT(60* ticks)
 23: 0x0280 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x0291 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 25: 0x02A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x02B3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 27: 0x02C4 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 28: 0x02CB [0x1C] WAIT(120* ticks)
 29: 0x02CE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 30: 0x02DF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 31: 0x02EE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 32: 0x02FF [0x1C] WAIT(30* ticks)
 33: 0x0302 [0x30] SET_UCOFF_CONTINUE_ZERO()
 34: 0x0303 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 35: 0x0314 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 36: 0x0325 [0x46] CAMERA_CONTROL: Restore default settings
 37: 0x0327 [0x01] GOTO 0x0436
 38: 0x032A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x042B
 39: 0x0332 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 40: 0x0334 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 41: 0x0336 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 42: 0x0337 [0x46] CAMERA_CONTROL: Disable user control
 43: 0x0339 [0x03] Work_Zone[1] = 2*
 44: 0x033E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 45: 0x034F [0x1C] WAIT(60* ticks)
 46: 0x0352 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 47: 0x0355 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 48: 0x035C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at04" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 49: 0x036D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x037E [0x1C] WAIT(60* ticks)
 51: 0x0381 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 52: 0x0392 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 53: 0x03A3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 54: 0x03B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 55: 0x03C5 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 56: 0x03CC [0x1C] WAIT(120* ticks)
 57: 0x03CF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 58: 0x03E0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 59: 0x03EF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 60: 0x0400 [0x1C] WAIT(30* ticks)
 61: 0x0403 [0x30] SET_UCOFF_CONTINUE_ZERO()
 62: 0x0404 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 63: 0x0415 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 64: 0x0426 [0x46] CAMERA_CONTROL: Restore default settings
 65: 0x0428 [0x01] GOTO 0x0436
 66: 0x042B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0436
 67: 0x0433 [0x01] GOTO 0x0436

SUBROUTINE_0436:
 68: 0x0436 [0x01] GOTO 0x0439

SUBROUTINE_0439:
 69: 0x0439 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 70: 0x043B [0x21] END_EVENT
 71: 0x043C [0x00] END_REQSTACK()
```
