# 17179468 - Vestillet

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 304 bytes                         |
| Total Events     | 10                                |
| References Count | 21                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [9](#event-9)            | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     13 |              3 |
| [65535.2](#event-655352) | 0x0015       |     14 |              4 |
| [10](#event-10)          | 0x0023       |      7 |              2 |
| [65535.3](#event-655353) | 0x002A       |     23 |              7 |
| [115](#event-115)        | 0x0041       |     27 |              3 |
| [65535.4](#event-655354) | 0x005C       |     22 |              6 |
| [116](#event-116)        | 0x0072       |     27 |              3 |
| [65535.5](#event-655355) | 0x008D       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0002      |           2 |
|       1 | 0x000D      |          13 |
|       2 | 0x09E8      |        2536 |
|       3 | 0x12C04     |       76804 |
|       4 | 0xFFFFEC79  |  4294962297 |
|       5 | 0x0028      |          40 |
|       6 | 0xFFFFFA99  |  4294965913 |
|       7 | 0x12A8A     |       76426 |
|       8 | 0xFFFFEC78  |  4294962296 |
|       9 | 0x001E      |          30 |
|      10 | 0x0003      |           3 |
|      11 | 0x0000      |           0 |
|      12 | 0x00D9      |         217 |
|      13 | 0x000C      |          12 |
|      14 | 0x00DD      |         221 |
|      15 | 0x000A      |          10 |
|      16 | 0xFFFF8796  |  4294936470 |
|      17 | 0x25CB      |        9675 |
|      18 | 0xFFFFFA25  |  4294965797 |
|      19 | 0x00FA      |         250 |
|      20 | 0x001B      |          27 |

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

### Event 9

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
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          6E 4C 23 06 01 00 80 99          nL#.....
0010: 4C 23 06 01 00                                    L#...           
```

#### Opcodes

```
  0: 0x0008 [0x6E] Vestillet (ID: 17179468/0x0106234C) uses emote 2*
  1: 0x000F [0x99] Wait for Vestillet (ID: 17179468/0x0106234C) animation to complete
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                32 01 80  1F 00 02 80 03 80 04 80       2..........
0020: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0015 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=2.536*, Z=76.804*, Y=-4.999*
  2: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0022 [0x00] END_REQSTACK()
```

### Event 10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0023  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0023 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 23 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                32 05 80 1F 00 06            2.....
0030: 80 07 80 08 80 1F 01 1E  46 23 06 01 1C 09 80 00  ........F#......
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x002A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.383*, Z=76.426*, Y=-5.000*
  2: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0037 [0x1E] EventEntity looks at Ragelise (ID: 17179462/0x01062346) and starts talking
  4: 0x003C [0x1C] WAIT(30* ticks)
  5: 0x003F [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0040 [0x00] END_REQSTACK()
```

### Event 115

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    92 01 F8 FF FF 7F B6  0B 0A 80 00 80 0B 80 0C   ...............
0050: 80 01 80 0D 80 0E 80 0B  80 0B 80 00              ............    
```

#### Opcodes

```
  0: 0x0041 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0047 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=0*, body=217*, hands=13*, legs=12*, feet=221*, main=0*, sub=0*)
  2: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      1C 0F 80 32              ...2
0060: 01 80 1F 00 10 80 11 80  12 80 1F 01 1E 71 23 06  .............q#.
0070: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x005C [0x1C] WAIT(10* ticks)
  1: 0x005F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0062 [0x1F] MOVE_ENTITY: EventEntity moves to X=-30.826*, Z=9.675*, Y=-1.499*
  3: 0x006A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x006C [0x1E] EventEntity looks at Cloud Walker (ID: 17179505/0x01062371) and starts talking
  5: 0x0071 [0x00] END_REQSTACK()
```

### Event 116

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       92 01 F8 FF FF 7F  B6 0B 0A 80 00 80 0B 80    ..............
0080: 0C 80 01 80 0D 80 0E 80  0B 80 0B 80 00           .............   
```

#### Opcodes

```
  0: 0x0072 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0078 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=0*, body=217*, hands=13*, legs=12*, feet=221*, main=0*, sub=0*)
  2: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         B6 0B 0A               ...
0090: 80 00 80 0B 80 0C 80 01  80 0D 80 0E 80 13 80 14  ................
00A0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x008D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=0*, body=217*, hands=13*, legs=12*, feet=221*, main=250*, sub=27*)
  1: 0x00A1 [0x00] END_REQSTACK()
```
