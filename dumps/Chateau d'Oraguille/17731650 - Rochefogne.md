# 17731650 - Rochefogne

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 540 bytes                     |
| Total Events     | 19                            |
| References Count | 33                            |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [111](#event-111)          | 0x0001       |     10 |              2 |
| [8](#event-8)              | 0x000B       |     10 |              2 |
| [65535.1](#event-655351)   | 0x0015       |     15 |              5 |
| [65535.2](#event-655352)   | 0x0024       |     12 |              4 |
| [65535.3](#event-655353)   | 0x0030       |     12 |              3 |
| [65535.4](#event-655354)   | 0x003C       |     27 |              7 |
| [65535.5](#event-655355)   | 0x0057       |     12 |              4 |
| [65535.6](#event-655356)   | 0x0063       |      7 |              3 |
| [65535.7](#event-655357)   | 0x006A       |     16 |              6 |
| [65535.8](#event-655358)   | 0x007A       |     15 |              5 |
| [65535.9](#event-655359)   | 0x0089       |     26 |              4 |
| [65535.10](#event-6553510) | 0x00A3       |     16 |              5 |
| [65535.11](#event-6553511) | 0x00B3       |     29 |              3 |
| [65535.12](#event-6553512) | 0x00D0       |      9 |              3 |
| [65535.13](#event-6553513) | 0x00D9       |     19 |              3 |
| [65535.14](#event-6553514) | 0x00EC       |     19 |              3 |
| [65535.15](#event-6553515) | 0x00FF       |     29 |              3 |
| [65535.16](#event-6553516) | 0x011C       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE9DA0  |  4294876576 |
|       1 | 0x1301F     |       77855 |
|       2 | 0x018E      |         398 |
|       3 | 0x06F1      |        1777 |
|       4 | 0x027E      |         638 |
|       5 | 0x6141      |       24897 |
|       6 | 0xFFFFFA24  |  4294965796 |
|       7 | 0x0C2D      |        3117 |
|       8 | 0x000D      |          13 |
|       9 | 0x6911      |       26897 |
|      10 | 0x0000      |           0 |
|      11 | 0x90BC      |       37052 |
|      12 | 0xFFFFF449  |  4294964297 |
|      13 | 0x0BD0      |        3024 |
|      14 | 0xFFFE9996  |  4294875542 |
|      15 | 0x12EE5     |       77541 |
|      16 | 0xFFFE8CD7  |  4294872279 |
|      17 | 0x128EB     |       76011 |
|      18 | 0x0151      |         337 |
|      19 | 0x001E      |          30 |
|      20 | 0x005A      |          90 |
|      21 | 0x0BC1      |        3009 |
|      22 | 0x0078      |         120 |
|      23 | 0x0901      |        2305 |
|      24 | 0x003C      |          60 |
|      25 | 0x0028      |          40 |
|      26 | 0xFFFE6F8E  |  4294864782 |
|      27 | 0x10160     |       65888 |
|      28 | 0x0730      |        1840 |
|      29 | 0xFFFE7A50  |  4294867536 |
|      30 | 0x11B66     |       72550 |
|      31 | 0x0014      |          20 |
|      32 | 0x001D      |          29 |

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

### Event 111

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-90.720*, z=77.855*, y=0.398*, direction=156.2°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   37 04 80 05 80             7....
0010: 06 80 07 80 00                                    .....           
```

#### Opcodes

```
  0: 0x000B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.638*, z=24.897*, y=-1.500*, direction=273.9°*
  1: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                32 08 80  1F 00 04 80 09 80 06 80       2..........
0020: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0015 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.638*, Z=26.897*, Y=-1.500*
  2: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             1F 00 0A 80  0B 80 0C 80 1F 01 6F 00      ..........o.
```

#### Opcodes

```
  0: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=37.052*, Y=-2.999*
  1: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x002E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 33 01 37 0A 80 0B 80 0C  80 0D 80 00              3.7.........    
```

#### Opcodes

```
  0: 0x0030 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0032 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=37.052*, y=-2.999*, direction=265.8°*
  2: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      22 00 32 08              ".2.
0040: 80 79 00 42 90 0E 01 F0  FF FF 7F 1F 00 0E 80 0F  .y.B............
0050: 80 02 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x003C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x003E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0041 [0x79] Rochefogne (ID: 17731650/0x010E9042) looks at LocalPlayer (Basic look)
  3: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=-91.754*, Z=77.541*, Y=0.398*
  4: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0055 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      1F  00 10 80 11 80 02 80 1F         .........
0060: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=-95.017*, Z=76.011*, Y=0.398*
  1: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          39 12 80 1C 13  80 00                       9......      
```

#### Opcodes

```
  0: 0x0063 [0x39] SET_ENTITY_DIRECTION(direction=1.9°*)
  1: 0x0066 [0x1C] WAIT(30* ticks)
  2: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 16 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                1C 14 80 39 15 80            ...9..
0070: 1C 16 80 39 17 80 1C 18  80 00                    ...9......      
```

#### Opcodes

```
  0: 0x006A [0x1C] WAIT(90* ticks)
  1: 0x006D [0x39] SET_ENTITY_DIRECTION(direction=16.5°*)
  2: 0x0070 [0x1C] WAIT(120* ticks)
  3: 0x0073 [0x39] SET_ENTITY_DIRECTION(direction=12.7°*)
  4: 0x0076 [0x1C] WAIT(60* ticks)
  5: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                32 19 80 1F 00 1A            2.....
0080: 80 1B 80 02 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x007A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x007D [0x1F] MOVE_ENTITY: EventEntity moves to X=-102.514*, Z=65.888*, Y=0.398*
  2: 0x0085 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0087 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 26 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             37 10 80 11 80 02 80           7......
0090: 1C 80 2C 42 90 0E 01 42  90 0E 01 72 65 73 30 1C  ..,B...B...res0.
00A0: 13 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0089 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-95.017*, z=76.011*, y=0.398*, direction=161.7°*
  1: 0x0092 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res0" with entities [Rochefogne (ID: 17731650/0x010E9042), Rochefogne (ID: 17731650/0x010E9042)]
  2: 0x009F [0x1C] WAIT(30* ticks)
  3: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          32 08 80 1F 00  1D 80 1E 80 02 80 1F 01     2............
00B0: 22 01 00                                          "..             
```

#### Opcodes

```
  0: 0x00A3 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A6 [0x1F] MOVE_ENTITY: EventEntity moves to X=-99.760*, Z=72.550*, Y=0.398*
  2: 0x00AE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B0 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          66 1F 80 F8 FF  FF 7F F8 FF FF 7F 74 6C     f..........tl
00C0: 6B 30 53 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 00  k0S........tlk0.
```

#### Opcodes

```
  0: 0x00B3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x00C2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D0  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 5E 69 64 6C 30 1C 18 80  00                       ^idl0....       
```

#### Opcodes

```
  0: 0x00D0 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00D5 [0x1C] WAIT(60* ticks)
  2: 0x00D8 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D9   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                             66 1F 80 F8 FF FF 7F           f......
00E0: F8 FF FF 7F 74 68 6B 31  1C 18 80 00              ....thk1....    
```

#### Opcodes

```
  0: 0x00D9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x00E8 [0x1C] WAIT(60* ticks)
  2: 0x00EB [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EC   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      66 1F 80 F8              f...
00F0: FF FF 7F F8 FF FF 7F 74  68 6B 32 1C 18 80 00     .......thk2.... 
```

#### Opcodes

```
  0: 0x00EC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
  1: 0x00FB [0x1C] WAIT(60* ticks)
  2: 0x00FE [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FF   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                               66                 f
0100: 20 80 F8 FF FF 7F F8 FF  FF 7F 73 68 61 30 53 F8   .........sha0S.
0110: FF FF 7F F8 FF FF 7F 73  68 61 30 00              .......sha0.    
```

#### Opcodes

```
  0: 0x00FF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  1: 0x010E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  2: 0x011B [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011C   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                      66 20 80 F8              f ..
0120: FF FF 7F F8 FF FF 7F 73  68 61 31 53 F8 FF FF 7F  .......sha1S....
0130: F8 FF FF 7F 73 68 61 31  00                       ....sha1.       
```

#### Opcodes

```
  0: 0x011C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=29*
  1: 0x012B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  2: 0x0138 [0x00] END_REQSTACK()
```
