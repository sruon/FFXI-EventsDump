# 17797242 - Shikaree Y

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 584 bytes        |
| Total Events     | 16               |
| References Count | 25               |

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
| [322](#event-322)          | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |     49 |             11 |
| [65535.9](#event-655359)   | 0x0076       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0086       |     16 |              2 |
| [65535.11](#event-6553511) | 0x0096       |    123 |             23 |
| [65535.12](#event-6553512) | 0x0111       |     87 |             15 |
| [65535.13](#event-6553513) | 0x0168       |     34 |              9 |
| [65535.14](#event-6553514) | 0x018A       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFF7BF3  |  4294933491 |
|       4 | 0xD764      |       55140 |
|       5 | 0xFFFFC181  |  4294951297 |
|       6 | 0x067B      |        1659 |
|       7 | 0xFFFFF060  |  4294963296 |
|       8 | 0x000D      |          13 |
|       9 | 0x07D0      |        2000 |
|      10 | 0x02FF      |         767 |
|      11 | 0xFFFFFDD0  |  4294966736 |
|      12 | 0x00E1      |         225 |
|      13 | 0x0078      |         120 |
|      14 | 0x000F      |          15 |
|      15 | 0x0028      |          40 |
|      16 | 0xFFFF6B0F  |  4294929167 |
|      17 | 0xAD1E      |       44318 |
|      18 | 0xFFFFC180  |  4294951296 |
|      19 | 0xFFFF6A73  |  4294929011 |
|      20 | 0x6A89      |       27273 |
|      21 | 0xFFFFE0D5  |  4294959317 |
|      22 | 0xFFFF826B  |  4294935147 |
|      23 | 0xDBC7      |       56263 |
|      24 | 0x05E3      |        1507 |

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
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 49 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                37 03 80  04 80 05 80 06 80 03 01       7..........
0050: 00 07 80 1A 24 01 37 02  00 03 00 04 00 05 00 32  ....$.7........2
0060: 08 80 03 01 00 09 80 1A  24 01 1F 00 02 00 03 00  ........$.......
0070: 04 00 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0045 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-33.805*, z=55.140*, y=-15.999*, direction=145.8°*
  1: 0x004E [0x03] ExtData[1]->WorkLocal[1] = 4294963296*
  2: 0x0053 [0x1A] CALL_SUBROUTINE(address=0x0124)
  3: 0x0056 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[2], z=ExtData[1]->WorkLocal[3], y=ExtData[1]->WorkLocal[4], direction=ExtData[1]->WorkLocal[5]
  4: 0x005F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x0062 [0x03] ExtData[1]->WorkLocal[1] = 2000*
  6: 0x0067 [0x1A] CALL_SUBROUTINE(address=0x0124)
  7: 0x006A [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[2], Z=ExtData[1]->WorkLocal[3], Y=ExtData[1]->WorkLocal[4]
  8: 0x0072 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   5B 0A  80 F8 FF FF 7F F8 FF FF        [.........
0080: 7F 65 64 30 30 00                                 .ed00.          
```

#### Opcodes

```
  0: 0x0076 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed00" with entities [EventEntity, EventEntity], work=767*
  1: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   5B 0A  80 F8 FF FF 7F F8 FF FF        [.........
0090: 7F 65 64 30 31 00                                 .ed01.          
```

#### Opcodes

```
  0: 0x0086 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed01" with entities [EventEntity, EventEntity], work=767*
  1: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0096    |
| Data Size    | 123 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   32 08  80 3B 7B 90 0F 01 02 00        2..;{.....
00A0: 03 00 04 00 3A 7B 90 0F  01 05 00 03 01 00 0B 80  ....:{..........
00B0: 17 06 00 05 00 01 00 16  07 00 05 00 01 00 07 02  ................
00C0: 00 06 00 07 03 00 07 00  03 05 00 00 80 03 01 00  ................
00D0: 0C 80 17 06 00 05 00 01  00 16 07 00 05 00 01 00  ................
00E0: 07 02 00 06 00 07 03 00  07 00 5B 0A 80 F8 FF FF  ..........[.....
00F0: 7F F8 FF FF 7F 00 FE FE  FE 1F 00 02 00 03 00 04  ................
0100: 00 1F 01 6F 3A 7B 90 0F  01 00 00 39 00 00 6F 70  ...o:{.....9..op
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x0096 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0099 [0x3B] GET_ENTITY_POSITION(entity=Shikaree X (ID: 17797243/0x010F907B), x_destination=ExtData[1]->WorkLocal[2], y_destination=ExtData[1]->WorkLocal[3], z_destination=ExtData[1]->WorkLocal[4])
  2: 0x00A4 [0x3A] CONVERT_YAW_TO_BYTE(entity=Shikaree X (ID: 17797243/0x010F907B), result_destination=ExtData[1]->WorkLocal[5])
  3: 0x00AB [0x03] ExtData[1]->WorkLocal[1] = 4294966736*
  4: 0x00B0 [0x17] ExtData[1]->WorkLocal[6] = cos(ExtData[1]->WorkLocal[5]) * ExtData[1]->WorkLocal[1]
  5: 0x00B7 [0x16] ExtData[1]->WorkLocal[7] = sin(ExtData[1]->WorkLocal[5]) * ExtData[1]->WorkLocal[1]
  6: 0x00BE [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
  7: 0x00C3 [0x07] ExtData[1]->WorkLocal[3] += ExtData[1]->WorkLocal[7]
  8: 0x00C8 [0x03] ExtData[1]->WorkLocal[5] = 0*
  9: 0x00CD [0x03] ExtData[1]->WorkLocal[1] = 225*
 10: 0x00D2 [0x17] ExtData[1]->WorkLocal[6] = cos(ExtData[1]->WorkLocal[5]) * ExtData[1]->WorkLocal[1]
 11: 0x00D9 [0x16] ExtData[1]->WorkLocal[7] = sin(ExtData[1]->WorkLocal[5]) * ExtData[1]->WorkLocal[1]
 12: 0x00E0 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 13: 0x00E5 [0x07] ExtData[1]->WorkLocal[3] += ExtData[1]->WorkLocal[7]
 14: 0x00EA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=767*
 15: 0x00F9 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[2], Z=ExtData[1]->WorkLocal[3], Y=ExtData[1]->WorkLocal[4]
 16: 0x0101 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 17: 0x0103 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 18: 0x0104 [0x3A] CONVERT_YAW_TO_BYTE(entity=Shikaree X (ID: 17797243/0x010F907B), result_destination=ExtData[1]->WorkLocal[0])
 19: 0x010B [0x39] SET_ENTITY_DIRECTION(direction=ExtData[1]->WorkLocal[0])
 20: 0x010E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 21: 0x010F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 22: 0x0110 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0111   |
| Data Size    | 87 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:    5B 0A 80 F8 FF FF 7F  F8 FF FF 7F 65 64 30 32   [..........ed02
0120: 1C 0D 80 00 3B F8 FF FF  7F 02 00 03 00 04 00 3A  ....;..........:
0130: F8 FF FF 7F 05 00 17 06  00 05 00 01 00 16 07 00  ................
0140: 05 00 01 00 07 02 00 06  00 07 03 00 07 00 1B 17  ................
0150: 06 00 05 00 01 00 16 07  00 05 00 01 00 07 02 00  ................
0160: 06 00 07 03 00 07 00 1B                           ........        
```

#### Opcodes

```
  0: 0x0111 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed02" with entities [EventEntity, EventEntity], work=767*
  1: 0x0120 [0x1C] WAIT(120* ticks)
  2: 0x0123 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0124 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[2], y_destination=ExtData[1]->WorkLocal[3], z_destination=ExtData[1]->WorkLocal[4])
     0x012F [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[5])
     0x0136 [0x17] ExtData[1]->WorkLocal[6] = cos(ExtData[1]->WorkLocal[5]) * ExtData[1]->WorkLocal[1]
     0x013D [0x16] ExtData[1]->WorkLocal[7] = sin(ExtData[1]->WorkLocal[5]) * ExtData[1]->WorkLocal[1]
     0x0144 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0149 [0x07] ExtData[1]->WorkLocal[3] += ExtData[1]->WorkLocal[7]
     0x014E [0x1B] RETURN
     0x014F [0x17] ExtData[1]->WorkLocal[6] = cos(ExtData[1]->WorkLocal[5]) * ExtData[1]->WorkLocal[1]
     0x0156 [0x16] ExtData[1]->WorkLocal[7] = sin(ExtData[1]->WorkLocal[5]) * ExtData[1]->WorkLocal[1]
     0x015D [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0162 [0x07] ExtData[1]->WorkLocal[3] += ExtData[1]->WorkLocal[7]
     0x0167 [0x1B] RETURN
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0168   |
| Data Size    | 34 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                          5E 69 64 6C 30 1C 0E 80          ^idl0...
0170: 32 0F 80 1F 00 10 80 11  80 12 80 1F 01 33 01 5A  2............3.Z
0180: 00 13 80 14 80 15 80 5A  01 00                    .......Z..      
```

#### Opcodes

```
  0: 0x0168 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x016D [0x1C] WAIT(15* ticks)
  2: 0x0170 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x0173 [0x1F] MOVE_ENTITY: EventEntity moves to X=-38.129*, Z=44.318*, Y=-16.000*
  4: 0x017B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x017D [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  6: 0x017F [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-38.285*, Z=27.273*, Y=-7.979*
  7: 0x0187 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  8: 0x0189 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                37 16 80 17 80 05            7.....
0190: 80 18 80 00                                       ....            
```

#### Opcodes

```
  0: 0x018A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-32.149*, z=56.263*, y=-15.999*, direction=132.4°*
  1: 0x0193 [0x00] END_REQSTACK()
```
