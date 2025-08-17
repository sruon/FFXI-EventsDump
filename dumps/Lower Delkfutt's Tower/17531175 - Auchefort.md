# 17531175 - Auchefort

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 432 bytes                        |
| Total Events     | 11                               |
| References Count | 40                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [22](#event-22)          | 0x000D       |     10 |              2 |
| [38](#event-38)          | 0x0017       |      1 |              1 |
| [39](#event-39)          | 0x0018       |      1 |              1 |
| [65535.1](#event-655351) | 0x0019       |     40 |             11 |
| [65535.2](#event-655352) | 0x0041       |     10 |              2 |
| [65535.3](#event-655353) | 0x004B       |     25 |              3 |
| [65535.4](#event-655354) | 0x0064       |     62 |             10 |
| [65535.5](#event-655355) | 0x00A2       |     10 |              2 |
| [65535.6](#event-655356) | 0x00AC       |     17 |              5 |
| [65535.7](#event-655357) | 0x00BD       |     20 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x28551     |      165201 |
|       1 | 0xFFFFA74D  |  4294944589 |
|       2 | 0xFFFFB23F  |  4294947391 |
|       3 | 0x07A4      |        1956 |
|       4 | 0x0028      |          40 |
|       5 | 0x24E08     |      151048 |
|       6 | 0xFFFFACDF  |  4294946015 |
|       7 | 0xFFFFB1E9  |  4294947305 |
|       8 | 0x1EEF5     |      126709 |
|       9 | 0xFFFFE238  |  4294959672 |
|      10 | 0xFFFFB1B1  |  4294947249 |
|      11 | 0x12EE3     |       77539 |
|      12 | 0x5E61      |       24161 |
|      13 | 0xFFFFB4ED  |  4294948077 |
|      14 | 0x6F4A2     |      455842 |
|      15 | 0x2003D     |      131133 |
|      16 | 0x0013      |          19 |
|      17 | 0x0F73      |        3955 |
|      18 | 0x6FB8A     |      457610 |
|      19 | 0x205E3     |      132579 |
|      20 | 0x0005      |           5 |
|      21 | 0x02DA      |         730 |
|      22 | 0x001D      |          29 |
|      23 | 0x701F2     |      459250 |
|      24 | 0x1FC0D     |      130061 |
|      25 | 0x0000      |           0 |
|      26 | 0x7045A     |      459866 |
|      27 | 0x1E33D     |      123709 |
|      28 | 0x702A6     |      459430 |
|      29 | 0x19942     |      104770 |
|      30 | 0x0DAB      |        3499 |
|      31 | 0xFFFFFC64  |  4294966372 |
|      32 | 0xFFFE363A  |  4294850106 |
|      33 | 0xFFFF7554  |  4294931796 |
|      34 | 0x0BDC      |        3036 |
|      35 | 0xFFFFF88D  |  4294965389 |
|      36 | 0xFFFE48A8  |  4294854824 |
|      37 | 0x089E      |        2206 |
|      38 | 0xFFFFFC8F  |  4294966415 |
|      39 | 0xFFFE6DBF  |  4294864319 |

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
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=165.201*, z=-22.707*, y=-19.905*, direction=171.9°*
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
  2: 0x001E [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=151.048*, Z=-21.281*, Y=-19.991*
  3: 0x0026 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  4: 0x0028 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=126.709*, Z=-7.624*, Y=-20.047*
  5: 0x0030 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  6: 0x0032 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=77.539*, Z=24.161*, Y=-19.219*
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
  0: 0x0041 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=455.842*, z=131.133*, y=0.019*, direction=347.6°*
  1: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   37 12 80 13 80             7....
0050: 14 80 15 80 66 16 80 F8  FF FF 7F F8 FF FF 7F 73  ....f..........s
0060: 68 61 30 00                                       ha0.            
```

#### Opcodes

```
  0: 0x004B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=457.610*, z=132.579*, y=0.005*, direction=64.2°*
  1: 0x0054 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  2: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 62 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             66 16 80 F8  FF FF 7F F8 FF FF 7F 73      f..........s
0070: 68 61 31 53 F8 FF FF 7F  F8 FF FF 7F 73 68 61 30  ha1S........sha0
0080: 32 04 80 1F 00 17 80 18  80 19 80 1F 01 1F 00 1A  2...............
0090: 80 1B 80 19 80 1F 01 1F  00 1C 80 1D 80 1E 80 1F  ................
00A0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0064 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  2: 0x0080 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x0083 [0x1F] MOVE_ENTITY: EventEntity moves to X=459.250*, Z=130.061*, Y=0.000*
  4: 0x008B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x008D [0x1F] MOVE_ENTITY: EventEntity moves to X=459.866*, Z=123.709*, Y=0.000*
  6: 0x0095 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0097 [0x1F] MOVE_ENTITY: EventEntity moves to X=459.430*, Z=104.770*, Y=3.499*
  8: 0x009F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       37 1F 80 20 80 21  80 22 80 00                7.. .!."..    
```

#### Opcodes

```
  0: 0x00A2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.924*, z=-117.190*, y=-35.500*, direction=266.8°*
  1: 0x00AB [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      32 04 80 1F              2...
00B0: 00 23 80 24 80 21 80 1F  01 39 25 80 00           .#.$.!...9%..   
```

#### Opcodes

```
  0: 0x00AC [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00AF [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.907*, Z=-112.472*, Y=-35.500*
  2: 0x00B7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B9 [0x39] SET_ENTITY_DIRECTION(direction=12.1°*)
  4: 0x00BC [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BD   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                         32 04 80               2..
00C0: 1F 00 26 80 27 80 21 80  1F 01 6F 1E 22 81 0B 01  ..&.'.!...o."...
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00BD [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00C0 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.881*, Z=-102.977*, Y=-35.500*
  2: 0x00C8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00CA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00CB [0x1E] EventEntity looks at Wolfgang (ID: 17531170/0x010B8122) and starts talking
  5: 0x00D0 [0x00] END_REQSTACK()
```
