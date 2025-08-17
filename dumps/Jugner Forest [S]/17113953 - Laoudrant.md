# 17113953 - Laoudrant

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 384 bytes                  |
| Total Events     | 14                         |
| References Count | 21                         |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [203](#event-203)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     25 |              3 |
| [65535.2](#event-655352)   | 0x001B       |      7 |              2 |
| [65535.3](#event-655353)   | 0x0022       |     15 |              5 |
| [65535.4](#event-655354)   | 0x0031       |     15 |              5 |
| [65535.5](#event-655355)   | 0x0040       |     15 |              5 |
| [206](#event-206)          | 0x004F       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0050       |     35 |              9 |
| [65535.7](#event-655357)   | 0x0073       |     35 |              9 |
| [65535.8](#event-655358)   | 0x0096       |     35 |              9 |
| [211](#event-211)          | 0x00B9       |      1 |              1 |
| [65535.9](#event-655359)   | 0x00BA       |     21 |              2 |
| [65535.10](#event-6553510) | 0x00CF       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0050      |          80 |
|       2 | 0x12721     |       75553 |
|       3 | 0x4B3BE     |      308158 |
|       4 | 0x00F3      |         243 |
|       5 | 0x11AC0     |       72384 |
|       6 | 0x4ECCC     |      322764 |
|       7 | 0x015E      |         350 |
|       8 | 0xF283      |       62083 |
|       9 | 0x4AABB     |      305851 |
|      10 | 0x0126      |         294 |
|      11 | 0x0028      |          40 |
|      12 | 0x000D      |          13 |
|      13 | 0x0003      |           3 |
|      14 | 0x0007      |           7 |
|      15 | 0x000C      |          12 |
|      16 | 0x00D2      |         210 |
|      17 | 0x0000      |           0 |
|      18 | 0x0038      |          56 |
|      19 | 0x00FB      |         251 |
|      20 | 0x001B      |          27 |

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

### Event 203

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
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       7E 06 F8 FF FF 7F  00 80 00 80 00 80 00 80    ~.............
0010: 00 80 00 80 7E 04 F8 FF  FF 7F 00                 ....~......     
```

#### Opcodes

```
  0: 0x0002 [0x7E] CHOCOBO_MOUNT: Mode 6 (custom mount) on EventEntity
  1: 0x0014 [0x7E] CHOCOBO_MOUNT: Mode 4 on EventEntity
  2: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   7E 05 F8 FF FF             ~....
0020: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x001B [0x7E] CHOCOBO_MOUNT: Dismount EventEntity (status = 0)
  1: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       32 01 80 1F 00 02  80 03 80 04 80 1F 01 6F    2............o
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0022 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=75.553*, Z=308.158*, Y=0.243*
  2: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    32 01 80 1F 00 05 80  06 80 07 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0031 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0034 [0x1F] MOVE_ENTITY: EventEntity moves to X=72.384*, Z=322.764*, Y=0.350*
  2: 0x003C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 32 01 80 1F 00 08 80 09  80 0A 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0040 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0043 [0x1F] MOVE_ENTITY: EventEntity moves to X=62.083*, Z=305.851*, Y=0.294*
  2: 0x004B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004E [0x00] END_REQSTACK()
```

### Event 206

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               00                 .
```

#### Opcodes

```
  0: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 03 00 00 25 10 03 01 00  27 10 03 02 00 26 10 03  ...%....'....&..
0060: 03 00 28 10 32 0B 80 1F  00 00 00 01 00 02 00 1F  ..(.2...........
0070: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0050 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0055 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[39]
  2: 0x005A [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[38]
  3: 0x005F [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0064 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x0067 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2]
  6: 0x006F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0071 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          03 00 00 25 10  03 01 00 27 10 03 02 00     ...%....'....
0080: 26 10 03 03 00 28 10 32  0C 80 1F 00 00 00 01 00  &....(.2........
0090: 02 00 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0073 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0078 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[39]
  2: 0x007D [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[38]
  3: 0x0082 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0087 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x008A [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2]
  6: 0x0092 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0094 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0096   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   03 00  00 25 10 03 01 00 27 10        ...%....'.
00A0: 03 02 00 26 10 03 03 00  28 10 32 0B 80 1F 00 00  ...&....(.2.....
00B0: 00 01 00 02 00 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x0096 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x009B [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[39]
  2: 0x00A0 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[38]
  3: 0x00A5 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x00AA [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x00AD [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2]
  6: 0x00B5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00B7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00B8 [0x00] END_REQSTACK()
```

### Event 211

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             00                             .      
```

#### Opcodes

```
  0: 0x00B9 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BA   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                B6 0B 0D 80 0E 80            ......
00C0: 0F 80 0F 80 0F 80 0F 80  0F 80 10 80 11 80 00     ............... 
```

#### Opcodes

```
  0: 0x00BA [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=7*, head=12*, body=12*, hands=12*, legs=12*, feet=12*, main=210*, sub=0*)
  1: 0x00CE [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CF   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                               B6                 .
00D0: 0B 0D 80 0E 80 12 80 0F  80 0F 80 0F 80 0F 80 13  ................
00E0: 80 14 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00CF [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=7*, head=56*, body=12*, hands=12*, legs=12*, feet=12*, main=251*, sub=27*)
  1: 0x00E3 [0x00] END_REQSTACK()
```
