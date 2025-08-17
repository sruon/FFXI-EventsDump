# 17768485 - Transporter

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 332 bytes               |
| Total Events     | 4                       |
| References Count | 7                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [83](#event-83)       | 0x0001       |     78 |             18 |
| [84](#event-84)       | 0x004F       |     96 |             22 |
| [85](#event-85)       | 0x00AF       |     94 |             21 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0050      |          80 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x01AA      |         426 |
|       6 | 0x0002      |           2 |

## String References

- **80**: Do you want to warp to the first floor? [Yes./Not now.]

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

### Event 83

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 78 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 24 00 80 01  80 01 80 25 02 00 10 01    .B$......%....
0010: 80 00 40 00 13 00 00 02  80 02 00 00 01 80 80 2B  ..@............+
0020: 00 29 0D 25 20 0F 01 02  01 3D 00 02 00 00 02 80  .).% ....=......
0030: 80 3D 00 29 0D 25 20 0F  01 03 01 3D 00 01 4B 00  .=.).% ....=..K.
0040: 02 00 10 02 80 00 4B 00  01 4B 00 20 00 21 00     ......K..K. .!. 
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x24] CREATE_DIALOG(message_id=80*, default_option=0*, option_flags=0*)
    → "Do you want to warp to the first floor? [Yes./Not now.]"
  3: 0x000B [0x25] WAIT_DIALOG_SELECT()
  4: 0x000C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0040
  5: 0x0014 [0x13] ExtData[1]->WorkLocal[0] = rand() % 1*
  6: 0x0019 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x002B
  7: 0x0021 [0x29] REQ_SET_WAIT(priority=0x0D, entity_id=Transporter (ID: 17768485/0x010F2025), tag_num=0x02)
  8: 0x0028 [0x01] GOTO 0x003D
  9: 0x002B [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x003D
 10: 0x0033 [0x29] REQ_SET_WAIT(priority=0x0D, entity_id=Transporter (ID: 17768485/0x010F2025), tag_num=0x03)
 11: 0x003A [0x01] GOTO 0x003D

SUBROUTINE_003D:
 12: 0x003D [0x01] GOTO 0x004B
 13: 0x0040 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004B
 14: 0x0048 [0x01] GOTO 0x004B

SUBROUTINE_004B:
 15: 0x004B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x004D [0x21] END_EVENT
 17: 0x004E [0x00] END_REQSTACK()
```

### Event 84

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 96 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               20                  
0050: 01 42 62 02 80 F0 FF FF  7F F0 FF FF 7F 6D 61 69  .Bb..........mai
0060: 6E 01 80 45 03 80 F0 FF  FF 7F F0 FF FF 7F 66 64  n..E..........fd
0070: 6F 31 01 80 1C 04 80 29  0B F0 FF FF 7F 15 75 00  o1.....)......u.
0080: 05 80 75 01 75 02 45 03  80 F0 FF FF 7F F0 FF FF  ..u.u.E.........
0090: 7F 66 64 69 31 01 80 62  06 80 F0 FF FF 7F F0 FF  .fdi1..b........
00A0: FF 7F 6D 61 69 6E 01 80  1C 04 80 20 00 21 00     ..main..... .!. 
```

#### Opcodes

```
  0: 0x004F [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0051 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0052 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  3: 0x0063 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0074 [0x1C] WAIT(60* ticks)
  5: 0x0077 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x15)
  6: 0x007E [0x75] LOAD_ROOM(Load indoor room, room=426*)
  7: 0x0082 [0x75] LOAD_ROOM(No action)
  8: 0x0084 [0x75] LOAD_ROOM(Change sub-map, room=0x0345)
  9: 0x0088 [0x80] LOAD_WAIT(entity=LocalPlayer)
 10: 0x008D [0xF0] UNKNOWN_OPCODE_0xF0
 11: 0x008E [0xFF] UNKNOWN_OPCODE_0xFF
 12: 0x008F [0xFF] UNKNOWN_OPCODE_0xFF
 13: 0x0090 [0x7F] WAIT_DIALOG_SELECT_ALT()
 14: 0x0091 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler 0xFFF07FFF with entities [Unknown NPC (ID: 1652556081/0x62800131), Unknown NPC (ID: 4293951494/0xFFF08006)], work=0x6964
 15: 0x00A0 [0xFF] UNKNOWN_OPCODE_0xFF
 16: 0x00A1 [0x7F] WAIT_DIALOG_SELECT_ALT()
 17: 0x00A2 [0x6D] DEPRECATED_OPCODE(unused1=0x6961, unused2=0x016E, unused3=0x1C80)
 18: 0x00A9 [0x04] DEPRECATED_NOP(unused=0x2080)
 19: 0x00AC [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00AD [0x21] END_EVENT
     0x00AE [0x00] END_REQSTACK()
```

### Event 85

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 94 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               42                 B
00B0: 62 02 80 F0 FF FF 7F F0  FF FF 7F 6D 61 69 6E 01  b..........main.
00C0: 80 45 03 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
00D0: 01 80 1C 04 80 29 0B F0  FF FF 7F 16 75 00 05 80  .....)......u...
00E0: 75 01 75 02 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  u.u.E..........f
00F0: 64 69 31 01 80 62 06 80  F0 FF FF 7F F0 FF FF 7F  di1..b..........
0100: 6D 61 69 6E 01 80 1C 04  80 20 00 21 00           main..... .!.   
```

#### Opcodes

```
  0: 0x00AF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00B0 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  2: 0x00C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x00D2 [0x1C] WAIT(60* ticks)
  4: 0x00D5 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x16)
  5: 0x00DC [0x75] LOAD_ROOM(Load indoor room, room=426*)
  6: 0x00E0 [0x75] LOAD_ROOM(No action)
  7: 0x00E2 [0x75] LOAD_ROOM(Change sub-map, room=0x0345)
  8: 0x00E6 [0x80] LOAD_WAIT(entity=LocalPlayer)
  9: 0x00EB [0xF0] UNKNOWN_OPCODE_0xF0
 10: 0x00EC [0xFF] UNKNOWN_OPCODE_0xFF
 11: 0x00ED [0xFF] UNKNOWN_OPCODE_0xFF
 12: 0x00EE [0x7F] WAIT_DIALOG_SELECT_ALT()
 13: 0x00EF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler 0xFFF07FFF with entities [Unknown NPC (ID: 1652556081/0x62800131), Unknown NPC (ID: 4293951494/0xFFF08006)], work=0x6964
 14: 0x00FE [0xFF] UNKNOWN_OPCODE_0xFF
 15: 0x00FF [0x7F] WAIT_DIALOG_SELECT_ALT()
 16: 0x0100 [0x6D] DEPRECATED_OPCODE(unused1=0x6961, unused2=0x016E, unused3=0x1C80)
 17: 0x0107 [0x04] DEPRECATED_NOP(unused=0x2080)
 18: 0x010A [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x010B [0x21] END_EVENT
     0x010C [0x00] END_REQSTACK()
```
