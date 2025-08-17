# 17748124 - Louverance

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 456 bytes            |
| Total Events     | 16                   |
| References Count | 36                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [849](#event-849)        | 0x0007       |     10 |              2 |
| [65535.1](#event-655351) | 0x0011       |     30 |              6 |
| [65535.2](#event-655352) | 0x002F       |     15 |              5 |
| [65535.3](#event-655353) | 0x003E       |     26 |              7 |
| [850](#event-850)        | 0x0058       |     10 |              2 |
| [65535.4](#event-655354) | 0x0062       |     18 |              6 |
| [65535.5](#event-655355) | 0x0074       |     25 |              7 |
| [852](#event-852)        | 0x008D       |     10 |              2 |
| [65535.6](#event-655356) | 0x0097       |     15 |              5 |
| [853](#event-853)        | 0x00A6       |      1 |              1 |
| [65535.7](#event-655357) | 0x00A7       |     10 |              2 |
| [856](#event-856)        | 0x00B1       |      1 |              1 |
| [857](#event-857)        | 0x00B2       |     10 |              2 |
| [65535.8](#event-655358) | 0x00BC       |     15 |              5 |
| [65535.9](#event-655359) | 0x00CB       |     26 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF7222  |  4294930978 |
|       1 | 0xFFFFF976  |  4294965622 |
|       2 | 0xFFFFD8F1  |  4294957297 |
|       3 | 0x0010      |          16 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFFA6B1  |  4294944433 |
|       6 | 0xFFFFF9FC  |  4294965756 |
|       7 | 0x001D      |          29 |
|       8 | 0xFFFFAA99  |  4294945433 |
|       9 | 0xFFFFFB28  |  4294966056 |
|      10 | 0x0028      |          40 |
|      11 | 0xFFFF6FCD  |  4294930381 |
|      12 | 0xFFFFF95B  |  4294965595 |
|      13 | 0xFFFF6072  |  4294926450 |
|      14 | 0xFFFFE98B  |  4294961547 |
|      15 | 0xFFFFCF1C  |  4294954780 |
|      16 | 0xFFFFED58  |  4294962520 |
|      17 | 0xFFFFD514  |  4294956308 |
|      18 | 0x0D41      |        3393 |
|      19 | 0xFFFFD15A  |  4294955354 |
|      20 | 0xFFFFF5C0  |  4294964672 |
|      21 | 0x0B86      |        2950 |
|      22 | 0xFFFFC56B  |  4294952299 |
|      23 | 0xFFFFE6D8  |  4294960856 |
|      24 | 0xFFFF7C86  |  4294933638 |
|      25 | 0xFFFFF95E  |  4294965598 |
|      26 | 0x0F07      |        3847 |
|      27 | 0xFFFF96B1  |  4294940337 |
|      28 | 0xFFFFF70D  |  4294965005 |
|      29 | 0xFFFFA077  |  4294942839 |
|      30 | 0xFFFFF8C0  |  4294965440 |
|      31 | 0x0F49      |        3913 |
|      32 | 0xFFFF903A  |  4294938682 |
|      33 | 0xFFFFFA38  |  4294965816 |
|      34 | 0x0047      |          71 |
|      35 | 0xFFFFA3C2  |  4294943682 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 849

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      37  00 80 01 80 02 80 03 80         7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-36.318*, z=-1.674*, y=-9.999*, direction=1.4°*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 30 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 6F 66   2............of
0020: 07 80 9C D0 0E 01 9C D0  0E 01 74 6C 6B 30 00     ..........tlk0. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-22.863*, Z=-1.540*, Y=-9.999*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Louverance (ID: 17748124/0x010ED09C), Louverance (ID: 17748124/0x010ED09C)], work=29*
  5: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               32                 2
0030: 04 80 1F 00 08 80 09 80  02 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x002F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=-21.863*, Z=-1.240*, Y=-9.999*
  2: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            32 0A                2.
0040: 80 1F 00 0B 80 0C 80 02  80 1F 01 1F 00 0D 80 0E  ................
0050: 80 02 80 1F 01 22 01 00                           ....."..        
```

#### Opcodes

```
  0: 0x003E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0041 [0x1F] MOVE_ENTITY: EventEntity moves to X=-36.915*, Z=-1.701*, Y=-9.999*
  2: 0x0049 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=-40.846*, Z=-5.749*, Y=-9.999*
  4: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0055 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x0057 [0x00] END_REQSTACK()
```

### Event 850

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          37 0F 80 10 80 11 80 12          7.......
0060: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0058 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-12.516*, z=-4.776*, y=-10.988*, direction=298.2°*
  1: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       32 04 80 1F 00 13  80 14 80 11 80 1F 01 6F    2............o
0070: 39 15 80 00                                       9...            
```

#### Opcodes

```
  0: 0x0062 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0065 [0x1F] MOVE_ENTITY: EventEntity moves to X=-11.942*, Z=-2.624*, Y=-10.988*
  2: 0x006D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0070 [0x39] SET_ENTITY_DIRECTION(direction=16.2°*)
  5: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             32 04 80 1F  00 0F 80 10 80 11 80 1F      2...........
0080: 01 1F 00 16 80 17 80 11  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x0074 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0077 [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.516*, Z=-4.776*, Y=-10.988*
  2: 0x007F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0081 [0x1F] MOVE_ENTITY: EventEntity moves to X=-14.997*, Z=-6.440*, Y=-10.988*
  4: 0x0089 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x008B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x008C [0x00] END_REQSTACK()
```

### Event 852

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         37 18 80               7..
0090: 19 80 02 80 1A 80 00                              .......         
```

#### Opcodes

```
  0: 0x008D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-33.658*, z=-1.698*, y=-9.999*, direction=338.1°*
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      32  0A 80 1F 00 1B 80 1C 80         2........
00A0: 02 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0097 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x009A [0x1F] MOVE_ENTITY: EventEntity moves to X=-26.959*, Z=-2.291*, Y=-9.999*
  2: 0x00A2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00A5 [0x00] END_REQSTACK()
```

### Event 853

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                   00                                    .         
```

#### Opcodes

```
  0: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      37  1D 80 1E 80 02 80 1F 80         7........
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x00A7 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-24.457*, z=-1.856*, y=-9.999*, direction=343.9°*
  1: 0x00B0 [0x00] END_REQSTACK()
```

### Event 856

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    00                                              .              
```

#### Opcodes

```
  0: 0x00B1 [0x00] END_REQSTACK()
```

### Event 857

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       37 20 80 21 80 02  80 22 80 00                7 .!..."..    
```

#### Opcodes

```
  0: 0x00B2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-28.614*, z=-1.480*, y=-9.999*, direction=6.2°*
  1: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      32 04 80 1F              2...
00C0: 00 23 80 21 80 02 80 1F  01 6F 00                 .#.!.....o.     
```

#### Opcodes

```
  0: 0x00BC [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00BF [0x1F] MOVE_ENTITY: EventEntity moves to X=-23.614*, Z=-1.480*, Y=-9.999*
  2: 0x00C7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00CA [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CB   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                   32 04 80 1F 00             2....
00D0: 0B 80 0C 80 02 80 1F 01  1F 00 0D 80 0E 80 02 80  ................
00E0: 1F 01 22 01 00                                    .."..           
```

#### Opcodes

```
  0: 0x00CB [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00CE [0x1F] MOVE_ENTITY: EventEntity moves to X=-36.915*, Z=-1.701*, Y=-9.999*
  2: 0x00D6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-40.846*, Z=-5.749*, Y=-9.999*
  4: 0x00E0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00E2 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x00E4 [0x00] END_REQSTACK()
```
