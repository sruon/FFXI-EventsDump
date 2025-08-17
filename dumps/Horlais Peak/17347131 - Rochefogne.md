# 17347131 - Rochefogne

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Horlais Peak (ID: 139) |
| Block Size       | 396 bytes              |
| Total Events     | 11                     |
| References Count | 21                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |      1 |              1 |
| [32001](#event-32001)    | 0x0002       |     10 |              2 |
| [65535.1](#event-655351) | 0x000C       |     15 |              5 |
| [65535.2](#event-655352) | 0x001B       |     19 |              4 |
| [65535.3](#event-655353) | 0x002E       |     29 |              5 |
| [65535.4](#event-655354) | 0x004B       |     21 |              6 |
| [65535.5](#event-655355) | 0x0060       |     75 |             11 |
| [65535.6](#event-655356) | 0x00AB       |     40 |              5 |
| [65535.7](#event-655357) | 0x00D3       |     19 |              3 |
| [65535.8](#event-655358) | 0x00E6       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF9FFDC  |  4294574044 |
|       1 | 0xFFFEEAF5  |  4294896373 |
|       2 | 0x16FAE     |       94126 |
|       3 | 0x0B0A      |        2826 |
|       4 | 0x000A      |          10 |
|       5 | 0xFFF9FF11  |  4294573841 |
|       6 | 0xFFFEE6B3  |  4294895283 |
|       7 | 0x16F9C     |       94108 |
|       8 | 0x002D      |          45 |
|       9 | 0x0000      |           0 |
|      10 | 0x0096      |         150 |
|      11 | 0x000D      |          13 |
|      12 | 0xFFF9FD3C  |  4294573372 |
|      13 | 0xFFFEF08A  |  4294897802 |
|      14 | 0x17170     |       94576 |
|      15 | 0x001E      |          30 |
|      16 | 0x0027      |          39 |
|      17 | 0x0082      |         130 |
|      18 | 0x0001      |           1 |
|      19 | 0x003C      |          60 |
|      20 | 0x001D      |          29 |

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

### Event 32000

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

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-393.252*, z=-70.923*, y=94.126*, direction=248.4°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      32 04 80 1F              2...
0010: 00 05 80 06 80 07 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-393.455*, Z=-72.013*, Y=94.108*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1C 08 80 6C F8             ...l.
0020: FF FF 7F 09 80 0A 80 92  01 F8 FF FF 7F 00        ..............  
```

#### Opcodes

```
  0: 0x001B [0x1C] WAIT(45* ticks)
  1: 0x001E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=150*)
  2: 0x0027 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 29 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            53 F0                S.
0030: FF FF 7F F0 FF FF 7F 73  68 61 31 4A F0 FF FF 7F  .......sha1J....
0040: 47 B2 08 01 6F 76 F0 FF  FF 7F 00                 G...ov.....     
```

#### Opcodes

```
  0: 0x002E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [LocalPlayer, LocalPlayer]
  1: 0x003B [0x4A] LocalPlayer looks at Eideialc (ID: 17347143/0x0108B247)
  2: 0x0044 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0045 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  4: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 21 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   4E 00 3B B2 08             N.;..
0050: 01 32 0B 80 1F 00 0C 80  0D 80 0E 80 1F 01 6F 00  .2............o.
```

#### Opcodes

```
  0: 0x004B [0x4E] SET_ENTITY_HIDE_FLAG: Show Rochefogne (ID: 17347131/0x0108B23B)
  1: 0x0051 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=-393.924*, Z=-69.494*, Y=94.576*
  3: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 75 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 6E F8 FF FF 7F 0B 80 99  F8 FF FF 7F 1C 0F 80 4A  n..............J
0070: 47 B2 08 01 F8 FF FF 7F  1C 04 80 4A F0 FF FF 7F  G..........J....
0080: F8 FF FF 7F 1C 04 80 45  10 80 F0 FF FF 7F F0 FF  .......E........
0090: FF 7F 71 30 30 35 09 80  1C 11 80 55 10 80 F0 FF  ..q005.....U....
00A0: FF 7F F0 FF FF 7F 71 30  30 35 00                 ......q005.     
```

#### Opcodes

```
  0: 0x0060 [0x6E] EventEntity uses emote 13*
  1: 0x0067 [0x99] Wait for EventEntity animation to complete
  2: 0x006C [0x1C] WAIT(30* ticks)
  3: 0x006F [0x4A] Eideialc (ID: 17347143/0x0108B247) looks at EventEntity
  4: 0x0078 [0x1C] WAIT(10* ticks)
  5: 0x007B [0x4A] LocalPlayer looks at EventEntity
  6: 0x0084 [0x1C] WAIT(10* ticks)
  7: 0x0087 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "q005" with entities [LocalPlayer, LocalPlayer], work=[39*, 0*]
  8: 0x0098 [0x1C] WAIT(130* ticks)
  9: 0x009B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "q005" with entities [LocalPlayer, LocalPlayer], work=39*
 10: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AB   |
| Data Size    | 40 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   2C F8 FF FF 7F             ,....
00B0: F8 FF FF 7F 73 73 77 68  62 12 80 F8 FF FF 7F F8  ....sswhb.......
00C0: FF FF 7F 6D 61 69 6E 09  80 1C 13 80 92 01 F8 FF  ...main.........
00D0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x00AB [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sswh" with entities [EventEntity, EventEntity]
  1: 0x00B8 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[1*, 0*]
  2: 0x00C9 [0x1C] WAIT(60* ticks)
  3: 0x00CC [0x92] EventEntity->Render.Flags3 ^= 0x01
  4: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          66 14 80 F8 FF  FF 7F F8 FF FF 7F 74 68     f..........th
00E0: 6B 31 1C 0F 80 00                                 k1....          
```

#### Opcodes

```
  0: 0x00D3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x00E2 [0x1C] WAIT(30* ticks)
  2: 0x00E5 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E6   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   66 14  80 F8 FF FF 7F F8 FF FF        f.........
00F0: 7F 74 68 6B 32 1C 0F 80  00                       .thk2....       
```

#### Opcodes

```
  0: 0x00E6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
  1: 0x00F5 [0x1C] WAIT(30* ticks)
  2: 0x00F8 [0x00] END_REQSTACK()
```
