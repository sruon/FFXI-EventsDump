# 17248869 - Shantotto

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 584 bytes                   |
| Total Events     | 22                          |
| References Count | 19                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     39 |              6 |
| [65535.2](#event-655352)   | 0x0028       |     10 |              2 |
| [65535.3](#event-655353)   | 0x0032       |     10 |              2 |
| [65535.4](#event-655354)   | 0x003C       |      3 |              2 |
| [65535.5](#event-655355)   | 0x003F       |     52 |              8 |
| [62](#event-62)            | 0x0073       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0074       |     19 |              3 |
| [65535.7](#event-655357)   | 0x0087       |     19 |              3 |
| [65535.8](#event-655358)   | 0x009A       |     19 |              3 |
| [65535.9](#event-655359)   | 0x00AD       |     19 |              3 |
| [65535.10](#event-6553510) | 0x00C0       |     19 |              3 |
| [65535.11](#event-6553511) | 0x00D3       |     19 |              3 |
| [65535.12](#event-6553512) | 0x00E6       |     19 |              3 |
| [65535.13](#event-6553513) | 0x00F9       |     19 |              3 |
| [65535.14](#event-6553514) | 0x010C       |     13 |              3 |
| [65535.15](#event-6553515) | 0x0119       |     10 |              2 |
| [65535.16](#event-6553516) | 0x0123       |     13 |              3 |
| [65535.17](#event-6553517) | 0x0130       |     29 |              3 |
| [65535.18](#event-6553518) | 0x014D       |     16 |              2 |
| [63](#event-63)            | 0x015D       |      1 |              1 |
| [65535.19](#event-6553519) | 0x015E       |     52 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0006      |           6 |
|       1 | 0x0000      |           0 |
|       2 | 0x00C9      |         201 |
|       3 | 0x0028      |          40 |
|       4 | 0x0080      |         128 |
|       5 | 0x0012      |          18 |
|       6 | 0xFFFFFB64  |  4294966116 |
|       7 | 0x0121      |         289 |
|       8 | 0x0AC8      |        2760 |
|       9 | 0x000F      |          15 |
|      10 | 0x0030      |          48 |
|      11 | 0x002C      |          44 |
|      12 | 0x0040      |          64 |
|      13 | 0x0043      |          67 |
|      14 | 0x0044      |          68 |
|      15 | 0x003C      |          60 |
|      16 | 0x0078      |         120 |
|      17 | 0x055D      |        1373 |
|      18 | 0xFFFFFEDF  |  4294967007 |

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
| Data Size    | 39 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    B6 0B 00 80 00 80 01  80 02 80 02 80 02 80 02   ...............
0010: 80 01 80 01 80 22 00 92  01 F8 FF FF 7F 94 01 F8  ....."..........
0020: FF FF 7F B6 0F 03 80 00                           ........        
```

#### Opcodes

```
  0: 0x0001 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=6*, head=0*, body=201*, hands=201*, legs=201*, feet=201*, main=0*, sub=0*)
  1: 0x0015 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x0017 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x001D [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0023 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=40*)
  5: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          6C F8 FF FF 7F 04 80 01          l.......
0030: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0028 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
  1: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       6C F8 FF FF 7F 01  80 01 80 00                l.........    
```

#### Opcodes

```
  0: 0x0032 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      A4 01 00                 ... 
```

#### Opcodes

```
  0: 0x003C [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 52 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               3B                 ;
0040: 64 32 07 01 00 00 01 00  02 00 3A 64 32 07 01 03  d2........:d2...
0050: 00 07 00 00 05 80 07 02  00 06 80 07 01 00 07 80  ................
0060: BA F8 FF FF 7F 00 00 01  00 02 00 03 00 80 F8 FF  ................
0070: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x003F [0x3B] GET_ENTITY_POSITION(entity=Moogle (ID: 17248868/0x01073264), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x004A [0x3A] CONVERT_YAW_TO_BYTE(entity=Moogle (ID: 17248868/0x01073264), result_destination=ExtData[1]->WorkLocal[3])
  2: 0x0051 [0x07] ExtData[1]->WorkLocal[0] += 18*
  3: 0x0056 [0x07] ExtData[1]->WorkLocal[2] += 4294966116*
  4: 0x005B [0x07] ExtData[1]->WorkLocal[1] += 289*
  5: 0x0060 [0xBA] SET_ENTITY_POSITION(entity_id=EventEntity, pos_x=ExtData[1]->WorkLocal[0], pos_z=ExtData[1]->WorkLocal[1], pos_y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3])
  6: 0x006D [0x80] LOAD_WAIT(entity=EventEntity)
  7: 0x0072 [0x00] END_REQSTACK()
```

### Event 62

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0073  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          00                                          .            
```

#### Opcodes

```
  0: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             5B 08 80 F8  FF FF 7F F8 FF FF 7F 64      [..........d
0080: 6F 6C 30 1C 09 80 00                              ol0....         
```

#### Opcodes

```
  0: 0x0074 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dol0" with entities [EventEntity, EventEntity], work=2760*
  1: 0x0083 [0x1C] WAIT(15* ticks)
  2: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      5B  08 80 F8 FF FF 7F F8 FF         [........
0090: FF 7F 74 6C 6B 30 1C 0A  80 00                    ..tlk0....      
```

#### Opcodes

```
  0: 0x0087 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=2760*
  1: 0x0096 [0x1C] WAIT(48* ticks)
  2: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                5B 08 80 F8 FF FF            [.....
00A0: 7F F8 FF FF 7F 74 6C 6B  31 1C 0B 80 00           .....tlk1....   
```

#### Opcodes

```
  0: 0x009A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=2760*
  1: 0x00A9 [0x1C] WAIT(44* ticks)
  2: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         5B 08 80               [..
00B0: F8 FF FF 7F F8 FF FF 7F  73 6A 69 30 1C 0C 80 00  ........sji0....
```

#### Opcodes

```
  0: 0x00AD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sji0" with entities [EventEntity, EventEntity], work=2760*
  1: 0x00BC [0x1C] WAIT(64* ticks)
  2: 0x00BF [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C0   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 5B 08 80 F8 FF FF 7F F8  FF FF 7F 73 6A 69 31 1C  [..........sji1.
00D0: 0D 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00C0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sji1" with entities [EventEntity, EventEntity], work=2760*
  1: 0x00CF [0x1C] WAIT(67* ticks)
  2: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          5B 08 80 F8 FF  FF 7F F8 FF FF 7F 73 6F     [..........so
00E0: 68 30 1C 0E 80 00                                 h0....          
```

#### Opcodes

```
  0: 0x00D3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "soh0" with entities [EventEntity, EventEntity], work=2760*
  1: 0x00E2 [0x1C] WAIT(68* ticks)
  2: 0x00E5 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E6   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   5B 08  80 F8 FF FF 7F F8 FF FF        [.........
00F0: 7F 6F 68 68 30 1C 0E 80  00                       .ohh0....       
```

#### Opcodes

```
  0: 0x00E6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ohh0" with entities [EventEntity, EventEntity], work=2760*
  1: 0x00F5 [0x1C] WAIT(68* ticks)
  2: 0x00F8 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F9   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                             5B 08 80 F8 FF FF 7F           [......
0100: F8 FF FF 7F 6F 68 68 31  1C 0E 80 00              ....ohh1....    
```

#### Opcodes

```
  0: 0x00F9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ohh1" with entities [EventEntity, EventEntity], work=2760*
  1: 0x0108 [0x1C] WAIT(68* ticks)
  2: 0x010B [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010C   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                      6C F8 FF FF              l...
0110: 7F 0F 80 10 80 1C 10 80  00                       .........       
```

#### Opcodes

```
  0: 0x010C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=60*, fade_time=120*)
  1: 0x0115 [0x1C] WAIT(120* ticks)
  2: 0x0118 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0119   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                             6C F8 FF FF 7F 0F 80           l......
0120: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0119 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=60*, fade_time=0*)
  1: 0x0122 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0123   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:          6C F8 FF FF 7F  01 80 10 80 1C 10 80 00     l............
```

#### Opcodes

```
  0: 0x0123 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=120*)
  1: 0x012C [0x1C] WAIT(120* ticks)
  2: 0x012F [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0130   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130: 5B 11 80 F8 FF FF 7F F8  FF FF 7F 67 75 64 30 53  [..........gud0S
0140: F8 FF FF 7F F8 FF FF 7F  67 75 64 30 00           ........gud0.   
```

#### Opcodes

```
  0: 0x0130 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gud0" with entities [EventEntity, EventEntity], work=1373*
  1: 0x013F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gud0" with entities [EventEntity, EventEntity]
  2: 0x014C [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                         5B 11 80               [..
0150: F8 FF FF 7F F8 FF FF 7F  67 75 64 31 00           ........gud1.   
```

#### Opcodes

```
  0: 0x014D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gud1" with entities [EventEntity, EventEntity], work=1373*
  1: 0x015C [0x00] END_REQSTACK()
```

### Event 63

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x015D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                         00                     .  
```

#### Opcodes

```
  0: 0x015D [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015E   |
| Data Size    | 52 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                            3B 64                ;d
0160: 32 07 01 04 00 05 00 06  00 3A 64 32 07 01 07 00  2........:d2....
0170: 07 04 00 12 80 07 06 00  06 80 07 05 00 05 80 BA  ................
0180: F8 FF FF 7F 04 00 05 00  06 00 07 00 80 F8 FF FF  ................
0190: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x015E [0x3B] GET_ENTITY_POSITION(entity=Moogle (ID: 17248868/0x01073264), x_destination=ExtData[1]->WorkLocal[4], y_destination=ExtData[1]->WorkLocal[5], z_destination=ExtData[1]->WorkLocal[6])
  1: 0x0169 [0x3A] CONVERT_YAW_TO_BYTE(entity=Moogle (ID: 17248868/0x01073264), result_destination=ExtData[1]->WorkLocal[7])
  2: 0x0170 [0x07] ExtData[1]->WorkLocal[4] += 4294967007*
  3: 0x0175 [0x07] ExtData[1]->WorkLocal[6] += 4294966116*
  4: 0x017A [0x07] ExtData[1]->WorkLocal[5] += 18*
  5: 0x017F [0xBA] SET_ENTITY_POSITION(entity_id=EventEntity, pos_x=ExtData[1]->WorkLocal[4], pos_z=ExtData[1]->WorkLocal[5], pos_y=ExtData[1]->WorkLocal[6], direction=ExtData[1]->WorkLocal[7])
  6: 0x018C [0x80] LOAD_WAIT(entity=EventEntity)
  7: 0x0191 [0x00] END_REQSTACK()
```
