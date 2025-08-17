# 17563883 - Ace of Swords

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Inner Horutoto Ruins (ID: 192) |
| Block Size       | 636 bytes                      |
| Total Events     | 32                             |
| References Count | 18                             |

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
| [46](#event-46)            | 0x010F       |      7 |              2 |
| [65535.19](#event-6553519) | 0x0116       |     20 |              5 |
| [65535.20](#event-6553520) | 0x012A       |     14 |              4 |
| [65535.21](#event-6553521) | 0x0138       |     14 |              4 |
| [65535.22](#event-6553522) | 0x0146       |     38 |              4 |
| [65535.23](#event-6553523) | 0x016C       |     20 |              5 |
| [65535.24](#event-6553524) | 0x0180       |      5 |              3 |
| [65535.25](#event-6553525) | 0x0185       |      5 |              3 |
| [65535.26](#event-6553526) | 0x018A       |      5 |              3 |
| [65535.27](#event-6553527) | 0x018F       |      5 |              3 |
| [65535.28](#event-6553528) | 0x0194       |      5 |              3 |
| [65535.29](#event-6553529) | 0x0199       |      5 |              3 |
| [65535.30](#event-6553530) | 0x019E       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00B5      |         181 |
|       1 | 0x000D      |          13 |
|       2 | 0xFFFFB725  |  4294948645 |
|       3 | 0x4CF7      |       19703 |
|       4 | 0x0000      |           0 |
|       5 | 0xFFFFAD98  |  4294946200 |
|       6 | 0x4CD1      |       19665 |
|       7 | 0xFFFFB33D  |  4294947645 |
|       8 | 0x4BCB      |       19403 |
|       9 | 0xFFFFC825  |  4294952997 |
|      10 | 0x4DA9      |       19881 |
|      11 | 0x1C7D      |        7293 |
|      12 | 0x1C82      |        7298 |
|      13 | 0x1C83      |        7299 |
|      14 | 0x1C89      |        7305 |
|      15 | 0x1C8B      |        7307 |
|      16 | 0x1C90      |        7312 |
|      17 | 0x1C93      |        7315 |

## String References

- **7293**: We have found you, Mithra! Return the lifeforce of our leader back to us!
- **7298**: It is not permissible for living fools such as you to take the property of the deceased...!
- **7299**: So, Mithra... Tell us where you hid our ruler's belongings! If you do not want to join him in death, then you had best speak the truth!
- **7305**: ...... You appear to be telling the truth.
- **7307**: Then you also know that we are incapable of lying as well.
- **7312**: It is the Minister of the Orastery...! Ajido-Marujido...!
- **7315**: ......

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

### Event 46

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               4E                 N
0110: 01 EB 00 0C 01 00                                 ......          
```

#### Opcodes

```
  0: 0x010F [0x4E] SET_ENTITY_HIDE_FLAG: Hide Ace of Swords (ID: 17563883/0x010C00EB)
  1: 0x0115 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0116   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   4E 00  EB 00 0C 01 32 01 80 1F        N.....2...
0120: 00 02 80 03 80 04 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0116 [0x4E] SET_ENTITY_HIDE_FLAG: Show Ace of Swords (ID: 17563883/0x010C00EB)
  1: 0x011C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x011F [0x1F] MOVE_ENTITY: EventEntity moves to X=-18.651*, Z=19.703*, Y=0.000*
  3: 0x0127 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0129 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                32 01 80 1F 00 05            2.....
0130: 80 06 80 04 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x012A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x012D [0x1F] MOVE_ENTITY: EventEntity moves to X=-21.096*, Z=19.665*, Y=0.000*
  2: 0x0135 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0138   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          32 01 80 1F 00 07 80 08          2.......
0140: 80 04 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0138 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x013B [0x1F] MOVE_ENTITY: EventEntity moves to X=-19.651*, Z=19.403*, Y=0.000*
  2: 0x0143 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0145 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0146   |
| Data Size    | 38 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                   5B 00  80 F8 FF FF 7F F8 FF FF        [.........
0150: 7F 6B 61 62 31 53 F8 FF  FF 7F F8 FF FF 7F 6B 61  .kab1S........ka
0160: 62 31 4A EA 00 0C 01 E9  00 0C 01 00              b1J.........    
```

#### Opcodes

```
  0: 0x0146 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kab1" with entities [EventEntity, EventEntity], work=181*
  1: 0x0155 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kab1" with entities [EventEntity, EventEntity]
  2: 0x0162 [0x4A] Ace of Wands (ID: 17563882/0x010C00EA) looks at Ace of Cups (ID: 17563881/0x010C00E9)
  3: 0x016B [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016C   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                      32 01 80 1F              2...
0170: 00 09 80 0A 80 04 80 1F  01 4E 01 EB 00 0C 01 00  .........N......
```

#### Opcodes

```
  0: 0x016C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x016F [0x1F] MOVE_ENTITY: EventEntity moves to X=-14.299*, Z=19.881*, Y=0.000*
  2: 0x0177 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0179 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Ace of Swords (ID: 17563883/0x010C00EB)
  4: 0x017F [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0180  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180: 1D 0B 80 23 00                                    ...#.           
```

#### Opcodes

```
  0: 0x0180 [0x1D] PRINT_EVENT_MESSAGE(message_id=7293*)
    → "We have found you, Mithra! Return the lifeforce of our leader back to us!"
  1: 0x0183 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0184 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0185  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                1D 0C 80  23 00                         ...#.      
```

#### Opcodes

```
  0: 0x0185 [0x1D] PRINT_EVENT_MESSAGE(message_id=7298*)
    → "It is not permissible for living fools such as you to take the property of the deceased...!"
  1: 0x0188 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0189 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x018A  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                1D 0D 80 23 00               ...#. 
```

#### Opcodes

```
  0: 0x018A [0x1D] PRINT_EVENT_MESSAGE(message_id=7299*)
    → "So, Mithra... Tell us where you hid our ruler's belongings! If you do not want to join him in death, then you had best speak the truth!"
  1: 0x018D [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x018E [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x018F  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                               1D                 .
0190: 0E 80 23 00                                       ..#.            
```

#### Opcodes

```
  0: 0x018F [0x1D] PRINT_EVENT_MESSAGE(message_id=7305*)
    → "...... You appear to be telling the truth."
  1: 0x0192 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0193 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0194  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:             1D 0F 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x0194 [0x1D] PRINT_EVENT_MESSAGE(message_id=7307*)
    → "Then you also know that we are incapable of lying as well."
  1: 0x0197 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0198 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0199  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                             1D 10 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x0199 [0x1D] PRINT_EVENT_MESSAGE(message_id=7312*)
    → "It is the Minister of the Orastery...! Ajido-Marujido...!"
  1: 0x019C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x019D [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x019E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                            1D 11                ..
01A0: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x019E [0x1D] PRINT_EVENT_MESSAGE(message_id=7315*)
    → "......"
  1: 0x01A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x01A2 [0x00] END_REQSTACK()
```
