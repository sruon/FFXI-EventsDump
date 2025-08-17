# 17114015 - Lilisette

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 400 bytes                  |
| Total Events     | 19                         |
| References Count | 29                         |

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
| [2](#event-2)              | 0x0044       |      1 |              1 |
| [3](#event-3)              | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     15 |              5 |
| [65535.9](#event-655359)   | 0x0055       |     15 |              5 |
| [65535.10](#event-6553510) | 0x0064       |     15 |              5 |
| [65535.11](#event-6553511) | 0x0073       |     15 |              5 |
| [65535.12](#event-6553512) | 0x0082       |     15 |              5 |
| [65535.13](#event-6553513) | 0x0091       |     15 |              5 |
| [65535.14](#event-6553514) | 0x00A0       |     15 |              5 |
| [65535.15](#event-6553515) | 0x00AF       |     15 |              5 |
| [7](#event-7)              | 0x00BE       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000B      |          11 |
|       4 | 0xBFBC      |       49084 |
|       5 | 0x4DBD9     |      318425 |
|       6 | 0x00FC      |         252 |
|       7 | 0xB629      |       46633 |
|       8 | 0x4D02F     |      315439 |
|       9 | 0x0065      |         101 |
|      10 | 0x000D      |          13 |
|      11 | 0xBE4F      |       48719 |
|      12 | 0x4D666     |      317030 |
|      13 | 0x00EA      |         234 |
|      14 | 0xBA33      |       47667 |
|      15 | 0x4D203     |      315907 |
|      16 | 0x00AF      |         175 |
|      17 | 0xB8AC      |       47276 |
|      18 | 0x4D3C4     |      316356 |
|      19 | 0x00A2      |         162 |
|      20 | 0xB3D5      |       46037 |
|      21 | 0x4D800     |      317440 |
|      22 | 0x0064      |         100 |
|      23 | 0x0028      |          40 |
|      24 | 0xA633      |       42547 |
|      25 | 0x4DA7A     |      318074 |
|      26 | 0x7B35      |       31541 |
|      27 | 0x4AB58     |      306008 |
|      28 | 0x0BFE      |        3070 |

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

### Event 2

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

### Event 3

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

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   32 03  80 1F 00 04 80 05 80 06        2.........
0050: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=49.084*, Z=318.425*, Y=0.252*
  2: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                32 03 80  1F 00 07 80 08 80 09 80       2..........
0060: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0055 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=46.633*, Z=315.439*, Y=0.101*
  2: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0062 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             32 0A 80 1F  00 0B 80 0C 80 0D 80 1F      2...........
0070: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0064 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0067 [0x1F] MOVE_ENTITY: EventEntity moves to X=48.719*, Z=317.030*, Y=0.234*
  2: 0x006F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0071 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          32 0A 80 1F 00  0E 80 0F 80 10 80 1F 01     2............
0080: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0073 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0076 [0x1F] MOVE_ENTITY: EventEntity moves to X=47.667*, Z=315.907*, Y=0.175*
  2: 0x007E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0080 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       32 0A 80 1F 00 11  80 12 80 13 80 1F 01 6F    2............o
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0082 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0085 [0x1F] MOVE_ENTITY: EventEntity moves to X=47.276*, Z=316.356*, Y=0.162*
  2: 0x008D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    32 0A 80 1F 00 14 80  15 80 16 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0091 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0094 [0x1F] MOVE_ENTITY: EventEntity moves to X=46.037*, Z=317.440*, Y=0.100*
  2: 0x009C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x009F [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A0   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0: 32 17 80 1F 00 18 80 19  80 00 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x00A0 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00A3 [0x1F] MOVE_ENTITY: EventEntity moves to X=42.547*, Z=318.074*, Y=0.000*
  2: 0x00AB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               32                 2
00B0: 17 80 1F 00 1A 80 1B 80  1C 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x00AF [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00B2 [0x1F] MOVE_ENTITY: EventEntity moves to X=31.541*, Z=306.008*, Y=3.070*
  2: 0x00BA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00BD [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BE  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            00                   . 
```

#### Opcodes

```
  0: 0x00BE [0x00] END_REQSTACK()
```
