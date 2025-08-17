# 17723580 - Milchupain

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 400 bytes                     |
| Total Events     | 10                            |
| References Count | 28                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |     18 |              4 |
| [65535.1](#event-655351) | 0x0013       |     20 |              6 |
| [65535.2](#event-655352) | 0x0027       |     49 |             11 |
| [65535.3](#event-655353) | 0x0058       |     25 |              3 |
| [65535.4](#event-655354) | 0x0071       |     37 |              5 |
| [65535.5](#event-655355) | 0x0096       |     35 |              9 |
| [0](#event-0)            | 0x00B9       |     13 |              3 |
| [65535.6](#event-655356) | 0x00C6       |     13 |              3 |
| [65535.7](#event-655357) | 0x00D3       |     20 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2200E     |      139278 |
|       1 | 0x225C2     |      140738 |
|       2 | 0xFFFFDF32  |  4294958898 |
|       3 | 0x011E      |         286 |
|       4 | 0x0028      |          40 |
|       5 | 0x2167C     |      136828 |
|       6 | 0x1ED89     |      126345 |
|       7 | 0x0000      |           0 |
|       8 | 0x225AE     |      140718 |
|       9 | 0x1FE88     |      130696 |
|      10 | 0x0018      |          24 |
|      11 | 0x2260A     |      140810 |
|      12 | 0x1F92A     |      129322 |
|      13 | 0x0AAA      |        2730 |
|      14 | 0x001D      |          29 |
|      15 | 0x005A      |          90 |
|      16 | 0x22605     |      140805 |
|      17 | 0x1FC5D     |      130141 |
|      18 | 0x0BD1      |        3025 |
|      19 | 0xFFFFFC18  |  4294966296 |
|      20 | 0xFFFFCDC3  |  4294954435 |
|      21 | 0x0C0F      |        3087 |
|      22 | 0x000D      |          13 |
|      23 | 0x3AE5      |       15077 |
|      24 | 0x050A      |        1290 |
|      25 | 0x16440     |       91200 |
|      26 | 0x1F294     |      127636 |
|      27 | 0xFFFFF830  |  4294965296 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 33  01 37 00 80 01 80 02 80   ......3.7......
0010: 03 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=139.278*, z=140.738*, y=-8.398*, direction=25.1°*
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          32 04 80 1F 00  05 80 06 80 07 80 1F 01     2............
0020: 6F 1E CF 70 0E 01 00                              o..p...         
```

#### Opcodes

```
  0: 0x0013 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0016 [0x1F] MOVE_ENTITY: EventEntity moves to X=136.828*, Z=126.345*, Y=0.000*
  2: 0x001E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0020 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0021 [0x1E] EventEntity looks at Rochefogne (ID: 17723599/0x010E70CF) and starts talking
  5: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 49 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  04 80 1F 00 08 80 09 80         2........
0030: 07 80 1F 01 6F 86 01 F8  FF FF 7F 1E CF 70 0E 01  ....o........p..
0040: 6F 70 86 00 F8 FF FF 7F  66 0A 80 F8 FF FF 7F F8  op......f.......
0050: FF FF 7F 31 72 64 79 00                           ...1rdy.        
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=140.718*, Z=130.696*, Y=0.000*
  2: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0034 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0035 [0x86] EventEntity->Render.Flags3 ^= 0x01
  5: 0x003B [0x1E] EventEntity looks at Rochefogne (ID: 17723599/0x010E70CF) and starts talking
  6: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0041 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x0042 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  9: 0x0048 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
 10: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          37 0B 80 0C 80 07 80 0D          7.......
0060: 80 66 0E 80 F8 FF FF 7F  F8 FF FF 7F 73 68 61 30  .f..........sha0
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0058 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=140.810*, z=129.322*, y=0.000*, direction=239.9°*
  1: 0x0061 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  2: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    1C 0F 80 66 0E 80 F8  FF FF 7F F8 FF FF 7F 73   ...f..........s
0080: 68 61 31 53 F8 FF FF 7F  F8 FF FF 7F 73 68 61 31  ha1S........sha1
0090: 1E CF 70 0E 01 00                                 ..p...          
```

#### Opcodes

```
  0: 0x0071 [0x1C] WAIT(90* ticks)
  1: 0x0074 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=29*
  2: 0x0083 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  3: 0x0090 [0x1E] EventEntity looks at Rochefogne (ID: 17723599/0x010E70CF) and starts talking
  4: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0096   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   32 04  80 1F 00 10 80 11 80 07        2.........
00A0: 80 1F 01 6F 39 12 80 6F  70 66 0E 80 F8 FF FF 7F  ...o9..opf......
00B0: F8 FF FF 7F 73 68 61 30  00                       ....sha0.       
```

#### Opcodes

```
  0: 0x0096 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0099 [0x1F] MOVE_ENTITY: EventEntity moves to X=140.805*, Z=130.141*, Y=0.000*
  2: 0x00A1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00A4 [0x39] SET_ENTITY_DIRECTION(direction=16.6°*)
  5: 0x00A7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00A8 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x00A9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  8: 0x00B8 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             37 13 80 14 80 07 80           7......
00C0: 15 80 32 16 80 00                                 ..2...          
```

#### Opcodes

```
  0: 0x00B9 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.000*, z=-12.861*, y=0.000*, direction=271.3°*
  1: 0x00C2 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   31 00  13 80 17 80 07 80 18 80        1.........
00D0: 31 01 00                                          1..             
```

#### Opcodes

```
  0: 0x00C6 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=-1.000*, Z=15.077*, Y=0.000*, Time=1290*
  1: 0x00D0 [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  2: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 20 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          37 13 80 19 80  07 80 15 80 1F 00 13 80     7............
00E0: 1A 80 1B 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x00D3 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.000*, z=91.200*, y=0.000*, direction=271.3°*
  1: 0x00DC [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.000*, Z=127.636*, Y=-2.000*
  2: 0x00E4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E6 [0x00] END_REQSTACK()
```
