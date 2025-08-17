# 17105432 - Halver M Borel

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 156 bytes                        |
| Total Events     | 7                                |
| References Count | 5                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [55](#event-55)          | 0x0001       |      1 |              1 |
| [87](#event-87)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     15 |              5 |
| [60](#event-60)          | 0x0012       |      1 |              1 |
| [65535.2](#event-655352) | 0x0013       |     35 |              9 |
| [65535.3](#event-655353) | 0x0036       |     35 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x00B1      |         177 |
|       2 | 0xB860      |       47200 |
|       3 | 0xFFFFF831  |  4294965297 |
|       4 | 0x0028      |          40 |

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

### Event 55

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

### Event 87

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.177*, Z=47.200*, Y=-1.999*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       00                                            .             
```

#### Opcodes

```
  0: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          03 00 00 25 10  03 02 00 27 10 03 01 00     ...%....'....
0020: 26 10 03 03 00 28 10 32  04 80 1F 00 00 00 02 00  &....(.2........
0030: 01 00 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0013 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0018 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x001D [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0022 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0027 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0034 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   03 00  00 25 10 03 02 00 27 10        ...%....'.
0040: 03 01 00 26 10 03 03 00  28 10 32 00 80 1F 00 00  ...&....(.2.....
0050: 00 02 00 01 00 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x0036 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x003B [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x0040 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0045 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x004A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0057 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0058 [0x00] END_REQSTACK()
```
