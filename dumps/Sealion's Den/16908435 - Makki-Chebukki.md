# 16908435 - Makki-Chebukki

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Sealion's Den (ID: 32) |
| Block Size       | 848 bytes              |
| Total Events     | 30                     |
| References Count | 41                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |     13 |              3 |
| [31](#event-31)            | 0x000D       |      7 |              2 |
| [32](#event-32)            | 0x0014       |      7 |              2 |
| [65535.1](#event-655351)   | 0x001B       |     10 |              2 |
| [65535.2](#event-655352)   | 0x0025       |     10 |              2 |
| [65535.3](#event-655353)   | 0x002F       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0039       |     14 |              4 |
| [1](#event-1)              | 0x0047       |     10 |              2 |
| [33](#event-33)            | 0x0051       |      7 |              2 |
| [34](#event-34)            | 0x0058       |      7 |              2 |
| [65535.5](#event-655355)   | 0x005F       |     10 |              2 |
| [65535.6](#event-655356)   | 0x0069       |     90 |             18 |
| [65535.7](#event-655357)   | 0x00C3       |     25 |              3 |
| [65535.8](#event-655358)   | 0x00DC       |     20 |              4 |
| [65535.9](#event-655359)   | 0x00F0       |     16 |              5 |
| [65535.10](#event-6553510) | 0x0100       |     16 |              2 |
| [65535.11](#event-6553511) | 0x0110       |     16 |              2 |
| [65535.12](#event-6553512) | 0x0120       |     16 |              2 |
| [65535.13](#event-6553513) | 0x0130       |     16 |              2 |
| [65535.14](#event-6553514) | 0x0140       |     16 |              2 |
| [65535.15](#event-6553515) | 0x0150       |     16 |              2 |
| [65535.16](#event-6553516) | 0x0160       |     29 |              3 |
| [65535.17](#event-6553517) | 0x017D       |     16 |              2 |
| [65535.18](#event-6553518) | 0x018D       |     16 |              2 |
| [65535.19](#event-6553519) | 0x019D       |     53 |              5 |
| [65535.20](#event-6553520) | 0x01D2       |     16 |              2 |
| [65535.21](#event-6553521) | 0x01E2       |     16 |              2 |
| [65535.22](#event-6553522) | 0x01F2       |     16 |              2 |
| [65535.23](#event-6553523) | 0x0202       |     16 |              2 |
| [65535.24](#event-6553524) | 0x0212       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF640F7  |  4294328567 |
|       1 | 0xFFF62A8E  |  4294322830 |
|       2 | 0x30397     |      197527 |
|       3 | 0x0BD7      |        3031 |
|       4 | 0xFFF63BCF  |  4294327247 |
|       5 | 0x7BCE3     |      507107 |
|       6 | 0xFFFC6BCE  |  4294732750 |
|       7 | 0x0C1C      |        3100 |
|       8 | 0xFFF63BFD  |  4294327293 |
|       9 | 0x7C1E7     |      508391 |
|      10 | 0x0954      |        2388 |
|      11 | 0x0009      |           9 |
|      12 | 0xFFF64372  |  4294329202 |
|      13 | 0x8142E     |      529454 |
|      14 | 0xFFFC784D  |  4294735949 |
|      15 | 0x00AE      |         174 |
|      16 | 0xFFF61BC4  |  4294319044 |
|      17 | 0x7F2CD     |      520909 |
|      18 | 0xFFFC7914  |  4294736148 |
|      19 | 0x0D22      |        3362 |
|      20 | 0x07D0      |        2000 |
|      21 | 0x0028      |          40 |
|      22 | 0xFFF613E0  |  4294317024 |
|      23 | 0x7E130     |      516400 |
|      24 | 0x051D      |        1309 |
|      25 | 0x0150      |         336 |
|      26 | 0xFFF4085F  |  4294183007 |
|      27 | 0xFFFEDDBE  |  4294892990 |
|      28 | 0xFFFE6D14  |  4294864148 |
|      29 | 0x0DB4      |        3508 |
|      30 | 0xFFF41406  |  4294185990 |
|      31 | 0xFFFEA38D  |  4294878093 |
|      32 | 0xFFFE6C4D  |  4294863949 |
|      33 | 0x01AF      |         431 |
|      34 | 0x01B9      |         441 |
|      35 | 0x0152      |         338 |
|      36 | 0x01BC      |         444 |
|      37 | 0x00A6      |         166 |
|      38 | 0x0000      |           0 |
|      39 | 0x002D      |          45 |
|      40 | 0x0156      |         342 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 94 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 31

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         94 01 F8               ...
0010: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x000D [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0013 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0014  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             94 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x0014 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   37 00 80 01 80             7....
0020: 02 80 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x001B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-638.729*, z=-644.466*, y=197.527*, direction=266.4°*
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                37 04 80  05 80 06 80 07 80 00          7......... 
```

#### Opcodes

```
  0: 0x0025 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-640.049*, z=507.107*, y=-234.546*, direction=272.5°*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               37                 7
0030: 08 80 09 80 06 80 0A 80  00                       .........       
```

#### Opcodes

```
  0: 0x002F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-640.003*, z=508.391*, y=-234.546*, direction=209.9°*
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 0B 80 1F 00 08 80           2......
0040: 09 80 06 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 9* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=-640.003*, Z=508.391*, Y=-234.546*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      37  0C 80 0D 80 0E 80 0F 80         7........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-638.094*, z=529.454*, y=-231.347*, direction=15.3°*
  1: 0x0050 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    94 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0051 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0057 [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0058  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          94 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0058 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               37                 7
0060: 10 80 11 80 12 80 13 80  00                       .........       
```

#### Opcodes

```
  0: 0x005F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-648.252*, z=520.909*, y=-231.148*, direction=295.5°*
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 90 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             03 00 00 14 80 1A 7F           .......
0070: 00 32 15 80 1F 00 01 00  02 00 03 00 1F 01 00 3B  .2.............;
0080: F8 FF FF 7F 01 00 02 00  03 00 3A F8 FF FF 7F 04  ..........:.....
0090: 00 17 05 00 04 00 00 00  16 06 00 04 00 00 00 07  ................
00A0: 01 00 05 00 07 02 00 06  00 1B 17 05 00 04 00 00  ................
00B0: 00 16 06 00 04 00 00 00  07 01 00 05 00 07 02 00  ................
00C0: 06 00 1B                                          ...             
```

#### Opcodes

```
  0: 0x0069 [0x03] ExtData[1]->WorkLocal[0] = 2000*
  1: 0x006E [0x1A] CALL_SUBROUTINE(address=0x007F)
  2: 0x0071 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x0074 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  4: 0x007C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x007E [0x00] END_REQSTACK()

SUBROUTINE_007F:
  6: 0x007F [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  7: 0x008A [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
  8: 0x0091 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
  9: 0x0098 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 10: 0x009F [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
 11: 0x00A4 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 12: 0x00A9 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00AA [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x00B1 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x00B8 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x00BD [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x00C2 [0x1B] RETURN
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          37 16 80 17 80  12 80 18 80 5B 19 80 F8     7........[...
00D0: FF FF 7F F8 FF FF 7F 6F  62 69 30 00              .......obi0.    
```

#### Opcodes

```
  0: 0x00C3 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-650.272*, z=516.400*, y=-231.148*, direction=115.0°*
  1: 0x00CC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "obi0" with entities [EventEntity, EventEntity], work=336*
  2: 0x00DB [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DC   |
| Data Size    | 20 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      37 1A 80 1B              7...
00E0: 80 1C 80 1D 80 5E 69 64  6C 30 1E 8D 00 02 01 00  .....^idl0......
```

#### Opcodes

```
  0: 0x00DC [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-784.289*, z=-74.306*, y=-103.148*, direction=308.3°*
  1: 0x00E5 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x00EA [0x1E] EventEntity looks at Prishe (ID: 16908429/0x0102008D) and starts talking
  3: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F0   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: 32 15 80 1F 00 1E 80 1F  80 20 80 1F 01 22 01 00  2........ ..."..
```

#### Opcodes

```
  0: 0x00F0 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00F3 [0x1F] MOVE_ENTITY: EventEntity moves to X=-781.306*, Z=-89.203*, Y=-103.347*
  2: 0x00FB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00FD [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x00FF [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0100   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100: 5B 21 80 F8 FF FF 7F F8  FF FF 7F 66 75 6B 31 00  [!.........fuk1.
```

#### Opcodes

```
  0: 0x0100 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fuk1" with entities [EventEntity, EventEntity], work=431*
  1: 0x010F [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0110   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110: 5B 19 80 F8 FF FF 7F F8  FF FF 7F 7A 69 74 30 00  [..........zit0.
```

#### Opcodes

```
  0: 0x0110 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "zit0" with entities [EventEntity, EventEntity], work=336*
  1: 0x011F [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 5B 22 80 F8 FF FF 7F F8  FF FF 7F 64 66 6D 30 00  [".........dfm0.
```

#### Opcodes

```
  0: 0x0120 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dfm0" with entities [EventEntity, EventEntity], work=441*
  1: 0x012F [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0130   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130: 5B 22 80 F8 FF FF 7F F8  FF FF 7F 64 66 6D 31 00  [".........dfm1.
```

#### Opcodes

```
  0: 0x0130 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dfm1" with entities [EventEntity, EventEntity], work=441*
  1: 0x013F [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0140   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140: 5B 19 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 00  [..........tlk0.
```

#### Opcodes

```
  0: 0x0140 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=336*
  1: 0x014F [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0150   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150: 5B 19 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 00  [..........tlk1.
```

#### Opcodes

```
  0: 0x0150 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=336*
  1: 0x015F [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0160   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160: 5B 23 80 F8 FF FF 7F F8  FF FF 7F 67 68 6E 31 53  [#.........ghn1S
0170: F8 FF FF 7F F8 FF FF 7F  67 68 6E 31 00           ........ghn1.   
```

#### Opcodes

```
  0: 0x0160 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ghn1" with entities [EventEntity, EventEntity], work=338*
  1: 0x016F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ghn1" with entities [EventEntity, EventEntity]
  2: 0x017C [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                         5B 24 80               [$.
0180: F8 FF FF 7F F8 FF FF 7F  68 69 30 33 00           ........hi03.   
```

#### Opcodes

```
  0: 0x017D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hi03" with entities [EventEntity, EventEntity], work=444*
  1: 0x018C [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                         5B 24 80               [$.
0190: F8 FF FF 7F F8 FF FF 7F  68 69 30 34 00           ........hi04.   
```

#### Opcodes

```
  0: 0x018D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hi04" with entities [EventEntity, EventEntity], work=444*
  1: 0x019C [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019D   |
| Data Size    | 53 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                         5B 19 80               [..
01A0: F8 FF FF 7F F8 FF FF 7F  77 61 69 30 45 25 80 95  ........wai0E%..
01B0: 00 02 01 95 00 02 01 73  65 31 32 26 80 1C 27 80  .......se12&..'.
01C0: 45 25 80 95 00 02 01 95  00 02 01 73 65 31 33 26  E%.........se13&
01D0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x019D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wai0" with entities [EventEntity, EventEntity], work=336*
  1: 0x01AC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se12" with entities [Shikaree Z (ID: 16908437/0x01020095), Shikaree Z (ID: 16908437/0x01020095)], work=[166*, 0*]
  2: 0x01BD [0x1C] WAIT(45* ticks)
  3: 0x01C0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se13" with entities [Shikaree Z (ID: 16908437/0x01020095), Shikaree Z (ID: 16908437/0x01020095)], work=[166*, 0*]
  4: 0x01D1 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D2   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:       5B 23 80 F8 FF FF  7F F8 FF FF 7F 73 68 6B    [#.........shk
01E0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x01D2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "shk0" with entities [EventEntity, EventEntity], work=338*
  1: 0x01E1 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E2   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:       5B 19 80 F8 FF FF  7F F8 FF FF 7F 7A 69 74    [..........zit
01F0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x01E2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "zit0" with entities [EventEntity, EventEntity], work=336*
  1: 0x01F1 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F2   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:       5B 28 80 F8 FF FF  7F F8 FF FF 7F 63 61 62    [(.........cab
0200: 6B 00                                             k.              
```

#### Opcodes

```
  0: 0x01F2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "cabk" with entities [EventEntity, EventEntity], work=342*
  1: 0x0201 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0202   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:       5B 28 80 F8 FF FF  7F F8 FF FF 7F 73 68 62    [(.........shb
0210: 6B 00                                             k.              
```

#### Opcodes

```
  0: 0x0202 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "shbk" with entities [EventEntity, EventEntity], work=342*
  1: 0x0211 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0212   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:       5B 23 80 F8 FF FF  7F F8 FF FF 7F 65 68 6E    [#.........ehn
0220: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0212 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ehn0" with entities [EventEntity, EventEntity], work=338*
  1: 0x0221 [0x00] END_REQSTACK()
```
