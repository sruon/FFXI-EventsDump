# 17563919 - Talking Doll

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Inner Horutoto Ruins (ID: 192) |
| Block Size       | 492 bytes                      |
| Total Events     | 4                              |
| References Count | 19                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [71](#event-71)       | 0x0001       |    178 |             34 |
| [72](#event-72)       | 0x00B3       |     12 |              7 |
| [74](#event-74)       | 0x00BF       |    193 |             35 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0013      |          19 |
|       1 | 0x6B675     |      439925 |
|       2 | 0x2BEB0     |      179888 |
|       3 | 0xFFFFE0C0  |  4294959296 |
|       4 | 0x07E8      |        2024 |
|       5 | 0x005C      |          92 |
|       6 | 0x0000      |           0 |
|       7 | 0x00C8      |         200 |
|       8 | 0x1CD1      |        7377 |
|       9 | 0x0064      |         100 |
|      10 | 0x1CD2      |        7378 |
|      11 | 0x1CD3      |        7379 |
|      12 | 0x1CD4      |        7380 |
|      13 | 0x1CD5      |        7381 |
|      14 | 0x1CD6      |        7382 |
|      15 | 0xFFFC0860  |  4294707296 |
|      16 | 0x3A45C     |      238684 |
|      17 | 0x1F3F      |        7999 |
|      18 | 0x0C1D      |        3101 |

## String References

- **7377**: ...Beep...
- **7378**: ...Beeeep! Beeeep! Beeeep!
- **7379**: ...Detected... Unclassifiable magic source... ...Location... Sealed area...
- **7380**: Contact manufacturer...
- **7381**: ...Detected... Unclassifiable magic source... ...Location... Behind door...
- **7382**: Contact manufacturer...

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

### Event 71

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 178 bytes |
| Instructions | 34        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 46 01 38 00 80 37  01 80 02 80 03 80 04 80   BF.8..7........
0010: 29 0B F0 FF FF 7F 31 92  01 F8 FF FF 7F 22 00 80  ).....1......"..
0020: 0F 01 0C 01 22 00 80 F0  FF FF 7F 45 05 80 F8 FF  ...."......E....
0030: FF 7F F8 FF FF 7F 73 30  37 35 06 80 45 07 80 F8  ......s075..E...
0040: FF FF 7F F8 FF FF 7F 66  64 69 31 06 80 1D 08 80  .......fdi1.....
0050: 23 1D 08 80 23 1D 08 80  23 1C 09 80 1D 0A 80 23  #...#...#......#
0060: 52 05 80 F8 FF FF 7F F8  FF FF 7F 73 30 37 35 45  R..........s075E
0070: 05 80 F8 FF FF 7F F8 FF  FF 7F 73 30 37 36 06 80  ..........s076..
0080: 1D 0B 80 23 1D 0C 80 23  45 07 80 F8 FF FF 7F F8  ...#...#E.......
0090: FF FF 7F 66 64 6F 31 06  80 1C 09 80 46 00 45 07  ...fdo1.....F.E.
00A0: 80 F8 FF FF 7F F8 FF FF  7F 66 64 69 31 06 80 20  .........fdi1.. 
00B0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0004 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  3: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=439.925*, z=179.888*, y=-8.000*, direction=177.9°*
  4: 0x0010 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x31)
  5: 0x0017 [0x92] EventEntity->Render.Flags3 ^= 0x01
  6: 0x001D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  7: 0x001F [0x80] LOAD_WAIT(entity=Talking Doll (ID: 17563919/0x010C010F))
  8: 0x0024 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  9: 0x0026 [0x80] LOAD_WAIT(entity=LocalPlayer)
 10: 0x002B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s075" with entities [EventEntity, EventEntity], work=[92*, 0*]
 11: 0x003C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 12: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=7377*)
    → "...Beep..."
 13: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=7377*)
    → "...Beep..."
 15: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=7377*)
    → "...Beep..."
 17: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0059 [0x1C] WAIT(100* ticks)
 19: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=7378*)
    → "...Beeeep! Beeeep! Beeeep!"
 20: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0060 [0x52] END_LOAD_SCHEDULER: End scheduler "s075" with entities [EventEntity, EventEntity], work=92*
 22: 0x006F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s076" with entities [EventEntity, EventEntity], work=[92*, 0*]
 23: 0x0080 [0x1D] PRINT_EVENT_MESSAGE(message_id=7379*)
    → "...Detected... Unclassifiable magic source... ...Location... Sealed area..."
 24: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=7380*)
    → "Contact manufacturer..."
 26: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0088 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 28: 0x0099 [0x1C] WAIT(100* ticks)
 29: 0x009C [0x46] CAMERA_CONTROL: Restore default settings
 30: 0x009E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 31: 0x00AF [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 32: 0x00B1 [0x21] END_EVENT
 33: 0x00B2 [0x00] END_REQSTACK()
```

### Event 72

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 12 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          1D 0D 80 23 1D  0E 80 23 20 00 21 00        ...#...# .!. 
```

#### Opcodes

```
  0: 0x00B3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7381*)
    → "...Detected... Unclassifiable magic source... ...Location... Behind door..."
  1: 0x00B6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00B7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7382*)
    → "Contact manufacturer..."
  3: 0x00BA [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00BB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  5: 0x00BD [0x21] END_EVENT
  6: 0x00BE [0x00] END_REQSTACK()
```

### Event 74

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00BF    |
| Data Size    | 193 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               42                 B
00C0: 46 01 38 00 80 37 0F 80  10 80 11 80 12 80 29 0B  F.8..7........).
00D0: F0 FF FF 7F 32 92 01 F8  FF FF 7F 22 00 80 0F 01  ....2......"....
00E0: 0C 01 22 00 80 F0 FF FF  7F 45 05 80 F8 FF FF 7F  .."......E......
00F0: F8 FF FF 7F 73 30 37 37  06 80 45 07 80 F8 FF FF  ....s077..E.....
0100: 7F F8 FF FF 7F 66 64 69  31 06 80 1D 08 80 23 1D  .....fdi1.....#.
0110: 08 80 23 1D 08 80 23 1C  09 80 1D 0A 80 23 52 05  ..#...#......#R.
0120: 80 F8 FF FF 7F F8 FF FF  7F 73 30 37 37 45 05 80  .........s077E..
0130: F8 FF FF 7F F8 FF FF 7F  73 30 37 38 06 80 1D 0B  ........s078....
0140: 80 23 1D 0C 80 23 45 07  80 F8 FF FF 7F F8 FF FF  .#...#E.........
0150: 7F 66 64 6F 31 06 80 1C  09 80 52 05 80 F8 FF FF  .fdo1.....R.....
0160: 7F F8 FF FF 7F 73 30 37  38 46 00 45 07 80 F8 FF  .....s078F.E....
0170: FF 7F F8 FF FF 7F 66 64  69 31 06 80 20 00 21 00  ......fdi1.. .!.
```

#### Opcodes

```
  0: 0x00BF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00C0 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x00C2 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  3: 0x00C5 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-260.000*, z=238.684*, y=7.999*, direction=272.5°*
  4: 0x00CE [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x32)
  5: 0x00D5 [0x92] EventEntity->Render.Flags3 ^= 0x01
  6: 0x00DB [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  7: 0x00DD [0x80] LOAD_WAIT(entity=Talking Doll (ID: 17563919/0x010C010F))
  8: 0x00E2 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  9: 0x00E4 [0x80] LOAD_WAIT(entity=LocalPlayer)
 10: 0x00E9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s077" with entities [EventEntity, EventEntity], work=[92*, 0*]
 11: 0x00FA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 12: 0x010B [0x1D] PRINT_EVENT_MESSAGE(message_id=7377*)
    → "...Beep..."
 13: 0x010E [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x010F [0x1D] PRINT_EVENT_MESSAGE(message_id=7377*)
    → "...Beep..."
 15: 0x0112 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0113 [0x1D] PRINT_EVENT_MESSAGE(message_id=7377*)
    → "...Beep..."
 17: 0x0116 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0117 [0x1C] WAIT(100* ticks)
 19: 0x011A [0x1D] PRINT_EVENT_MESSAGE(message_id=7378*)
    → "...Beeeep! Beeeep! Beeeep!"
 20: 0x011D [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x011E [0x52] END_LOAD_SCHEDULER: End scheduler "s077" with entities [EventEntity, EventEntity], work=92*
 22: 0x012D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s078" with entities [EventEntity, EventEntity], work=[92*, 0*]
 23: 0x013E [0x1D] PRINT_EVENT_MESSAGE(message_id=7379*)
    → "...Detected... Unclassifiable magic source... ...Location... Sealed area..."
 24: 0x0141 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0142 [0x1D] PRINT_EVENT_MESSAGE(message_id=7380*)
    → "Contact manufacturer..."
 26: 0x0145 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0146 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 28: 0x0157 [0x1C] WAIT(100* ticks)
 29: 0x015A [0x52] END_LOAD_SCHEDULER: End scheduler "s078" with entities [EventEntity, EventEntity], work=92*
 30: 0x0169 [0x46] CAMERA_CONTROL: Restore default settings
 31: 0x016B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 32: 0x017C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 33: 0x017E [0x21] END_EVENT
 34: 0x017F [0x00] END_REQSTACK()
```
