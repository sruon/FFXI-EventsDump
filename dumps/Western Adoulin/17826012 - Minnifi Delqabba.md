# 17826012 - Minnifi Delqabba

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 708 bytes                 |
| Total Events     | 30                        |
| References Count | 27                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [5045](#event-5045)        | 0x0001       |      2 |              2 |
| [5046](#event-5046)        | 0x0003       |      2 |              2 |
| [5047](#event-5047)        | 0x0005       |      2 |              2 |
| [5048](#event-5048)        | 0x0007       |      2 |              2 |
| [5049](#event-5049)        | 0x0009       |      2 |              2 |
| [5050](#event-5050)        | 0x000B       |      2 |              2 |
| [5051](#event-5051)        | 0x000D       |      2 |              2 |
| [65535.1](#event-655351)   | 0x000F       |     19 |              3 |
| [65535.2](#event-655352)   | 0x0022       |     19 |              3 |
| [65535.3](#event-655353)   | 0x0035       |     19 |              3 |
| [65535.4](#event-655354)   | 0x0048       |     19 |              3 |
| [65535.5](#event-655355)   | 0x005B       |     19 |              3 |
| [65535.6](#event-655356)   | 0x006E       |     16 |              4 |
| [65535.7](#event-655357)   | 0x007E       |     16 |              4 |
| [65535.8](#event-655358)   | 0x008E       |     16 |              4 |
| [65535.9](#event-655359)   | 0x009E       |     16 |              4 |
| [65535.10](#event-6553510) | 0x00AE       |     16 |              4 |
| [5067](#event-5067)        | 0x00BE       |      1 |              1 |
| [5095](#event-5095)        | 0x00BF       |      7 |              2 |
| [65535.11](#event-6553511) | 0x00C6       |     15 |              5 |
| [5208](#event-5208)        | 0x00D5       |      7 |              2 |
| [65535.12](#event-6553512) | 0x00DC       |     45 |              9 |
| [5218](#event-5218)        | 0x0109       |      7 |              2 |
| [65535.13](#event-6553513) | 0x0110       |     45 |              7 |
| [65535.14](#event-6553514) | 0x013D       |     13 |              3 |
| [65535.15](#event-6553515) | 0x014A       |     13 |              3 |
| [65535.16](#event-6553516) | 0x0157       |     13 |              3 |
| [65535.17](#event-6553517) | 0x0164       |      9 |              3 |
| [65535.18](#event-6553518) | 0x016D       |     96 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003B      |          59 |
|       1 | 0x00C7      |         199 |
|       2 | 0x0008      |           8 |
|       3 | 0x0079      |         121 |
|       4 | 0x000A      |          10 |
|       5 | 0x0001      |           1 |
|       6 | 0x0009      |           9 |
|       7 | 0x000D      |          13 |
|       8 | 0x0018      |          24 |
|       9 | 0x12CC8     |       77000 |
|      10 | 0xFFFE19AC  |  4294842796 |
|      11 | 0x0FA0      |        4000 |
|      12 | 0x003C      |          60 |
|      13 | 0x15338     |       86840 |
|      14 | 0xFFFE2DAC  |  4294847916 |
|      15 | 0x001E      |          30 |
|      16 | 0x0364      |         868 |
|      17 | 0x00B4      |         180 |
|      18 | 0x0530      |        1328 |
|      19 | 0x005A      |          90 |
|      20 | 0x07FF      |        2047 |
|      21 | 0x0004      |           4 |
|      22 | 0x062B      |        1579 |
|      23 | 0x0005      |           5 |
|      24 | 0x012C      |         300 |
|      25 | 0x0002      |           2 |
|      26 | 0x0000      |           0 |

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

### Event 5045

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 2 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    26 00                                           &.             
```

#### Opcodes

```
  0: 0x0001 [0x26] DEPRECATED_YIELD
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0002 [0x00] END_REQSTACK()
```

### Event 5046

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 2 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          26 00                                       &.           
```

#### Opcodes

```
  0: 0x0003 [0x26] DEPRECATED_YIELD
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0004 [0x00] END_REQSTACK()
```

### Event 5047

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 2 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                26 00                                   &.         
```

#### Opcodes

```
  0: 0x0005 [0x26] DEPRECATED_YIELD
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0006 [0x00] END_REQSTACK()
```

### Event 5048

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 2 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      26  00                              &.       
```

#### Opcodes

```
  0: 0x0007 [0x26] DEPRECATED_YIELD
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0008 [0x00] END_REQSTACK()
```

### Event 5049

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 2 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             26 00                          &.     
```

#### Opcodes

```
  0: 0x0009 [0x26] DEPRECATED_YIELD
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x000A [0x00] END_REQSTACK()
```

### Event 5050

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 2 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   26 00                      &.   
```

#### Opcodes

```
  0: 0x000B [0x26] DEPRECATED_YIELD
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x000C [0x00] END_REQSTACK()
```

### Event 5051

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 2 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         26 00                  &. 
```

#### Opcodes

```
  0: 0x000D [0x26] DEPRECATED_YIELD
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               66                 f
0010: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1C 00  ..........tlk0..
0020: 17 00                                             ..              
```

#### Opcodes

```
  0: 0x000F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  1: 0x001E [0x1C] WAIT(Work_Zone_1700[0] ticks)
  2: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       66 01 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B    f..........tlk
0030: 30 1C 00 17 00                                    0....           
```

#### Opcodes

```
  0: 0x0022 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=199*
  1: 0x0031 [0x1C] WAIT(Work_Zone_1700[0] ticks)
  2: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                66 02 80  F8 FF FF 7F F8 FF FF 7F       f..........
0040: 75 72 65 30 1C 00 17 00                           ure0....        
```

#### Opcodes

```
  0: 0x0035 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ure0" with entities [EventEntity, EventEntity], work=8*
  1: 0x0044 [0x1C] WAIT(Work_Zone_1700[0] ticks)
  2: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          66 03 80 F8 FF FF 7F F8          f.......
0050: FF FF 7F 70 61 73 30 1C  00 17 00                 ...pas0....     
```

#### Opcodes

```
  0: 0x0048 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=121*
  1: 0x0057 [0x1C] WAIT(Work_Zone_1700[0] ticks)
  2: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   66 00 80 F8 FF             f....
0060: FF 7F F8 FF FF 7F 74 68  6B 31 1C 00 17 00        ......thk1....  
```

#### Opcodes

```
  0: 0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=59*
  1: 0x006A [0x1C] WAIT(Work_Zone_1700[0] ticks)
  2: 0x006D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            6E F8                n.
0070: FF FF 7F 04 80 99 F8 FF  FF 7F 1C 00 17 00        ..............  
```

#### Opcodes

```
  0: 0x006E [0x6E] EventEntity uses emote 10*
  1: 0x0075 [0x99] Wait for EventEntity animation to complete
  2: 0x007A [0x1C] WAIT(Work_Zone_1700[0] ticks)
  3: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            6E F8                n.
0080: FF FF 7F 05 80 99 F8 FF  FF 7F 1C 00 17 00        ..............  
```

#### Opcodes

```
  0: 0x007E [0x6E] EventEntity uses emote 1*
  1: 0x0085 [0x99] Wait for EventEntity animation to complete
  2: 0x008A [0x1C] WAIT(Work_Zone_1700[0] ticks)
  3: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            6E F8                n.
0090: FF FF 7F 06 80 99 F8 FF  FF 7F 1C 00 17 00        ..............  
```

#### Opcodes

```
  0: 0x008E [0x6E] EventEntity uses emote 9*
  1: 0x0095 [0x99] Wait for EventEntity animation to complete
  2: 0x009A [0x1C] WAIT(Work_Zone_1700[0] ticks)
  3: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            6E F8                n.
00A0: FF FF 7F 07 80 99 F8 FF  FF 7F 1C 00 17 00        ..............  
```

#### Opcodes

```
  0: 0x009E [0x6E] EventEntity uses emote 13*
  1: 0x00A5 [0x99] Wait for EventEntity animation to complete
  2: 0x00AA [0x1C] WAIT(Work_Zone_1700[0] ticks)
  3: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            6E F8                n.
00B0: FF FF 7F 08 80 99 F8 FF  FF 7F 1C 00 17 00        ..............  
```

#### Opcodes

```
  0: 0x00AE [0x6E] EventEntity uses emote 24*
  1: 0x00B5 [0x99] Wait for EventEntity animation to complete
  2: 0x00BA [0x1C] WAIT(Work_Zone_1700[0] ticks)
  3: 0x00BD [0x00] END_REQSTACK()
```

### Event 5067

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BE  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            00                   . 
```

#### Opcodes

```
  0: 0x00BE [0x00] END_REQSTACK()
```

### Event 5095

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BF  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               92                 .
00C0: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x00BF [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   32 07  80 1F 00 09 80 0A 80 0B        2.........
00D0: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x00C6 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00C9 [0x1F] MOVE_ENTITY: EventEntity moves to X=77.000*, Z=-124.500*, Y=4.000*
  2: 0x00D1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00D4 [0x00] END_REQSTACK()
```

### Event 5208

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D5  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x00D5 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00DB [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DC   |
| Data Size    | 45 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      1C 0C 80 32              ...2
00E0: 07 80 1F 00 0D 80 0E 80  0B 80 1F 01 1E DA 00 10  ................
00F0: 01 7B F8 FF FF 7F 1C 0F  80 66 00 80 F8 FF FF 7F  .{.......f......
0100: F8 FF FF 7F 73 69 74 30  00                       ....sit0.       
```

#### Opcodes

```
  0: 0x00DC [0x1C] WAIT(60* ticks)
  1: 0x00DF [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x00E2 [0x1F] MOVE_ENTITY: EventEntity moves to X=86.840*, Z=-119.380*, Y=4.000*
  3: 0x00EA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00EC [0x1E] EventEntity looks at Tuffle-Buffle (ID: 17826010/0x011000DA) and starts talking
  5: 0x00F1 [0x7B] EventEntity stops talking
  6: 0x00F6 [0x1C] WAIT(30* ticks)
  7: 0x00F9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit0" with entities [EventEntity, EventEntity], work=59*
  8: 0x0108 [0x00] END_REQSTACK()
```

### Event 5218

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0109  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x0109 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x010F [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0110   |
| Data Size    | 45 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110: 5B 10 80 F8 FF FF 7F F8  FF FF 7F 79 61 64 30 1C  [..........yad0.
0120: 11 80 5B 12 80 F8 FF FF  7F F8 FF FF 7F 69 72 6F  ..[..........iro
0130: 31 1C 13 80 7B F8 FF FF  7F 39 14 80 00           1...{....9...   
```

#### Opcodes

```
  0: 0x0110 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yad0" with entities [EventEntity, EventEntity], work=868*
  1: 0x011F [0x1C] WAIT(180* ticks)
  2: 0x0122 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "iro1" with entities [EventEntity, EventEntity], work=1328*
  3: 0x0131 [0x1C] WAIT(90* ticks)
  4: 0x0134 [0x7B] EventEntity stops talking
  5: 0x0139 [0x39] SET_ENTITY_DIRECTION(direction=11.2°*)
  6: 0x013C [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013D   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                         6E F8 FF               n..
0140: FF 7F 04 80 99 F8 FF FF  7F 00                    ..........      
```

#### Opcodes

```
  0: 0x013D [0x6E] EventEntity uses emote 10*
  1: 0x0144 [0x99] Wait for EventEntity animation to complete
  2: 0x0149 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014A   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                6E F8 FF FF 7F 15            n.....
0150: 80 99 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x014A [0x6E] EventEntity uses emote 4*
  1: 0x0151 [0x99] Wait for EventEntity animation to complete
  2: 0x0156 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0157   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      6E  F8 FF FF 7F 16 80 99 F8         n........
0160: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0157 [0x6E] EventEntity uses emote 1579*
  1: 0x015E [0x99] Wait for EventEntity animation to complete
  2: 0x0163 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0164  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:             7B F8 FF FF  7F 39 14 80 00               {....9...   
```

#### Opcodes

```
  0: 0x0164 [0x7B] EventEntity stops talking
  1: 0x0169 [0x39] SET_ENTITY_DIRECTION(direction=11.2°*)
  2: 0x016C [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016D   |
| Data Size    | 96 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                         13 00 00               ...
0170: 17 80 14 00 00 0C 80 07  00 00 18 80 1C 00 00 13  ................
0180: 00 00 19 80 02 00 00 1A  80 80 9B 01 6E F8 FF FF  ............n...
0190: 7F 02 80 99 F8 FF FF 7F  01 C9 01 02 00 00 05 80  ................
01A0: 80 B2 01 6E F8 FF FF 7F  04 80 99 F8 FF FF 7F 01  ...n............
01B0: C9 01 02 00 00 19 80 80  C9 01 6E F8 FF FF 7F 15  ..........n.....
01C0: 80 99 F8 FF FF 7F 01 C9  01 01 6D 01 00           ..........m..   
```

#### Opcodes

```
  0: 0x016D [0x13] ExtData[1]->WorkLocal[0] = rand() % 5*
  1: 0x0172 [0x14] ExtData[1]->WorkLocal[0] *= 60*
  2: 0x0177 [0x07] ExtData[1]->WorkLocal[0] += 300*
  3: 0x017C [0x1C] WAIT(ExtData[1]->WorkLocal[0] ticks)
  4: 0x017F [0x13] ExtData[1]->WorkLocal[0] = rand() % 2*
  5: 0x0184 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x019B
  6: 0x018C [0x6E] EventEntity uses emote 8*
  7: 0x0193 [0x99] Wait for EventEntity animation to complete
  8: 0x0198 [0x01] GOTO 0x01C9
  9: 0x019B [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x01B2
 10: 0x01A3 [0x6E] EventEntity uses emote 10*
 11: 0x01AA [0x99] Wait for EventEntity animation to complete
 12: 0x01AF [0x01] GOTO 0x01C9
 13: 0x01B2 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x01C9
 14: 0x01BA [0x6E] EventEntity uses emote 4*
 15: 0x01C1 [0x99] Wait for EventEntity animation to complete
 16: 0x01C6 [0x01] GOTO 0x01C9

SUBROUTINE_01C9:
 17: 0x01C9 [0x01] GOTO 0x016D
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x01CC [0x00] END_REQSTACK()
```
