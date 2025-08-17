# 17343216 - Demon Suppressor

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 364 bytes                          |
| Total Events     | 12                                 |
| References Count | 29                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [2](#event-2)            | 0x0002       |      1 |              1 |
| [14](#event-14)          | 0x0003       |      1 |              1 |
| [3](#event-3)            | 0x0004       |      1 |              1 |
| [65535.1](#event-655351) | 0x0005       |     10 |              2 |
| [65535.2](#event-655352) | 0x000F       |     10 |              2 |
| [65535.3](#event-655353) | 0x0019       |     14 |              4 |
| [65535.4](#event-655354) | 0x0027       |     14 |              4 |
| [65535.5](#event-655355) | 0x0035       |     37 |              5 |
| [65535.6](#event-655356) | 0x005A       |     77 |             21 |
| [65535.7](#event-655357) | 0x00A7       |     17 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0x22B8B     |      142219 |
|       5 | 0xE022      |       57378 |
|       6 | 0xFFFFA207  |  4294943239 |
|       7 | 0x0028      |          40 |
|       8 | 0xFFFA3F78  |  4294590328 |
|       9 | 0x45F6      |       17910 |
|      10 | 0xFFFF6903  |  4294928643 |
|      11 | 0x0078      |         120 |
|      12 | 0x08B5      |        2229 |
|      13 | 0x00D2      |         210 |
|      14 | 0x0044      |          68 |
|      15 | 0x11CA3     |       72867 |
|      16 | 0x515A      |       20826 |
|      17 | 0xFFFFA220  |  4294943264 |
|      18 | 0x001E      |          30 |
|      19 | 0x11D03     |       72963 |
|      20 | 0x45D2      |       17874 |
|      21 | 0xFFFFA23A  |  4294943290 |
|      22 | 0x002D      |          45 |
|      23 | 0x19A0E     |      104974 |
|      24 | 0x4836      |       18486 |
|      25 | 0xFFFFA240  |  4294943296 |
|      26 | 0x214BD     |      136381 |
|      27 | 0x4CA2      |       19618 |
|      28 | 0xFFFFA231  |  4294943281 |

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

### Event 1

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

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0005   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                6C F0 A2  08 01 00 80 01 80 00          l......... 
```

#### Opcodes

```
  0: 0x0005 [0x6C] FADE_ENTITY_COLOR(entity_id=Demon Suppressor (ID: 17343216/0x0108A2F0), end_alpha=0*, fade_time=1*)
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               6C                 l
0010: F0 A2 08 01 02 80 01 80  00                       .........       
```

#### Opcodes

```
  0: 0x000F [0x6C] FADE_ENTITY_COLOR(entity_id=Demon Suppressor (ID: 17343216/0x0108A2F0), end_alpha=128*, fade_time=1*)
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             32 03 80 1F 00 04 80           2......
0020: 05 80 06 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0019 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=142.219*, Z=57.378*, Y=-24.057*
  2: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  07 80 1F 00 08 80 09 80         2........
0030: 0A 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=-376.968*, Z=17.910*, Y=-38.653*
  2: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                1C 0B 80  5B 0C 80 F0 A2 08 01 F0       ...[.......
0040: A2 08 01 77 61 6C 31 1C  0D 80 5B 0C 80 F0 A2 08  ...wal1...[.....
0050: 01 F0 A2 08 01 77 61 6C  32 00                    .....wal2.      
```

#### Opcodes

```
  0: 0x0035 [0x1C] WAIT(120* ticks)
  1: 0x0038 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wal1" with entities [Demon Suppressor (ID: 17343216/0x0108A2F0), Demon Suppressor (ID: 17343216/0x0108A2F0)], work=2229*
  2: 0x0047 [0x1C] WAIT(210* ticks)
  3: 0x004A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wal2" with entities [Demon Suppressor (ID: 17343216/0x0108A2F0), Demon Suppressor (ID: 17343216/0x0108A2F0)], work=2229*
  4: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 77 bytes |
| Instructions | 21       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                32 0E 80 1F 00 0F            2.....
0060: 80 10 80 11 80 1F 01 6F  1C 12 80 1F 00 13 80 14  .......o........
0070: 80 15 80 1F 01 6F 1C 16  80 1F 00 0F 80 10 80 11  .....o..........
0080: 80 1F 01 6F 1C 12 80 1F  00 13 80 14 80 15 80 1F  ...o............
0090: 01 6F 4B F0 A2 08 01 00  80 1C 12 80 1F 00 17 80  .oK.............
00A0: 18 80 19 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x005A [0x32] ExtData[1]->MainSpeed = 68* * 0.1
  1: 0x005D [0x1F] MOVE_ENTITY: EventEntity moves to X=72.867*, Z=20.826*, Y=-24.032*
  2: 0x0065 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0067 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0068 [0x1C] WAIT(30* ticks)
  5: 0x006B [0x1F] MOVE_ENTITY: EventEntity moves to X=72.963*, Z=17.874*, Y=-24.006*
  6: 0x0073 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0075 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0076 [0x1C] WAIT(45* ticks)
  9: 0x0079 [0x1F] MOVE_ENTITY: EventEntity moves to X=72.867*, Z=20.826*, Y=-24.032*
 10: 0x0081 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x0083 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 12: 0x0084 [0x1C] WAIT(30* ticks)
 13: 0x0087 [0x1F] MOVE_ENTITY: EventEntity moves to X=72.963*, Z=17.874*, Y=-24.006*
 14: 0x008F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 15: 0x0091 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 16: 0x0092 [0x4B] UPDATE_ENTITY_YAW(entity=Demon Suppressor (ID: 17343216/0x0108A2F0), yaw=0.0°*)
 17: 0x0099 [0x1C] WAIT(30* ticks)
 18: 0x009C [0x1F] MOVE_ENTITY: EventEntity moves to X=104.974*, Z=18.486*, Y=-24.000*
 19: 0x00A4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 20: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      1C  0B 80 32 0E 80 1F 00 1A         ...2.....
00B0: 80 1B 80 1C 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x00A7 [0x1C] WAIT(120* ticks)
  1: 0x00AA [0x32] ExtData[1]->MainSpeed = 68* * 0.1
  2: 0x00AD [0x1F] MOVE_ENTITY: EventEntity moves to X=136.381*, Z=19.618*, Y=-24.015*
  3: 0x00B5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00B7 [0x00] END_REQSTACK()
```
