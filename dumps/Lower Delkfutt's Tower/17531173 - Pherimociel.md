# 17531173 - Pherimociel

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 376 bytes                        |
| Total Events     | 12                               |
| References Count | 31                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [22](#event-22)          | 0x000D       |     10 |              2 |
| [38](#event-38)          | 0x0017       |      1 |              1 |
| [39](#event-39)          | 0x0018       |      1 |              1 |
| [65535.1](#event-655351) | 0x0019       |     40 |             11 |
| [65535.2](#event-655352) | 0x0041       |     10 |              2 |
| [65535.3](#event-655353) | 0x004B       |     16 |              2 |
| [65535.4](#event-655354) | 0x005B       |     34 |              4 |
| [65535.5](#event-655355) | 0x007D       |     24 |              6 |
| [65535.6](#event-655356) | 0x0095       |     10 |              2 |
| [65535.7](#event-655357) | 0x009F       |     22 |              8 |
| [65535.8](#event-655358) | 0x00B5       |      6 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x28551     |      165201 |
|       1 | 0xFFFFB72A  |  4294948650 |
|       2 | 0xFFFFB2A2  |  4294947490 |
|       3 | 0x0727      |        1831 |
|       4 | 0x0028      |          40 |
|       5 | 0x251AA     |      151978 |
|       6 | 0xFFFFBB53  |  4294949715 |
|       7 | 0xFFFFB120  |  4294947104 |
|       8 | 0x22068     |      139368 |
|       9 | 0xFFFFCBC1  |  4294953921 |
|      10 | 0xFFFFAEE2  |  4294946530 |
|      11 | 0x1A9FE     |      109054 |
|      12 | 0x2861      |       10337 |
|      13 | 0xFFFFB1E1  |  4294947297 |
|      14 | 0x71477     |      463991 |
|      15 | 0x20464     |      132196 |
|      16 | 0x001B      |          27 |
|      17 | 0x08E6      |        2278 |
|      18 | 0x001D      |          29 |
|      19 | 0x70A0C     |      461324 |
|      20 | 0x1F618     |      128536 |
|      21 | 0x0000      |           0 |
|      22 | 0x70862     |      460898 |
|      23 | 0x1BCB7     |      113847 |
|      24 | 0x05DB      |        1499 |
|      25 | 0x0393      |         915 |
|      26 | 0xFFFE2F14  |  4294848276 |
|      27 | 0xFFFF7554  |  4294931796 |
|      28 | 0x0C04      |        3076 |
|      29 | 0x07AB      |        1963 |
|      30 | 0xFFFE7286  |  4294865542 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 94 01 F8 FF FF 7F 92 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=165.201*, z=-18.646*, y=-19.806*, direction=160.9°*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 38

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      00                                  .        
```

#### Opcodes

```
  0: 0x0017 [0x00] END_REQSTACK()
```

### Event 39

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0018  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          00                               .       
```

#### Opcodes

```
  0: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 40 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             32 04 80 33 01 5A 00           2..3.Z.
0020: 05 80 06 80 07 80 5A 01  5A 00 08 80 09 80 0A 80  ......Z.Z.......
0030: 5A 01 5A 00 0B 80 0C 80  0D 80 5A 01 33 00 22 01  Z.Z.......Z.3.".
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0019 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001C [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x001E [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=151.978*, Z=-17.581*, Y=-20.192*
  3: 0x0026 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  4: 0x0028 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=139.368*, Z=-13.375*, Y=-20.766*
  5: 0x0030 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  6: 0x0032 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=109.054*, Z=10.337*, Y=-19.999*
  7: 0x003A [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  8: 0x003C [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  9: 0x003E [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 10: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    37 0E 80 0F 80 10 80  11 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0041 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=463.991*, z=132.196*, y=0.027*, direction=200.2°*
  1: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   66 12 80 F8 FF             f....
0050: FF 7F F8 FF FF 7F 73 68  61 30 00                 ......sha0.     
```

#### Opcodes

```
  0: 0x004B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   66 12 80 F8 FF             f....
0060: FF 7F F8 FF FF 7F 73 68  61 31 53 F8 FF FF 7F F8  ......sha1S.....
0070: FF FF 7F 73 68 61 31 1E  22 81 0B 01 00           ...sha1."....   
```

#### Opcodes

```
  0: 0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=29*
  1: 0x006A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  2: 0x0077 [0x1E] EventEntity looks at Wolfgang (ID: 17531170/0x010B8122) and starts talking
  3: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         32 04 80               2..
0080: 1F 00 13 80 14 80 15 80  1F 01 1F 00 16 80 17 80  ................
0090: 18 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x007D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0080 [0x1F] MOVE_ENTITY: EventEntity moves to X=461.324*, Z=128.536*, Y=0.000*
  2: 0x0088 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008A [0x1F] MOVE_ENTITY: EventEntity moves to X=460.898*, Z=113.847*, Y=1.499*
  4: 0x0092 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                37 19 80  1A 80 1B 80 1C 80 00          7......... 
```

#### Opcodes

```
  0: 0x0095 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.915*, z=-119.020*, y=-35.500*, direction=270.3°*
  1: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               32                 2
00A0: 04 80 1F 00 1D 80 1E 80  1B 80 1F 01 6F 1E 36 81  ............o.6.
00B0: 0B 01 6F 70 00                                    ..op.           
```

#### Opcodes

```
  0: 0x009F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00A2 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.963*, Z=-101.754*, Y=-35.500*
  2: 0x00AA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AD [0x1E] EventEntity looks at Unnamed NPC (ID: 17531190/0x010B8136) and starts talking
  5: 0x00B2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00B3 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B5  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                1E 22 81  0B 01 00                      ."....     
```

#### Opcodes

```
  0: 0x00B5 [0x1E] EventEntity looks at Wolfgang (ID: 17531170/0x010B8122) and starts talking
  1: 0x00BA [0x00] END_REQSTACK()
```
