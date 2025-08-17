# 17776696 - Deadly Minnow

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 392 bytes             |
| Total Events     | 12                    |
| References Count | 15                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [187](#event-187)        | 0x0001       |     15 |              7 |
| [155](#event-155)        | 0x0010       |      1 |              1 |
| [65535.1](#event-655351) | 0x0011       |     15 |              4 |
| [86](#event-86)          | 0x0020       |     28 |              8 |
| [24](#event-24)          | 0x003C       |     63 |             13 |
| [65535.2](#event-655352) | 0x007B       |     64 |             13 |
| [65535.3](#event-655353) | 0x00BB       |     14 |              5 |
| [65535.4](#event-655354) | 0x00C9       |     19 |              3 |
| [65535.5](#event-655355) | 0x00DC       |      9 |              3 |
| [65535.6](#event-655356) | 0x00E5       |     19 |              3 |
| [65535.7](#event-655357) | 0x00F8       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D9B      |        7579 |
|       1 | 0x1D9C      |        7580 |
|       2 | 0xFFFFF6C8  |  4294964936 |
|       3 | 0xAF49      |       44873 |
|       4 | 0x0513      |        1299 |
|       5 | 0x0A4C      |        2636 |
|       6 | 0x000D      |          13 |
|       7 | 0x003C      |          60 |
|       8 | 0x1E13      |        7699 |
|       9 | 0x1E16      |        7702 |
|      10 | 0x1E17      |        7703 |
|      11 | 0x1E18      |        7704 |
|      12 | 0xFFFFF1A4  |  4294963620 |
|      13 | 0xBAD4      |       47828 |
|      14 | 0x001E      |          30 |

## String References

- **7579**: Greetings! We deal in all sorts of armor. They say the best defense is a good offense, but it never hurts to play it safe.
- **7580**: I know it sounds obvious, but a good suit of armor can save your life.
- **7699**: Much is told of Borghertz, but it's all just a legend. Don't let greed cloud your judgment.

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

### Event 187

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 21 00   ........#...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7579*)
    → "Greetings! We deal in all sorts of armor. They say the best defense is a good offense, but it never hurts to play it safe."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=7580*)
    → "I know it sounds obvious, but a good suit of armor can save your life."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 155

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    22 01 37 02 80 03 80  04 80 05 80 32 06 80 00   ".7........2...
```

#### Opcodes

```
  0: 0x0011 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0013 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-2.360*, z=44.873*, y=1.299*, direction=231.7°*
  2: 0x001C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x001F [0x00] END_REQSTACK()
```

### Event 86

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 1E F0 FF FF 7F 6F 70 66  07 80 F8 FF FF 7F F8 FF  .....opf........
0030: FF 7F 74 6C 6B 30 1D 08  80 23 21 00              ..tlk0...#!.    
```

#### Opcodes

```
  0: 0x0020 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0025 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0026 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  4: 0x0036 [0x1D] PRINT_EVENT_MESSAGE(message_id=7699*)
    → "Much is told of Borghertz, but it's all just a legend. Don't let greed cloud your judgment."
  5: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003A [0x21] END_EVENT
  7: 0x003B [0x00] END_REQSTACK()
```

### Event 24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 63 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      1E F0 FF FF              ....
0040: 7F 6F 70 66 07 80 F8 FF  FF 7F F8 FF FF 7F 74 68  .opf..........th
0050: 6B 31 2B 38 40 0F 01 09  80 23 2B 38 40 0F 01 0A  k1+8@....#+8@...
0060: 80 23 66 07 80 F8 FF FF  7F F8 FF FF 7F 74 68 6B  .#f..........thk
0070: 32 2B 38 40 0F 01 0B 80  23 21 00                 2+8@....#!.     
```

#### Opcodes

```
  0: 0x003C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0041 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0042 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0043 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=60*
  4: 0x0052 [0x2B] Deadly Minnow (ID: 17776696/0x010F4038) [7702*]:
    → "Wait. I heard that a Mithra working for the Tenshodo acquired a strange toolbox long ago."
  5: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x005A [0x2B] Deadly Minnow (ID: 17776696/0x010F4038) [7703*]:
    → "Some mysterious device held it shut; nobody could open it!"
  7: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0062 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=60*
  9: 0x0071 [0x2B] Deadly Minnow (ID: 17776696/0x010F4038) [7704*]:
    → "Even if it held some magical tool, I doubt anybody has the skill to repair these gauntlets."
 10: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0079 [0x21] END_EVENT
 12: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 64 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   22 00 1F 00 0C             "....
0080: 80 0D 80 04 80 1F 01 6F  1E 37 40 0F 01 29 04 37  .......o.7@..).7
0090: 40 0F 01 0A 4A 37 40 0F  01 38 40 0F 01 4A F0 FF  @...J7@..8@..J..
00A0: FF 7F 38 40 0F 01 6F 70  66 07 80 F8 FF FF 7F F8  ..8@..opf.......
00B0: FF FF 7F 74 68 6B 31 1C  07 80 00                 ...thk1....     
```

#### Opcodes

```
  0: 0x007B [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x007D [0x1F] MOVE_ENTITY: EventEntity moves to X=-3.676*, Z=47.828*, Y=1.299*
  2: 0x0085 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0087 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0088 [0x1E] EventEntity looks at Guslam (ID: 17776695/0x010F4037) and starts talking
  5: 0x008D [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Guslam (ID: 17776695/0x010F4037), tag_num=0x0A)
  6: 0x0094 [0x4A] Guslam (ID: 17776695/0x010F4037) looks at Deadly Minnow (ID: 17776696/0x010F4038)
  7: 0x009D [0x4A] LocalPlayer looks at Deadly Minnow (ID: 17776696/0x010F4038)
  8: 0x00A6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x00A7 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 10: 0x00A8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=60*
 11: 0x00B7 [0x1C] WAIT(60* ticks)
 12: 0x00BA [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 14 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   1F 00 02 80 03             .....
00C0: 80 04 80 1F 01 6F 22 01  00                       .....o"..       
```

#### Opcodes

```
  0: 0x00BB [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.360*, Z=44.873*, Y=1.299*
  1: 0x00C3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00C5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00C6 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             66 07 80 F8 FF FF 7F           f......
00D0: F8 FF FF 7F 74 6C 6B 30  1C 0E 80 00              ....tlk0....    
```

#### Opcodes

```
  0: 0x00C9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  1: 0x00D8 [0x1C] WAIT(30* ticks)
  2: 0x00DB [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DC  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      5E 69 64 6C              ^idl
00E0: 30 1C 07 80 00                                    0....           
```

#### Opcodes

```
  0: 0x00DC [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00E1 [0x1C] WAIT(60* ticks)
  2: 0x00E4 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E5   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                66 07 80  F8 FF FF 7F F8 FF FF 7F       f..........
00F0: 74 68 6B 31 1C 0E 80 00                           thk1....        
```

#### Opcodes

```
  0: 0x00E5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=60*
  1: 0x00F4 [0x1C] WAIT(30* ticks)
  2: 0x00F7 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F8   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                          66 07 80 F8 FF FF 7F F8          f.......
0100: FF FF 7F 74 68 6B 32 1C  07 80 00                 ...thk2....     
```

#### Opcodes

```
  0: 0x00F8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=60*
  1: 0x0107 [0x1C] WAIT(60* ticks)
  2: 0x010A [0x00] END_REQSTACK()
```
