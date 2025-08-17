# 17776809 - Ajido-Marujido

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 300 bytes             |
| Total Events     | 9                     |
| References Count | 6                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [81](#event-81)          | 0x0001       |     18 |              4 |
| [65535.1](#event-655351) | 0x0013       |     29 |              3 |
| [65535.2](#event-655352) | 0x0030       |     29 |              3 |
| [65535.3](#event-655353) | 0x004D       |     29 |              3 |
| [65535.4](#event-655354) | 0x006A       |     29 |              3 |
| [65535.5](#event-655355) | 0x0087       |     29 |              3 |
| [65535.6](#event-655356) | 0x00A4       |     29 |              3 |
| [65535.7](#event-655357) | 0x00C1       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x878D      |       34701 |
|       1 | 0x10B54     |       68436 |
|       2 | 0x07C7      |        1991 |
|       3 | 0x0884      |        2180 |
|       4 | 0x00A5      |         165 |
|       5 | 0x0151      |         337 |

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

### Event 81

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 01 94 01 F8 FF FF  7F 37 00 80 01 80 02 80   ".......7......
0010: 03 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0003 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=34.701*, z=68.436*, y=1.991*, direction=191.6°*
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          5B 04 80 F8 FF  FF 7F F8 FF FF 7F 74 6C     [..........tl
0020: 6B 30 53 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 00  k0S........tlk0.
```

#### Opcodes

```
  0: 0x0013 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=165*
  1: 0x0022 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 5B 04 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 53  [..........tlk1S
0040: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 00           ........tlk1.   
```

#### Opcodes

```
  0: 0x0030 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=165*
  1: 0x003F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         5B 05 80               [..
0050: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 53 F8 FF FF  ........thk1S...
0060: 7F F8 FF FF 7F 74 68 6B  31 00                    .....thk1.      
```

#### Opcodes

```
  0: 0x004D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=337*
  1: 0x005C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                5B 05 80 F8 FF FF            [.....
0070: 7F F8 FF FF 7F 74 68 6B  32 53 F8 FF FF 7F F8 FF  .....thk2S......
0080: FF 7F 74 68 6B 32 00                              ..thk2.         
```

#### Opcodes

```
  0: 0x006A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=337*
  1: 0x0079 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      5B  04 80 F8 FF FF 7F F8 FF         [........
0090: FF 7F 6B 62 6B 30 53 F8  FF FF 7F F8 FF FF 7F 6B  ..kbk0S........k
00A0: 62 6B 30 00                                       bk0.            
```

#### Opcodes

```
  0: 0x0087 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kbk0" with entities [EventEntity, EventEntity], work=165*
  1: 0x0096 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kbk0" with entities [EventEntity, EventEntity]
  2: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             5B 04 80 F8  FF FF 7F F8 FF FF 7F 6B      [..........k
00B0: 62 6B 31 53 F8 FF FF 7F  F8 FF FF 7F 6B 62 6B 31  bk1S........kbk1
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00A4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kbk1" with entities [EventEntity, EventEntity], work=165*
  1: 0x00B3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kbk1" with entities [EventEntity, EventEntity]
  2: 0x00C0 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C1   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    5B 05 80 F8 FF FF 7F  F8 FF FF 7F 64 69 73 30   [..........dis0
00D0: 53 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 00        S........thk1.  
```

#### Opcodes

```
  0: 0x00C1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=337*
  1: 0x00D0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x00DD [0x00] END_REQSTACK()
```
