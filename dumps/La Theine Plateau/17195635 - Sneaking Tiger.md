# 17195635 - Sneaking Tiger

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 380 bytes                   |
| Total Events     | 19                          |
| References Count | 9                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     22 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0037       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0045       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0055       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0063       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0073       |     22 |              4 |
| [65535.9](#event-655359)   | 0x0089       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0099       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00A7       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00B7       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00C5       |      9 |              3 |
| [119](#event-119)          | 0x00CE       |      1 |              1 |
| [65535.14](#event-6553514) | 0x00CF       |     14 |              4 |
| [65535.15](#event-6553515) | 0x00DD       |     19 |              5 |
| [65535.16](#event-6553516) | 0x00F0       |      5 |              3 |
| [65535.17](#event-6553517) | 0x00F5       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0037      |          55 |
|       1 | 0x001E      |          30 |
|       2 | 0x000D      |          13 |
|       3 | 0xFFFED1A4  |  4294889892 |
|       4 | 0xFFF9661F  |  4294534687 |
|       5 | 0xD685      |       54917 |
|       6 | 0x1D5D      |        7517 |
|       7 | 0x1D6B      |        7531 |
|       8 | 0x1D71      |        7537 |

## String References

- **7517**: I've seen that face before!
- **7531**: But Vauderame, these guys have seen what's in the chest. If we don't knock 'em off now, there's bound to be trouble later.
- **7537**: I'll get rid of the rust. I brought the gear with me.

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=55*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5B  00 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 74 68 61 31 00                              ..tha1.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tha1" with entities [EventEntity, EventEntity], work=55*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 74 68 61 31 00                                    tha1.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tha1" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                5B 00 80  F8 FF FF 7F F8 FF FF 7F       [..........
0050: 74 68 61 32 00                                    tha2.           
```

#### Opcodes

```
  0: 0x0045 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tha2" with entities [EventEntity, EventEntity], work=55*
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                53 F8 FF  FF 7F F8 FF FF 7F 74 68       S........th
0060: 61 32 00                                          a2.             
```

#### Opcodes

```
  0: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tha2" with entities [EventEntity, EventEntity]
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          5B 00 80 F8 FF  FF 7F F8 FF FF 7F 64 69     [..........di
0070: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x0063 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=55*
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          53 F8 FF FF 7F  F8 FF FF 7F 64 69 73 30     S........dis0
0080: 5E 69 64 6C 30 1C 01 80  00                       ^idl0....       
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x0080 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0085 [0x1C] WAIT(30* ticks)
  3: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             5B 00 80 F8 FF FF 7F           [......
0090: F8 FF FF 7F 74 68 62 31  00                       ....thb1.       
```

#### Opcodes

```
  0: 0x0089 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb1" with entities [EventEntity, EventEntity], work=55*
  1: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             53 F8 FF FF 7F F8 FF           S......
00A0: FF 7F 74 68 62 31 00                              ..thb1.         
```

#### Opcodes

```
  0: 0x0099 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thb1" with entities [EventEntity, EventEntity]
  1: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      5B  00 80 F8 FF FF 7F F8 FF         [........
00B0: FF 7F 74 68 62 32 00                              ..thb2.         
```

#### Opcodes

```
  0: 0x00A7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb2" with entities [EventEntity, EventEntity], work=55*
  1: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00C0: 74 68 62 32 00                                    thb2.           
```

#### Opcodes

```
  0: 0x00B7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thb2" with entities [EventEntity, EventEntity]
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C5  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                5E 69 64  6C 30 1C 01 80 00             ^idl0....  
```

#### Opcodes

```
  0: 0x00C5 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00CA [0x1C] WAIT(30* ticks)
  2: 0x00CD [0x00] END_REQSTACK()
```

### Event 119

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CE  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            00                   . 
```

#### Opcodes

```
  0: 0x00CE [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CF   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                               32                 2
00D0: 02 80 1F 00 03 80 04 80  05 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x00CF [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00D2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-77.404*, Z=-432.609*, Y=54.917*
  2: 0x00DA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00DC [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         29 08 73               ).s
00E0: 62 06 01 01 1D 06 80 23  29 08 73 62 06 01 02 00  b......#).sb....
```

#### Opcodes

```
  0: 0x00DD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Sneaking Tiger (ID: 17195635/0x01066273), tag_num=0x01)
  1: 0x00E4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7517*)
    → "I've seen that face before!"
  2: 0x00E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00E8 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Sneaking Tiger (ID: 17195635/0x01066273), tag_num=0x02)
  4: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F0  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: 1D 07 80 23 00                                    ...#.           
```

#### Opcodes

```
  0: 0x00F0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7531*)
    → "But Vauderame, these guys have seen what's in the chest. If we don't knock 'em off now, there's bound to be trouble later."
  1: 0x00F3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F5  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                1D 08 80  23 00                         ...#.      
```

#### Opcodes

```
  0: 0x00F5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7537*)
    → "I'll get rid of the rust. I brought the gear with me."
  1: 0x00F8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00F9 [0x00] END_REQSTACK()
```
