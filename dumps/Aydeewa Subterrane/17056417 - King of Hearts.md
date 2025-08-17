# 17056417 - King of Hearts

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Aydeewa Subterrane (ID: 68) |
| Block Size       | 340 bytes                   |
| Total Events     | 15                          |
| References Count | 25                          |

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
| [11](#event-11)            | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |     10 |              2 |
| [65535.9](#event-655359)   | 0x004F       |     15 |              5 |
| [65535.10](#event-6553510) | 0x005E       |     25 |              9 |
| [65535.11](#event-6553511) | 0x0077       |     15 |              5 |
| [65535.12](#event-6553512) | 0x0086       |     15 |              5 |
| [65535.13](#event-6553513) | 0x0095       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFB102B  |  4294643755 |
|       4 | 0xFFFFB254  |  4294947412 |
|       5 | 0x8B69      |       35689 |
|       6 | 0x0801      |        2049 |
|       7 | 0x000B      |          11 |
|       8 | 0xFFFBA1AE  |  4294681006 |
|       9 | 0xFFFF697D  |  4294928765 |
|      10 | 0x8FE1      |       36833 |
|      11 | 0x001E      |          30 |
|      12 | 0x000D      |          13 |
|      13 | 0xFFFB9863  |  4294678627 |
|      14 | 0xFFFF6CBD  |  4294929597 |
|      15 | 0x9028      |       36904 |
|      16 | 0xFFFAFC27  |  4294638631 |
|      17 | 0xFFFFC108  |  4294951176 |
|      18 | 0x88D6      |       35030 |
|      19 | 0xFFFB0349  |  4294640457 |
|      20 | 0xFFFFBDB6  |  4294950326 |
|      21 | 0x8993      |       35219 |
|      22 | 0xFFFAFC30  |  4294638640 |
|      23 | 0xFFFFC6E1  |  4294952673 |
|      24 | 0x88E2      |       35042 |

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

### Event 11

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

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                37 03 80  04 80 05 80 06 80 00          7......... 
```

#### Opcodes

```
  0: 0x0045 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-323.541*, z=-19.884*, y=35.689*, direction=180.1°*
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               32                 2
0050: 07 80 1F 00 08 80 09 80  0A 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x004F [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=-286.290*, Z=-38.531*, Y=36.833*
  2: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 25 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            1E 98                ..
0060: 42 04 01 6F 70 1C 0B 80  32 0C 80 1F 00 0D 80 0E  B..op...2.......
0070: 80 0F 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x005E [0x1E] EventEntity looks at Wawaroon (ID: 17056408/0x01044298) and starts talking
  1: 0x0063 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0064 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0065 [0x1C] WAIT(30* ticks)
  4: 0x0068 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x006B [0x1F] MOVE_ENTITY: EventEntity moves to X=-288.669*, Z=-37.699*, Y=36.904*
  6: 0x0073 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0075 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      32  07 80 1F 00 10 80 11 80         2........
0080: 12 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0077 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=-328.665*, Z=-16.120*, Y=35.030*
  2: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0084 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   32 07  80 1F 00 13 80 14 80 15        2.........
0090: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0086 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0089 [0x1F] MOVE_ENTITY: EventEntity moves to X=-326.839*, Z=-16.970*, Y=35.219*
  2: 0x0091 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0093 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                32 0C 80  1F 00 16 80 17 80 18 80       2..........
00A0: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0095 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0098 [0x1F] MOVE_ENTITY: EventEntity moves to X=-328.656*, Z=-14.623*, Y=35.042*
  2: 0x00A0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00A3 [0x00] END_REQSTACK()
```
