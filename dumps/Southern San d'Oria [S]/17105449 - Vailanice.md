# 17105449 - Vailanice

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 196 bytes                        |
| Total Events     | 8                                |
| References Count | 7                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [632](#event-632)        | 0x0001       |      1 |              1 |
| [633](#event-633)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     35 |              9 |
| [65535.2](#event-655352) | 0x0026       |     35 |              9 |
| [82](#event-82)          | 0x0049       |      1 |              1 |
| [65535.3](#event-655353) | 0x004A       |     25 |              3 |
| [65535.4](#event-655354) | 0x0063       |     19 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x000D      |          13 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0xFFFEFC71  |  4294900849 |
|       5 | 0x923D      |       37437 |
|       6 | 0x0166      |         358 |

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

### Event 632

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

### Event 633

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
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          03 00 00 25 10  03 02 00 27 10 03 01 00     ...%....'....
0010: 26 10 03 03 00 28 10 32  00 80 1F 00 00 00 02 00  &....(.2........
0020: 01 00 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0003 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0008 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x000D [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0012 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0017 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0024 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   03 00  00 25 10 03 02 00 27 10        ...%....'.
0030: 03 01 00 26 10 03 03 00  28 10 32 01 80 1F 00 00  ...&....(.2.....
0040: 00 02 00 01 00 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x0026 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x002B [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x0030 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0035 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x003A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0048 [0x00] END_REQSTACK()
```

### Event 82

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0049  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             00                             .      
```

#### Opcodes

```
  0: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                7E 06 F8 FF FF 7F            ~.....
0050: 02 80 03 80 02 80 02 80  02 80 02 80 7E 04 F8 FF  ............~...
0060: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x004A [0x7E] CHOCOBO_MOUNT: Mode 6 (custom mount) on EventEntity
  1: 0x005C [0x7E] CHOCOBO_MOUNT: Mode 4 on EventEntity
  2: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          59 04 0A 02 05  01 00 80 1F 00 04 80 05     Y............
0070: 80 06 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0063 [0x59] UPDATE_ENTITY_DATA: Set Excenmille (ID: 17105418/0x0105020A) main speed = 40* * 0.1
  1: 0x006B [0x1F] MOVE_ENTITY: EventEntity moves to X=-66.447*, Z=37.437*, Y=0.358*
  2: 0x0073 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0075 [0x00] END_REQSTACK()
```
