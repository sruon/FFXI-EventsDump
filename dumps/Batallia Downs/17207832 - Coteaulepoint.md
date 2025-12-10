# 17207832 - Coteaulepoint

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Batallia Downs (ID: 105) |
| Block Size       | 556 bytes                |
| Total Events     | 14                       |
| References Count | 36                       |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [904](#event-904)          | 0x0001       |     13 |              3 |
| [65535.1](#event-655351)   | 0x000E       |     11 |              3 |
| [65535.2](#event-655352)   | 0x0019       |     12 |              4 |
| [65535.3](#event-655353)   | 0x0025       |     10 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              4 |
| [65535.5](#event-655355)   | 0x003D       |     31 |             10 |
| [65535.6](#event-655356)   | 0x005C       |     29 |              3 |
| [65535.7](#event-655357)   | 0x0079       |     29 |              3 |
| [65535.8](#event-655358)   | 0x0096       |     29 |              3 |
| [65535.9](#event-655359)   | 0x00B3       |     38 |              4 |
| [65535.10](#event-6553510) | 0x00D9       |     59 |              7 |
| [65535.11](#event-6553511) | 0x0114       |     29 |              3 |
| [65535.12](#event-6553512) | 0x0131       |     34 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x347A8     |      214952 |
|       2 | 0xFFF6F0B0  |  4294373552 |
|       3 | 0x3301      |       13057 |
|       4 | 0x03A8      |         936 |
|       5 | 0x34546     |      214342 |
|       6 | 0xFFF6E604  |  4294370820 |
|       7 | 0x3513      |       13587 |
|       8 | 0x347B4     |      214964 |
|       9 | 0xFFF6E01A  |  4294369306 |
|      10 | 0x3477      |       13431 |
|      11 | 0x03C5      |         965 |
|      12 | 0x0028      |          40 |
|      13 | 0x34AF2     |      215794 |
|      14 | 0xFFF6C4C1  |  4294362305 |
|      15 | 0x3458      |       13400 |
|      16 | 0x37595     |      226709 |
|      17 | 0xFFF6A450  |  4294354000 |
|      18 | 0x74E7      |       29927 |
|      19 | 0x0505      |        1285 |
|      20 | 0x36B29     |      224041 |
|      21 | 0xFFF69804  |  4294350852 |
|      22 | 0x75C9      |       30153 |
|      23 | 0x000A      |          10 |
|      24 | 0x01D6      |         470 |
|      25 | 0x0017      |          23 |
|      26 | 0x000E      |          14 |
|      27 | 0x358A9     |      219305 |
|      28 | 0xFFF6D51F  |  4294366495 |
|      29 | 0x31C7      |       12743 |
|      30 | 0x00F4      |         244 |
|      31 | 0x001C      |          28 |
|      32 | 0x0000      |           0 |
|      33 | 0x0032      |          50 |
|      34 | 0x001D      |          29 |
|      35 | 0x003C      |          60 |

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

### Event 904

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    32 00 80 37 01 80 02  80 03 80 04 80 00         2..7.........  
```

#### Opcodes

```
  0: 0x0001 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=214.952*, z=-593.744*, y=13.057*, direction=82.3°*
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            1F 00                ..
0010: 05 80 06 80 07 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=214.342*, Z=-596.476*, Y=13.587*
  1: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             1F 00 08 80 09 80 0A           .......
0020: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=214.964*, Z=-597.990*, Y=13.431*
  1: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                37 08 80  09 80 0A 80 0B 80 00          7......... 
```

#### Opcodes

```
  0: 0x0025 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=214.964*, z=-597.990*, y=13.431*, direction=84.8°*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               32                 2
0030: 0C 80 1F 00 0D 80 0E 80  0F 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x002F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=215.794*, Z=-604.991*, Y=13.400*
  2: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 31 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         61 00 37               a.7
0040: 10 80 11 80 12 80 13 80  1F 00 14 80 15 80 16 80  ................
0050: 1F 01 6F 1C 17 80 39 18  80 6F 70 00              ..o...9..op.    
```

#### Opcodes

```
  0: 0x003D [0x61] EventEntity->Render.Flags2 &= ~0x00000001
  1: 0x003F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=226.709*, z=-613.296*, y=29.927*, direction=112.9°*
  2: 0x0048 [0x1F] MOVE_ENTITY: EventEntity moves to X=224.041*, Z=-616.444*, Y=30.153*
  3: 0x0050 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0052 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0053 [0x1C] WAIT(10* ticks)
  6: 0x0056 [0x39] SET_ENTITY_DIRECTION(direction=2.6°*)
  7: 0x0059 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x005A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  9: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      66 19 80 F8              f...
0060: FF FF 7F F8 FF FF 7F 6B  61 6D 30 53 F8 FF FF 7F  .......kam0S....
0070: F8 FF FF 7F 6B 61 6D 30  00                       ....kam0.       
```

#### Opcodes

```
  0: 0x005C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "kam0" with entities [EventEntity, EventEntity], work=23*
  1: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kam0" with entities [EventEntity, EventEntity]
  2: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             66 19 80 F8 FF FF 7F           f......
0080: F8 FF FF 7F 6B 61 6D 31  53 F8 FF FF 7F F8 FF FF  ....kam1S.......
0090: 7F 6B 61 6D 31 00                                 .kam1.          
```

#### Opcodes

```
  0: 0x0079 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "kam1" with entities [EventEntity, EventEntity], work=23*
  1: 0x0088 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kam1" with entities [EventEntity, EventEntity]
  2: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0096   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   5B 1A  80 F8 FF FF 7F F8 FF FF        [.........
00A0: 7F 61 65 76 30 53 F8 FF  FF 7F F8 FF FF 7F 61 65  .aev0S........ae
00B0: 76 30 00                                          v0.             
```

#### Opcodes

```
  0: 0x0096 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "aev0" with entities [EventEntity, EventEntity], work=14*
  1: 0x00A5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "aev0" with entities [EventEntity, EventEntity]
  2: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 38 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          37 1B 80 1C 80  1D 80 1E 80 5B 1A 80 F8     7........[...
00C0: FF FF 7F F8 FF FF 7F 61  65 76 31 53 F8 FF FF 7F  .......aev1S....
00D0: F8 FF FF 7F 61 65 76 31  00                       ....aev1.       
```

#### Opcodes

```
  0: 0x00B3 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=219.305*, z=-600.801*, y=12.743*, direction=21.4°*
  1: 0x00BC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "aev1" with entities [EventEntity, EventEntity], work=14*
  2: 0x00CB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "aev1" with entities [EventEntity, EventEntity]
  3: 0x00D8 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D9   |
| Data Size    | 59 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                             9F 1F 80 18 92 06 01           .......
00E0: 18 92 06 01 6D 61 69 6E  20 80 1C 17 80 5B 1A 80  ....main ....[..
00F0: F8 FF FF 7F F8 FF FF 7F  61 65 76 32 1C 21 80 5E  ........aev2.!.^
0100: 69 64 6C 30 66 22 80 F8  FF FF 7F F8 FF FF 7F 73  idl0f".........s
0110: 69 72 30 00                                       ir0.            
```

#### Opcodes

```
  0: 0x00D9 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [Coteaulepoint (ID: 17207832/0x01069218), Coteaulepoint (ID: 17207832/0x01069218)], work=[28*, 0*]
  1: 0x00EA [0x1C] WAIT(10* ticks)
  2: 0x00ED [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "aev2" with entities [EventEntity, EventEntity], work=14*
  3: 0x00FC [0x1C] WAIT(50* ticks)
  4: 0x00FF [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  5: 0x0104 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir0" with entities [EventEntity, EventEntity], work=29*
  6: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             66 22 80 F8  FF FF 7F F8 FF FF 7F 73      f".........s
0120: 68 61 31 53 F8 FF FF 7F  F8 FF FF 7F 73 68 61 31  ha1S........sha1
0130: 00                                                .               
```

#### Opcodes

```
  0: 0x0114 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0123 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  2: 0x0130 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0131   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:    66 22 80 F8 FF FF 7F  F8 FF FF 7F 73 68 61 30   f".........sha0
0140: 1C 23 80 66 22 80 F8 FF  FF 7F F8 FF FF 7F 73 69  .#.f".........si
0150: 72 30 00                                          r0.             
```

#### Opcodes

```
  0: 0x0131 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0140 [0x1C] WAIT(60* ticks)
  2: 0x0143 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir0" with entities [EventEntity, EventEntity], work=29*
  3: 0x0152 [0x00] END_REQSTACK()
```
