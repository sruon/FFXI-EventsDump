# 17134167 - Derek Karst

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 344 bytes                   |
| Total Events     | 11                          |
| References Count | 27                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [56](#event-56)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     14 |              4 |
| [65535.2](#event-655352) | 0x0016       |     22 |              6 |
| [65535.3](#event-655353) | 0x002C       |     14 |              4 |
| [57](#event-57)          | 0x003A       |      7 |              2 |
| [65535.4](#event-655354) | 0x0041       |     28 |              6 |
| [65535.5](#event-655355) | 0x005D       |     14 |              4 |
| [65535.6](#event-655356) | 0x006B       |     44 |             10 |
| [63](#event-63)          | 0x0097       |      7 |              2 |
| [65535.7](#event-655357) | 0x009E       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFBBBEC  |  4294687724 |
|       2 | 0xFFFE96D3  |  4294874835 |
|       3 | 0xFFFFD121  |  4294955297 |
|       4 | 0xFFFBB8C7  |  4294686919 |
|       5 | 0xFFFE92A3  |  4294873763 |
|       6 | 0xFFFFD120  |  4294955296 |
|       7 | 0x001E      |          30 |
|       8 | 0xFFFBC399  |  4294689689 |
|       9 | 0xFFFE9C6F  |  4294876271 |
|      10 | 0x1691D     |       92445 |
|      11 | 0x380B      |       14347 |
|      12 | 0xFFFFB127  |  4294947111 |
|      13 | 0x15E6F     |       89711 |
|      14 | 0x30FB      |       12539 |
|      15 | 0xFFFFB136  |  4294947126 |
|      16 | 0x0550      |        1360 |
|      17 | 0x15B20     |       88864 |
|      18 | 0x2895      |       10389 |
|      19 | 0x15A90     |       88720 |
|      20 | 0x23A3      |        9123 |
|      21 | 0x005A      |          90 |
|      22 | 0x15A83     |       88707 |
|      23 | 0x1830      |        6192 |
|      24 | 0x130EA     |       78058 |
|      25 | 0xFFFFFC6F  |  4294966383 |
|      26 | 0xFFFFB3B5  |  4294947765 |

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

### Event 56

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=-279.572*, Z=-92.461*, Y=-11.999*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   32 00  80 1F 00 04 80 05 80 06        2.........
0020: 80 1F 01 1E F4 71 05 01  1C 07 80 00              .....q......    
```

#### Opcodes

```
  0: 0x0016 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=-280.377*, Z=-93.533*, Y=-12.000*
  2: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0023 [0x1E] EventEntity looks at Five Moons (ID: 17134068/0x010571F4) and starts talking
  4: 0x0028 [0x1C] WAIT(30* ticks)
  5: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      32 00 80 1F              2...
0030: 00 08 80 09 80 03 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x002C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=-277.607*, Z=-91.025*, Y=-11.999*
  2: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0039 [0x00] END_REQSTACK()
```

### Event 57

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                92 01 F8 FF FF 7F            ......
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x003A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 28 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    32 00 80 1F 00 0A 80  0B 80 0C 80 1F 01 37 0D   2............7.
0050: 80 0E 80 0F 80 10 80 80  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0041 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=92.445*, Z=14.347*, Y=-20.185*
  2: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=89.711*, z=12.539*, y=-20.170*, direction=119.5°*
  4: 0x0057 [0x80] LOAD_WAIT(entity=EventEntity)
  5: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         32 00 80               2..
0060: 1F 00 11 80 12 80 0F 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x005D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0060 [0x1F] MOVE_ENTITY: EventEntity moves to X=88.864*, Z=10.389*, Y=-20.170*
  2: 0x0068 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   32 00 80 1F 00             2....
0070: 13 80 14 80 0F 80 1F 01  27 05 41 72 05 01 03 1C  ........'.Ar....
0080: 15 80 1F 00 16 80 17 80  0F 80 1F 01 27 05 41 72  ............'.Ar
0090: 05 01 04 1C 15 80 00                              .......         
```

#### Opcodes

```
  0: 0x006B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006E [0x1F] MOVE_ENTITY: EventEntity moves to X=88.720*, Z=9.123*, Y=-20.170*
  2: 0x0076 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0078 [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17134145/0x01057241), tag_num=0x03)
  4: 0x007F [0x1C] WAIT(90* ticks)
  5: 0x0082 [0x1F] MOVE_ENTITY: EventEntity moves to X=88.707*, Z=6.192*, Y=-20.170*
  6: 0x008A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x008C [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17134145/0x01057241), tag_num=0x04)
  8: 0x0093 [0x1C] WAIT(90* ticks)
  9: 0x0096 [0x00] END_REQSTACK()
```

### Event 63

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0097  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0097 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            32 00                2.
00A0: 80 1F 00 18 80 19 80 1A  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x009E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=78.058*, Z=-0.913*, Y=-19.531*
  2: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AC [0x00] END_REQSTACK()
```
