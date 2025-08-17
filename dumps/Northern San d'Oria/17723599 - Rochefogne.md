# 17723599 - Rochefogne

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 748 bytes                     |
| Total Events     | 15                            |
| References Count | 23                            |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [1](#event-1)              | 0x0001       |     18 |              4 |
| [65535.1](#event-655351)   | 0x0013       |     40 |              5 |
| [65535.2](#event-655352)   | 0x003B       |     45 |              6 |
| [65535.3](#event-655353)   | 0x0068       |     12 |              3 |
| [65535.4](#event-655354)   | 0x0074       |     29 |              3 |
| [65535.5](#event-655355)   | 0x0091       |     64 |              6 |
| [65535.6](#event-655356)   | 0x00D1       |     39 |              4 |
| [65535.7](#event-655357)   | 0x00F8       |     49 |              5 |
| [65535.8](#event-655358)   | 0x0129       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0139       |     53 |              5 |
| [65535.10](#event-6553510) | 0x016E       |    107 |             11 |
| [65535.11](#event-6553511) | 0x01D9       |     49 |              5 |
| [65535.12](#event-6553512) | 0x020A       |     29 |              3 |
| [65535.13](#event-6553513) | 0x0227       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x24910     |      149776 |
|       1 | 0x1FFF7     |      131063 |
|       2 | 0xFFFFDF32  |  4294958898 |
|       3 | 0x0C36      |        3126 |
|       4 | 0x237A6     |      145318 |
|       5 | 0x2095E     |      133470 |
|       6 | 0x0000      |           0 |
|       7 | 0x0DB1      |        3505 |
|       8 | 0x000D      |          13 |
|       9 | 0x000F      |          15 |
|      10 | 0x001E      |          30 |
|      11 | 0x00F3      |         243 |
|      12 | 0x003C      |          60 |
|      13 | 0x0010      |          16 |
|      14 | 0x23CBD     |      146621 |
|      15 | 0x20670     |      132720 |
|      16 | 0x077D      |        1917 |
|      17 | 0x0018      |          24 |
|      18 | 0x0001      |           1 |
|      19 | 0x0080      |         128 |
|      20 | 0x22567     |      140647 |
|      21 | 0x2035B     |      131931 |
|      22 | 0x060A      |        1546 |

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

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 33  01 37 00 80 01 80 02 80   ......3.7......
0010: 03 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=149.776*, z=131.063*, y=-8.398*, direction=274.7°*
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 40 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          37 04 80 05 80  06 80 07 80 33 00 5B 08     7........3.[.
0020: 80 F8 FF FF 7F F8 FF FF  7F 6B 73 67 30 53 F8 FF  .........ksg0S..
0030: FF 7F F8 FF FF 7F 6B 73  67 30 00                 ......ksg0.     
```

#### Opcodes

```
  0: 0x0013 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=145.318*, z=133.470*, y=0.000*, direction=308.0°*
  1: 0x001C [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  2: 0x001E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ksg0" with entities [EventEntity, EventEntity], work=13*
  3: 0x002D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ksg0" with entities [EventEntity, EventEntity]
  4: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 45 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   22 00 37 04 80             ".7..
0040: 05 80 06 80 07 80 80 F8  FF FF 7F 5B 08 80 F8 FF  ...........[....
0050: FF 7F F8 FF FF 7F 6B 73  67 30 53 F8 FF FF 7F F8  ......ksg0S.....
0060: FF FF 7F 6B 73 67 30 00                           ...ksg0.        
```

#### Opcodes

```
  0: 0x003B [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x003D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=145.318*, z=133.470*, y=0.000*, direction=308.0°*
  2: 0x0046 [0x80] LOAD_WAIT(entity=EventEntity)
  3: 0x004B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ksg0" with entities [EventEntity, EventEntity], work=13*
  4: 0x005A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ksg0" with entities [EventEntity, EventEntity]
  5: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          22 00 37 04 80 05 80 06          ".7.....
0070: 80 07 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0068 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x006A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=145.318*, z=133.470*, y=0.000*, direction=308.0°*
  2: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             5B 08 80 F8  FF FF 7F F8 FF FF 7F 6B      [..........k
0080: 73 67 31 53 F8 FF FF 7F  F8 FF FF 7F 6B 73 67 31  sg1S........ksg1
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0074 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ksg1" with entities [EventEntity, EventEntity], work=13*
  1: 0x0083 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ksg1" with entities [EventEntity, EventEntity]
  2: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 64 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    5B 08 80 F8 FF FF 7F  F8 FF FF 7F 77 6F 6E 32   [..........won2
00A0: 5B 09 80 F8 FF FF 7F F8  FF FF 7F 75 6B 74 30 1C  [..........ukt0.
00B0: 0A 80 45 0B 80 10 70 0E  01 10 70 0E 01 73 65 30  ..E...p...p..se0
00C0: 31 06 80 53 F8 FF FF 7F  F8 FF FF 7F 75 6B 74 30  1..S........ukt0
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x0091 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "won2" with entities [EventEntity, EventEntity], work=13*
  1: 0x00A0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ukt0" with entities [EventEntity, EventEntity], work=15*
  2: 0x00AF [0x1C] WAIT(30* ticks)
  3: 0x00B2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se01" with entities [Shamonde (ID: 17723408/0x010E7010), Shamonde (ID: 17723408/0x010E7010)], work=[243*, 0*]
  4: 0x00C3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ukt0" with entities [EventEntity, EventEntity]
  5: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 39 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    79 00 F8 FF FF 7F 02  70 0E 01 5B 09 80 F8 FF   y......p..[....
00E0: FF 7F F8 FF FF 7F 6B 6D  65 30 53 F8 FF FF 7F F8  ......kme0S.....
00F0: FF FF 7F 6B 6D 65 30 00                           ...kme0.        
```

#### Opcodes

```
  0: 0x00D1 [0x79] EventEntity looks at Trion (ID: 17723394/0x010E7002) (Basic look)
  1: 0x00DB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kme0" with entities [EventEntity, EventEntity], work=15*
  2: 0x00EA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kme0" with entities [EventEntity, EventEntity]
  3: 0x00F7 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F8   |
| Data Size    | 49 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                          5B 09 80 F8 FF FF 7F F8          [.......
0100: FF FF 7F 73 74 72 30 1C  0C 80 45 0B 80 10 70 0E  ...str0...E...p.
0110: 01 10 70 0E 01 73 65 30  34 06 80 53 F8 FF FF 7F  ..p..se04..S....
0120: F8 FF FF 7F 73 74 72 30  00                       ....str0.       
```

#### Opcodes

```
  0: 0x00F8 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "str0" with entities [EventEntity, EventEntity], work=15*
  1: 0x0107 [0x1C] WAIT(60* ticks)
  2: 0x010A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se04" with entities [Shamonde (ID: 17723408/0x010E7010), Shamonde (ID: 17723408/0x010E7010)], work=[243*, 0*]
  3: 0x011B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "str0" with entities [EventEntity, EventEntity]
  4: 0x0128 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0129   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                             5B 0D 80 F8 FF FF 7F           [......
0130: F8 FF FF 7F 6D 61 62 30  00                       ....mab0.       
```

#### Opcodes

```
  0: 0x0129 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mab0" with entities [EventEntity, EventEntity], work=16*
  1: 0x0138 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0139   |
| Data Size    | 53 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                             37 0E 80 0F 80 06 80           7......
0140: 10 80 66 11 80 F8 FF FF  7F F8 FF FF 7F 6B 6E 30  ..f..........kn0
0150: 30 53 F8 FF FF 7F F8 FF  FF 7F 6B 6E 30 30 5B 0D  0S........kn00[.
0160: 80 F8 FF FF 7F F8 FF FF  7F 00 FE FE FE 00        ..............  
```

#### Opcodes

```
  0: 0x0139 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=146.621*, z=132.720*, y=0.000*, direction=168.5°*
  1: 0x0142 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "kn00" with entities [EventEntity, EventEntity], work=24*
  2: 0x0151 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kn00" with entities [EventEntity, EventEntity]
  3: 0x015E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=16*
  4: 0x016D [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x016E    |
| Data Size    | 107 bytes |
| Instructions | 11        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                            6C CF                l.
0170: 70 0E 01 06 80 12 80 3B  D0 70 0E 01 00 00 01 00  p......;.p......
0180: 02 00 3A D0 70 0E 01 03  00 37 00 00 01 00 02 00  ..:.p....7......
0190: 03 00 5B 0D 80 F8 FF FF  7F F8 FF FF 7F 61 74 6B  ..[..........atk
01A0: 30 6C CF 70 0E 01 13 80  12 80 53 F8 FF FF 7F F8  0l.p......S.....
01B0: FF FF 7F 61 74 6B 30 6C  CF 70 0E 01 06 80 12 80  ...atk0l.p......
01C0: 37 14 80 15 80 06 80 16  80 5B 09 80 F8 FF FF 7F  7........[......
01D0: F8 FF FF 7F 73 68 67 30  00                       ....shg0.       
```

#### Opcodes

```
  0: 0x016E [0x6C] FADE_ENTITY_COLOR(entity_id=Rochefogne (ID: 17723599/0x010E70CF), end_alpha=0*, fade_time=1*)
  1: 0x0177 [0x3B] GET_ENTITY_POSITION(entity=Unnamed NPC (ID: 17723600/0x010E70D0), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  2: 0x0182 [0x3A] CONVERT_YAW_TO_BYTE(entity=Unnamed NPC (ID: 17723600/0x010E70D0), result_destination=ExtData[1]->WorkLocal[3])
  3: 0x0189 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
  4: 0x0192 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "atk0" with entities [EventEntity, EventEntity], work=16*
  5: 0x01A1 [0x6C] FADE_ENTITY_COLOR(entity_id=Rochefogne (ID: 17723599/0x010E70CF), end_alpha=128*, fade_time=1*)
  6: 0x01AA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "atk0" with entities [EventEntity, EventEntity]
  7: 0x01B7 [0x6C] FADE_ENTITY_COLOR(entity_id=Rochefogne (ID: 17723599/0x010E70CF), end_alpha=0*, fade_time=1*)
  8: 0x01C0 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=140.647*, z=131.931*, y=0.000*, direction=135.9°*
  9: 0x01C9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "shg0" with entities [EventEntity, EventEntity], work=15*
 10: 0x01D8 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D9   |
| Data Size    | 49 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                             5B 09 80 F8 FF FF 7F           [......
01E0: F8 FF FF 7F 74 61 6F 30  1C 0A 80 45 0B 80 F8 FF  ....tao0...E....
01F0: FF 7F F8 FF FF 7F 73 65  30 39 06 80 53 F8 FF FF  ......se09..S...
0200: 7F F8 FF FF 7F 74 61 6F  30 00                    .....tao0.      
```

#### Opcodes

```
  0: 0x01D9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tao0" with entities [EventEntity, EventEntity], work=15*
  1: 0x01E8 [0x1C] WAIT(30* ticks)
  2: 0x01EB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se09" with entities [EventEntity, EventEntity], work=[243*, 0*]
  3: 0x01FC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tao0" with entities [EventEntity, EventEntity]
  4: 0x0209 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x020A   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                5B 08 80 F8 FF FF            [.....
0210: 7F F8 FF FF 7F 77 6F 6E  32 53 F8 FF FF 7F F8 FF  .....won2S......
0220: FF 7F 77 6F 6E 32 00                              ..won2.         
```

#### Opcodes

```
  0: 0x020A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "won2" with entities [EventEntity, EventEntity], work=13*
  1: 0x0219 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "won2" with entities [EventEntity, EventEntity]
  2: 0x0226 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0227   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                      5B  08 80 F8 FF FF 7F F8 FF         [........
0230: FF 7F 77 6F 66 32 53 F8  FF FF 7F F8 FF FF 7F 77  ..wof2S........w
0240: 6F 66 32 00                                       of2.            
```

#### Opcodes

```
  0: 0x0227 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wof2" with entities [EventEntity, EventEntity], work=13*
  1: 0x0236 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wof2" with entities [EventEntity, EventEntity]
  2: 0x0243 [0x00] END_REQSTACK()
```
