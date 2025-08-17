# 17101322 - Runic Portal

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Caedarva Mire (ID: 79) |
| Block Size       | 684 bytes              |
| Total Events     | 3                      |
| References Count | 13                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [134](#event-134)     | 0x0001       |    298 |             38 |
| [125](#event-125)     | 0x012B       |    305 |             41 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CA6      |        7334 |
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
|      11 | 0x1CA8      |        7336 |
|      12 | 0x1CAC      |        7340 |

## String References

- **7334**: Use the device? [Yes./No.]
- **7336**: Attuning yourself to this runic portal will open a path to the Chamber of Passage.
- **7340**: <Player> has attuned [himself/herself] to the runic portal, and opened a path from the Dvucca Isle staging point to the Chamber of Passage.

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

### Event 134

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 298 bytes |
| Instructions | 38        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  02 80 25 02 00 10 02 80    .$......%.....
0010: 00 1C 01 43 00 43 01 42  46 01 03 01 10 01 80 45  ...C.C.BF......E
0020: 03 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 02 80  ..........fdo1..
0030: 1C 04 80 38 05 80 29 01  F0 FF FF 7F 13 45 06 80  ...8..)......E..
0040: F0 FF FF 7F F0 FF FF 7F  7A 37 39 67 02 80 45 03  ........z79g..E.
0050: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 02 80 1C  .........fdi1...
0060: 04 80 2D F8 FF FF 7F F8  FF FF 7F 31 70 62 32 1C  ..-........1pb2.
0070: 07 80 45 03 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  ..E..........blo
0080: 6E 02 80 45 08 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  n..E..........bl
0090: 6F 6E 02 80 45 03 80 F0  FF FF 7F F0 FF FF 7F 6F  on..E..........o
00A0: 76 6C 31 02 80 45 06 80  F0 FF FF 7F F0 FF FF 7F  vl1..E..........
00B0: 7A 37 39 68 02 80 29 01  F0 FF FF 7F 03 1C 09 80  z79h..).........
00C0: 45 08 80 F8 FF FF 7F F8  FF FF 7F 77 68 6F 31 02  E..........who1.
00D0: 80 55 08 80 F8 FF FF 7F  F8 FF FF 7F 77 68 6F 31  .U..........who1
00E0: 45 03 80 F8 FF FF 7F F8  FF FF 7F 66 64 6F 30 02  E..........fdo0.
00F0: 80 1C 0A 80 30 45 08 80  F8 FF FF 7F F8 FF FF 7F  ....0E..........
0100: 77 68 69 31 02 80 45 03  80 F0 FF FF 7F F0 FF FF  whi1..E.........
0110: 7F 62 6C 6F 66 02 80 46  00 01 27 01 02 00 10 01  .blof..F..'.....
0120: 80 00 27 01 01 27 01 20  00 21 00                 ..'..'. .!.     
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7334*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x011C
  4: 0x0013 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0015 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x0017 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0018 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x001A [0x03] Work_Zone[1] = 1*
  9: 0x001F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0030 [0x1C] WAIT(60* ticks)
 11: 0x0033 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0036 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x13)
 13: 0x003D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z79g" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 14: 0x004E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x005F [0x1C] WAIT(60* ticks)
 16: 0x0062 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 17: 0x006F [0x1C] WAIT(360* ticks)
 18: 0x0072 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0083 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 20: 0x0094 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x00A5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z79h" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 22: 0x00B6 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 23: 0x00BD [0x1C] WAIT(120* ticks)
 24: 0x00C0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 25: 0x00D1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 26: 0x00E0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 27: 0x00F1 [0x1C] WAIT(30* ticks)
 28: 0x00F4 [0x30] SET_UCOFF_CONTINUE_ZERO()
 29: 0x00F5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 30: 0x0106 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x0117 [0x46] CAMERA_CONTROL: Restore default settings
 32: 0x0119 [0x01] GOTO 0x0127
 33: 0x011C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0127
 34: 0x0124 [0x01] GOTO 0x0127

SUBROUTINE_0127:
 35: 0x0127 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 36: 0x0129 [0x21] END_EVENT
 37: 0x012A [0x00] END_REQSTACK()
