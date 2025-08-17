# 17473711 - King of Cups

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 548 bytes                    |
| Total Events     | 26                           |
| References Count | 9                            |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      6 |              2 |
| [65535.2](#event-655352)   | 0x0007       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0017       |     14 |              2 |
| [65535.4](#event-655354)   | 0x0025       |     16 |              2 |
| [65535.5](#event-655355)   | 0x0035       |     14 |              2 |
| [65535.6](#event-655356)   | 0x0043       |     16 |              2 |
| [65535.7](#event-655357)   | 0x0053       |     14 |              2 |
| [65535.8](#event-655358)   | 0x0061       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0071       |     14 |              2 |
| [65535.10](#event-6553510) | 0x007F       |     16 |              2 |
| [65535.11](#event-6553511) | 0x008F       |     14 |              2 |
| [65535.12](#event-6553512) | 0x009D       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00AD       |     14 |              2 |
| [65535.14](#event-6553514) | 0x00BB       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00CB       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00D9       |     34 |              4 |
| [65535.17](#event-6553517) | 0x00FB       |     29 |              3 |
| [65535.18](#event-6553518) | 0x0118       |     16 |              2 |
| [61](#event-61)            | 0x0128       |     16 |              3 |
| [65535.19](#event-6553519) | 0x0138       |     30 |              6 |
| [62](#event-62)            | 0x0156       |      1 |              1 |
| [65535.20](#event-6553520) | 0x0157       |     43 |              9 |
| [32000](#event-32000)      | 0x0182       |      1 |              1 |
| [32004](#event-32004)      | 0x0183       |      1 |              1 |
| [32001](#event-32001)      | 0x0184       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00B5      |         181 |
|       1 | 0x00B6      |         182 |
|       2 | 0xFFFF0D5E  |  4294905182 |
|       3 | 0x5CCE      |       23758 |
|       4 | 0x2415      |        9237 |
|       5 | 0x0B70      |        2928 |
|       6 | 0x000D      |          13 |
|       7 | 0x1F40      |        8000 |
|       8 | 0x01F4      |         500 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5E 69 64 6C 30 00                               ^idl0.         
```

#### Opcodes

```
  0: 0x0001 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      5B  00 80 F8 FF FF 7F F8 FF         [........
0010: FF 7F 6B 61 61 30 00                              ..kaa0.         
```

#### Opcodes

```
  0: 0x0007 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kaa0" with entities [EventEntity, EventEntity], work=181*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0020: 6B 61 61 30 00                                    kaa0.           
```

#### Opcodes

```
  0: 0x0017 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kaa0" with entities [EventEntity, EventEntity]
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                5B 00 80  F8 FF FF 7F F8 FF FF 7F       [..........
0030: 6B 61 61 31 00                                    kaa1.           
```

#### Opcodes

```
  0: 0x0025 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kaa1" with entities [EventEntity, EventEntity], work=181*
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                53 F8 FF  FF 7F F8 FF FF 7F 6B 61       S........ka
0040: 61 31 00                                          a1.             
```

#### Opcodes

```
  0: 0x0035 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kaa1" with entities [EventEntity, EventEntity]
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          5B 00 80 F8 FF  FF 7F F8 FF FF 7F 6B 61     [..........ka
0050: 62 30 00                                          b0.             
```

#### Opcodes

```
  0: 0x0043 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kab0" with entities [EventEntity, EventEntity], work=181*
  1: 0x0052 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          53 F8 FF FF 7F  F8 FF FF 7F 6B 61 62 30     S........kab0
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0053 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kab0" with entities [EventEntity, EventEntity]
  1: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 6B 61 62 31   [..........kab1
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0061 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kab1" with entities [EventEntity, EventEntity], work=181*
  1: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    53 F8 FF FF 7F F8 FF  FF 7F 6B 61 62 31 00      S........kab1. 
```

#### Opcodes

```
  0: 0x0071 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kab1" with entities [EventEntity, EventEntity]
  1: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               5B                 [
0080: 00 80 F8 FF FF 7F F8 FF  FF 7F 6B 61 63 30 00     ..........kac0. 
```

#### Opcodes

```
  0: 0x007F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kac0" with entities [EventEntity, EventEntity], work=181*
  1: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               53                 S
0090: F8 FF FF 7F F8 FF FF 7F  6B 61 63 30 00           ........kac0.   
```

#### Opcodes

```
  0: 0x008F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kac0" with entities [EventEntity, EventEntity]
  1: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         5B 00 80               [..
00A0: F8 FF FF 7F F8 FF FF 7F  6B 61 63 31 00           ........kac1.   
```

#### Opcodes

```
  0: 0x009D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kac1" with entities [EventEntity, EventEntity], work=181*
  1: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         53 F8 FF               S..
00B0: FF 7F F8 FF FF 7F 6B 61  63 30 00                 ......kac0.     
```

#### Opcodes

```
  0: 0x00AD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kac0" with entities [EventEntity, EventEntity]
  1: 0x00BA [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   5B 00 80 F8 FF             [....
00C0: FF 7F F8 FF FF 7F 64 65  64 30 00                 ......ded0.     
```

#### Opcodes

```
  0: 0x00BB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ded0" with entities [EventEntity, EventEntity], work=181*
  1: 0x00CA [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CB   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                   53 F8 FF FF 7F             S....
00D0: F8 FF FF 7F 64 65 64 30  00                       ....ded0.       
```

#### Opcodes

```
  0: 0x00CB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ded0" with entities [EventEntity, EventEntity]
  1: 0x00D8 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D9   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                             5B 01 80 F8 FF FF 7F           [......
00E0: F8 FF FF 7F 61 77 6B 30  53 F8 FF FF 7F F8 FF FF  ....awk0S.......
00F0: 7F 61 77 6B 30 1E A8 A0  0A 01 00                 .awk0......     
```

#### Opcodes

```
  0: 0x00D9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "awk0" with entities [EventEntity, EventEntity], work=182*
  1: 0x00E8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "awk0" with entities [EventEntity, EventEntity]
  2: 0x00F5 [0x1E] EventEntity looks at Unnamed NPC (ID: 17473704/0x010AA0A8) and starts talking
  3: 0x00FA [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FB   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                   5B 01 80 F8 FF             [....
0100: FF 7F F8 FF FF 7F 64 77  6E 30 53 F8 FF FF 7F F8  ......dwn0S.....
0110: FF FF 7F 64 77 6E 30 00                           ...dwn0.        
```

#### Opcodes

```
  0: 0x00FB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dwn0" with entities [EventEntity, EventEntity], work=182*
  1: 0x010A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dwn0" with entities [EventEntity, EventEntity]
  2: 0x0117 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0118   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                          5B 01 80 F8 FF FF 7F F8          [.......
0120: FF FF 7F 73 63 6B 30 00                           ...sck0.        
```

#### Opcodes

```
  0: 0x0118 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sck0" with entities [EventEntity, EventEntity], work=182*
  1: 0x0127 [0x00] END_REQSTACK()
```

### Event 61

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0128   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                          92 01 F8 FF FF 7F 37 02          ......7.
0130: 80 03 80 04 80 05 80 00                           ........        
```

#### Opcodes

```
  0: 0x0128 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x012E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-62.114*, z=23.758*, y=9.237*, direction=257.3°*
  2: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0138   |
| Data Size    | 30 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          32 06 80 3B F8 FF FF 7F          2..;....
0140: 00 00 02 00 01 00 07 02  00 07 80 1F 00 00 00 02  ................
0150: 00 01 00 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0138 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x013B [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[1])
  2: 0x0146 [0x07] ExtData[1]->WorkLocal[2] += 8000*
  3: 0x014B [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  4: 0x0153 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0155 [0x00] END_REQSTACK()
```

### Event 62

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0156  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   00                                    .         
```

#### Opcodes

```
  0: 0x0156 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0157   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      32  06 80 3B F8 FF FF 7F 00         2..;.....
0160: 00 02 00 01 00 08 00 00  08 80 08 02 00 08 80 1F  ................
0170: 00 00 00 02 00 01 00 1F  01 6F 29 08 AF A0 0A 01  .........o).....
0180: 06 00                                             ..              
```

#### Opcodes

```
  0: 0x0157 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x015A [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[1])
  2: 0x0165 [0x08] ExtData[1]->WorkLocal[0] -= 500*
  3: 0x016A [0x08] ExtData[1]->WorkLocal[2] -= 500*
  4: 0x016F [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  5: 0x0177 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0179 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x017A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=King of Cups (ID: 17473711/0x010AA0AF), tag_num=0x06)
  8: 0x0181 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0182  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:       00                                            .             
```

#### Opcodes

```
  0: 0x0182 [0x00] END_REQSTACK()
```

### Event 32004

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0183  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:          00                                          .            
```

#### Opcodes

```
  0: 0x0183 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0184  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:             00                                        .           
```

#### Opcodes

```
  0: 0x0184 [0x00] END_REQSTACK()
```
