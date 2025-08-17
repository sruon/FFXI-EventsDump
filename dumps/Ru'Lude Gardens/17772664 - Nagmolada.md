# 17772664 - Nagmolada

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 656 bytes                 |
| Total Events     | 19                        |
| References Count | 13                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |     15 |              4 |
| [58](#event-58)            | 0x000F       |     10 |              2 |
| [65535.1](#event-655351)   | 0x0019       |     65 |             14 |
| [65535.2](#event-655352)   | 0x005A       |     29 |              9 |
| [65535.3](#event-655353)   | 0x0077       |     90 |             18 |
| [65535.4](#event-655354)   | 0x00D1       |     16 |              2 |
| [65535.5](#event-655355)   | 0x00E1       |     29 |              3 |
| [65535.6](#event-655356)   | 0x00FE       |     16 |              2 |
| [65535.7](#event-655357)   | 0x010E       |     16 |              2 |
| [65535.8](#event-655358)   | 0x011E       |     29 |              3 |
| [65535.9](#event-655359)   | 0x013B       |     16 |              2 |
| [65535.10](#event-6553510) | 0x014B       |     16 |              2 |
| [65535.11](#event-6553511) | 0x015B       |     29 |              3 |
| [65535.12](#event-6553512) | 0x0178       |     16 |              2 |
| [65535.13](#event-6553513) | 0x0188       |     29 |              3 |
| [65535.14](#event-6553514) | 0x01A5       |     16 |              2 |
| [65535.15](#event-6553515) | 0x01B5       |     29 |              3 |
| [65535.16](#event-6553516) | 0x01D2       |     16 |              2 |
| [65535.17](#event-6553517) | 0x01E2       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x1129C     |       70300 |
|       2 | 0xFFFFEC78  |  4294962296 |
|       3 | 0x0C00      |        3072 |
|       4 | 0x1770      |        6000 |
|       5 | 0x000D      |          13 |
|       6 | 0x00D2      |         210 |
|       7 | 0x13880     |       80000 |
|       8 | 0x0AF0      |        2800 |
|       9 | 0x07D0      |        2000 |
|      10 | 0x03E8      |        1000 |
|      11 | 0x01D1      |         465 |
|      12 | 0x0283      |         643 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 94 01 F8 FF FF 7F 33 01  92 01 F8 FF FF 7F 00     ......3........ 
```

#### Opcodes

```
  0: 0x0000 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000E [0x00] END_REQSTACK()
```

### Event 58

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               37                 7
0010: 00 80 01 80 02 80 03 80  00                       .........       
```

#### Opcodes

```
  0: 0x000F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=70.300*, y=-5.000*, direction=270.0°*
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 65 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             03 00 00 04 80 1A 8D           .......
0020: 00 32 05 80 31 00 01 00  02 00 03 00 06 80 31 01  .2..1.........1.
0030: 37 00 80 07 80 02 80 03  80 79 00 F8 FF FF 7F F0  7........y......
0040: FF FF 7F 03 00 00 08 80  1A 8D 00 32 05 80 1F 00  ...........2....
0050: 01 00 02 00 03 00 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0019 [0x03] ExtData[1]->WorkLocal[0] = 6000*
  1: 0x001E [0x1A] CALL_SUBROUTINE(address=0x008D)
  2: 0x0021 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0024 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3], Time=210*
  4: 0x002E [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  5: 0x0030 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=80.000*, y=-5.000*, direction=270.0°*
  6: 0x0039 [0x79] EventEntity looks at LocalPlayer (Basic look)
  7: 0x0043 [0x03] ExtData[1]->WorkLocal[0] = 2800*
  8: 0x0048 [0x1A] CALL_SUBROUTINE(address=0x008D)
  9: 0x004B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
 10: 0x004E [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
 11: 0x0056 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 12: 0x0058 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 13: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 29 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                1E 76 30 0F 01 6F            .v0..o
0060: 70 03 00 00 09 80 1A 8D  00 32 05 80 1F 00 01 00  p........2......
0070: 02 00 03 00 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x005A [0x1E] EventEntity looks at Esha'ntarl (ID: 17772662/0x010F3076) and starts talking
  1: 0x005F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0060 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0061 [0x03] ExtData[1]->WorkLocal[0] = 2000*
  4: 0x0066 [0x1A] CALL_SUBROUTINE(address=0x008D)
  5: 0x0069 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  6: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  7: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 90 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      03  00 00 0A 80 1A 8D 00 32         ........2
0080: 05 80 1F 00 01 00 02 00  03 00 1F 01 00 3B F8 FF  .............;..
0090: FF 7F 01 00 02 00 03 00  3A F8 FF FF 7F 04 00 17  ........:.......
00A0: 05 00 04 00 00 00 16 06  00 04 00 00 00 07 01 00  ................
00B0: 05 00 07 02 00 06 00 1B  17 05 00 04 00 00 00 16  ................
00C0: 06 00 04 00 00 00 07 01  00 05 00 07 02 00 06 00  ................
00D0: 1B                                                .               
```

#### Opcodes

```
  0: 0x0077 [0x03] ExtData[1]->WorkLocal[0] = 1000*
  1: 0x007C [0x1A] CALL_SUBROUTINE(address=0x008D)
  2: 0x007F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0082 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  4: 0x008A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x008C [0x00] END_REQSTACK()

SUBROUTINE_008D:
  6: 0x008D [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  7: 0x0098 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
  8: 0x009F [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
  9: 0x00A6 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 10: 0x00AD [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
 11: 0x00B2 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 12: 0x00B7 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00B8 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x00BF [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x00C6 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x00CB [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x00D0 [0x1B] RETURN
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    5B 0B 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 61 30   [..........tla0
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=465*
  1: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    5B 0B 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 61 31   [..........tla1
00F0: 53 F8 FF FF 7F F8 FF FF  7F 74 6C 61 31 00        S........tla1.  
```

#### Opcodes

```
  0: 0x00E1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [EventEntity, EventEntity], work=465*
  1: 0x00F0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tla1" with entities [EventEntity, EventEntity]
  2: 0x00FD [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FE   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                            5B 0B                [.
0100: 80 F8 FF FF 7F F8 FF FF  7F 74 61 68 61 00        .........taha.  
```

#### Opcodes

```
  0: 0x00FE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "taha" with entities [EventEntity, EventEntity], work=465*
  1: 0x010D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                            5B 0B                [.
0110: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 62 30 00        .........tlb0.  
```

#### Opcodes

```
  0: 0x010E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=465*
  1: 0x011D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011E   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                            5B 0B                [.
0120: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 62 31 53 F8 FF  .........tlb1S..
0130: FF 7F F8 FF FF 7F 74 6C  62 31 00                 ......tlb1.     
```

#### Opcodes

```
  0: 0x011E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=465*
  1: 0x012D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
  2: 0x013A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                   5B 0B 80 F8 FF             [....
0140: FF 7F F8 FF FF 7F 74 62  68 61 00                 ......tbha.     
```

#### Opcodes

```
  0: 0x013B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tbha" with entities [EventEntity, EventEntity], work=465*
  1: 0x014A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                   5B 0B 80 F8 FF             [....
0150: FF 7F F8 FF FF 7F 74 68  62 30 00                 ......thb0.     
```

#### Opcodes

```
  0: 0x014B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb0" with entities [EventEntity, EventEntity], work=465*
  1: 0x015A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015B   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                   5B 0B 80 F8 FF             [....
0160: FF 7F F8 FF FF 7F 74 68  62 31 53 F8 FF FF 7F F8  ......thb1S.....
0170: FF FF 7F 74 68 62 31 00                           ...thb1.        
```

#### Opcodes

```
  0: 0x015B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb1" with entities [EventEntity, EventEntity], work=465*
  1: 0x016A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thb1" with entities [EventEntity, EventEntity]
  2: 0x0177 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0178   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                          5B 0C 80 F8 FF FF 7F F8          [.......
0180: FF FF 7F 74 6C 63 30 00                           ...tlc0.        
```

#### Opcodes

```
  0: 0x0178 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=643*
  1: 0x0187 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0188   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                          5B 0C 80 F8 FF FF 7F F8          [.......
0190: FF FF 7F 74 6C 63 31 53  F8 FF FF 7F F8 FF FF 7F  ...tlc1S........
01A0: 74 6C 63 31 00                                    tlc1.           
```

#### Opcodes

```
  0: 0x0188 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc1" with entities [EventEntity, EventEntity], work=643*
  1: 0x0197 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc1" with entities [EventEntity, EventEntity]
  2: 0x01A4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                5B 0C 80  F8 FF FF 7F F8 FF FF 7F       [..........
01B0: 74 6C 64 30 00                                    tld0.           
```

#### Opcodes

```
  0: 0x01A5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tld0" with entities [EventEntity, EventEntity], work=643*
  1: 0x01B4 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B5   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                5B 0C 80  F8 FF FF 7F F8 FF FF 7F       [..........
01C0: 74 6C 64 31 53 F8 FF FF  7F F8 FF FF 7F 74 6C 64  tld1S........tld
01D0: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x01B5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tld1" with entities [EventEntity, EventEntity], work=643*
  1: 0x01C4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tld1" with entities [EventEntity, EventEntity]
  2: 0x01D1 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D2   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:       5B 0C 80 F8 FF FF  7F F8 FF FF 7F 74 72 30    [..........tr0
01E0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x01D2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tr00" with entities [EventEntity, EventEntity], work=643*
  1: 0x01E1 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E2   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:       5B 0C 80 F8 FF FF  7F F8 FF FF 7F 74 72 30    [..........tr0
01F0: 31 53 F8 FF FF 7F F8 FF  FF 7F 74 72 30 31 00     1S........tr01. 
```

#### Opcodes

```
  0: 0x01E2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tr01" with entities [EventEntity, EventEntity], work=643*
  1: 0x01F1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tr01" with entities [EventEntity, EventEntity]
  2: 0x01FE [0x00] END_REQSTACK()
```