```

### Event 125

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x012B    |
| Data Size    | 305 bytes |
| Instructions | 41        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   20 01 48 0B 80              .H..
0130: 23 24 00 80 01 80 02 80  25 02 00 10 02 80 00 4D  #$......%......M
0140: 02 43 00 43 01 42 46 01  03 01 10 01 80 45 03 80  .C.C.BF......E..
0150: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 02 80 1C 04  ........fdo1....
0160: 80 38 05 80 29 01 F0 FF  FF 7F 13 45 06 80 F0 FF  .8..)......E....
0170: FF 7F F0 FF FF 7F 7A 37  39 67 02 80 45 03 80 F0  ......z79g..E...
0180: FF FF 7F F0 FF FF 7F 66  64 69 31 02 80 48 0C 80  .......fdi1..H..
0190: 1C 04 80 2D F8 FF FF 7F  F8 FF FF 7F 31 70 62 32  ...-........1pb2
01A0: 1C 07 80 45 03 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  ...E..........bl
01B0: 6F 6E 02 80 45 08 80 F0  FF FF 7F F0 FF FF 7F 62  on..E..........b
01C0: 6C 6F 6E 02 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  lon..E..........
01D0: 6F 76 6C 31 02 80 45 06  80 F0 FF FF 7F F0 FF FF  ovl1..E.........
01E0: 7F 7A 37 39 68 02 80 29  01 F0 FF FF 7F 03 1C 09  .z79h..)........
01F0: 80 45 08 80 F8 FF FF 7F  F8 FF FF 7F 77 68 6F 31  .E..........who1
0200: 02 80 55 08 80 F8 FF FF  7F F8 FF FF 7F 77 68 6F  ..U..........who
0210: 31 45 03 80 F8 FF FF 7F  F8 FF FF 7F 66 64 6F 30  1E..........fdo0
0220: 02 80 1C 0A 80 30 45 08  80 F8 FF FF 7F F8 FF FF  .....0E.........
0230: 7F 77 68 69 31 02 80 45  03 80 F0 FF FF 7F F0 FF  .whi1..E........
0240: FF 7F 62 6C 6F 66 02 80  46 00 01 58 02 02 00 10  ..blof..F..X....
0250: 01 80 00 58 02 01 58 02  20 00 21 00              ...X..X. .!.    
```

#### Opcodes

```
  0: 0x012B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x012D [0x48] [System] [7336*]:
    → "Attuning yourself to this runic portal will open a path to the Chamber of Passage."
  2: 0x0130 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0131 [0x24] CREATE_DIALOG(message_id=7334*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  4: 0x0138 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0139 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x024D
  6: 0x0141 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x0143 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x0145 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0146 [0x46] CAMERA_CONTROL: Disable user control
 10: 0x0148 [0x03] Work_Zone[1] = 1*
 11: 0x014D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x015E [0x1C] WAIT(60* ticks)
 13: 0x0161 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 14: 0x0164 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x13)
 15: 0x016B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z79g" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 16: 0x017C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x018D [0x48] [System] [7340*]:
    → "<Player> has attuned [himself/herself] to the runic portal, and opened a path from the Dvucca Isle staging point to the Chamber of Passage."
 18: 0x0190 [0x1C] WAIT(60* ticks)
 19: 0x0193 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 20: 0x01A0 [0x1C] WAIT(360* ticks)
 21: 0x01A3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x01B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 23: 0x01C5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x01D6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z79h" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 25: 0x01E7 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 26: 0x01EE [0x1C] WAIT(120* ticks)
 27: 0x01F1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 28: 0x0202 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 29: 0x0211 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 30: 0x0222 [0x1C] WAIT(30* ticks)
 31: 0x0225 [0x30] SET_UCOFF_CONTINUE_ZERO()
 32: 0x0226 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 33: 0x0237 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 34: 0x0248 [0x46] CAMERA_CONTROL: Restore default settings
 35: 0x024A [0x01] GOTO 0x0258
 36: 0x024D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0258
 37: 0x0255 [0x01] GOTO 0x0258

SUBROUTINE_0258:
 38: 0x0258 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 39: 0x025A [0x21] END_EVENT
 40: 0x025B [0x00] END_REQSTACK()
```
