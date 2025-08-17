# 17793100 - Sneaking Tiger

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Selbina (ID: 248) |
| Block Size       | 484 bytes         |
| Total Events     | 27                |
| References Count | 14                |

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
| [65535.13](#event-6553513) | 0x00C5       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00D5       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00E3       |      9 |              3 |
| [10002](#event-10002)      | 0x00EC       |      1 |              1 |
| [65535.16](#event-6553516) | 0x00ED       |     10 |              2 |
| [65535.17](#event-6553517) | 0x00F7       |      5 |              3 |
| [65535.18](#event-6553518) | 0x00FC       |      5 |              3 |
| [65535.19](#event-6553519) | 0x0101       |     19 |              5 |
| [65535.20](#event-6553520) | 0x0114       |      5 |              3 |
| [65535.21](#event-6553521) | 0x0119       |      5 |              3 |
| [65535.22](#event-6553522) | 0x011E       |      5 |              3 |
| [10004](#event-10004)      | 0x0123       |      1 |              1 |
| [65535.23](#event-6553523) | 0x0124       |      5 |              3 |
| [65535.24](#event-6553524) | 0x0129       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0037      |          55 |
|       1 | 0x001E      |          30 |
|       2 | 0x10538     |       66872 |
|       3 | 0xFFFFFDB0  |  4294966704 |
|       4 | 0xFFFFC722  |  4294952738 |
|       5 | 0x0034      |          52 |
|       6 | 0x1C73      |        7283 |
|       7 | 0x1C75      |        7285 |
|       8 | 0x1C76      |        7286 |
|       9 | 0x1C77      |        7287 |
|      10 | 0x1C78      |        7288 |
|      11 | 0x1C79      |        7289 |
|      12 | 0x1C7F      |        7295 |
|      13 | 0x1C80      |        7296 |

## String References

- **7283**: ...Whaddayawant!? I'm busy! Who on Vana'diel are you? Never seen ya before!
- **7285**: Out here is better. Whatcha got there? Show me that $3.
- **7286**: Well, ain't this amusing. I'm on the straight and narrow these days, so I could just sign it for ya. But that wouldn't be any fun now, would it?
- **7287**: Let me see. You're still a young thief, but how good are ya? You can't get by in this world on thieving alone, ya know!
- **7288**: Could ya steal $2 from those turtle guys in Beadeaux? Those turtle guys gang up on ya and ya can't just pull a snatch and grab job!
- **7289**: Show me how good you young thieves are these days! Steal me $2 from the turtle guys in Beadeaux, an' I'll sign ya paper.
- **7295**: Good for you, stripling! Those turtles pack quite a punch, huh?
- **7296**: Here, take this back. I signed the $3 for ya. Enjoy your thievin' days, <Player>!

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                5B 00 80  F8 FF FF 7F F8 FF FF 7F       [..........
00D0: 70 61 73 30 00                                    pas0.           
```

#### Opcodes

```
  0: 0x00C5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=55*
  1: 0x00D4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                53 F8 FF  FF 7F F8 FF FF 7F 70 61       S........pa
00E0: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x00D5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E3  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          5E 69 64 6C 30  1C 01 80 00                 ^idl0....    
```

#### Opcodes

```
  0: 0x00E3 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00E8 [0x1C] WAIT(30* ticks)
  2: 0x00EB [0x00] END_REQSTACK()
```

### Event 10002

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      00                       .   
```

#### Opcodes

```
  0: 0x00EC [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00ED   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                         37 02 80               7..
00F0: 03 80 04 80 05 80 00                              .......         
```

#### Opcodes

```
  0: 0x00ED [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=66.872*, z=-0.592*, y=-14.558*, direction=4.6°*
  1: 0x00F6 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F7  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      1D  06 80 23 00                     ...#.    
```

#### Opcodes

```
  0: 0x00F7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7283*)
    → "...Whaddayawant!? I'm busy! Who on Vana'diel are you? Never seen ya before!"
  1: 0x00FA [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00FC  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      1D 07 80 23              ...#
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00FC [0x1D] PRINT_EVENT_MESSAGE(message_id=7285*)
    → "Out here is better. Whatcha got there? Show me that $3."
  1: 0x00FF [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    29 08 4C 80 0F 01 01  1D 08 80 23 29 08 4C 80   ).L.......#).L.
0110: 0F 01 02 00                                       ....            
```

#### Opcodes

```
  0: 0x0101 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Sneaking Tiger (ID: 17793100/0x010F804C), tag_num=0x01)
  1: 0x0108 [0x1D] PRINT_EVENT_MESSAGE(message_id=7286*)
    → "Well, ain't this amusing. I'm on the straight and narrow these days, so I could just sign it for ya. But that wouldn't be any fun now, would it?"
  2: 0x010B [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x010C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Sneaking Tiger (ID: 17793100/0x010F804C), tag_num=0x02)
  4: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0114  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             1D 09 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x0114 [0x1D] PRINT_EVENT_MESSAGE(message_id=7287*)
    → "Let me see. You're still a young thief, but how good are ya? You can't get by in this world on thieving alone, ya know!"
  1: 0x0117 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0118 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0119  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                             1D 0A 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x0119 [0x1D] PRINT_EVENT_MESSAGE(message_id=7288*)
    → "Could ya steal $2 from those turtle guys in Beadeaux? Those turtle guys gang up on ya and ya can't just pull a snatch and grab job!"
  1: 0x011C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x011D [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                            1D 0B                ..
0120: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x011E [0x1D] PRINT_EVENT_MESSAGE(message_id=7289*)
    → "Show me how good you young thieves are these days! Steal me $2 from the turtle guys in Beadeaux, an' I'll sign ya paper."
  1: 0x0121 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0122 [0x00] END_REQSTACK()
```

### Event 10004

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0123  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:          00                                          .            
```

#### Opcodes

```
  0: 0x0123 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0124  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:             1D 0C 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x0124 [0x1D] PRINT_EVENT_MESSAGE(message_id=7295*)
    → "Good for you, stripling! Those turtles pack quite a punch, huh?"
  1: 0x0127 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0128 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0129  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                             1D 0D 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x0129 [0x1D] PRINT_EVENT_MESSAGE(message_id=7296*)
    → "Here, take this back. I signed the $3 for ya. Enjoy your thievin' days, <Player>!"
  1: 0x012C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x012D [0x00] END_REQSTACK()
```
