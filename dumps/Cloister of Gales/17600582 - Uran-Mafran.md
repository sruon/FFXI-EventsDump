# 17600582 - Uran-Mafran

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Cloister of Gales (ID: 201) |
| Block Size       | 768 bytes                   |
| Total Events     | 29                          |
| References Count | 30                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     32 |              4 |
| [65535.3](#event-655353)   | 0x0031       |     50 |              5 |
| [65535.4](#event-655354)   | 0x0063       |     35 |              4 |
| [65535.5](#event-655355)   | 0x0086       |     34 |              4 |
| [65535.6](#event-655356)   | 0x00A8       |     44 |              4 |
| [65535.7](#event-655357)   | 0x00D4       |     28 |              4 |
| [65535.8](#event-655358)   | 0x00F0       |     14 |              2 |
| [65535.9](#event-655359)   | 0x00FE       |     22 |              3 |
| [65535.10](#event-6553510) | 0x0114       |     20 |              3 |
| [65535.11](#event-6553511) | 0x0128       |     16 |              2 |
| [65535.12](#event-6553512) | 0x0138       |     14 |              2 |
| [65535.13](#event-6553513) | 0x0146       |     16 |              2 |
| [65535.14](#event-6553514) | 0x0156       |     29 |              3 |
| [65535.15](#event-6553515) | 0x0173       |     16 |              2 |
| [32000](#event-32000)      | 0x0183       |      1 |              1 |
| [32001](#event-32001)      | 0x0184       |      1 |              1 |
| [65535.16](#event-6553516) | 0x0185       |      1 |              1 |
| [65535.17](#event-6553517) | 0x0186       |     10 |              2 |
| [65535.18](#event-6553518) | 0x0190       |     15 |              5 |
| [65535.19](#event-6553519) | 0x019F       |     30 |              8 |
| [65535.20](#event-6553520) | 0x01BD       |      1 |              1 |
| [65535.21](#event-6553521) | 0x01BE       |     10 |              2 |
| [65535.22](#event-6553522) | 0x01C8       |     10 |              2 |
| [65535.23](#event-6553523) | 0x01D2       |     10 |              2 |
| [65535.24](#event-6553524) | 0x01DC       |     10 |              2 |
| [65535.25](#event-6553525) | 0x01E6       |     15 |              5 |
| [65535.26](#event-6553526) | 0x01F5       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x000F      |          15 |
|       2 | 0x003C      |          60 |
|       3 | 0x002A      |          42 |
|       4 | 0x002E      |          46 |
|       5 | 0x001E      |          30 |
|       6 | 0x5896      |       22678 |
|       7 | 0x6406      |       25606 |
|       8 | 0xFFFFB748  |  4294948680 |
|       9 | 0x0B3E      |        2878 |
|      10 | 0x000D      |          13 |
|      11 | 0x58AE      |       22702 |
|      12 | 0x6C92      |       27794 |
|      13 | 0xFFFFB867  |  4294948967 |
|      14 | 0x4C13      |       19475 |
|      15 | 0x6945      |       26949 |
|      16 | 0xFFFFB7D0  |  4294948816 |
|      17 | 0x5952      |       22866 |
|      18 | 0x7ACE      |       31438 |
|      19 | 0xFFFFB8EA  |  4294949098 |
|      20 | 0x0640      |        1600 |
|      21 | 0x592D      |       22829 |
|      22 | 0x7269      |       29289 |
|      23 | 0xFFFFB8CD  |  4294949069 |
|      24 | 0x0396      |         918 |
|      25 | 0x0548      |        1352 |
|      26 | 0x04B0      |        1200 |
|      27 | 0x5360      |       21344 |
|      28 | 0x7CC5      |       31941 |
|      29 | 0xFFFFB8ED  |  4294949101 |

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
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 32 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 66 01   S........tlk0f.
0020: 80 F8 FF FF 7F F8 FF FF  7F 73 74 64 30 1C 02 80  .........std0...
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=15*
  2: 0x002D [0x1C] WAIT(60* ticks)
  3: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 50 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    81 00 F8 FF FF 7F 66  03 80 46 90 0C 01 46 90   ......f..F...F.
0040: 0C 01 77 6F 6E 32 66 04  80 F8 FF FF 7F F8 FF FF  ..won2f.........
0050: 7F 6D 67 63 30 53 F8 FF  FF 7F F8 FF FF 7F 6D 67  .mgc0S........mg
0060: 63 30 00                                          c0.             
```

#### Opcodes

```
  0: 0x0031 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "won2" with entities [Uran-Mafran (ID: 17600582/0x010C9046), Uran-Mafran (ID: 17600582/0x010C9046)], work=42*
  2: 0x0046 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "mgc0" with entities [EventEntity, EventEntity], work=46*
  3: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mgc0" with entities [EventEntity, EventEntity]
  4: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 35 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          66 04 80 F8 FF  FF 7F F8 FF FF 7F 6D 64     f..........md
0070: 71 32 53 F8 FF FF 7F F8  FF FF 7F 6D 64 71 32 81  q2S........mdq2.
0080: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "mdq2" with entities [EventEntity, EventEntity], work=46*
  1: 0x0072 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mdq2" with entities [EventEntity, EventEntity]
  2: 0x007F [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  3: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   66 03  80 46 90 0C 01 46 90 0C        f..F...F..
0090: 01 77 6F 66 32 66 01 80  F8 FF FF 7F F8 FF FF 7F  .wof2f..........
00A0: 73 74 64 30 1C 05 80 00                           std0....        
```

#### Opcodes

```
  0: 0x0086 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wof2" with entities [Uran-Mafran (ID: 17600582/0x010C9046), Uran-Mafran (ID: 17600582/0x010C9046)], work=42*
  1: 0x0095 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=15*
  2: 0x00A4 [0x1C] WAIT(30* ticks)
  3: 0x00A7 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A8   |
| Data Size    | 44 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                          66 03 80 46 90 0C 01 46          f..F...F
00B0: 90 0C 01 77 6F 66 32 66  01 80 F8 FF FF 7F F8 FF  ...wof2f........
00C0: FF 7F 73 74 64 30 53 F8  FF FF 7F F8 FF FF 7F 73  ..std0S........s
00D0: 74 64 30 00                                       td0.            
```

#### Opcodes

```
  0: 0x00A8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wof2" with entities [Uran-Mafran (ID: 17600582/0x010C9046), Uran-Mafran (ID: 17600582/0x010C9046)], work=42*
  1: 0x00B7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=15*
  2: 0x00C6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "std0" with entities [EventEntity, EventEntity]
  3: 0x00D3 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D4   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             81 00 F8 FF  FF 7F 7C 00 F8 FF FF 7F      ......|.....
00E0: 66 01 80 F8 FF FF 7F F8  FF FF 7F 77 72 75 30 00  f..........wru0.
```

#### Opcodes

```
  0: 0x00D4 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x00DA [0x7C] EventEntity->Render.Flags2 |= 0x00
  2: 0x00E0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wru0" with entities [EventEntity, EventEntity], work=15*
  3: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F0   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: 53 F8 FF FF 7F F8 FF FF  7F 77 72 75 30 00        S........wru0.  
```

#### Opcodes

```
  0: 0x00F0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wru0" with entities [EventEntity, EventEntity]
  1: 0x00FD [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FE   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                            7C 01                |.
0100: F8 FF FF 7F 66 01 80 F8  FF FF 7F F8 FF FF 7F 77  ....f..........w
0110: 72 75 31 00                                       ru1.            
```

#### Opcodes

```
  0: 0x00FE [0x7C] EventEntity->Render.Flags2 |= 0x01
  1: 0x0104 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wru1" with entities [EventEntity, EventEntity], work=15*
  2: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             53 F8 FF FF  7F F8 FF FF 7F 77 72 75      S........wru
0120: 31 81 01 F8 FF FF 7F 00                           1.......        
```

#### Opcodes

```
  0: 0x0114 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wru1" with entities [EventEntity, EventEntity]
  1: 0x0121 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x0127 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0128   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                          66 01 80 F8 FF FF 7F F8          f.......
0130: FF FF 7F 69 6B 75 30 00                           ...iku0.        
```

#### Opcodes

```
  0: 0x0128 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iku0" with entities [EventEntity, EventEntity], work=15*
  1: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0138   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          53 F8 FF FF 7F F8 FF FF          S.......
0140: 7F 69 6B 75 30 00                                 .iku0.          
```

#### Opcodes

```
  0: 0x0138 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iku0" with entities [EventEntity, EventEntity]
  1: 0x0145 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0146   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                   66 01  80 F8 FF FF 7F F8 FF FF        f.........
0150: 7F 69 6B 75 31 00                                 .iku1.          
```

#### Opcodes

```
  0: 0x0146 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iku1" with entities [EventEntity, EventEntity], work=15*
  1: 0x0155 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0156   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   53 F8  FF FF 7F F8 FF FF 7F 69        S........i
0160: 6B 75 31 66 01 80 F8 FF  FF 7F F8 FF FF 7F 73 74  ku1f..........st
0170: 64 30 00                                          d0.             
```

#### Opcodes

```
  0: 0x0156 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iku1" with entities [EventEntity, EventEntity]
  1: 0x0163 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=15*
  2: 0x0172 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0173   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:          66 04 80 F8 FF  FF 7F F8 FF FF 7F 00 FE     f............
0180: FE FE 00                                          ...             
```

#### Opcodes

```
  0: 0x0173 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=46*
  1: 0x0182 [0x00] END_REQSTACK()
```

### Event 32000

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

### Event 65535.16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0185  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                00                                      .          
```

#### Opcodes

```
  0: 0x0185 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0186   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                   37 06  80 07 80 08 80 09 80 00        7.........
```

#### Opcodes

```
  0: 0x0186 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.678*, z=25.606*, y=-18.616*, direction=252.9°*
  1: 0x018F [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0190   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190: 32 0A 80 1F 00 0B 80 0C  80 0D 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0190 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0193 [0x1F] MOVE_ENTITY: EventEntity moves to X=22.702*, Z=27.794*, Y=-18.329*
  2: 0x019B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x019D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x019E [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019F   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                               32                 2
01A0: 0A 80 1F 00 0E 80 0F 80  10 80 1F 01 6F 4A 46 90  ............oJF.
01B0: 0C 01 F0 FF FF 7F 6F 76  46 90 0C 01 00           ......ovF....   
```

#### Opcodes

```
  0: 0x019F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01A2 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.475*, Z=26.949*, Y=-18.480*
  2: 0x01AA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01AC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01AD [0x4A] Uran-Mafran (ID: 17600582/0x010C9046) looks at LocalPlayer
  5: 0x01B6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x01B7 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Uran-Mafran (ID: 17600582/0x010C9046) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x01BC [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01BD  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                         00                     .  
```

#### Opcodes

```
  0: 0x01BD [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BE   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                            37 11                7.
01C0: 80 12 80 13 80 14 80 00                           ........        
```

#### Opcodes

```
  0: 0x01BE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.866*, z=31.438*, y=-18.198*, direction=140.6°*
  1: 0x01C7 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C8   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                          37 15 80 16 80 17 80 18          7.......
01D0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x01C8 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.829*, z=29.289*, y=-18.227*, direction=80.7°*
  1: 0x01D1 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D2   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:       37 11 80 12 80 13  80 19 80 00                7.........    
```

#### Opcodes

```
  0: 0x01D2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.866*, z=31.438*, y=-18.198*, direction=118.8°*
  1: 0x01DB [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01DC   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                      37 11 80 12              7...
01E0: 80 13 80 1A 80 00                                 ......          
```

#### Opcodes

```
  0: 0x01DC [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.866*, z=31.438*, y=-18.198*, direction=105.5°*
  1: 0x01E5 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E6   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                   32 0A  80 1F 00 15 80 16 80 17        2.........
01F0: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x01E6 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01E9 [0x1F] MOVE_ENTITY: EventEntity moves to X=22.829*, Z=29.289*, Y=-18.227*
  2: 0x01F1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01F3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01F4 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F5   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                32 0A 80  1F 00 1B 80 1C 80 1D 80       2..........
0200: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x01F5 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01F8 [0x1F] MOVE_ENTITY: EventEntity moves to X=21.344*, Z=31.941*, Y=-18.195*
  2: 0x0200 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0202 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0203 [0x00] END_REQSTACK()
```
