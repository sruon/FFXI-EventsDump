# 17793052 - Mathildes Son

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Selbina (ID: 248) |
| Block Size       | 504 bytes         |
| Total Events     | 7                 |
| References Count | 23                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [173](#event-173)        | 0x0001       |      3 |              2 |
| [65535.1](#event-655351) | 0x0004       |     29 |              9 |
| [65535.2](#event-655352) | 0x0021       |    159 |             30 |
| [65535.3](#event-655353) | 0x00C0       |    164 |             31 |
| [65535.4](#event-655354) | 0x0164       |      5 |              2 |
| [65535.5](#event-655355) | 0x0169       |      5 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x3798      |       14232 |
|       1 | 0xFFFFE93A  |  4294961466 |
|       2 | 0xFFFFE304  |  4294959876 |
|       3 | 0x3341      |       13121 |
|       4 | 0xFFFFE60E  |  4294960654 |
|       5 | 0xFFFFE389  |  4294960009 |
|       6 | 0x1B37      |        6967 |
|       7 | 0x0094      |         148 |
|       8 | 0x0000      |           0 |
|       9 | 0x354F      |       13647 |
|      10 | 0x0C2B      |        3115 |
|      11 | 0x004B      |          75 |
|      12 | 0x1B38      |        6968 |
|      13 | 0x003C      |          60 |
|      14 | 0x1B39      |        6969 |
|      15 | 0x0600      |        1536 |
|      16 | 0x4B78      |       19320 |
|      17 | 0x1CE1      |        7393 |
|      18 | 0xFFFFE355  |  4294959957 |
|      19 | 0x0A09      |        2569 |
|      20 | 0x001E      |          30 |
|      21 | 0x092E      |        2350 |
|      22 | 0x0072      |         114 |

## String References

- **6967**: Always do!
- **6968**: I'll get one for you too, Grandma!

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

### Event 173

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 00                                        "..            
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 29 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             1F 00 00 80  01 80 02 80 1F 01 1F 00      ............
0010: 03 80 04 80 05 80 1F 01  6F 1E 1B 80 0F 01 6F 70  ........o.....op
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0004 [0x1F] MOVE_ENTITY: EventEntity moves to X=14.232*, Z=-5.830*, Y=-7.420*
  1: 0x000C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=13.121*, Z=-6.642*, Y=-7.287*
  3: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0019 [0x1E] EventEntity looks at Mathilde (ID: 17793051/0x010F801B) and starts talking
  6: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x001F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0021    |
| Data Size    | 159 bytes |
| Instructions | 30        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    1D 06 80 23 1F 00 00  80 01 80 02 80 1F 01 45   ...#..........E
0030: 07 80 F0 FF FF 7F F0 FF  FF 7F 73 65 31 30 08 80  ..........se10..
0040: 1F 00 09 80 0A 80 05 80  1F 01 6F 1E 1A 80 0F 01  ..........o.....
0050: 4A F0 FF FF 7F F8 FF FF  7F 4A 1A 80 0F 01 F8 FF  J........J......
0060: FF 7F 4A 1B 80 0F 01 F8  FF FF 7F 6F 70 5B 0B 80  ..J........op[..
0070: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 0C 80 23  ........tlk0...#
0080: 5B 0D 80 1A 80 0F 01 1A  80 0F 01 74 6C 6B 30 2B  [..........tlk0+
0090: 1A 80 0F 01 0E 80 23 53  F8 FF FF 7F F8 FF FF 7F  ......#S........
00A0: 74 6C 6B 30 03 00 00 03  7F 07 00 00 0F 80 39 00  tlk0..........9.
00B0: 00 6F 70 1F 00 10 80 11  80 12 80 1F 01 22 01 00  .op.........."..
```

#### Opcodes

```
  0: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=6967*)
    → "Always do!"
  1: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=14.232*, Z=-5.830*, Y=-7.420*
  3: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x002F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se10" with entities [LocalPlayer, LocalPlayer], work=[148*, 0*]
  5: 0x0040 [0x1F] MOVE_ENTITY: EventEntity moves to X=13.647*, Z=3.115*, Y=-7.287*
  6: 0x0048 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x004A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x004B [0x1E] EventEntity looks at Ramona (ID: 17793050/0x010F801A) and starts talking
  9: 0x0050 [0x4A] LocalPlayer looks at EventEntity
 10: 0x0059 [0x4A] Ramona (ID: 17793050/0x010F801A) looks at EventEntity
 11: 0x0062 [0x4A] Mathilde (ID: 17793051/0x010F801B) looks at EventEntity
 12: 0x006B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 13: 0x006C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 14: 0x006D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
 15: 0x007C [0x1D] PRINT_EVENT_MESSAGE(message_id=6968*)
    → "I'll get one for you too, Grandma!"
 16: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0080 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Ramona (ID: 17793050/0x010F801A), Ramona (ID: 17793050/0x010F801A)], work=60*
 18: 0x008F [0x2B] Ramona (ID: 17793050/0x010F801A) [6969*]:
    → "Why thanks, Aldo. That would be nice."
 19: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0097 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 21: 0x00A4 [0x03] ExtData[1]->WorkLocal[0] = enDirCli(ExtData[1]->EventDir[1]) * 4096.0 * 0.15915963
 22: 0x00A9 [0x07] ExtData[1]->WorkLocal[0] += 1536*
 23: 0x00AE [0x39] SET_ENTITY_DIRECTION(direction=ExtData[1]->WorkLocal[0])
 24: 0x00B1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 25: 0x00B2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 26: 0x00B3 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.320*, Z=7.393*, Y=-7.339*
 27: 0x00BB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 28: 0x00BD [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 29: 0x00BF [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00C0    |
| Data Size    | 164 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 1D 06 80 23 1F 00 00 80  01 80 02 80 1F 01 45 07  ...#..........E.
00D0: 80 F0 FF FF 7F F0 FF FF  7F 73 65 31 30 08 80 1F  .........se10...
00E0: 00 09 80 0A 80 05 80 1F  01 6F 1E 1A 80 0F 01 4A  .........o.....J
00F0: F0 FF FF 7F F8 FF FF 7F  4A 1A 80 0F 01 F8 FF FF  ........J.......
0100: 7F 4A 1B 80 0F 01 F8 FF  FF 7F 6F 70 5B 13 80 F8  .J........op[...
0110: FF FF 7F F8 FF FF 7F 74  6C 62 30 1C 14 80 1D 0C  .......tlb0.....
0120: 80 23 5B 13 80 F8 FF FF  7F F8 FF FF 7F 74 6C 62  .#[..........tlb
0130: 31 5B 0D 80 1A 80 0F 01  1A 80 0F 01 74 6C 6B 30  1[..........tlk0
0140: 2B 1A 80 0F 01 0E 80 23  03 00 00 03 7F 07 00 00  +......#........
0150: 0F 80 39 00 00 6F 70 1F  00 10 80 11 80 12 80 1F  ..9..op.........
0160: 01 22 01 00                                       ."..            
```

#### Opcodes

```
  0: 0x00C0 [0x1D] PRINT_EVENT_MESSAGE(message_id=6967*)
    → "Always do!"
  1: 0x00C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00C4 [0x1F] MOVE_ENTITY: EventEntity moves to X=14.232*, Z=-5.830*, Y=-7.420*
  3: 0x00CC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00CE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se10" with entities [LocalPlayer, LocalPlayer], work=[148*, 0*]
  5: 0x00DF [0x1F] MOVE_ENTITY: EventEntity moves to X=13.647*, Z=3.115*, Y=-7.287*
  6: 0x00E7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00E9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00EA [0x1E] EventEntity looks at Ramona (ID: 17793050/0x010F801A) and starts talking
  9: 0x00EF [0x4A] LocalPlayer looks at EventEntity
 10: 0x00F8 [0x4A] Ramona (ID: 17793050/0x010F801A) looks at EventEntity
 11: 0x0101 [0x4A] Mathilde (ID: 17793051/0x010F801B) looks at EventEntity
 12: 0x010A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 13: 0x010B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 14: 0x010C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=2569*
 15: 0x011B [0x1C] WAIT(30* ticks)
 16: 0x011E [0x1D] PRINT_EVENT_MESSAGE(message_id=6968*)
    → "I'll get one for you too, Grandma!"
 17: 0x0121 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0122 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=2569*
 19: 0x0131 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Ramona (ID: 17793050/0x010F801A), Ramona (ID: 17793050/0x010F801A)], work=60*
 20: 0x0140 [0x2B] Ramona (ID: 17793050/0x010F801A) [6969*]:
    → "Why thanks, Aldo. That would be nice."
 21: 0x0147 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0148 [0x03] ExtData[1]->WorkLocal[0] = enDirCli(ExtData[1]->EventDir[1]) * 4096.0 * 0.15915963
 23: 0x014D [0x07] ExtData[1]->WorkLocal[0] += 1536*
 24: 0x0152 [0x39] SET_ENTITY_DIRECTION(direction=ExtData[1]->WorkLocal[0])
 25: 0x0155 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 26: 0x0156 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 27: 0x0157 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.320*, Z=7.393*, Y=-7.339*
 28: 0x015F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 29: 0x0161 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 30: 0x0163 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0164  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:             B6 00 15 80  00                           .....       
```

#### Opcodes

```
  0: 0x0164 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2350*)
  1: 0x0168 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0169  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                             B6 00 16 80 00                 .....  
```

#### Opcodes

```
  0: 0x0169 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=114*)
  1: 0x016D [0x00] END_REQSTACK()
```
