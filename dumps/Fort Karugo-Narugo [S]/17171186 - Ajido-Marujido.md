# 17171186 - Ajido-Marujido

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 180 bytes                       |
| Total Events     | 8                               |
| References Count | 11                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [102](#event-102)        | 0x0001       |      1 |              1 |
| [103](#event-103)        | 0x0002       |      1 |              1 |
| [101](#event-101)        | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     33 |              7 |
| [65535.2](#event-655352) | 0x0025       |     41 |              5 |
| [65535.3](#event-655353) | 0x004E       |      3 |              2 |
| [65535.4](#event-655354) | 0x0051       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0010      |          16 |
|       1 | 0x316F6     |      202486 |
|       2 | 0x9934      |       39220 |
|       3 | 0xFFFF92FB  |  4294939387 |
|       4 | 0x0005      |           5 |
|       5 | 0x0508      |        1288 |
|       6 | 0x007D      |         125 |
|       7 | 0x007F      |         127 |
|       8 | 0x0000      |           0 |
|       9 | 0x0014      |          20 |
|      10 | 0x02F8      |         760 |

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

### Event 102

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

### Event 103

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

### Event 101

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 1F  00 01 80 02 80 03 80 1F      2...........
0010: 01 6F 1C 04 80 5B 05 80  F2 02 06 01 F2 02 06 01  .o...[..........
0020: 73 74 64 32 00                                    std2.           
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 16* * 0.1
  1: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=202.486*, Z=39.220*, Y=-27.909*
  2: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0011 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0012 [0x1C] WAIT(5* ticks)
  5: 0x0015 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "std2" with entities [Ajido-Marujido (ID: 17171186/0x010602F2), Ajido-Marujido (ID: 17171186/0x010602F2)], work=1288*
  6: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                1C 06 80  9F 07 80 F8 FF FF 7F F8       ...........
0030: FF FF 7F 73 74 72 30 08  80 1C 09 80 9F 07 80 F8  ...str0.........
0040: FF FF 7F F8 FF FF 7F 6B  69 6C 6C 08 80 00        .......kill...  
```

#### Opcodes

```
  0: 0x0025 [0x1C] WAIT(125* ticks)
  1: 0x0028 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "str0" with entities [EventEntity, EventEntity], work=[127*, 0*]
  2: 0x0039 [0x1C] WAIT(20* ticks)
  3: 0x003C [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "kill" with entities [EventEntity, EventEntity], work=[127*, 0*]
  4: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004E  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            A4 01                ..
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x004E [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    39 0A 80 00                                     9...           
```

#### Opcodes

```
  0: 0x0051 [0x39] SET_ENTITY_DIRECTION(direction=4.2°*)
  1: 0x0054 [0x00] END_REQSTACK()
```
