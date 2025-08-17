# 17764364 - Kohlo-Lakolo

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 376 bytes                |
| Total Events     | 16                       |
| References Count | 16                       |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0021       |     14 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     16 |              2 |
| [65535.5](#event-655355)   | 0x003F       |     14 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     16 |              2 |
| [65535.7](#event-655357)   | 0x005D       |     16 |              2 |
| [65535.8](#event-655358)   | 0x006D       |      9 |              3 |
| [65535.9](#event-655359)   | 0x0076       |     35 |              8 |
| [65535.10](#event-6553510) | 0x0099       |     15 |              5 |
| [11](#event-11)            | 0x00A8       |      1 |              1 |
| [367](#event-367)          | 0x00A9       |      1 |              1 |
| [65535.11](#event-6553511) | 0x00AA       |      5 |              3 |
| [65535.12](#event-6553512) | 0x00AF       |     37 |              9 |
| [65535.13](#event-6553513) | 0x00D4       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0055      |          85 |
|       1 | 0x001E      |          30 |
|       2 | 0x3BCC      |       15308 |
|       3 | 0xFFFF477E  |  4294920062 |
|       4 | 0x07CF      |        1999 |
|       5 | 0x0E39      |        3641 |
|       6 | 0x0015      |          21 |
|       7 | 0x5C8A      |       23690 |
|       8 | 0xFFFF5A6C  |  4294924908 |
|       9 | 0x482A      |       18474 |
|      10 | 0xFFFFA770  |  4294944624 |
|      11 | 0x04AF      |        1199 |
|      12 | 0x20A4      |        8356 |
|      13 | 0x20A5      |        8357 |
|      14 | 0x20A6      |        8358 |
|      15 | 0x20AA      |        8362 |

## String References

- **8356**: Hold it right there!
- **8357**: Nanaa Mihgo!!! You're up to your old tricks of duping travelers out of their hard-earned gil, aren't you?
- **8358**: We, the "Star Onion Brigade," won't let you get away with it!
- **8362**: Hey, she's getting away! After her!

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 6A 6D 70 30   [..........jmp0
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "jmp0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    53 F8 FF FF 7F F8 FF  FF 7F 6A 6D 70 30 00      S........jmp0. 
```

#### Opcodes

```
  0: 0x0021 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "jmp0" with entities [EventEntity, EventEntity]
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               5B                 [
0030: 00 80 F8 FF FF 7F F8 FF  FF 7F 61 6E 67 30 00     ..........ang0. 
```

#### Opcodes

```
  0: 0x002F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=85*
  1: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               53                 S
0040: F8 FF FF 7F F8 FF FF 7F  61 6E 67 30 00           ........ang0.   
```

#### Opcodes

```
  0: 0x003F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang0" with entities [EventEntity, EventEntity]
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         5B 00 80               [..
0050: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 00           ........thk1.   
```

#### Opcodes

```
  0: 0x004D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=85*
  1: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         5B 00 80               [..
0060: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 00           ........thk2.   
```

#### Opcodes

```
  0: 0x005D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=85*
  1: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006D  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         5E 69 64               ^id
0070: 6C 30 1C 01 80 00                                 l0....          
```

#### Opcodes

```
  0: 0x006D [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0072 [0x1C] WAIT(30* ticks)
  2: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 35 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   37 02  80 03 80 04 80 05 80 4E        7........N
0080: 00 0C 10 0F 01 32 06 80  1F 00 07 80 08 80 04 80  .....2..........
0090: 1F 01 6F 1E 0F 10 0F 01  00                       ..o......       
```

#### Opcodes

```
  0: 0x0076 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=15.308*, z=-47.234*, y=1.999*, direction=320.0°*
  1: 0x007F [0x4E] SET_ENTITY_HIDE_FLAG: Show Kohlo-Lakolo (ID: 17764364/0x010F100C)
  2: 0x0085 [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  3: 0x0088 [0x1F] MOVE_ENTITY: EventEntity moves to X=23.690*, Z=-42.388*, Y=1.999*
  4: 0x0090 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0092 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0093 [0x1E] EventEntity looks at Nanaa Mihgo (ID: 17764367/0x010F100F) and starts talking
  7: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             32 06 80 1F 00 09 80           2......
00A0: 0A 80 0B 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0099 [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x009C [0x1F] MOVE_ENTITY: EventEntity moves to X=18.474*, Z=-22.672*, Y=1.199*
  2: 0x00A4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00A7 [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                          00                               .       
```

#### Opcodes

```
  0: 0x00A8 [0x00] END_REQSTACK()
```

### Event 367

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             00                             .      
```

#### Opcodes

```
  0: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AA  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                1D 0C 80 23 00               ...#. 
```

#### Opcodes

```
  0: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=8356*)
    → "Hold it right there!"
  1: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               29                 )
00B0: 08 0C 10 0F 01 02 1D 0D  80 23 29 08 0C 10 0F 01  .........#).....
00C0: 03 29 08 0C 10 0F 01 04  1D 0E 80 23 29 08 0C 10  .).........#)...
00D0: 0F 01 05 00                                       ....            
```

#### Opcodes

```
  0: 0x00AF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17764364/0x010F100C), tag_num=0x02)
  1: 0x00B6 [0x1D] PRINT_EVENT_MESSAGE(message_id=8357*)
    → "Nanaa Mihgo!!! You're up to your old tricks of duping travelers out of their hard-earned gil, aren't you?"
  2: 0x00B9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00BA [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17764364/0x010F100C), tag_num=0x03)
  4: 0x00C1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17764364/0x010F100C), tag_num=0x04)
  5: 0x00C8 [0x1D] PRINT_EVENT_MESSAGE(message_id=8358*)
    → "We, the "Star Onion Brigade," won't let you get away with it!"
  6: 0x00CB [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00CC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17764364/0x010F100C), tag_num=0x05)
  8: 0x00D3 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D4   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             29 08 0C 10  0F 01 02 1D 0F 80 23 29      ).........#)
00E0: 08 0C 10 0F 01 03 00                              .......         
```

#### Opcodes

```
  0: 0x00D4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17764364/0x010F100C), tag_num=0x02)
  1: 0x00DB [0x1D] PRINT_EVENT_MESSAGE(message_id=8362*)
    → "Hey, she's getting away! After her!"
  2: 0x00DE [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00DF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17764364/0x010F100C), tag_num=0x03)
  4: 0x00E6 [0x00] END_REQSTACK()
```
