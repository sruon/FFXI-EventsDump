# 17801244 - Bhoyu Halpatacco

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 352 bytes        |
| Total Events     | 5                |
| References Count | 12               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [67](#event-67)          | 0x001A       |     29 |             10 |
| [116](#event-116)        | 0x0037       |    211 |             34 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x2706      |        9990 |
|       3 | 0x2707      |        9991 |
|       4 | 0x2708      |        9992 |
|       5 | 0x0001      |           1 |
|       6 | 0x0000      |           0 |
|       7 | 0x0003      |           3 |
|       8 | 0x00C8      |         200 |
|       9 | 0x003C      |          60 |
|      10 | 0x003B      |          59 |
|      11 | 0x0078      |         120 |

## String References

- **9990**: This counter is for departurrres only. The arrivals counter is on the otherrr side.
- **9991**: The prrrice for an airship ride to Jeuno is $1 gil.
- **9992**: Board the airship? [Yes./Not yet.]

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 67

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 29 08 1C A0 0F 01 01  1D 02 80 23 29 08 1C A0  p).........#)...
0030: 0F 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bhoyu Halpatacco (ID: 17801244/0x010FA01C), tag_num=0x01)
  4: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=9990*)
    → "This counter is for departurrres only. The arrivals counter is on the otherrr side."
  5: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bhoyu Halpatacco (ID: 17801244/0x010FA01C), tag_num=0x02)
  7: 0x0033 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0035 [0x21] END_EVENT
  9: 0x0036 [0x00] END_REQSTACK()
```

### Event 116

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0037    |
| Data Size    | 211 bytes |
| Instructions | 34        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      1E  F0 FF FF 7F 6F 70 29 08         .....op).
0040: 1C A0 0F 01 01 1D 03 80  23 29 08 1C A0 0F 01 02  ........#)......
0050: 24 04 80 05 80 06 80 25  02 00 10 06 80 00 06 01  $......%........
0060: 42 46 01 03 01 10 07 80  45 08 80 F8 FF FF 7F F8  BF......E.......
0070: FF FF 7F 66 64 6F 31 06  80 27 0B 20 A0 0F 01 02  ...fdo1..'. ....
0080: 1C 09 80 29 0B F0 FF FF  7F 12 29 0B 1D A0 0F 01  ...)......).....
0090: 04 45 0A 80 F8 FF FF 7F  F8 FF FF 7F 73 30 33 36  .E..........s036
00A0: 06 80 45 08 80 F8 FF FF  7F F8 FF FF 7F 66 64 69  ..E..........fdi
00B0: 31 06 80 1C 09 80 27 0B  F0 FF FF 7F 14 1C 0B 80  1.....'.........
00C0: 45 08 80 F8 FF FF 7F F8  FF FF 7F 66 64 6F 31 06  E..........fdo1.
00D0: 80 1C 09 80 52 0A 80 F8  FF FF 7F F8 FF FF 7F 73  ....R..........s
00E0: 30 33 36 29 0B F0 FF FF  7F 13 2A 0B 20 A0 0F 01  036)......*. ...
00F0: 45 08 80 F8 FF FF 7F F8  FF FF 7F 66 64 69 31 06  E..........fdi1.
0100: 80 46 00 01 06 01 20 00  21 00                    .F.... .!.      
```

#### Opcodes

```
  0: 0x0037 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x003E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bhoyu Halpatacco (ID: 17801244/0x010FA01C), tag_num=0x01)
  4: 0x0045 [0x1D] PRINT_EVENT_MESSAGE(message_id=9991*)
    → "The prrrice for an airship ride to Jeuno is $1 gil."
  5: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0049 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bhoyu Halpatacco (ID: 17801244/0x010FA01C), tag_num=0x02)
  7: 0x0050 [0x24] CREATE_DIALOG(message_id=9992*, default_option=1*, option_flags=0*)
    → "Board the airship? [Yes./Not yet.]"
  8: 0x0057 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0058 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0106
 10: 0x0060 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 11: 0x0061 [0x46] CAMERA_CONTROL: Disable user control
 12: 0x0063 [0x03] Work_Zone[1] = 3*
 13: 0x0068 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 14: 0x0079 [0x27] REQ_SET(priority=0x0B, entity_id=Door_a (ID: 17801248/0x010FA020), tag_num=0x02)
 15: 0x0080 [0x1C] WAIT(60* ticks)
 16: 0x0083 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x12)
 17: 0x008A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Flame Walker (ID: 17801245/0x010FA01D), tag_num=0x04)
 18: 0x0091 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s036" with entities [EventEntity, EventEntity], work=[59*, 0*]
 19: 0x00A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 20: 0x00B3 [0x1C] WAIT(60* ticks)
 21: 0x00B6 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x14)
 22: 0x00BD [0x1C] WAIT(120* ticks)
 23: 0x00C0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 24: 0x00D1 [0x1C] WAIT(60* ticks)
 25: 0x00D4 [0x52] END_LOAD_SCHEDULER: End scheduler "s036" with entities [EventEntity, EventEntity], work=59*
 26: 0x00E3 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x13)
 27: 0x00EA [0x2A] GET_REQ_LEVEL(level=11, entity_id=Door_a (ID: 17801248/0x010FA020))
 28: 0x00F0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 29: 0x0101 [0x46] CAMERA_CONTROL: Restore default settings
 30: 0x0103 [0x01] GOTO 0x0106

SUBROUTINE_0106:
 31: 0x0106 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 32: 0x0108 [0x21] END_EVENT
 33: 0x0109 [0x00] END_REQSTACK()
```
