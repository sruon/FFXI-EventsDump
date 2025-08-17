# 17731655 - Coteaulepoint

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 264 bytes                     |
| Total Events     | 8                             |
| References Count | 7                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [76](#event-76)          | 0x0001       |     43 |              5 |
| [65535.1](#event-655351) | 0x002C       |     29 |              3 |
| [65535.2](#event-655352) | 0x0049       |     29 |              3 |
| [65535.3](#event-655353) | 0x0066       |     19 |              3 |
| [65535.4](#event-655354) | 0x0079       |     29 |              3 |
| [65535.5](#event-655355) | 0x0096       |     19 |              3 |
| [65535.6](#event-655356) | 0x00A9       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE73FA  |  4294865914 |
|       1 | 0x1035D     |       66397 |
|       2 | 0x018E      |         398 |
|       3 | 0x060E      |        1550 |
|       4 | 0x0018      |          24 |
|       5 | 0x001D      |          29 |
|       6 | 0x003C      |          60 |

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

### Event 76

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 80 F8 FF FF 7F 66   7.............f
0010: 04 80 F8 FF FF 7F F8 FF  FF 7F 31 72 64 79 53 F8  ..........1rdyS.
0020: FF FF 7F F8 FF FF 7F 31  72 64 79 00              .......1rdy.    
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-101.382*, z=66.397*, y=0.398*, direction=136.2°*
  1: 0x000A [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x000F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
  3: 0x001E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rdy" with entities [EventEntity, EventEntity]
  4: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      66 04 80 F8              f...
0030: FF FF 7F F8 FF FF 7F 31  72 64 79 53 F8 FF FF 7F  .......1rdyS....
0040: F8 FF FF 7F 31 72 64 79  00                       ....1rdy.       
```

#### Opcodes

```
  0: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
  1: 0x003B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rdy" with entities [EventEntity, EventEntity]
  2: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             66 04 80 F8 FF FF 7F           f......
0050: F8 FF FF 7F 31 72 74 6E  53 F8 FF FF 7F F8 FF FF  ....1rtnS.......
0060: 7F 31 72 74 6E 00                                 .1rtn.          
```

#### Opcodes

```
  0: 0x0049 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rtn" with entities [EventEntity, EventEntity], work=24*
  1: 0x0058 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rtn" with entities [EventEntity, EventEntity]
  2: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   66 05  80 F8 FF FF 7F F8 FF FF        f.........
0070: 7F 74 6C 6B 30 1C 06 80  00                       .tlk0....       
```

#### Opcodes

```
  0: 0x0066 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0075 [0x1C] WAIT(60* ticks)
  2: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             66 05 80 F8 FF FF 7F           f......
0080: F8 FF FF 7F 74 6C 6B 31  53 F8 FF FF 7F F8 FF FF  ....tlk1S.......
0090: 7F 74 6C 6B 31 00                                 .tlk1.          
```

#### Opcodes

```
  0: 0x0079 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0088 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0096   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   66 05  80 F8 FF FF 7F F8 FF FF        f.........
00A0: 7F 74 68 6B 31 1C 06 80  00                       .thk1....       
```

#### Opcodes

```
  0: 0x0096 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x00A5 [0x1C] WAIT(60* ticks)
  2: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             66 05 80 F8 FF FF 7F           f......
00B0: F8 FF FF 7F 74 68 6B 32  1C 06 80 00              ....thk2....    
```

#### Opcodes

```
  0: 0x00A9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
  1: 0x00B8 [0x1C] WAIT(60* ticks)
  2: 0x00BB [0x00] END_REQSTACK()
```
