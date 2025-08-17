# 17105424 - Alphonimile

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 576 bytes                        |
| Total Events     | 19                               |
| References Count | 33                               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [22](#event-22)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     35 |              7 |
| [65535.2](#event-655352)   | 0x0025       |     30 |              8 |
| [60](#event-60)            | 0x0043       |      1 |              1 |
| [65535.3](#event-655353)   | 0x0044       |     35 |              9 |
| [65535.4](#event-655354)   | 0x0067       |     35 |              9 |
| [65535.5](#event-655355)   | 0x008A       |     35 |              9 |
| [65535.6](#event-655356)   | 0x00AD       |     35 |              9 |
| [65535.7](#event-655357)   | 0x00D0       |     35 |              9 |
| [631](#event-631)          | 0x00F3       |      1 |              1 |
| [65535.8](#event-655358)   | 0x00F4       |     25 |              3 |
| [65535.9](#event-655359)   | 0x010D       |      7 |              2 |
| [65535.10](#event-6553510) | 0x0114       |     48 |             14 |
| [82](#event-82)            | 0x0144       |      1 |              1 |
| [65535.11](#event-6553511) | 0x0145       |     19 |              4 |
| [650](#event-650)          | 0x0158       |      1 |              1 |
| [65535.12](#event-6553512) | 0x0159       |      3 |              2 |
| [65535.13](#event-6553513) | 0x015C       |      3 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE9E17  |  4294876695 |
|       1 | 0xC4C1      |       50369 |
|       2 | 0xFFFFEF99  |  4294963097 |
|       3 | 0x0443      |        1091 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFE9CBF  |  4294876351 |
|       6 | 0xB488      |       46216 |
|       7 | 0xFFFFF060  |  4294963296 |
|       8 | 0x08EB      |        2283 |
|       9 | 0xFFFE6CDD  |  4294864093 |
|      10 | 0x7F46      |       32582 |
|      11 | 0xFFFFF830  |  4294965296 |
|      12 | 0xFFFE9AE8  |  4294875880 |
|      13 | 0x65CF      |       26063 |
|      14 | 0xFFFFF769  |  4294965097 |
|      15 | 0x0028      |          40 |
|      16 | 0x0050      |          80 |
|      17 | 0x0014      |          20 |
|      18 | 0x0001      |           1 |
|      19 | 0x0000      |           0 |
|      20 | 0x001E      |          30 |
|      21 | 0x007E      |         126 |
|      22 | 0xFFFE6E44  |  4294864452 |
|      23 | 0x03E7      |         999 |
|      24 | 0xFFFFFFDB  |  4294967259 |
|      25 | 0xFFFE4A88  |  4294855304 |
|      26 | 0xFFFFE9B3  |  4294961587 |
|      27 | 0xFFFE1E17  |  4294843927 |
|      28 | 0xFFFFC99D  |  4294953373 |
|      29 | 0xFFFDFF0A  |  4294835978 |
|      30 | 0xFFFE4259  |  4294853209 |
|      31 | 0x9147      |       37191 |
|      32 | 0xFFFFFF69  |  4294967145 |

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

### Event 22

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 35 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       BA 10 02 05 01 00  80 01 80 02 80 03 80 32    .............2
0010: 04 80 1F 00 05 80 06 80  07 80 1F 01 6F 4B 10 02  ............oK..
0020: 05 01 08 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0002 [0xBA] SET_ENTITY_POSITION(entity_id=Alphonimile (ID: 17105424/0x01050210), pos_x=-90.601*, pos_z=50.369*, pos_y=-4.199*, direction=95.9°*)
  1: 0x000F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=-90.945*, Z=46.216*, Y=-4.000*
  3: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x001C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x001D [0x4B] UPDATE_ENTITY_YAW(entity=Alphonimile (ID: 17105424/0x01050210), yaw=12.5°*)
  6: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                1F 00 09  80 0A 80 0B 80 1F 01 6F       ..........o
0030: 29 0F B4 01 05 01 04 1F  00 0C 80 0D 80 0E 80 1F  )...............
0040: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=-103.203*, Z=32.582*, Y=-2.000*
  1: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0030 [0x29] REQ_SET_WAIT(priority=0x0F, entity_id=Portcullis (ID: 17105332/0x010501B4), tag_num=0x04)
  4: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=-91.416*, Z=26.063*, Y=-2.199*
  5: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0041 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0042 [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          00                                          .            
```

#### Opcodes

```
  0: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             03 00 00 25  10 03 02 00 27 10 03 01      ...%....'...
0050: 00 26 10 03 03 00 28 10  32 0F 80 1F 00 00 00 02  .&....(.2.......
0060: 00 01 00 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0044 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0049 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x004E [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0053 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0058 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0065 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      03  00 00 25 10 03 02 00 27         ...%....'
0070: 10 03 01 00 26 10 03 03  00 28 10 32 04 80 1F 00  ....&....(.2....
0080: 00 00 02 00 01 00 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0067 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x006C [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x0071 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0076 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x007B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x007E [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0086 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0088 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                03 00 00 25 10 03            ...%..
0090: 02 00 27 10 03 01 00 26  10 03 03 00 28 10 32 10  ..'....&....(.2.
00A0: 80 1F 00 00 00 02 00 01  00 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x008A [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x008F [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x0094 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0099 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x009E [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  5: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00AB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         03 00 00               ...
00B0: 25 10 03 02 00 27 10 03  01 00 26 10 03 03 00 28  %....'....&....(
00C0: 10 32 0F 80 1F 00 00 00  02 00 01 00 1F 01 6F 00  .2............o.
```

#### Opcodes

```
  0: 0x00AD [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x00B2 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x00B7 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x00BC [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x00C1 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x00C4 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x00CC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00CE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D0   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 03 00 00 25 10 03 02 00  27 10 03 01 00 26 10 03  ...%....'....&..
00E0: 03 00 28 10 32 11 80 1F  00 00 00 02 00 01 00 1F  ..(.2...........
00F0: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x00D0 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x00D5 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x00DA [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x00DF [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x00E4 [0x32] ExtData[1]->MainSpeed = 20* * 0.1
  5: 0x00E7 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x00EF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00F1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00F2 [0x00] END_REQSTACK()
```

### Event 631

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:          00                                          .            
```

#### Opcodes

```
  0: 0x00F3 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F4   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:             7E 06 F8 FF  FF 7F 12 80 13 80 12 80      ~...........
0100: 12 80 12 80 12 80 7E 04  F8 FF FF 7F 00           ......~......   
```

#### Opcodes

```
  0: 0x00F4 [0x7E] CHOCOBO_MOUNT: Mode 6 (custom mount) on EventEntity
  1: 0x0106 [0x7E] CHOCOBO_MOUNT: Mode 4 on EventEntity
  2: 0x010C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         7E 05 F8               ~..
0110: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x010D [0x7E] CHOCOBO_MOUNT: Dismount EventEntity (status = 0)
  1: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 48 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             32 14 80 1F  00 15 80 16 80 17 80 1F      2...........
0120: 01 6F 1F 00 18 80 19 80  17 80 1F 01 6F 1F 00 1A  .o..........o...
0130: 80 1B 80 17 80 1F 01 6F  1F 00 1C 80 1D 80 17 80  .......o........
0140: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0114 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x0117 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.126*, Z=-102.844*, Y=0.999*
  2: 0x011F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0121 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0122 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.037*, Z=-111.992*, Y=0.999*
  5: 0x012A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x012C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x012D [0x1F] MOVE_ENTITY: EventEntity moves to X=-5.709*, Z=-123.369*, Y=0.999*
  8: 0x0135 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0137 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x0138 [0x1F] MOVE_ENTITY: EventEntity moves to X=-13.923*, Z=-131.318*, Y=0.999*
 11: 0x0140 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 12: 0x0142 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 13: 0x0143 [0x00] END_REQSTACK()
```

### Event 82

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0144  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:             00                                        .           
```

#### Opcodes

```
  0: 0x0144 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0145   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                59 04 10  02 05 01 0F 80 1F 00 1E       Y..........
0150: 80 1F 80 20 80 1F 01 00                           ... ....        
```

#### Opcodes

```
  0: 0x0145 [0x59] UPDATE_ENTITY_DATA: Set Alphonimile (ID: 17105424/0x01050210) main speed = 40* * 0.1
  1: 0x014D [0x1F] MOVE_ENTITY: EventEntity moves to X=-114.087*, Z=37.191*, Y=-0.151*
  2: 0x0155 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0157 [0x00] END_REQSTACK()
```

### Event 650

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0158  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                          00                               .       
```

#### Opcodes

```
  0: 0x0158 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0159  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                             61 01 00                       a..    
```

#### Opcodes

```
  0: 0x0159 [0x61] EventEntity->Render.Flags2 |= 0x00000001
  1: 0x015B [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x015C  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                      61 00 00                 a.. 
```

#### Opcodes

```
  0: 0x015C [0x61] EventEntity->Render.Flags2 &= ~0x00000001
  1: 0x015E [0x00] END_REQSTACK()
```
