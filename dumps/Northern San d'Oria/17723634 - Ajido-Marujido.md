# 17723634 - Ajido-Marujido

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 296 bytes                     |
| Total Events     | 9                             |
| References Count | 6                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [36](#event-36)          | 0x0001       |     16 |              3 |
| [65535.1](#event-655351) | 0x0011       |     29 |              3 |
| [65535.2](#event-655352) | 0x002E       |     29 |              3 |
| [65535.3](#event-655353) | 0x004B       |     29 |              3 |
| [65535.4](#event-655354) | 0x0068       |     29 |              3 |
| [65535.5](#event-655355) | 0x0085       |     29 |              3 |
| [65535.6](#event-655356) | 0x00A2       |     29 |              3 |
| [65535.7](#event-655357) | 0x00BF       |     29 |              3 |

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

### Event 36

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    94 01 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   ......7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=34.701*, z=68.436*, y=1.991*, direction=191.6°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5B 04 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0020: 53 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 00        S........tlk0.  
```

#### Opcodes

```
  0: 0x0011 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=165*
  1: 0x0020 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            5B 04                [.
0030: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 31 53 F8 FF  .........tlk1S..
0040: FF 7F F8 FF FF 7F 74 6C  6B 31 00                 ......tlk1.     
```

#### Opcodes

```
  0: 0x002E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=165*
  1: 0x003D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   5B 05 80 F8 FF             [....
0050: FF 7F F8 FF FF 7F 74 68  6B 31 53 F8 FF FF 7F F8  ......thk1S.....
0060: FF FF 7F 74 68 6B 31 00                           ...thk1.        
```

#### Opcodes

```
  0: 0x004B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=337*
  1: 0x005A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          5B 05 80 F8 FF FF 7F F8          [.......
0070: FF FF 7F 74 68 6B 32 53  F8 FF FF 7F F8 FF FF 7F  ...thk2S........
0080: 74 68 6B 32 00                                    thk2.           
```

#### Opcodes

```
  0: 0x0068 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=337*
  1: 0x0077 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                5B 04 80  F8 FF FF 7F F8 FF FF 7F       [..........
0090: 6B 62 6B 30 53 F8 FF FF  7F F8 FF FF 7F 6B 62 6B  kbk0S........kbk
00A0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0085 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kbk0" with entities [EventEntity, EventEntity], work=165*
  1: 0x0094 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kbk0" with entities [EventEntity, EventEntity]
  2: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       5B 04 80 F8 FF FF  7F F8 FF FF 7F 6B 62 6B    [..........kbk
00B0: 31 53 F8 FF FF 7F F8 FF  FF 7F 6B 62 6B 31 00     1S........kbk1. 
```

#### Opcodes

```
  0: 0x00A2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kbk1" with entities [EventEntity, EventEntity], work=165*
  1: 0x00B1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kbk1" with entities [EventEntity, EventEntity]
  2: 0x00BE [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               5B                 [
00C0: 05 80 F8 FF FF 7F F8 FF  FF 7F 64 69 73 30 53 F8  ..........dis0S.
00D0: FF FF 7F F8 FF FF 7F 74  68 6B 31 00              .......thk1.    
```

#### Opcodes

```
  0: 0x00BF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=337*
  1: 0x00CE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x00DB [0x00] END_REQSTACK()
```
