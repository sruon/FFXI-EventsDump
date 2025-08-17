# 17465601 - Goblin Intimidator

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Chamber of Oracles (ID: 168) |
| Block Size       | 528 bytes                    |
| Total Events     | 21                           |
| References Count | 22                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     15 |              4 |
| [65535.2](#event-655352)   | 0x0010       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001A       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0024       |      8 |              3 |
| [65535.5](#event-655355)   | 0x002C       |     16 |              2 |
| [65535.6](#event-655356)   | 0x003C       |     33 |              3 |
| [5](#event-5)              | 0x005D       |      1 |              1 |
| [65535.7](#event-655357)   | 0x005E       |     34 |              4 |
| [65535.8](#event-655358)   | 0x0080       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0090       |     19 |              3 |
| [65535.10](#event-6553510) | 0x00A3       |     19 |              3 |
| [65535.11](#event-6553511) | 0x00B6       |     19 |              3 |
| [65535.12](#event-6553512) | 0x00C9       |     19 |              3 |
| [6](#event-6)              | 0x00DC       |      1 |              1 |
| [65535.13](#event-6553513) | 0x00DD       |     13 |              3 |
| [65535.14](#event-6553514) | 0x00EA       |     34 |              8 |
| [65535.15](#event-6553515) | 0x010C       |     19 |              3 |
| [65535.16](#event-6553516) | 0x011F       |     16 |              2 |
| [65535.17](#event-6553517) | 0x012F       |     19 |              3 |
| [65535.18](#event-6553518) | 0x0142       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x00B4      |         180 |
|       2 | 0x01F1      |         497 |
|       3 | 0x0001      |           1 |
|       4 | 0x0A54      |        2644 |
|       5 | 0x008B      |         139 |
|       6 | 0x00D8      |         216 |
|       7 | 0x0064      |         100 |
|       8 | 0x003C      |          60 |
|       9 | 0x00DA      |         218 |
|      10 | 0x00D7      |         215 |
|      11 | 0x0866      |        2150 |
|      12 | 0x00BC      |         188 |
|      13 | 0x0050      |          80 |
|      14 | 0x002D      |          45 |
|      15 | 0x0694      |        1684 |
|      16 | 0x087C      |        2172 |
|      17 | 0xFFFFF736  |  4294965046 |
|      18 | 0xFFFFC562  |  4294952290 |
|      19 | 0x023E      |         574 |
|      20 | 0xFFFF0212  |  4294902290 |
|      21 | 0x004A      |          74 |

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
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 92 01 F8 FF FF  7F 94 01 F8 FF FF 7F 00   "..............
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0009 [0x94] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 6C F8 FF FF 7F 00 80 00  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0010 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                6C F8 FF FF 7F 01            l.....
0020: 80 00 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=180*, fade_time=0*)
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             B6 00 02 80  C0 03 80 00                  ........    
```

#### Opcodes

```
  0: 0x0024 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=497*)
  1: 0x0028 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      5B 04 80 F8              [...
0030: FF FF 7F F8 FF FF 7F 66  6B 69 30 00              .......fki0.    
```

#### Opcodes

```
  0: 0x002C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fki0" with entities [EventEntity, EventEntity], work=2644*
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      C5 05 80 F8              ....
0040: FF FF 7F F8 FF FF 7F 6D  61 69 6E 00 80 5B 04 80  .......main..[..
0050: F8 FF FF 7F F8 FF FF 7F  66 6B 69 31 00           ........fki1.   
```

#### Opcodes

```
  0: 0x003C [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80006E69 for entities [EventEntity, EventEntity], work=139*, param=24941
  1: 0x004D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fki1" with entities [EventEntity, EventEntity], work=2644*
  2: 0x005C [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         00                     .  
```

#### Opcodes

```
  0: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            5B 06                [.
0060: 80 F8 FF FF 7F F8 FF FF  7F 66 6E 64 30 1C 07 80  .........fnd0...
0070: 5B 06 80 F8 FF FF 7F F8  FF FF 7F 66 6E 64 31 00  [..........fnd1.
```

#### Opcodes

```
  0: 0x005E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fnd0" with entities [EventEntity, EventEntity], work=216*
  1: 0x006D [0x1C] WAIT(100* ticks)
  2: 0x0070 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fnd1" with entities [EventEntity, EventEntity], work=216*
  3: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 5B 06 80 F8 FF FF 7F F8  FF FF 7F 68 61 70 30 00  [..........hap0.
```

#### Opcodes

```
  0: 0x0080 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap0" with entities [EventEntity, EventEntity], work=216*
  1: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 5B 06 80 F8 FF FF 7F F8  FF FF 7F 68 61 70 31 1C  [..........hap1.
00A0: 08 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0090 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap1" with entities [EventEntity, EventEntity], work=216*
  1: 0x009F [0x1C] WAIT(60* ticks)
  2: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          5B 09 80 F8 FF  FF 7F F8 FF FF 7F 77 65     [..........we
00B0: 74 63 1C 08 80 00                                 tc....          
```

#### Opcodes

```
  0: 0x00A3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wetc" with entities [EventEntity, EventEntity], work=218*
  1: 0x00B2 [0x1C] WAIT(60* ticks)
  2: 0x00B5 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B6   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   5B 0A  80 F8 FF FF 7F F8 FF FF        [.........
00C0: 7F 74 6C 6B 65 1C 08 80  00                       .tlke....       
```

#### Opcodes

```
  0: 0x00B6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlke" with entities [EventEntity, EventEntity], work=215*
  1: 0x00C5 [0x1C] WAIT(60* ticks)
  2: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             5B 0B 80 F8 FF FF 7F           [......
00D0: F8 FF FF 7F 70 6E 74 30  1C 0C 80 00              ....pnt0....    
```

#### Opcodes

```
  0: 0x00C9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pnt0" with entities [EventEntity, EventEntity], work=2150*
  1: 0x00D8 [0x1C] WAIT(188* ticks)
  2: 0x00DB [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      00                       .   
```

#### Opcodes

```
  0: 0x00DC [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         1C 0D 80               ...
00E0: 4A F8 FF FF 7F FF 80 0A  01 00                    J.........      
```

#### Opcodes

```
  0: 0x00DD [0x1C] WAIT(80* ticks)
  1: 0x00E0 [0x4A] EventEntity looks at Nanaa Mihgo (ID: 17465599/0x010A80FF)
  2: 0x00E9 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EA   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                32 0E 80 1F 00 0F            2.....
00F0: 80 10 80 11 80 1F 01 1F  00 00 80 12 80 13 80 1F  ................
0100: 01 5A 00 00 80 14 80 13  80 5A 01 00              .Z.......Z..    
```

#### Opcodes

```
  0: 0x00EA [0x32] ExtData[1]->MainSpeed = 45* * 0.1
  1: 0x00ED [0x1F] MOVE_ENTITY: EventEntity moves to X=1.684*, Z=2.172*, Y=-2.250*
  2: 0x00F5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F7 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=-15.006*, Y=0.574*
  4: 0x00FF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0101 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=0.000*, Z=-65.006*, Y=0.574*
  6: 0x0109 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  7: 0x010B [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010C   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                      5B 0B 80 F8              [...
0110: FF FF 7F F8 FF FF 7F 6F  64 6F 30 1C 15 80 00     .......odo0.... 
```

#### Opcodes

```
  0: 0x010C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "odo0" with entities [EventEntity, EventEntity], work=2150*
  1: 0x011B [0x1C] WAIT(74* ticks)
  2: 0x011E [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                               5B                 [
0120: 0B 80 F8 FF FF 7F F8 FF  FF 7F 6F 64 6F 31 00     ..........odo1. 
```

#### Opcodes

```
  0: 0x011F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "odo1" with entities [EventEntity, EventEntity], work=2150*
  1: 0x012E [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012F   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                               5B                 [
0130: 09 80 F8 FF FF 7F F8 FF  FF 7F 77 65 74 63 1C 01  ..........wetc..
0140: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x012F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wetc" with entities [EventEntity, EventEntity], work=218*
  1: 0x013E [0x1C] WAIT(180* ticks)
  2: 0x0141 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0142   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:       5B 0A 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B    [..........tlk
0150: 65 00                                             e.              
```

#### Opcodes

```
  0: 0x0142 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlke" with entities [EventEntity, EventEntity], work=215*
  1: 0x0151 [0x00] END_REQSTACK()
```
