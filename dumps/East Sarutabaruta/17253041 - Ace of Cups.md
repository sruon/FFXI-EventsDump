# 17253041 - Ace of Cups

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | East Sarutabaruta (ID: 116) |
| Block Size       | 544 bytes                   |
| Total Events     | 28                          |
| References Count | 14                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     14 |              2 |
| [65535.7](#event-655357)   | 0x005B       |     16 |              2 |
| [65535.8](#event-655358)   | 0x006B       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0079       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0089       |     14 |              2 |
| [65535.11](#event-6553511) | 0x0097       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00A7       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00B5       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00C5       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00D3       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00E3       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00F1       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0101       |     14 |              2 |
| [65535.19](#event-6553519) | 0x010F       |     16 |              2 |
| [65535.20](#event-6553520) | 0x011F       |     14 |              2 |
| [48](#event-48)            | 0x012D       |     12 |              3 |
| [65535.21](#event-6553521) | 0x0139       |     11 |              3 |
| [65535.22](#event-6553522) | 0x0144       |     16 |              5 |
| [65535.23](#event-6553523) | 0x0154       |      5 |              3 |
| [65535.24](#event-6553524) | 0x0159       |      5 |              3 |
| [65535.25](#event-6553525) | 0x015E       |      5 |              3 |
| [65535.26](#event-6553526) | 0x0163       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00B5      |         181 |
|       1 | 0x3F4F2     |      259314 |
|       2 | 0xFFF90781  |  4294510465 |
|       3 | 0xFFFFBC9F  |  4294950047 |
|       4 | 0x031F      |         799 |
|       5 | 0x3F5BA     |      259514 |
|       6 | 0xFFF90655  |  4294510165 |
|       7 | 0x000D      |          13 |
|       8 | 0x3F506     |      259334 |
|       9 | 0xFFF939D5  |  4294523349 |
|      10 | 0x1D11      |        7441 |
|      11 | 0x1D16      |        7446 |
|      12 | 0x1D19      |        7449 |
|      13 | 0x1D1B      |        7451 |

## String References

- **7441**: Mana Orbs are Cardians' hearts!
- **7446**: You too, adventurer! Hand over those Mana Orbs to us Cardians now!
- **7449**: Well...?
- **7451**: Is this all of them!?

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 6B 61 61 30   [..........kaa0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kaa0" with entities [EventEntity, EventEntity], work=181*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 6B 61 61 30 00      S........kaa0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kaa0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               5B                 [
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 6B 61 61 31 00     ..........kaa1. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kaa1" with entities [EventEntity, EventEntity], work=181*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  6B 61 61 31 00           ........kaa1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kaa1" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         5B 00 80               [..
0040: F8 FF FF 7F F8 FF FF 7F  6B 61 62 30 00           ........kab0.   
```

#### Opcodes

```
  0: 0x003D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kab0" with entities [EventEntity, EventEntity], work=181*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         53 F8 FF               S..
0050: FF 7F F8 FF FF 7F 6B 61  62 30 00                 ......kab0.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kab0" with entities [EventEntity, EventEntity]
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   5B 00 80 F8 FF             [....
0060: FF 7F F8 FF FF 7F 6B 61  62 31 00                 ......kab1.     
```

#### Opcodes

```
  0: 0x005B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kab1" with entities [EventEntity, EventEntity], work=181*
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   53 F8 FF FF 7F             S....
0070: F8 FF FF 7F 6B 61 62 31  00                       ....kab1.       
```

#### Opcodes

```
  0: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kab1" with entities [EventEntity, EventEntity]
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             5B 00 80 F8 FF FF 7F           [......
0080: F8 FF FF 7F 6B 61 63 30  00                       ....kac0.       
```

#### Opcodes

```
  0: 0x0079 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kac0" with entities [EventEntity, EventEntity], work=181*
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             53 F8 FF FF 7F F8 FF           S......
0090: FF 7F 6B 61 63 30 00                              ..kac0.         
```

#### Opcodes

```
  0: 0x0089 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kac0" with entities [EventEntity, EventEntity]
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      5B  00 80 F8 FF FF 7F F8 FF         [........
00A0: FF 7F 6B 61 63 31 00                              ..kac1.         
```

#### Opcodes

```
  0: 0x0097 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kac1" with entities [EventEntity, EventEntity], work=181*
  1: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00B0: 6B 61 63 30 00                                    kac0.           
```

#### Opcodes

```
  0: 0x00A7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kac0" with entities [EventEntity, EventEntity]
  1: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                5B 00 80  F8 FF FF 7F F8 FF FF 7F       [..........
00C0: 79 62 69 30 00                                    ybi0.           
```

#### Opcodes

```
  0: 0x00B5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ybi0" with entities [EventEntity, EventEntity], work=181*
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                53 F8 FF  FF 7F F8 FF FF 7F 79 62       S........yb
00D0: 69 30 00                                          i0.             
```

#### Opcodes

```
  0: 0x00C5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ybi0" with entities [EventEntity, EventEntity]
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          5B 00 80 F8 FF  FF 7F F8 FF FF 7F 79 6B     [..........yk
00E0: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x00D3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yks0" with entities [EventEntity, EventEntity], work=181*
  1: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          53 F8 FF FF 7F  F8 FF FF 7F 79 6B 73 30     S........yks0
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "yks0" with entities [EventEntity, EventEntity]
  1: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 79 6B 73 31   [..........yks1
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00F1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yks1" with entities [EventEntity, EventEntity], work=181*
  1: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    53 F8 FF FF 7F F8 FF  FF 7F 79 6B 73 31 00      S........yks1. 
```

#### Opcodes

```
  0: 0x0101 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "yks1" with entities [EventEntity, EventEntity]
  1: 0x010E [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               5B                 [
0110: 00 80 F8 FF FF 7F F8 FF  FF 7F 64 65 64 30 00     ..........ded0. 
```

#### Opcodes

```
  0: 0x010F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ded0" with entities [EventEntity, EventEntity], work=181*
  1: 0x011E [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                               53                 S
0120: F8 FF FF 7F F8 FF FF 7F  64 65 64 30 00           ........ded0.   
```

#### Opcodes

```
  0: 0x011F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ded0" with entities [EventEntity, EventEntity]
  1: 0x012C [0x00] END_REQSTACK()
```

### Event 48

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012D   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                         37 01 80               7..
0130: 02 80 03 80 04 80 22 00  00                       ......"..       
```

#### Opcodes

```
  0: 0x012D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=259.314*, z=-456.831*, y=-17.249*, direction=70.2°*
  1: 0x0136 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x0138 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0139   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                             1F 00 05 80 06 80 03           .......
0140: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0139 [0x1F] MOVE_ENTITY: EventEntity moves to X=259.514*, Z=-457.131*, Y=-17.249*
  1: 0x0141 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0143 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0144   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:             32 07 80 1F  00 08 80 09 80 03 80 1F      2...........
0150: 01 22 01 00                                       ."..            
```

#### Opcodes

```
  0: 0x0144 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0147 [0x1F] MOVE_ENTITY: EventEntity moves to X=259.334*, Z=-443.947*, Y=-17.249*
  2: 0x014F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0151 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x0153 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0154  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:             1D 0A 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x0154 [0x1D] PRINT_EVENT_MESSAGE(message_id=7441*)
    → "Mana Orbs are Cardians' hearts!"
  1: 0x0157 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0158 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0159  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                             1D 0B 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x0159 [0x1D] PRINT_EVENT_MESSAGE(message_id=7446*)
    → "You too, adventurer! Hand over those Mana Orbs to us Cardians now!"
  1: 0x015C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x015D [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x015E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                            1D 0C                ..
0160: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x015E [0x1D] PRINT_EVENT_MESSAGE(message_id=7449*)
    → "Well...?"
  1: 0x0161 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0162 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0163  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:          1D 0D 80 23 00                              ...#.        
```

#### Opcodes

```
  0: 0x0163 [0x1D] PRINT_EVENT_MESSAGE(message_id=7451*)
    → "Is this all of them!?"
  1: 0x0166 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0167 [0x00] END_REQSTACK()
```
