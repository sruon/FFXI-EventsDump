# 17723417 - Halaviabeau

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 276 bytes                     |
| Total Events     | 7                             |
| References Count | 18                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |     16 |              3 |
| [65535.1](#event-655351) | 0x0011       |     28 |              8 |
| [65](#event-65)          | 0x002D       |      1 |              1 |
| [62](#event-62)          | 0x002E       |      1 |              1 |
| [611](#event-611)        | 0x002F       |     94 |             16 |
| [16](#event-16)          | 0x008D       |     18 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x23076     |      143478 |
|       1 | 0x1FFC8     |      131016 |
|       2 | 0x0000      |           0 |
|       3 | 0x0A1F      |        2591 |
|       4 | 0x000D      |          13 |
|       5 | 0x23782     |      145282 |
|       6 | 0x1F212     |      127506 |
|       7 | 0x231D7     |      143831 |
|       8 | 0x1ECA0     |      126112 |
|       9 | 0x0B97      |        2967 |
|      10 | 0x0014      |          20 |
|      11 | 0x2C25      |       11301 |
|      12 | 0x001E      |          30 |
|      13 | 0x2BBA      |       11194 |
|      14 | 0x003C      |          60 |
|      15 | 0x1CB8B     |      117643 |
|      16 | 0x1BFE0     |      114656 |
|      17 | 0x021B      |         539 |

## String References

- **11194**: May Paradise open its gates to you.
- **11301**: I study scripture so that I, too, may one day give sermons like Vicasque Arnau.

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

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   ......7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=143.478*, z=131.016*, y=0.000*, direction=227.7°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 1F 00   2..............
0020: 07 80 08 80 02 80 1F 01  6F 39 09 80 00           ........o9...   
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=145.282*, Z=127.506*, Y=0.000*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=143.831*, Z=126.112*, Y=0.000*
  4: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0029 [0x39] SET_ENTITY_DIRECTION(direction=16.3°*)
  7: 0x002C [0x00] END_REQSTACK()
```

### Event 65

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         00                     .  
```

#### Opcodes

```
  0: 0x002D [0x00] END_REQSTACK()
```

### Event 62

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            00                   . 
```

#### Opcodes

```
  0: 0x002E [0x00] END_REQSTACK()
```

### Event 611

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 94 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               1E                 .
0030: F0 FF FF 7F 6F 70 5B 0A  80 F8 FF FF 7F F8 FF FF  ....op[.........
0040: 7F 74 6C 6B 30 1D 0B 80  23 5B 0A 80 F8 FF FF 7F  .tlk0...#[......
0050: F8 FF FF 7F 74 6C 6B 31  53 F8 FF FF 7F F8 FF FF  ....tlk1S.......
0060: 7F 74 6C 6B 31 1C 0C 80  5B 0A 80 F8 FF FF 7F F8  .tlk1...[.......
0070: FF FF 7F 69 6E 6F 30 1D  0D 80 23 53 F8 FF FF 7F  ...ino0...#S....
0080: F8 FF FF 7F 69 6E 6F 30  1C 0E 80 21 00           ....ino0...!.   
```

#### Opcodes

```
  0: 0x002F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0034 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0035 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0036 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0045 [0x1D] PRINT_EVENT_MESSAGE(message_id=11301*)
    → "I study scripture so that I, too, may one day give sermons like Vicasque Arnau."
  5: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0049 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  7: 0x0058 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  8: 0x0065 [0x1C] WAIT(30* ticks)
  9: 0x0068 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
 10: 0x0077 [0x1D] PRINT_EVENT_MESSAGE(message_id=11194*)
    → "May Paradise open its gates to you."
 11: 0x007A [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x007B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
 13: 0x0088 [0x1C] WAIT(60* ticks)
 14: 0x008B [0x21] END_EVENT
 15: 0x008C [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         22 00 92               "..
0090: 01 F8 FF FF 7F 37 0F 80  10 80 02 80 11 80 00     .....7......... 
```

#### Opcodes

```
  0: 0x008D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x008F [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0095 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=117.643*, z=114.656*, y=0.000*, direction=47.4°*
  3: 0x009E [0x00] END_REQSTACK()
```
