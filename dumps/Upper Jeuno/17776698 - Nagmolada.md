# 17776698 - Nagmolada

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 292 bytes             |
| Total Events     | 10                    |
| References Count | 10                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [207](#event-207)        | 0x000D       |     20 |              3 |
| [65535.1](#event-655351) | 0x0021       |     14 |              4 |
| [65535.2](#event-655352) | 0x002F       |     13 |              4 |
| [65535.3](#event-655353) | 0x003C       |     16 |              2 |
| [65535.4](#event-655354) | 0x004C       |     29 |              3 |
| [65535.5](#event-655355) | 0x0069       |     16 |              2 |
| [65535.6](#event-655356) | 0x0079       |     29 |              3 |
| [65535.7](#event-655357) | 0x0096       |     16 |              2 |
| [65535.8](#event-655358) | 0x00A6       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFEFC8D  |  4294900877 |
|       1 | 0x3AB5      |       15029 |
|       2 | 0x03E8      |        1000 |
|       3 | 0x01A4      |         420 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFF05C3  |  4294903235 |
|       6 | 0x4063      |       16483 |
|       7 | 0xFFFF1BCF  |  4294908879 |
|       8 | 0x5215      |       21013 |
|       9 | 0x01D1      |         465 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 94 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 207

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 79 00  F8 FF FF 7F 01 40 0F 01  ......y......@..
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-66.419*, z=15.029*, y=1.000*, direction=36.9°*
  1: 0x0016 [0x79] EventEntity looks at Monberaux (ID: 17776641/0x010F4001) (Basic look)
  2: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0021 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=-64.061*, Z=16.483*, Y=1.000*
  2: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 13 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               1F                 .
0030: 00 07 80 08 80 02 80 1F  01 22 01 00              ........."..    
```

#### Opcodes

```
  0: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=-58.417*, Z=21.013*, Y=1.000*
  1: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0039 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      5B 09 80 F8              [...
0040: FF FF 7F F8 FF FF 7F 74  6C 61 30 00              .......tla0.    
```

#### Opcodes

```
  0: 0x003C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=465*
  1: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      5B 09 80 F8              [...
0050: FF FF 7F F8 FF FF 7F 74  6C 61 31 53 F8 FF FF 7F  .......tla1S....
0060: F8 FF FF 7F 74 6C 61 31  00                       ....tla1.       
```

#### Opcodes

```
  0: 0x004C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [EventEntity, EventEntity], work=465*
  1: 0x005B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tla1" with entities [EventEntity, EventEntity]
  2: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             5B 09 80 F8 FF FF 7F           [......
0070: F8 FF FF 7F 74 6C 62 30  00                       ....tlb0.       
```

#### Opcodes

```
  0: 0x0069 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=465*
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             5B 09 80 F8 FF FF 7F           [......
0080: F8 FF FF 7F 74 6C 62 31  53 F8 FF FF 7F F8 FF FF  ....tlb1S.......
0090: 7F 74 6C 62 31 00                                 .tlb1.          
```

#### Opcodes

```
  0: 0x0079 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=465*
  1: 0x0088 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
  2: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0096   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   5B 09  80 F8 FF FF 7F F8 FF FF        [.........
00A0: 7F 74 68 62 30 00                                 .thb0.          
```

#### Opcodes

```
  0: 0x0096 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb0" with entities [EventEntity, EventEntity], work=465*
  1: 0x00A5 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A6   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                   5B 09  80 F8 FF FF 7F F8 FF FF        [.........
00B0: 7F 74 68 62 31 53 F8 FF  FF 7F F8 FF FF 7F 74 68  .thb1S........th
00C0: 62 31 00                                          b1.             
```

#### Opcodes

```
  0: 0x00A6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb1" with entities [EventEntity, EventEntity], work=465*
  1: 0x00B5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thb1" with entities [EventEntity, EventEntity]
  2: 0x00C2 [0x00] END_REQSTACK()
```
