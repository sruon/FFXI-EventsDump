# 17339236 - Bartholomaus

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 352 bytes               |
| Total Events     | 16                      |
| References Count | 19                      |

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
| [65535.8](#event-655358)   | 0x0044       |     20 |              5 |
| [65535.9](#event-655359)   | 0x0058       |     13 |              3 |
| [65535.10](#event-6553510) | 0x0065       |     38 |              8 |
| [65535.11](#event-6553511) | 0x008B       |     25 |              6 |
| [19](#event-19)            | 0x00A4       |      1 |              1 |
| [20](#event-20)            | 0x00A5       |      7 |              2 |
| [41](#event-41)            | 0x00AC       |      7 |              2 |
| [65535.12](#event-6553512) | 0x00B3       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0x2755D     |      161117 |
|       5 | 0xFFFF9098  |  4294938776 |
|       6 | 0xFFFFC361  |  4294951777 |
|       7 | 0x0102      |         258 |
|       8 | 0x2740F     |      160783 |
|       9 | 0xFFFF92E1  |  4294939361 |
|      10 | 0xFFFFC357  |  4294951767 |
|      11 | 0x0078      |         120 |
|      12 | 0x26F82     |      159618 |
|      13 | 0xFFFFBC29  |  4294949929 |
|      14 | 0xFFFFC4E5  |  4294952165 |
|      15 | 0x0028      |          40 |
|      16 | 0xFFFDBA69  |  4294818409 |
|      17 | 0xFFFFF801  |  4294965249 |
|      18 | 0xFFFFC2E2  |  4294951650 |

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

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             59 04 F8 FF  FF 7F 03 80 1F 00 04 80      Y...........
0050: 05 80 06 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0044 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=161.117*, Z=-28.520*, Y=-15.519*
  2: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          6E F8 FF FF 7F 07 80 99          n.......
0060: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0058 [0x6E] EventEntity uses emote 258*
  1: 0x005F [0x99] Wait for EventEntity animation to complete
  2: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 38 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                7B F8 FF  FF 7F 59 04 F8 FF FF 7F       {....Y.....
0070: 03 80 1F 00 08 80 09 80  0A 80 1F 01 6F 1C 0B 80  ............o...
0080: 79 00 64 93 08 01 67 93  08 01 00                 y.d...g....     
```

#### Opcodes

```
  0: 0x0065 [0x7B] EventEntity stops talking
  1: 0x006A [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  2: 0x0072 [0x1F] MOVE_ENTITY: EventEntity moves to X=160.783*, Z=-27.935*, Y=-15.529*
  3: 0x007A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x007C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x007D [0x1C] WAIT(120* ticks)
  6: 0x0080 [0x79] Bartholomaus (ID: 17339236/0x01089364) looks at Invincible Shield (ID: 17339239/0x01089367) (Basic look)
  7: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   7B F8 FF FF 7F             {....
0090: 59 04 F8 FF FF 7F 03 80  1F 00 0C 80 0D 80 0E 80  Y...............
00A0: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x008B [0x7B] EventEntity stops talking
  1: 0x0090 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  2: 0x0098 [0x1F] MOVE_ENTITY: EventEntity moves to X=159.618*, Z=-17.367*, Y=-15.131*
  3: 0x00A0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00A2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00A3 [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             00                                        .           
```

#### Opcodes

```
  0: 0x00A4 [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A5  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x00A5 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00AB [0x00] END_REQSTACK()
```

### Event 41

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AC  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      92 01 F8 FF              ....
00B0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x00AC [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          32 0F 80 1F 00  10 80 11 80 12 80 1F 01     2............
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00B3 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00B6 [0x1F] MOVE_ENTITY: EventEntity moves to X=-148.887*, Z=-2.047*, Y=-15.646*
  2: 0x00BE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C0 [0x00] END_REQSTACK()
```
