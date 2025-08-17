# 17801243 - Dakha Topsalwan

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 368 bytes        |
| Total Events     | 5                |
| References Count | 13               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [66](#event-66)          | 0x001A       |     33 |             12 |
| [121](#event-121)        | 0x003B       |    221 |             37 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x270D      |        9997 |
|       3 | 0x270E      |        9998 |
|       4 | 0x0001      |           1 |
|       5 | 0x286B      |       10347 |
|       6 | 0x270F      |        9999 |
|       7 | 0x2710      |       10000 |
|       8 | 0x0000      |           0 |
|       9 | 0x00C8      |         200 |
|      10 | 0x003C      |          60 |
|      11 | 0x003B      |          59 |
|      12 | 0x0078      |         120 |

## String References

- **9997**: Hello? Where do you think you're going?
- **9998**: The departures counter is on the other side. And don't forget to pay Bhoyu Halpatacco on your way in.
- **9999**: Welcome to Kazham--a lush tropical paradise!
- **10000**: Enter Kazham? [Yes./Not yet.]
- **10347**: Welcome to Kazha...a lush tropical parad... Would you just hurrrry up and leave!?

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

### Event 66

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 29 08 1B A0 0F 01 01  1D 02 80 23 1D 03 80 23  p).........#...#
0030: 29 08 1B A0 0F 01 02 20  00 21 00                 )...... .!.     
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dakha Topsalwan (ID: 17801243/0x010FA01B), tag_num=0x01)
  4: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=9997*)
    → "Hello? Where do you think you're going?"
  5: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=9998*)
    → "The departures counter is on the other side. And don't forget to pay Bhoyu Halpatacco on your way in."
  7: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0030 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dakha Topsalwan (ID: 17801243/0x010FA01B), tag_num=0x02)
  9: 0x0037 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0039 [0x21] END_EVENT
 11: 0x003A [0x00] END_REQSTACK()
```

### Event 121

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x003B    |
| Data Size    | 221 bytes |
| Instructions | 37        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   1E F0 FF FF 7F             .....
0040: 6F 70 29 08 1B A0 0F 01  01 02 05 10 04 80 00 58  op)............X
0050: 00 1D 05 80 23 01 5C 00  1D 06 80 23 29 08 1B A0  ....#.\....#)...
0060: 0F 01 02 24 07 80 04 80  08 80 25 02 00 10 08 80  ...$......%.....
0070: 00 14 01 42 46 01 45 09  80 F8 FF FF 7F F8 FF FF  ...BF.E.........
0080: 7F 66 64 6F 31 08 80 27  0B 21 A0 0F 01 02 1C 0A  .fdo1..'.!......
0090: 80 29 0B F0 FF FF 7F 15  29 0B 1E A0 0F 01 04 45  .)......)......E
00A0: 0B 80 F8 FF FF 7F F8 FF  FF 7F 73 30 33 37 08 80  ..........s037..
00B0: 45 09 80 F8 FF FF 7F F8  FF FF 7F 66 64 69 31 08  E..........fdi1.
00C0: 80 1C 0A 80 27 0B F0 FF  FF 7F 17 1C 0C 80 45 09  ....'.........E.
00D0: 80 F8 FF FF 7F F8 FF FF  7F 66 64 6F 31 08 80 1C  .........fdo1...
00E0: 0A 80 52 0B 80 F8 FF FF  7F F8 FF FF 7F 73 30 33  ..R..........s03
00F0: 37 29 0B F0 FF FF 7F 16  2A 0B 21 A0 0F 01 45 09  7)......*.!...E.
0100: 80 F8 FF FF 7F F8 FF FF  7F 66 64 69 31 08 80 46  .........fdi1..F
0110: 00 01 14 01 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x003B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0041 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0042 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dakha Topsalwan (ID: 17801243/0x010FA01B), tag_num=0x01)
  4: 0x0049 [0x02] IF !(Work_Zone[5] == 1*) GOTO 0x0058
  5: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=10347*)
    → "Welcome to Kazha...a lush tropical parad... Would you just hurrrry up and leave!?"
  6: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0055 [0x01] GOTO 0x005C
  8: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=9999*)
    → "Welcome to Kazham--a lush tropical paradise!"
  9: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_005C:
 10: 0x005C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dakha Topsalwan (ID: 17801243/0x010FA01B), tag_num=0x02)
 11: 0x0063 [0x24] CREATE_DIALOG(message_id=10000*, default_option=1*, option_flags=0*)
    → "Enter Kazham? [Yes./Not yet.]"
 12: 0x006A [0x25] WAIT_DIALOG_SELECT()
 13: 0x006B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0114
 14: 0x0073 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 15: 0x0074 [0x46] CAMERA_CONTROL: Disable user control
 16: 0x0076 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 17: 0x0087 [0x27] REQ_SET(priority=0x0B, entity_id=Door_b (ID: 17801249/0x010FA021), tag_num=0x02)
 18: 0x008E [0x1C] WAIT(60* ticks)
 19: 0x0091 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x15)
 20: 0x0098 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Shark Teeth (ID: 17801246/0x010FA01E), tag_num=0x04)
 21: 0x009F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s037" with entities [EventEntity, EventEntity], work=[59*, 0*]
 22: 0x00B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 23: 0x00C1 [0x1C] WAIT(60* ticks)
 24: 0x00C4 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x17)
 25: 0x00CB [0x1C] WAIT(120* ticks)
 26: 0x00CE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 27: 0x00DF [0x1C] WAIT(60* ticks)
 28: 0x00E2 [0x52] END_LOAD_SCHEDULER: End scheduler "s037" with entities [EventEntity, EventEntity], work=59*
 29: 0x00F1 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x16)
 30: 0x00F8 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Door_b (ID: 17801249/0x010FA021))
 31: 0x00FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 32: 0x010F [0x46] CAMERA_CONTROL: Restore default settings
 33: 0x0111 [0x01] GOTO 0x0114

SUBROUTINE_0114:
 34: 0x0114 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 35: 0x0116 [0x21] END_EVENT
 36: 0x0117 [0x00] END_REQSTACK()
```
