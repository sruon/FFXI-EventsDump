# 17723581 - Aramaviont

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 344 bytes                     |
| Total Events     | 9                             |
| References Count | 24                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |     16 |              3 |
| [65535.1](#event-655351) | 0x0011       |     20 |              6 |
| [65535.2](#event-655352) | 0x0025       |     49 |             11 |
| [65535.3](#event-655353) | 0x0056       |     25 |              3 |
| [65535.4](#event-655354) | 0x006F       |     37 |              5 |
| [0](#event-0)            | 0x0094       |     13 |              3 |
| [65535.5](#event-655355) | 0x00A1       |     13 |              3 |
| [65535.6](#event-655356) | 0x00AE       |     20 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2013C     |      131388 |
|       1 | 0x1FED9     |      130777 |
|       2 | 0x0000      |           0 |
|       3 | 0x0371      |         881 |
|       4 | 0x0028      |          40 |
|       5 | 0x20D9B     |      134555 |
|       6 | 0x1F7E2     |      128994 |
|       7 | 0x22B21     |      142113 |
|       8 | 0x207AD     |      133037 |
|       9 | 0x0018      |          24 |
|      10 | 0x22F0A     |      143114 |
|      11 | 0x2001B     |      131099 |
|      12 | 0x0CE8      |        3304 |
|      13 | 0x001D      |          29 |
|      14 | 0x003C      |          60 |
|      15 | 0x03E8      |        1000 |
|      16 | 0xFFFFCDC3  |  4294954435 |
|      17 | 0x0C0F      |        3087 |
|      18 | 0x000D      |          13 |
|      19 | 0x3AE5      |       15077 |
|      20 | 0x050A      |        1290 |
|      21 | 0x16440     |       91200 |
|      22 | 0x1F294     |      127636 |
|      23 | 0xFFFFF830  |  4294965296 |

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
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   ......7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=131.388*, z=130.777*, y=0.000*, direction=77.4°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 6F 1E   2............o.
0020: CF 70 0E 01 00                                    .p...           
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=134.555*, Z=128.994*, Y=0.000*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001F [0x1E] EventEntity looks at Rochefogne (ID: 17723599/0x010E70CF) and starts talking
  5: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 49 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                32 04 80  1F 00 07 80 08 80 02 80       2..........
0030: 1F 01 6F 86 01 F8 FF FF  7F 1E CF 70 0E 01 6F 70  ..o........p..op
0040: 86 00 F8 FF FF 7F 66 09  80 F8 FF FF 7F F8 FF FF  ......f.........
0050: 7F 31 72 64 79 00                                 .1rdy.          
```

#### Opcodes

```
  0: 0x0025 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=142.113*, Z=133.037*, Y=0.000*
  2: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0033 [0x86] EventEntity->Render.Flags3 ^= 0x01
  5: 0x0039 [0x1E] EventEntity looks at Rochefogne (ID: 17723599/0x010E70CF) and starts talking
  6: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x003F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x0040 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  9: 0x0046 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
 10: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   37 0A  80 0B 80 02 80 0C 80 66        7........f
0060: 0D 80 F8 FF FF 7F F8 FF  FF 7F 73 68 61 30 00     ..........sha0. 
```

#### Opcodes

```
  0: 0x0056 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=143.114*, z=131.099*, y=0.000*, direction=290.4°*
  1: 0x005F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  2: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               1C                 .
0070: 0E 80 66 0D 80 F8 FF FF  7F F8 FF FF 7F 73 68 61  ..f..........sha
0080: 31 53 F8 FF FF 7F F8 FF  FF 7F 73 68 61 31 1E CF  1S........sha1..
0090: 70 0E 01 00                                       p...            
```

#### Opcodes

```
  0: 0x006F [0x1C] WAIT(60* ticks)
  1: 0x0072 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=29*
  2: 0x0081 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  3: 0x008E [0x1E] EventEntity looks at Rochefogne (ID: 17723599/0x010E70CF) and starts talking
  4: 0x0093 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             37 0F 80 10  80 02 80 11 80 32 12 80      7........2..
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0094 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=1.000*, z=-12.861*, y=0.000*, direction=271.3°*
  1: 0x009D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x00A0 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A1   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    31 00 0F 80 13 80 02  80 14 80 31 01 00         1.........1..  
```

#### Opcodes

```
  0: 0x00A1 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=1.000*, Z=15.077*, Y=0.000*, Time=1290*
  1: 0x00AB [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  2: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 20 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            37 0F                7.
00B0: 80 15 80 02 80 11 80 1F  00 0F 80 16 80 17 80 1F  ................
00C0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x00AE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=1.000*, z=91.200*, y=0.000*, direction=271.3°*
  1: 0x00B7 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.000*, Z=127.636*, Y=-2.000*
  2: 0x00BF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C1 [0x00] END_REQSTACK()
```
