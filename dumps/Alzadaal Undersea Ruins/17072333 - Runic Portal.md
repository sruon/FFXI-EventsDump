# 17072333 - Runic Portal

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Alzadaal Undersea Ruins (ID: 72) |
| Block Size       | 684 bytes                        |
| Total Events     | 3                                |
| References Count | 13                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [118](#event-118)     | 0x0001       |    295 |             37 |
| [122](#event-122)     | 0x0128       |    305 |             41 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C46      |        7238 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x0013      |          19 |
|       6 | 0x00D9      |         217 |
|       7 | 0x0168      |         360 |
|       8 | 0x00C9      |         201 |
|       9 | 0x0078      |         120 |
|      10 | 0x001E      |          30 |
|      11 | 0x1C48      |        7240 |
|      12 | 0x1C4E      |        7246 |

## String References

- **7238**: Use the device? [Yes./No.]
- **7240**: Attuning yourself to this runic portal will open a path to the Chamber of Passage.
- **7246**: <Player> has attuned [himself/herself] to the runic portal, and opened a path from the Nyzul Isle staging point to the Chamber of Passage.

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

### Event 118

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 295 bytes |
| Instructions | 37        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  02 80 25 02 00 10 02 80    .$......%.....
0010: 00 19 01 43 00 43 01 42  46 01 03 01 10 01 80 45  ...C.C.BF......E
0020: 03 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 02 80  ..........fdo1..
0030: 1C 04 80 38 05 80 29 01  F0 FF FF 7F 2C 45 06 80  ...8..).....,E..
0040: F0 FF FF 7F F0 FF FF 7F  7A 37 32 67 02 80 45 03  ........z72g..E.
0050: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 02 80 2D  .........fdi1..-
0060: F8 FF FF 7F F8 FF FF 7F  31 70 62 32 1C 07 80 45  ........1pb2...E
0070: 03 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 02 80  ..........blon..
0080: 45 08 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 02  E..........blon.
0090: 80 45 03 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  .E..........ovl1
00A0: 02 80 45 06 80 F0 FF FF  7F F0 FF FF 7F 7A 37 32  ..E..........z72
00B0: 68 02 80 29 01 F0 FF FF  7F 03 1C 09 80 45 08 80  h..).........E..
00C0: F8 FF FF 7F F8 FF FF 7F  77 68 6F 31 02 80 55 08  ........who1..U.
00D0: 80 F8 FF FF 7F F8 FF FF  7F 77 68 6F 31 45 03 80  .........who1E..
00E0: F8 FF FF 7F F8 FF FF 7F  66 64 6F 30 02 80 1C 0A  ........fdo0....
00F0: 80 30 45 08 80 F8 FF FF  7F F8 FF FF 7F 77 68 69  .0E..........whi
0100: 31 02 80 45 03 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  1..E..........bl
0110: 6F 66 02 80 46 00 01 24  01 02 00 10 01 80 00 24  of..F..$.......$
0120: 01 01 24 01 20 00 21 00                           ..$. .!.        
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7238*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0119
  4: 0x0013 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0015 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x0017 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0018 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x001A [0x03] Work_Zone[1] = 1*
  9: 0x001F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0030 [0x1C] WAIT(60* ticks)
 11: 0x0033 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0036 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x2C)
 13: 0x003D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z72g" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 14: 0x004E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x005F [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 16: 0x006C [0x1C] WAIT(360* ticks)
 17: 0x006F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0080 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 19: 0x0091 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x00A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z72h" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 21: 0x00B3 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 22: 0x00BA [0x1C] WAIT(120* ticks)
 23: 0x00BD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 24: 0x00CE [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 25: 0x00DD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 26: 0x00EE [0x1C] WAIT(30* ticks)
 27: 0x00F1 [0x30] SET_UCOFF_CONTINUE_ZERO()
 28: 0x00F2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 29: 0x0103 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 30: 0x0114 [0x46] CAMERA_CONTROL: Restore default settings
 31: 0x0116 [0x01] GOTO 0x0124
 32: 0x0119 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0124
 33: 0x0121 [0x01] GOTO 0x0124

SUBROUTINE_0124:
 34: 0x0124 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 35: 0x0126 [0x21] END_EVENT
 36: 0x0127 [0x00] END_REQSTACK()
```

### Event 122

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0128    |
| Data Size    | 305 bytes |
| Instructions | 41        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                          20 01 48 0B 80 23 24 00           .H..#$.
0130: 80 01 80 02 80 25 02 00  10 02 80 00 4A 02 43 00  .....%......J.C.
0140: 43 01 42 46 01 03 01 10  01 80 45 03 80 F0 FF FF  C.BF......E.....
0150: 7F F0 FF FF 7F 66 64 6F  31 02 80 1C 04 80 38 05  .....fdo1.....8.
0160: 80 29 01 F0 FF FF 7F 2C  45 06 80 F0 FF FF 7F F0  .).....,E.......
0170: FF FF 7F 7A 37 32 67 02  80 45 03 80 F0 FF FF 7F  ...z72g..E......
0180: F0 FF FF 7F 66 64 69 31  02 80 48 0C 80 1C 04 80  ....fdi1..H.....
0190: 2D F8 FF FF 7F F8 FF FF  7F 31 70 62 32 1C 07 80  -........1pb2...
01A0: 45 03 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 02  E..........blon.
01B0: 80 45 08 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
01C0: 02 80 45 03 80 F0 FF FF  7F F0 FF FF 7F 6F 76 6C  ..E..........ovl
01D0: 31 02 80 45 06 80 F0 FF  FF 7F F0 FF FF 7F 7A 37  1..E..........z7
01E0: 32 68 02 80 29 01 F0 FF  FF 7F 03 1C 09 80 45 08  2h..).........E.
01F0: 80 F8 FF FF 7F F8 FF FF  7F 77 68 6F 31 02 80 55  .........who1..U
0200: 08 80 F8 FF FF 7F F8 FF  FF 7F 77 68 6F 31 45 03  ..........who1E.
0210: 80 F8 FF FF 7F F8 FF FF  7F 66 64 6F 30 02 80 1C  .........fdo0...
0220: 0A 80 30 45 08 80 F8 FF  FF 7F F8 FF FF 7F 77 68  ..0E..........wh
0230: 69 31 02 80 45 03 80 F0  FF FF 7F F0 FF FF 7F 62  i1..E..........b
0240: 6C 6F 66 02 80 46 00 01  55 02 02 00 10 01 80 00  lof..F..U.......
0250: 55 02 01 55 02 20 00 21  00                       U..U. .!.       
```

#### Opcodes

```
  0: 0x0128 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x012A [0x48] [System] [7240*]:
    → "Attuning yourself to this runic portal will open a path to the Chamber of Passage."
  2: 0x012D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x012E [0x24] CREATE_DIALOG(message_id=7238*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  4: 0x0135 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0136 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x024A
  6: 0x013E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x0140 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x0142 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0143 [0x46] CAMERA_CONTROL: Disable user control
 10: 0x0145 [0x03] Work_Zone[1] = 1*
 11: 0x014A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x015B [0x1C] WAIT(60* ticks)
 13: 0x015E [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 14: 0x0161 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x2C)
 15: 0x0168 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z72g" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 16: 0x0179 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x018A [0x48] [System] [7246*]:
    → "<Player> has attuned [himself/herself] to the runic portal, and opened a path from the Nyzul Isle staging point to the Chamber of Passage."
 18: 0x018D [0x1C] WAIT(60* ticks)
 19: 0x0190 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 20: 0x019D [0x1C] WAIT(360* ticks)
 21: 0x01A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x01B1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 23: 0x01C2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x01D3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z72h" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 25: 0x01E4 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 26: 0x01EB [0x1C] WAIT(120* ticks)
 27: 0x01EE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 28: 0x01FF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 29: 0x020E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 30: 0x021F [0x1C] WAIT(30* ticks)
 31: 0x0222 [0x30] SET_UCOFF_CONTINUE_ZERO()
 32: 0x0223 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 33: 0x0234 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 34: 0x0245 [0x46] CAMERA_CONTROL: Restore default settings
 35: 0x0247 [0x01] GOTO 0x0255
 36: 0x024A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0255
 37: 0x0252 [0x01] GOTO 0x0255

SUBROUTINE_0255:
 38: 0x0255 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 39: 0x0257 [0x21] END_EVENT
 40: 0x0258 [0x00] END_REQSTACK()
```
