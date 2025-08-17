# 17780772 - Runga-Kopunga

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 364 bytes             |
| Total Events     | 14                    |
| References Count | 24                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      4 |              2 |
| [17](#event-17)            | 0x0004       |      1 |              1 |
| [154](#event-154)          | 0x0005       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0006       |      3 |              2 |
| [65535.2](#event-655352)   | 0x0009       |     20 |              4 |
| [65535.3](#event-655353)   | 0x001D       |     35 |              7 |
| [65535.4](#event-655354)   | 0x0040       |     19 |              3 |
| [65535.5](#event-655355)   | 0x0053       |      9 |              3 |
| [65535.6](#event-655356)   | 0x005C       |     29 |              3 |
| [65535.7](#event-655357)   | 0x0079       |     11 |              3 |
| [65535.8](#event-655358)   | 0x0084       |     10 |              2 |
| [65535.9](#event-655359)   | 0x008E       |     11 |              3 |
| [65535.10](#event-6553510) | 0x0099       |     29 |              3 |
| [65535.11](#event-6553511) | 0x00B6       |     13 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFFE9B4  |  4294961588 |
|       2 | 0xFFFF9EDA  |  4294942426 |
|       3 | 0xFFFFE891  |  4294961297 |
|       4 | 0x0D5D      |        3421 |
|       5 | 0xFFFFD967  |  4294957415 |
|       6 | 0xFFFF8B96  |  4294937494 |
|       7 | 0xFFFFC8AB  |  4294953131 |
|       8 | 0xFFFF643E  |  4294927422 |
|       9 | 0x0218      |         536 |
|      10 | 0xFFFFCEA2  |  4294954658 |
|      11 | 0xFFFF593D  |  4294924605 |
|      12 | 0x0028      |          40 |
|      13 | 0x001E      |          30 |
|      14 | 0x003C      |          60 |
|      15 | 0xFFFFC57B  |  4294952315 |
|      16 | 0xFFFF54A3  |  4294923427 |
|      17 | 0xFFFFBEAE  |  4294950574 |
|      18 | 0xFFFF6B16  |  4294929174 |
|      19 | 0x0D29      |        3369 |
|      20 | 0xFFFFC226  |  4294951462 |
|      21 | 0xFFFF739C  |  4294931356 |
|      22 | 0xFFFFCCDB  |  4294954203 |
|      23 | 0xFFFF8190  |  4294934928 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 32 00 80 00                                       2...            
```

#### Opcodes

```
  0: 0x0000 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 17

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

### Event 154

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                00                                      .          
```

#### Opcodes

```
  0: 0x0005 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   22 00  00                             "..       
```

#### Opcodes

```
  0: 0x0006 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0009   |
| Data Size    | 20 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             37 01 80 02 80 03 80           7......
0010: 04 80 1F 00 05 80 06 80  03 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-5.708*, z=-24.870*, y=-5.999*, direction=300.7°*
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=-9.881*, Z=-29.802*, Y=-5.999*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 35 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         37 07 80               7..
0020: 08 80 03 80 09 80 1F 00  0A 80 0B 80 03 80 1F 01  ................
0030: 4A 24 50 0F 01 23 50 0F  01 6F 76 24 50 0F 01 00  J$P..#P..ov$P...
```

#### Opcodes

```
  0: 0x001D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-14.165*, z=-39.874*, y=-5.999*, direction=47.1°*
  1: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.638*, Z=-42.691*, Y=-5.999*
  2: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0030 [0x4A] Runga-Kopunga (ID: 17780772/0x010F5024) looks at Chululu (ID: 17780771/0x010F5023)
  4: 0x0039 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x003A [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Runga-Kopunga (ID: 17780772/0x010F5024) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 66 0C 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1C  f..........tlk0.
0050: 0D 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0040 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x004F [0x1C] WAIT(30* ticks)
  2: 0x0052 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0053  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          5E 69 64 6C 30  1C 0E 80 00                 ^idl0....    
```

#### Opcodes

```
  0: 0x0053 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0058 [0x1C] WAIT(60* ticks)
  2: 0x005B [0x00] END_REQSTACK()
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
0050:                                      66 0C 80 F8              f...
0060: FF FF 7F F8 FF FF 7F 69  72 6F 30 53 F8 FF FF 7F  .......iro0S....
0070: F8 FF FF 7F 69 72 6F 30  00                       ....iro0.       
```

#### Opcodes

```
  0: 0x005C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=40*
  1: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iro0" with entities [EventEntity, EventEntity]
  2: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             1F 00 0F 80 10 80 03           .......
0080: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0079 [0x1F] MOVE_ENTITY: EventEntity moves to X=-14.981*, Z=-43.869*, Y=-5.999*
  1: 0x0081 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             37 11 80 12  80 03 80 13 80 00            7.........  
```

#### Opcodes

```
  0: 0x0084 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-16.722*, z=-38.122*, y=-5.999*, direction=296.1°*
  1: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            1F 00                ..
0090: 14 80 15 80 03 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x008E [0x1F] MOVE_ENTITY: EventEntity moves to X=-15.834*, Z=-35.940*, Y=-5.999*
  1: 0x0096 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             66 0C 80 F8 FF FF 7F           f......
00A0: F8 FF FF 7F 64 69 73 30  53 F8 FF FF 7F F8 FF FF  ....dis0S.......
00B0: 7F 64 69 73 30 00                                 .dis0.          
```

#### Opcodes

```
  0: 0x0099 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00A8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  2: 0x00B5 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B6   |
| Data Size    | 13 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   1F 00  16 80 17 80 03 80 1F 01        ..........
00C0: 22 01 00                                          "..             
```

#### Opcodes

```
  0: 0x00B6 [0x1F] MOVE_ENTITY: EventEntity moves to X=-13.093*, Z=-32.368*, Y=-5.999*
  1: 0x00BE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00C0 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x00C2 [0x00] END_REQSTACK()
```
