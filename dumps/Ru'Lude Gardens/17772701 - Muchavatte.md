# 17772701 - Muchavatte

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 636 bytes                 |
| Total Events     | 28                        |
| References Count | 10                        |

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
| [65535.9](#event-655359)   | 0x0079       |     44 |              4 |
| [65535.10](#event-6553510) | 0x00A5       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00B3       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00C3       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00D1       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00E1       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00EF       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00FF       |     14 |              2 |
| [65535.17](#event-6553517) | 0x010D       |     16 |              2 |
| [65535.18](#event-6553518) | 0x011D       |     14 |              2 |
| [65535.19](#event-6553519) | 0x012B       |     16 |              2 |
| [65535.20](#event-6553520) | 0x013B       |     14 |              2 |
| [65535.21](#event-6553521) | 0x0149       |      3 |              2 |
| [10008](#event-10008)      | 0x014C       |     12 |              3 |
| [65535.22](#event-6553522) | 0x0158       |     19 |              5 |
| [65535.23](#event-6553523) | 0x016B       |     19 |              5 |
| [65535.24](#event-6553524) | 0x017E       |     33 |              7 |
| [65535.25](#event-6553525) | 0x019F       |     19 |              5 |
| [65535.26](#event-6553526) | 0x01B2       |     33 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0087      |         135 |
|       1 | 0x06F4      |        1780 |
|       2 | 0x9CC5      |       40133 |
|       3 | 0xFFFFF2BA  |  4294963898 |
|       4 | 0x093A      |        2362 |
|       5 | 0x1AA7      |        6823 |
|       6 | 0x1AA8      |        6824 |
|       7 | 0x1AAD      |        6829 |
|       8 | 0x1AAE      |        6830 |
|       9 | 0x1AAF      |        6831 |

## String References

- **6823**: It is true! The Humes are fools, and no better. Can they truly believe that some ancient power lies hidden in that forsaken wasteland?
- **6824**: Hah! Do they hope to find the gates to eternal Paradise there, in that lair of fiends most uncouth? Preposterous!
- **6829**: These foreigners are wily and faithless. Never let down your guard, and may the Goddess of the Dawn protect you in Her mercy.
- **6830**: The king has taken a beautiful queen, and I think a splendid addition to the royal family is not far off. An heir, perhaps...
- **6831**: We people of San d'Oria, too, must ever look to the future. The Elvaan must never fall behind foreigners, in power or faith.

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=135*
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
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00      S........tlk0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
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
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 00     ..........tlk1. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=135*
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
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 00           ........tlk1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
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
0040: F8 FF FF 7F F8 FF FF 7F  61 6E 67 30 00           ........ang0.   
```

#### Opcodes

```
  0: 0x003D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=135*
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
0050: FF 7F F8 FF FF 7F 61 6E  67 30 00                 ......ang0.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang0" with entities [EventEntity, EventEntity]
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
0060: FF 7F F8 FF FF 7F 61 6E  67 31 00                 ......ang1.     
```

#### Opcodes

```
  0: 0x005B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang1" with entities [EventEntity, EventEntity], work=135*
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
0070: F8 FF FF 7F 61 6E 67 31  00                       ....ang1.       
```

#### Opcodes

```
  0: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang1" with entities [EventEntity, EventEntity]
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 44 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             5B 00 80 F8 FF FF 7F           [......
0080: F8 FF FF 7F 65 6E 7A 30  53 F8 FF FF 7F F8 FF FF  ....enz0S.......
0090: 7F 65 6E 7A 30 5B 00 80  F8 FF FF 7F F8 FF FF 7F  .enz0[..........
00A0: 65 6E 7A 31 00                                    enz1.           
```

#### Opcodes

```
  0: 0x0079 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "enz0" with entities [EventEntity, EventEntity], work=135*
  1: 0x0088 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "enz0" with entities [EventEntity, EventEntity]
  2: 0x0095 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "enz1" with entities [EventEntity, EventEntity], work=135*
  3: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                53 F8 FF  FF 7F F8 FF FF 7F 65 6E       S........en
00B0: 7A 31 00                                          z1.             
```

#### Opcodes

```
  0: 0x00A5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "enz1" with entities [EventEntity, EventEntity]
  1: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          5B 00 80 F8 FF  FF 7F F8 FF FF 7F 69 6E     [..........in
00C0: 6F 30 00                                          o0.             
```

#### Opcodes

```
  0: 0x00B3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=135*
  1: 0x00C2 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          53 F8 FF FF 7F  F8 FF FF 7F 69 6E 6F 30     S........ino0
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00C3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
  1: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31   [..........thk1
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=135*
  1: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 00      S........thk1. 
```

#### Opcodes

```
  0: 0x00E1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x00EE [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                               5B                 [
00F0: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00     ..........thk2. 
```

#### Opcodes

```
  0: 0x00EF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=135*
  1: 0x00FE [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FF   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                               53                 S
0100: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 00           ........thk2.   
```

#### Opcodes

```
  0: 0x00FF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x010C [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         5B 00 80               [..
0110: F8 FF FF 7F F8 FF FF 7F  6C 61 75 30 00           ........lau0.   
```

#### Opcodes

```
  0: 0x010D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "lau0" with entities [EventEntity, EventEntity], work=135*
  1: 0x011C [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                         53 F8 FF               S..
0120: FF 7F F8 FF FF 7F 6C 61  75 30 00                 ......lau0.     
```

#### Opcodes

```
  0: 0x011D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "lau0" with entities [EventEntity, EventEntity]
  1: 0x012A [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   5B 00 80 F8 FF             [....
0130: FF 7F F8 FF FF 7F 6C 61  75 31 00                 ......lau1.     
```

#### Opcodes

```
  0: 0x012B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "lau1" with entities [EventEntity, EventEntity], work=135*
  1: 0x013A [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                   53 F8 FF FF 7F             S....
0140: F8 FF FF 7F 74 68 6B 32  00                       ....thk2.       
```

#### Opcodes

```
  0: 0x013B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0148 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0149  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                             22 00 00                       "..    
```

#### Opcodes

```
  0: 0x0149 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x014B [0x00] END_REQSTACK()
```

### Event 10008

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014C   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                      22 00 37 01              ".7.
0150: 80 02 80 03 80 04 80 00                           ........        
```

#### Opcodes

```
  0: 0x014C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x014E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=1.780*, z=40.133*, y=-3.398*, direction=207.6°*
  2: 0x0157 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0158   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                          29 08 9D 30 0F 01 11 1D          )..0....
0160: 05 80 23 29 08 9D 30 0F  01 12 00                 ..#)..0....     
```

#### Opcodes

```
  0: 0x0158 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x11)
  1: 0x015F [0x1D] PRINT_EVENT_MESSAGE(message_id=6823*)
    → "It is true! The Humes are fools, and no better. Can they truly believe that some ancient power lies hidden in that forsaken wasteland?"
  2: 0x0162 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0163 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x12)
  4: 0x016A [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016B   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                   29 08 9D 30 0F             )..0.
0170: 01 13 1D 06 80 23 29 08  9D 30 0F 01 14 00        .....#)..0....  
```

#### Opcodes

```
  0: 0x016B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x13)
  1: 0x0172 [0x1D] PRINT_EVENT_MESSAGE(message_id=6824*)
    → "Hah! Do they hope to find the gates to eternal Paradise there, in that lair of fiends most uncouth? Preposterous!"
  2: 0x0175 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0176 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x14)
  4: 0x017D [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017E   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                            29 08                ).
0180: 9D 30 0F 01 0D 1D 07 80  23 29 08 9D 30 0F 01 0E  .0......#)..0...
0190: 29 08 9D 30 0F 01 0F 29  08 9D 30 0F 01 10 00     )..0...)..0.... 
```

#### Opcodes

```
  0: 0x017E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x0D)
  1: 0x0185 [0x1D] PRINT_EVENT_MESSAGE(message_id=6829*)
    → "These foreigners are wily and faithless. Never let down your guard, and may the Goddess of the Dawn protect you in Her mercy."
  2: 0x0188 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0189 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x0E)
  4: 0x0190 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x0F)
  5: 0x0197 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x10)
  6: 0x019E [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019F   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                               29                 )
01A0: 08 9D 30 0F 01 09 1D 08  80 23 29 08 9D 30 0F 01  ..0......#)..0..
01B0: 0A 00                                             ..              
```

#### Opcodes

```
  0: 0x019F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x09)
  1: 0x01A6 [0x1D] PRINT_EVENT_MESSAGE(message_id=6830*)
    → "The king has taken a beautiful queen, and I think a splendid addition to the royal family is not far off. An heir, perhaps..."
  2: 0x01A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01AA [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x0A)
  4: 0x01B1 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B2   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:       29 08 9D 30 0F 01  05 1D 09 80 23 29 08 9D    )..0......#)..
01C0: 30 0F 01 06 29 08 9D 30  0F 01 07 29 08 9D 30 0F  0...)..0...)..0.
01D0: 01 08 00                                          ...             
```

#### Opcodes

```
  0: 0x01B2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x05)
  1: 0x01B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=6831*)
    → "We people of San d'Oria, too, must ever look to the future. The Elvaan must never fall behind foreigners, in power or faith."
  2: 0x01BC [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01BD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x06)
  4: 0x01C4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x07)
  5: 0x01CB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Muchavatte (ID: 17772701/0x010F309D), tag_num=0x08)
  6: 0x01D2 [0x00] END_REQSTACK()
```
