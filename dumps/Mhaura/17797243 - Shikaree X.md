# 17797243 - Shikaree X

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 412 bytes        |
| Total Events     | 14               |
| References Count | 21               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [322](#event-322)          | 0x0044       |      3 |              2 |
| [65535.8](#event-655358)   | 0x0047       |    117 |             23 |
| [65535.9](#event-655359)   | 0x00BC       |     10 |              2 |
| [65535.10](#event-6553510) | 0x00C6       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00D6       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00E6       |     26 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFF7964  |  4294932836 |
|       4 | 0xD763      |       55139 |
|       5 | 0xFFFFC180  |  4294951296 |
|       6 | 0x05B9      |        1465 |
|       7 | 0xFFFFE890  |  4294961296 |
|       8 | 0x0028      |          40 |
|       9 | 0x157C      |        5500 |
|      10 | 0xFFFF7AA5  |  4294933157 |
|      11 | 0xD8E1      |       55521 |
|      12 | 0xFFFFC181  |  4294951297 |
|      13 | 0x057A      |        1402 |
|      14 | 0x029D      |         669 |
|      15 | 0xFFFF784C  |  4294932556 |
|      16 | 0xAD56      |       44374 |
|      17 | 0xFFFFC1C2  |  4294951362 |
|      18 | 0xFFFF71B6  |  4294930870 |
|      19 | 0x69F1      |       27121 |
|      20 | 0xFFFFE0DF  |  4294959327 |

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
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 322

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             A4 01 00                                  ...         
```

#### Opcodes

```
  0: 0x0044 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0047    |
| Data Size    | 117 bytes |
| Instructions | 18        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      37  03 80 04 80 05 80 06 80         7........
0050: 03 00 00 07 80 1A 78 00  37 01 00 02 00 03 00 04  ......x.7.......
0060: 00 32 08 80 03 00 00 09  80 1A 78 00 1F 00 01 00  .2........x.....
0070: 02 00 03 00 1F 01 6F 00  3B F8 FF FF 7F 01 00 02  ......o.;.......
0080: 00 03 00 3A F8 FF FF 7F  04 00 17 05 00 04 00 00  ...:............
0090: 00 16 06 00 04 00 00 00  07 01 00 05 00 07 02 00  ................
00A0: 06 00 1B 17 05 00 04 00  00 00 16 06 00 04 00 00  ................
00B0: 00 07 01 00 05 00 07 02  00 06 00 1B              ............    
```

#### Opcodes

```
  0: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-34.460*, z=55.139*, y=-16.000*, direction=128.8°*
  1: 0x0050 [0x03] ExtData[1]->WorkLocal[0] = 4294961296*
  2: 0x0055 [0x1A] CALL_SUBROUTINE(address=0x0078)
  3: 0x0058 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[1], z=ExtData[1]->WorkLocal[2], y=ExtData[1]->WorkLocal[3], direction=ExtData[1]->WorkLocal[4]
  4: 0x0061 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x0064 [0x03] ExtData[1]->WorkLocal[0] = 5500*
  6: 0x0069 [0x1A] CALL_SUBROUTINE(address=0x0078)
  7: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  8: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0076 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x0077 [0x00] END_REQSTACK()

SUBROUTINE_0078:
 11: 0x0078 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
 12: 0x0083 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
 13: 0x008A [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 14: 0x0091 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 15: 0x0098 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
 16: 0x009D [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 17: 0x00A2 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00A3 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x00AA [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x00B1 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x00B6 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x00BB [0x1B] RETURN
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      37 0A 80 0B              7...
00C0: 80 0C 80 0D 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00BC [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-34.139*, z=55.521*, y=-15.999*, direction=123.2°*
  1: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   5B 0E  80 F8 FF FF 7F F8 FF FF        [.........
00D0: 7F 65 64 30 30 00                                 .ed00.          
```

#### Opcodes

```
  0: 0x00C6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed00" with entities [EventEntity, EventEntity], work=669*
  1: 0x00D5 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D6   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   5B 0E  80 F8 FF FF 7F F8 FF FF        [.........
00E0: 7F 65 64 30 31 00                                 .ed01.          
```

#### Opcodes

```
  0: 0x00D6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed01" with entities [EventEntity, EventEntity], work=669*
  1: 0x00E5 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E6   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   32 08  80 1F 00 0F 80 10 80 11        2.........
00F0: 80 1F 01 33 01 5A 00 12  80 13 80 14 80 5A 01 00  ...3.Z.......Z..
```

#### Opcodes

```
  0: 0x00E6 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00E9 [0x1F] MOVE_ENTITY: EventEntity moves to X=-34.740*, Z=44.374*, Y=-15.934*
  2: 0x00F1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F3 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  4: 0x00F5 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-36.426*, Z=27.121*, Y=-7.969*
  5: 0x00FD [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  6: 0x00FF [0x00] END_REQSTACK()
```
