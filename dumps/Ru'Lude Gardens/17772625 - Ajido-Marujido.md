# 17772625 - Ajido-Marujido

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 468 bytes                 |
| Total Events     | 19                        |
| References Count | 28                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     22 |              3 |
| [65535.4](#event-655354)   | 0x0035       |     20 |              3 |
| [65535.5](#event-655355)   | 0x0049       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0059       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0067       |     22 |              3 |
| [65535.8](#event-655358)   | 0x007D       |     20 |              3 |
| [65535.9](#event-655359)   | 0x0091       |      9 |              3 |
| [10010](#event-10010)      | 0x009A       |      1 |              1 |
| [65535.10](#event-6553510) | 0x009B       |      1 |              1 |
| [65535.11](#event-6553511) | 0x009C       |      1 |              1 |
| [65535.12](#event-6553512) | 0x009D       |     10 |              2 |
| [65535.13](#event-6553513) | 0x00A7       |     10 |              2 |
| [65535.14](#event-6553514) | 0x00B1       |     70 |             16 |
| [65535.15](#event-6553515) | 0x00F7       |      5 |              3 |
| [65535.16](#event-6553516) | 0x00FC       |      5 |              3 |
| [65535.17](#event-6553517) | 0x0101       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00A6      |         166 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFE2255  |  4294845013 |
|       3 | 0x18B02     |      101122 |
|       4 | 0xFFFEEBA4  |  4294896548 |
|       5 | 0x0F95      |        3989 |
|       6 | 0xFFFE79A1  |  4294867361 |
|       7 | 0x176BF     |       95935 |
|       8 | 0xFFFEE6C1  |  4294895297 |
|       9 | 0x0C70      |        3184 |
|      10 | 0x0028      |          40 |
|      11 | 0xFFFE3EE4  |  4294852324 |
|      12 | 0x19534     |      103732 |
|      13 | 0xFFFE47B5  |  4294854581 |
|      14 | 0x17970     |       96624 |
|      15 | 0xFFFE6493  |  4294861971 |
|      16 | 0x16694     |       91796 |
|      17 | 0xFFFEE6C0  |  4294895296 |
|      18 | 0xFFFE7795  |  4294866837 |
|      19 | 0x16E73     |       93811 |
|      20 | 0xFFFE796C  |  4294867308 |
|      21 | 0x1724E     |       94798 |
|      22 | 0x000D      |          13 |
|      23 | 0xFFFE7A18  |  4294867480 |
|      24 | 0x17FBC     |       98236 |
|      25 | 0x2B00      |       11008 |
|      26 | 0x2B0B      |       11019 |
|      27 | 0x2B0C      |       11020 |

## String References

- **11008**: Shoo! Shoo! Keep your grimy claws off of Windurst Orastery minister, Ajido-Marujido!
- **11019**: The towers are all damaged! How do you explain magic still being drained from the plains of Sarutabaruta?
- **11020**: What about you Yagudo? What are those things that you continue digging? Those stones...maybe they are the cause of all this?

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 6B 73 77 30   [..........ksw0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ksw0" with entities [EventEntity, EventEntity], work=166*
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
0010:    53 F8 FF FF 7F F8 FF  FF 7F 6B 73 77 30 00      S........ksw0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ksw0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               81                 .
0020: 00 F8 FF FF 7F 5B 00 80  F8 FF FF 7F F8 FF FF 7F  .....[..........
0030: 6B 73 74 30 00                                    kst0.           
```

#### Opcodes

```
  0: 0x001F [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0025 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kst0" with entities [EventEntity, EventEntity], work=166*
  2: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                53 F8 FF  FF 7F F8 FF FF 7F 6B 73       S........ks
0040: 74 30 81 01 F8 FF FF 7F  00                       t0.......       
```

#### Opcodes

```
  0: 0x0035 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kst0" with entities [EventEntity, EventEntity]
  1: 0x0042 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             5B 00 80 F8 FF FF 7F           [......
0050: F8 FF FF 7F 6B 73 74 31  00                       ....kst1.       
```

#### Opcodes

```
  0: 0x0049 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kst1" with entities [EventEntity, EventEntity], work=166*
  1: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             53 F8 FF FF 7F F8 FF           S......
0060: FF 7F 6B 73 74 31 00                              ..kst1.         
```

#### Opcodes

```
  0: 0x0059 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kst1" with entities [EventEntity, EventEntity]
  1: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      81  00 F8 FF FF 7F 5B 00 80         ......[..
0070: F8 FF FF 7F F8 FF FF 7F  6B 75 70 30 00           ........kup0.   
```

#### Opcodes

```
  0: 0x0067 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x006D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kup0" with entities [EventEntity, EventEntity], work=166*
  2: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         53 F8 FF               S..
0080: FF 7F F8 FF FF 7F 6B 75  70 30 81 01 F8 FF FF 7F  ......kup0......
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x007D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kup0" with entities [EventEntity, EventEntity]
  1: 0x008A [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0091  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0091 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0096 [0x1C] WAIT(30* ticks)
  2: 0x0099 [0x00] END_REQSTACK()
```

### Event 10010

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                00                           .     
```

#### Opcodes

```
  0: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   00                         .    
```

#### Opcodes

```
  0: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      00                       .   
```

#### Opcodes

```
  0: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         37 02 80               7..
00A0: 03 80 04 80 05 80 00                              .......         
```

#### Opcodes

```
  0: 0x009D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-122.283*, z=101.122*, y=-70.748*, direction=350.6°*
  1: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      37  06 80 07 80 08 80 09 80         7........
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x00A7 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-99.935*, z=95.935*, y=-71.999*, direction=279.8°*
  1: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 70 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    32 0A 80 1F 00 0B 80  0C 80 08 80 1F 01 32 0A   2............2.
00C0: 80 1F 00 0D 80 0E 80 08  80 1F 01 1F 00 0F 80 10  ................
00D0: 80 11 80 1F 01 1F 00 12  80 13 80 11 80 1F 01 1F  ................
00E0: 00 14 80 15 80 11 80 1F  01 32 16 80 1F 00 17 80  .........2......
00F0: 18 80 11 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x00B1 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00B4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-114.972*, Z=103.732*, Y=-71.999*
  2: 0x00BC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BE [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  4: 0x00C1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-112.715*, Z=96.624*, Y=-71.999*
  5: 0x00C9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x00CB [0x1F] MOVE_ENTITY: EventEntity moves to X=-105.325*, Z=91.796*, Y=-72.000*
  7: 0x00D3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x00D5 [0x1F] MOVE_ENTITY: EventEntity moves to X=-100.459*, Z=93.811*, Y=-72.000*
  9: 0x00DD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 10: 0x00DF [0x1F] MOVE_ENTITY: EventEntity moves to X=-99.988*, Z=94.798*, Y=-72.000*
 11: 0x00E7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 12: 0x00E9 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
 13: 0x00EC [0x1F] MOVE_ENTITY: EventEntity moves to X=-99.816*, Z=98.236*, Y=-72.000*
 14: 0x00F4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 15: 0x00F6 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F7  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      1D  19 80 23 00                     ...#.    
```

#### Opcodes

```
  0: 0x00F7 [0x1D] PRINT_EVENT_MESSAGE(message_id=11008*)
    → "Shoo! Shoo! Keep your grimy claws off of Windurst Orastery minister, Ajido-Marujido!"
  1: 0x00FA [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00FC  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      1D 1A 80 23              ...#
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00FC [0x1D] PRINT_EVENT_MESSAGE(message_id=11019*)
    → "The towers are all damaged! How do you explain magic still being drained from the plains of Sarutabaruta?"
  1: 0x00FF [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0101  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    1D 1B 80 23 00                                  ...#.          
```

#### Opcodes

```
  0: 0x0101 [0x1D] PRINT_EVENT_MESSAGE(message_id=11020*)
    → "What about you Yagudo? What are those things that you continue digging? Those stones...maybe they are the cause of all this?"
  1: 0x0104 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0105 [0x00] END_REQSTACK()
```
