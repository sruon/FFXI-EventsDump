# 17826013 - Patrillaut

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 580 bytes                 |
| Total Events     | 19                        |
| References Count | 29                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     19 |              3 |
| [65535.2](#event-655352)   | 0x0014       |     19 |              3 |
| [65535.3](#event-655353)   | 0x0027       |     19 |              3 |
| [5067](#event-5067)        | 0x003A       |      1 |              1 |
| [65535.4](#event-655354)   | 0x003B       |     14 |              4 |
| [65535.5](#event-655355)   | 0x0049       |     17 |              5 |
| [5095](#event-5095)        | 0x005A       |      7 |              2 |
| [65535.6](#event-655356)   | 0x0061       |     14 |              4 |
| [65535.7](#event-655357)   | 0x006F       |      9 |              3 |
| [5208](#event-5208)        | 0x0078       |      7 |              2 |
| [65535.8](#event-655358)   | 0x007F       |     45 |              9 |
| [65535.9](#event-655359)   | 0x00AC       |     13 |              3 |
| [65535.10](#event-6553510) | 0x00B9       |     96 |             19 |
| [5218](#event-5218)        | 0x0119       |      7 |              2 |
| [65535.11](#event-6553511) | 0x0120       |     45 |              7 |
| [65535.12](#event-6553512) | 0x014D       |     13 |              3 |
| [65535.13](#event-6553513) | 0x015A       |     13 |              3 |
| [65535.14](#event-6553514) | 0x0167       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001D      |          29 |
|       1 | 0x00A9      |         169 |
|       2 | 0x005B      |          91 |
|       3 | 0x000D      |          13 |
|       4 | 0x128BB     |       75963 |
|       5 | 0xFFFE1FDF  |  4294844383 |
|       6 | 0x0FA0      |        4000 |
|       7 | 0x07FF      |        2047 |
|       8 | 0xDF2D      |       57133 |
|       9 | 0xFFFE2503  |  4294845699 |
|      10 | 0x12682     |       75394 |
|      11 | 0xFFFE1DB4  |  4294843828 |
|      12 | 0x003C      |          60 |
|      13 | 0x151C6     |       86470 |
|      14 | 0xFFFE3068  |  4294848616 |
|      15 | 0x0F96      |        3990 |
|      16 | 0x001E      |          30 |
|      17 | 0x062B      |        1579 |
|      18 | 0x0005      |           5 |
|      19 | 0x012C      |         300 |
|      20 | 0x0002      |           2 |
|      21 | 0x0000      |           0 |
|      22 | 0x0008      |           8 |
|      23 | 0x0001      |           1 |
|      24 | 0x000C      |          12 |
|      25 | 0x0004      |           4 |
|      26 | 0x0078      |         120 |
|      27 | 0x010E      |         270 |
|      28 | 0x0025      |          37 |

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
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 1C 00 17 00                                       ....            
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0010 [0x1C] WAIT(Work_Zone_1700[0] ticks)
  2: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             66 01 80 F8  FF FF 7F F8 FF FF 7F 74      f..........t
0020: 6C 6B 30 1C 00 17 00                              lk0....         
```

#### Opcodes

```
  0: 0x0014 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=169*
  1: 0x0023 [0x1C] WAIT(Work_Zone_1700[0] ticks)
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      66  02 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 70 61 73 30 1C 00  17 00                    ..pas0....      
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=91*
  1: 0x0036 [0x1C] WAIT(Work_Zone_1700[0] ticks)
  2: 0x0039 [0x00] END_REQSTACK()
```

### Event 5067

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                00                           .     
```

#### Opcodes

```
  0: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   32 03 80 1F 00             2....
0040: 04 80 05 80 06 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x003B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=75.963*, Z=-122.913*, Y=4.000*
  2: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             32 03 80 39 07 80 1F           2..9...
0050: 00 08 80 09 80 06 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0049 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004C [0x39] SET_ENTITY_DIRECTION(direction=11.2°*)
  2: 0x004F [0x1F] MOVE_ENTITY: EventEntity moves to X=57.133*, Z=-121.597*, Y=4.000*
  3: 0x0057 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0059 [0x00] END_REQSTACK()
```

### Event 5095

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                92 01 F8 FF FF 7F            ......
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x005A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    32 03 80 1F 00 0A 80  0B 80 06 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0061 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0064 [0x1F] MOVE_ENTITY: EventEntity moves to X=75.394*, Z=-123.468*, Y=4.000*
  2: 0x006C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006F  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               7B                 {
0070: F8 FF FF 7F 39 07 80 00                           ....9...        
```

#### Opcodes

```
  0: 0x006F [0x7B] EventEntity stops talking
  1: 0x0074 [0x39] SET_ENTITY_DIRECTION(direction=11.2°*)
  2: 0x0077 [0x00] END_REQSTACK()
```

### Event 5208

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0078  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0078 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 45 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               1C                 .
0080: 0C 80 32 03 80 1F 00 0D  80 0E 80 0F 80 1F 01 1E  ..2.............
0090: DA 00 10 01 7B F8 FF FF  7F 1C 10 80 66 00 80 F8  ....{.......f...
00A0: FF FF 7F F8 FF FF 7F 73  69 74 30 00              .......sit0.    
```

#### Opcodes

```
  0: 0x007F [0x1C] WAIT(60* ticks)
  1: 0x0082 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0085 [0x1F] MOVE_ENTITY: EventEntity moves to X=86.470*, Z=-118.680*, Y=3.990*
  3: 0x008D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x008F [0x1E] EventEntity looks at Tuffle-Buffle (ID: 17826010/0x011000DA) and starts talking
  5: 0x0094 [0x7B] EventEntity stops talking
  6: 0x0099 [0x1C] WAIT(30* ticks)
  7: 0x009C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit0" with entities [EventEntity, EventEntity], work=29*
  8: 0x00AB [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      6E F8 FF FF              n...
00B0: 7F 11 80 99 F8 FF FF 7F  00                       .........       
```

#### Opcodes

```
  0: 0x00AC [0x6E] EventEntity uses emote 1579*
  1: 0x00B3 [0x99] Wait for EventEntity animation to complete
  2: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 96 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             13 00 00 12 80 14 00           .......
00C0: 00 0C 80 07 00 00 13 80  1C 00 00 13 00 00 14 80  ................
00D0: 02 00 00 15 80 80 E7 00  6E F8 FF FF 7F 16 80 99  ........n.......
00E0: F8 FF FF 7F 01 15 01 02  00 00 17 80 80 FE 00 6E  ...............n
00F0: F8 FF FF 7F 18 80 99 F8  FF FF 7F 01 15 01 02 00  ................
0100: 00 14 80 80 15 01 6E F8  FF FF 7F 19 80 99 F8 FF  ......n.........
0110: FF 7F 01 15 01 01 B9 00  00                       .........       
```

#### Opcodes

```
  0: 0x00B9 [0x13] ExtData[1]->WorkLocal[0] = rand() % 5*
  1: 0x00BE [0x14] ExtData[1]->WorkLocal[0] *= 60*
  2: 0x00C3 [0x07] ExtData[1]->WorkLocal[0] += 300*
  3: 0x00C8 [0x1C] WAIT(ExtData[1]->WorkLocal[0] ticks)
  4: 0x00CB [0x13] ExtData[1]->WorkLocal[0] = rand() % 2*
  5: 0x00D0 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x00E7
  6: 0x00D8 [0x6E] EventEntity uses emote 8*
  7: 0x00DF [0x99] Wait for EventEntity animation to complete
  8: 0x00E4 [0x01] GOTO 0x0115
  9: 0x00E7 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x00FE
 10: 0x00EF [0x6E] EventEntity uses emote 12*
 11: 0x00F6 [0x99] Wait for EventEntity animation to complete
 12: 0x00FB [0x01] GOTO 0x0115
 13: 0x00FE [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x0115
 14: 0x0106 [0x6E] EventEntity uses emote 4*
 15: 0x010D [0x99] Wait for EventEntity animation to complete
 16: 0x0112 [0x01] GOTO 0x0115

SUBROUTINE_0115:
 17: 0x0115 [0x01] GOTO 0x00B9
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0118 [0x00] END_REQSTACK()
```

### Event 5218

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0119  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x0119 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x011F [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 45 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 66 01 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1C  f..........tlk0.
0130: 1A 80 66 01 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  ..f..........tlk
0140: 31 1C 1B 80 7B F8 FF FF  7F 39 07 80 00           1...{....9...   
```

#### Opcodes

```
  0: 0x0120 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=169*
  1: 0x012F [0x1C] WAIT(120* ticks)
  2: 0x0132 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=169*
  3: 0x0141 [0x1C] WAIT(270* ticks)
  4: 0x0144 [0x7B] EventEntity stops talking
  5: 0x0149 [0x39] SET_ENTITY_DIRECTION(direction=11.2°*)
  6: 0x014C [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014D   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                         6E F8 FF               n..
0150: FF 7F 1C 80 99 F8 FF FF  7F 00                    ..........      
```

#### Opcodes

```
  0: 0x014D [0x6E] EventEntity uses emote 37*
  1: 0x0154 [0x99] Wait for EventEntity animation to complete
  2: 0x0159 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015A   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                6E F8 FF FF 7F 18            n.....
0160: 80 99 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x015A [0x6E] EventEntity uses emote 12*
  1: 0x0161 [0x99] Wait for EventEntity animation to complete
  2: 0x0166 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0167   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                      6E  F8 FF FF 7F 19 80 99 F8         n........
0170: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0167 [0x6E] EventEntity uses emote 4*
  1: 0x016E [0x99] Wait for EventEntity animation to complete
  2: 0x0173 [0x00] END_REQSTACK()
```
