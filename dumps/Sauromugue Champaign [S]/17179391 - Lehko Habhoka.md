# 17179391 - Lehko Habhoka

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 400 bytes                         |
| Total Events     | 18                                |
| References Count | 23                                |

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
| [65535.8](#event-655358)   | 0x0047       |     15 |              5 |
| [65535.9](#event-655359)   | 0x0056       |     15 |              5 |
| [65535.10](#event-6553510) | 0x0065       |     11 |              3 |
| [65535.11](#event-6553511) | 0x0070       |     70 |             12 |
| [65535.12](#event-6553512) | 0x00B6       |      3 |              2 |
| [65535.13](#event-6553513) | 0x00B9       |      3 |              2 |
| [65535.14](#event-6553514) | 0x00BC       |     31 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000B      |          11 |
|       4 | 0x5AD3B     |      372027 |
|       5 | 0xFFFD3DFC  |  4294786556 |
|       6 | 0x2967      |       10599 |
|       7 | 0x000C      |          12 |
|       8 | 0x5B408     |      373768 |
|       9 | 0xFFFD38C5  |  4294785221 |
|      10 | 0x547F8     |      346104 |
|      11 | 0xFFFD99CD  |  4294810061 |
|      12 | 0x40C9      |       16585 |
|      13 | 0x548E2     |      346338 |
|      14 | 0xFFFD9DF4  |  4294811124 |
|      15 | 0x40B2      |       16562 |
|      16 | 0x05A3      |        1443 |
|      17 | 0x00C8      |         200 |
|      18 | 0x5B16C     |      373100 |
|      19 | 0xFFFD831F  |  4294804255 |
|      20 | 0x416F      |       16751 |
|      21 | 0x000F      |          15 |
|      22 | 0x002D      |          45 |

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
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      32  03 80 1F 00 04 80 05 80         2........
0050: 06 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0047 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x004A [0x1F] MOVE_ENTITY: EventEntity moves to X=372.027*, Z=-180.740*, Y=10.599*
  2: 0x0052 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0054 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   32 07  80 1F 00 08 80 09 80 06        2.........
0060: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0056 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x0059 [0x1F] MOVE_ENTITY: EventEntity moves to X=373.768*, Z=-182.075*, Y=10.599*
  2: 0x0061 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0063 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                1F 00 0A  80 0B 80 0C 80 1F 01 00       ...........
```

#### Opcodes

```
  0: 0x0065 [0x1F] MOVE_ENTITY: EventEntity moves to X=346.104*, Z=-157.235*, Y=16.585*
  1: 0x006D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x006F [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0070   |
| Data Size    | 70 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 1F 00 0D 80 0E 80 0F 80  1F 01 6F 4A FF 22 06 01  ..........oJ."..
0080: 03 23 06 01 6F 76 FF 22  06 01 5B 10 80 FF 22 06  .#..ov."..[...".
0090: 01 FF 22 06 01 74 6C 61  30 1C 11 80 5B 10 80 FF  .."..tla0...[...
00A0: 22 06 01 FF 22 06 01 74  6C 61 31 1F 00 12 80 13  "..."..tla1.....
00B0: 80 14 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=346.338*, Z=-156.172*, Y=16.562*
  1: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x007A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x007B [0x4A] Lehko Habhoka (ID: 17179391/0x010622FF) looks at Naho Gwanboh (ID: 17179395/0x01062303)
  4: 0x0084 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0085 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Lehko Habhoka (ID: 17179391/0x010622FF) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x008A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [Lehko Habhoka (ID: 17179391/0x010622FF), Lehko Habhoka (ID: 17179391/0x010622FF)], work=1443*
  7: 0x0099 [0x1C] WAIT(200* ticks)
  8: 0x009C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [Lehko Habhoka (ID: 17179391/0x010622FF), Lehko Habhoka (ID: 17179391/0x010622FF)], work=1443*
  9: 0x00AB [0x1F] MOVE_ENTITY: EventEntity moves to X=373.100*, Z=-163.041*, Y=16.751*
 10: 0x00B3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x00B5 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B6  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   A4 01  00                             ...       
```

#### Opcodes

```
  0: 0x00B6 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B9  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             A4 00 00                       ...    
```

#### Opcodes

```
  0: 0x00B9 [0xA4] EventEntity->Flags3.unknown_3_2 = 0
  1: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 31 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      1C 15 80 5B              ...[
00C0: 10 80 FF 22 06 01 FF 22  06 01 74 68 61 31 1C 16  ..."..."..tha1..
00D0: 80 4A FF 22 06 01 01 23  06 01 00                 .J."...#...     
```

#### Opcodes

```
  0: 0x00BC [0x1C] WAIT(15* ticks)
  1: 0x00BF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tha1" with entities [Lehko Habhoka (ID: 17179391/0x010622FF), Lehko Habhoka (ID: 17179391/0x010622FF)], work=1443*
  2: 0x00CE [0x1C] WAIT(45* ticks)
  3: 0x00D1 [0x4A] Lehko Habhoka (ID: 17179391/0x010622FF) looks at Shantotto (ID: 17179393/0x01062301)
  4: 0x00DA [0x00] END_REQSTACK()
```
