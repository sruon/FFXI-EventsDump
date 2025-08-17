# 17772554 - Ealdnarche

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 572 bytes                 |
| Total Events     | 16                        |
| References Count | 26                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      3 |              2 |
| [128](#event-128)          | 0x0003       |     10 |              2 |
| [65535.1](#event-655351)   | 0x000D       |     78 |             17 |
| [60](#event-60)            | 0x005B       |     10 |              2 |
| [65535.2](#event-655352)   | 0x0065       |     18 |              6 |
| [65535.3](#event-655353)   | 0x0077       |     54 |             11 |
| [65535.4](#event-655354)   | 0x00AD       |     19 |              3 |
| [65535.5](#event-655355)   | 0x00C0       |     29 |              3 |
| [65535.6](#event-655356)   | 0x00DD       |     19 |              3 |
| [65535.7](#event-655357)   | 0x00F0       |     29 |              3 |
| [65535.8](#event-655358)   | 0x010D       |     19 |              3 |
| [65535.9](#event-655359)   | 0x0120       |     29 |              3 |
| [65535.10](#event-6553510) | 0x013D       |     29 |              3 |
| [65535.11](#event-6553511) | 0x015A       |     29 |              3 |
| [65535.12](#event-6553512) | 0x0177       |      9 |              3 |
| [65535.13](#event-6553513) | 0x0180       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFEBCB  |  4294962123 |
|       1 | 0x1816A     |       98666 |
|       2 | 0xFFFFE4AC  |  4294960300 |
|       3 | 0x0409      |        1033 |
|       4 | 0x001E      |          30 |
|       5 | 0xFFFFEAA3  |  4294961827 |
|       6 | 0x17304     |       94980 |
|       7 | 0xFFFFF523  |  4294964515 |
|       8 | 0x1725C     |       94812 |
|       9 | 0xFFFFFBCE  |  4294966222 |
|      10 | 0x170E8     |       94440 |
|      11 | 0xFFFFE230  |  4294959664 |
|      12 | 0x000A      |          10 |
|      13 | 0xFFFFFF60  |  4294967136 |
|      14 | 0x10BB2     |       68530 |
|      15 | 0xFFFFEC79  |  4294962297 |
|      16 | 0x0BB0      |        2992 |
|      17 | 0x003C      |          60 |
|      18 | 0xFFFFFFE0  |  4294967264 |
|      19 | 0x1197B     |       72059 |
|      20 | 0x04C5      |        1221 |
|      21 | 0x11F14     |       73492 |
|      22 | 0x0000      |           0 |
|      23 | 0x12530     |       75056 |
|      24 | 0x153DA     |       87002 |
|      25 | 0x0064      |         100 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 22 01 00                                          "..             
```

#### Opcodes

```
  0: 0x0000 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0002 [0x00] END_REQSTACK()
```

### Event 128

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          37 00 80 01 80  02 80 03 80 00              7.........   
```

#### Opcodes

```
  0: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-5.173*, z=98.666*, y=-6.996*, direction=90.8°*
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 78 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         22 00 32               ".2
0010: 04 80 1F 00 05 80 06 80  02 80 1F 01 4A F0 FF FF  ............J...
0020: 7F 0A 30 0F 01 1F 00 07  80 08 80 02 80 1F 01 4A  ..0............J
0030: F0 FF FF 7F 0A 30 0F 01  1F 00 09 80 0A 80 0B 80  .....0..........
0040: 1F 01 6F 4A F0 FF FF 7F  0A 30 0F 01 1E F0 FF FF  ..oJ.....0......
0050: 7F 6F 76 F8 FF FF 7F 32  0C 80 00                 .ov....2...     
```

#### Opcodes

```
  0: 0x000D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x000F [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  2: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=-5.469*, Z=94.980*, Y=-6.996*
  3: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x001C [0x4A] LocalPlayer looks at Eald'narche (ID: 17772554/0x010F300A)
  5: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.781*, Z=94.812*, Y=-6.996*
  6: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x002F [0x4A] LocalPlayer looks at Eald'narche (ID: 17772554/0x010F300A)
  8: 0x0038 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.074*, Z=94.440*, Y=-7.632*
  9: 0x0040 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 10: 0x0042 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x0043 [0x4A] LocalPlayer looks at Eald'narche (ID: 17772554/0x010F300A)
 12: 0x004C [0x1E] EventEntity looks at LocalPlayer and starts talking
 13: 0x0051 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 14: 0x0052 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
 15: 0x0057 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
 16: 0x005A [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   37 0D 80 0E 80             7....
0060: 0F 80 10 80 00                                    .....           
```

#### Opcodes

```
  0: 0x005B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.160*, z=68.530*, y=-4.999*, direction=263.0°*
  1: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                1C 11 80  32 04 80 1F 00 12 80 13       ...2.......
0070: 80 0F 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0065 [0x1C] WAIT(60* ticks)
  1: 0x0068 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  2: 0x006B [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.032*, Z=72.059*, Y=-4.999*
  3: 0x0073 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0075 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 54 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      32  04 80 1F 00 14 80 15 80         2........
0080: 0F 80 1F 01 4A F0 FF FF  7F F8 FF FF 7F 1F 00 16  ....J...........
0090: 80 17 80 0F 80 1F 01 4A  F0 FF FF 7F F8 FF FF 7F  .......J........
00A0: 1F 00 16 80 18 80 0F 80  1F 01 22 01 00           .........."..   
```

#### Opcodes

```
  0: 0x0077 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=1.221*, Z=73.492*, Y=-4.999*
  2: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0084 [0x4A] LocalPlayer looks at EventEntity
  4: 0x008D [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=75.056*, Y=-4.999*
  5: 0x0095 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0097 [0x4A] LocalPlayer looks at EventEntity
  7: 0x00A0 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=87.002*, Y=-4.999*
  8: 0x00A8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00AA [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 10: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         5B 19 80               [..
00B0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1C 11 80 00  ........tlk0....
```

#### Opcodes

```
  0: 0x00AD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=100*
  1: 0x00BC [0x1C] WAIT(60* ticks)
  2: 0x00BF [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C0   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 5B 19 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 53  [..........tlk1S
00D0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 00           ........tlk1.   
```

#### Opcodes

```
  0: 0x00C0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=100*
  1: 0x00CF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x00DC [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         5B 19 80               [..
00E0: F8 FF FF 7F F8 FF FF 7F  74 6C 61 30 1C 04 80 00  ........tla0....
```

#### Opcodes

```
  0: 0x00DD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=100*
  1: 0x00EC [0x1C] WAIT(30* ticks)
  2: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F0   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: 5B 19 80 F8 FF FF 7F F8  FF FF 7F 74 6C 61 31 53  [..........tla1S
0100: F8 FF FF 7F F8 FF FF 7F  74 6C 61 31 00           ........tla1.   
```

#### Opcodes

```
  0: 0x00F0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [EventEntity, EventEntity], work=100*
  1: 0x00FF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tla1" with entities [EventEntity, EventEntity]
  2: 0x010C [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010D   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         5B 19 80               [..
0110: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 1C 11 80 00  ........thk1....
```

#### Opcodes

```
  0: 0x010D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=100*
  1: 0x011C [0x1C] WAIT(60* ticks)
  2: 0x011F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 5B 19 80 F8 FF FF 7F F8  FF FF 7F 74 68 6B 32 53  [..........thk2S
0130: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 00           ........thk2.   
```

#### Opcodes

```
  0: 0x0120 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=100*
  1: 0x012F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x013C [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013D   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                         5B 19 80               [..
0140: F8 FF FF 7F F8 FF FF 7F  74 65 6C 30 53 F8 FF FF  ........tel0S...
0150: 7F F8 FF FF 7F 74 65 6C  30 00                    .....tel0.      
```

#### Opcodes

```
  0: 0x013D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tel0" with entities [EventEntity, EventEntity], work=100*
  1: 0x014C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tel0" with entities [EventEntity, EventEntity]
  2: 0x0159 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015A   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                5B 19 80 F8 FF FF            [.....
0160: 7F F8 FF FF 7F 74 65 6C  31 53 F8 FF FF 7F F8 FF  .....tel1S......
0170: FF 7F 74 65 6C 31 00                              ..tel1.         
```

#### Opcodes

```
  0: 0x015A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tel1" with entities [EventEntity, EventEntity], work=100*
  1: 0x0169 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tel1" with entities [EventEntity, EventEntity]
  2: 0x0176 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0177  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                      5E  69 64 6C 30 1C 04 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0177 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x017C [0x1C] WAIT(30* ticks)
  2: 0x017F [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0180  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180: 00                                                .               
```

#### Opcodes

```
  0: 0x0180 [0x00] END_REQSTACK()
```
