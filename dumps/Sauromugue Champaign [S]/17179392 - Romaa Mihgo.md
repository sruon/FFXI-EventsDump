# 17179392 - Romaa Mihgo

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 352 bytes                         |
| Total Events     | 16                                |
| References Count | 21                                |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [113](#event-113)          | 0x0044       |      1 |              1 |
| [109](#event-109)          | 0x0045       |      1 |              1 |
| [110](#event-110)          | 0x0046       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0047       |     11 |              3 |
| [65535.9](#event-655359)   | 0x0052       |     11 |              3 |
| [65535.10](#event-6553510) | 0x005D       |     25 |              6 |
| [65535.11](#event-6553511) | 0x0076       |     48 |              8 |
| [65535.12](#event-6553512) | 0x00A6       |     20 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x536C7     |      341703 |
|       4 | 0xFFFD7804  |  4294801412 |
|       5 | 0x4158      |       16728 |
|       6 | 0x58D87     |      363911 |
|       7 | 0xFFFD7587  |  4294800775 |
|       8 | 0x3EFC      |       16124 |
|       9 | 0x0028      |          40 |
|      10 | 0x281E0     |      164320 |
|      11 | 0xFFFD806A  |  4294803562 |
|      12 | 0x1F40      |        8000 |
|      13 | 0x096C      |        2412 |
|      14 | 0x1218C     |       74124 |
|      15 | 0xFFFDF076  |  4294832246 |
|      16 | 0x1E45      |        7749 |
|      17 | 0x000B      |          11 |
|      18 | 0x11BC0     |       72640 |
|      19 | 0xFFFDF8F7  |  4294834423 |
|      20 | 0x1F66      |        8038 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 113

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 109

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0046  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   00                                    .         
```

#### Opcodes

```
  0: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      1F  00 03 80 04 80 05 80 1F         .........
0050: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=341.703*, Z=-165.884*, Y=16.728*
  1: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       1F 00 06 80 07 80  08 80 1F 01 00             ...........   
```

#### Opcodes

```
  0: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=363.911*, Z=-166.521*, Y=16.124*
  1: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         32 09 80               2..
0060: 1F 00 0A 80 0B 80 0C 80  1F 01 6F 79 00 F8 FF FF  ..........oy....
0070: 7F 03 23 06 01 00                                 ..#...          
```

#### Opcodes

```
  0: 0x005D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0060 [0x1F] MOVE_ENTITY: EventEntity moves to X=164.320*, Z=-163.734*, Y=8.000*
  2: 0x0068 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006B [0x79] EventEntity looks at Naho Gwanboh (ID: 17179395/0x01062303) (Basic look)
  5: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 48 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   5B 0D  80 F8 FF FF 7F F8 FF FF        [.........
0080: 7F 72 62 74 31 53 F8 FF  FF 7F F8 FF FF 7F 72 62  .rbt1S........rb
0090: 74 31 32 09 80 1F 00 0E  80 0F 80 10 80 1F 01 6F  t12............o
00A0: 1E FF 22 06 01 00                                 .."...          
```

#### Opcodes

```
  0: 0x0076 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rbt1" with entities [EventEntity, EventEntity], work=2412*
  1: 0x0085 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "rbt1" with entities [EventEntity, EventEntity]
  2: 0x0092 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x0095 [0x1F] MOVE_ENTITY: EventEntity moves to X=74.124*, Z=-135.050*, Y=7.749*
  4: 0x009D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x009F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00A0 [0x1E] EventEntity looks at Lehko Habhoka (ID: 17179391/0x010622FF) and starts talking
  7: 0x00A5 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A6   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                   32 11  80 1F 00 12 80 13 80 14        2.........
00B0: 80 1F 01 6F 1E F0 FF FF  7F 00                    ...o......      
```

#### Opcodes

```
  0: 0x00A6 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x00A9 [0x1F] MOVE_ENTITY: EventEntity moves to X=72.640*, Z=-132.873*, Y=8.038*
  2: 0x00B1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x00B9 [0x00] END_REQSTACK()
```
