# 17335047 - Cait Sith Seachd

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Beaucedine Glacier [S] (ID: 136) |
| Block Size       | 560 bytes                        |
| Total Events     | 16                               |
| References Count | 22                               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     18 |              4 |
| [65535.2](#event-655352)   | 0x0013       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001D       |      9 |              3 |
| [65535.4](#event-655354)   | 0x0026       |      9 |              3 |
| [65535.5](#event-655355)   | 0x002F       |     10 |              2 |
| [65535.6](#event-655356)   | 0x0039       |     10 |              2 |
| [17](#event-17)            | 0x0043       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0044       |     27 |              5 |
| [9](#event-9)              | 0x005F       |      7 |              2 |
| [65535.8](#event-655358)   | 0x0066       |    258 |             45 |
| [65535.9](#event-655359)   | 0x0168       |      6 |              2 |
| [18](#event-18)            | 0x016E       |      7 |              2 |
| [65535.10](#event-6553510) | 0x0175       |     14 |              4 |
| [65535.11](#event-6553511) | 0x0183       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFDE94B  |  4294830411 |
|       4 | 0xFFFD537B  |  4294792059 |
|       5 | 0xFFFF13CD  |  4294906829 |
|       6 | 0x09D9      |        2521 |
|       7 | 0x0002      |           2 |
|       8 | 0x0005      |           5 |
|       9 | 0x0078      |         120 |
|      10 | 0x00F0      |         240 |
|      11 | 0x0003      |           3 |
|      12 | 0x0DAC      |        3500 |
|      13 | 0x00ED      |         237 |
|      14 | 0x001E      |          30 |
|      15 | 0x03C1      |         961 |
|      16 | 0x000F      |          15 |
|      17 | 0x0BF0      |        3056 |
|      18 | 0x0028      |          40 |
|      19 | 0x60C9A     |      396442 |
|      20 | 0xFFF90F4C  |  4294512460 |
|      21 | 0x05AA      |        1450 |

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
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 2F 00 F8 FF FF  7F 6C F8 FF FF 7F 00 80   "./.....l......
0010: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0009 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          6C F8 FF FF 7F  02 80 01 80 00              l.........   
```

#### Opcodes

```
  0: 0x0013 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         22 00 2F               "./
0020: 00 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x001D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x001F [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0026  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   22 01  2F 01 F8 FF FF 7F 00           "./...... 
```

#### Opcodes

```
  0: 0x0026 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0028 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               6C                 l
0030: F8 FF FF 7F 00 80 01 80  00                       .........       
```

#### Opcodes

```
  0: 0x002F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             6C F8 FF FF 7F 02 80           l......
0040: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0039 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          00                                          .            
```

#### Opcodes

```
  0: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 27 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             1F 00 03 80  04 80 05 80 1F 01 6F 5B      ..........o[
0050: 06 80 07 83 08 01 07 83  08 01 79 72 65 30 00     ..........yre0. 
```

#### Opcodes

```
  0: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=-136.885*, Z=-175.237*, Y=-60.467*
  1: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x004E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x004F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yre0" with entities [Cait Sith Seachd (ID: 17335047/0x01088307), Cait Sith Seachd (ID: 17335047/0x01088307)], work=2521*
  4: 0x005E [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               92                 .
0060: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x005F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0066    |
| Data Size    | 258 bytes |
| Instructions | 45        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   03 00  00 00 80 03 01 00 00 80        ..........
0070: 02 01 00 00 80 00 67 01  13 02 00 07 80 02 02 00  ......g.........
0080: 00 80 80 9B 00 02 00 00  08 80 04 93 00 1C 09 80  ................
0090: 01 98 00 07 00 00 01 80  01 B7 00 02 02 00 01 80  ................
00A0: 80 A9 00 1C 09 80 01 B7  00 02 02 00 07 80 80 B7  ................
00B0: 00 1C 0A 80 01 B7 00 13  02 00 0B 80 02 02 00 00  ................
00C0: 80 80 E2 00 4B F8 FF FF  7F 0C 80 CD 0D 80 F8 FF  ....K...........
00D0: FF 7F F8 FF FF 7F 6F 6E  6D 79 00 80 1C 0E 80 01  ......onmy......
00E0: F4 00 4B F8 FF FF 7F 0F  80 1C 10 80 03 27 10 01  ..K..........'..
00F0: 80 1C 10 80 13 02 00 07  80 02 02 00 00 80 80 07  ................
0100: 01 1C 0E 80 01 23 01 02  02 00 01 80 80 15 01 1C  .....#..........
0110: 09 80 01 23 01 02 02 00  07 80 80 23 01 1C 0A 80  ...#.......#....
0120: 01 23 01 CE 0D 80 F8 FF  FF 7F F8 FF FF 7F 6F 6E  .#............on
0130: 6D 79 CD 0D 80 F8 FF FF  7F F8 FF FF 7F 6F 66 6D  my...........ofm
0140: 79 00 80 CE 0D 80 F8 FF  FF 7F F8 FF FF 7F 6F 66  y.............of
0150: 6D 79 4B F8 FF FF 7F 11  80 1C 10 80 03 27 10 00  myK..........'..
0160: 80 1C 10 80 01 70 00 00                           .....p..        
```

#### Opcodes

```
  0: 0x0066 [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x006B [0x03] ExtData[1]->WorkLocal[1] = 0*
  2: 0x0070 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0167
  3: 0x0078 [0x13] ExtData[1]->WorkLocal[2] = rand() % 2*
  4: 0x007D [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x009B
  5: 0x0085 [0x02] IF !(ExtData[1]->WorkLocal[0] < 5*) GOTO 0x0093
  6: 0x008D [0x1C] WAIT(120* ticks)
  7: 0x0090 [0x01] GOTO 0x0098
  8: 0x0093 [0x07] ExtData[1]->WorkLocal[0] += 1*

SUBROUTINE_0098:
  9: 0x0098 [0x01] GOTO 0x00B7
 10: 0x009B [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x00A9
 11: 0x00A3 [0x1C] WAIT(120* ticks)
 12: 0x00A6 [0x01] GOTO 0x00B7
 13: 0x00A9 [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x00B7
 14: 0x00B1 [0x1C] WAIT(240* ticks)
 15: 0x00B4 [0x01] GOTO 0x00B7

SUBROUTINE_00B7:
 16: 0x00B7 [0x13] ExtData[1]->WorkLocal[2] = rand() % 3*
 17: 0x00BC [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x00E2
 18: 0x00C4 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=19.2°*)
 19: 0x00CB [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "onmy" with entities [EventEntity, EventEntity], work=[237*, 0*]
 20: 0x00DC [0x1C] WAIT(30* ticks)
 21: 0x00DF [0x01] GOTO 0x00F4
 22: 0x00E2 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=5.3°*)
 23: 0x00E9 [0x1C] WAIT(15* ticks)
 24: 0x00EC [0x03] Work_Zone[39] = 1*
 25: 0x00F1 [0x1C] WAIT(15* ticks)

SUBROUTINE_00F4:
 26: 0x00F4 [0x13] ExtData[1]->WorkLocal[2] = rand() % 2*
 27: 0x00F9 [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x0107
 28: 0x0101 [0x1C] WAIT(30* ticks)
 29: 0x0104 [0x01] GOTO 0x0123
 30: 0x0107 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x0115
 31: 0x010F [0x1C] WAIT(120* ticks)
 32: 0x0112 [0x01] GOTO 0x0123
 33: 0x0115 [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x0123
 34: 0x011D [0x1C] WAIT(240* ticks)
 35: 0x0120 [0x01] GOTO 0x0123

SUBROUTINE_0123:
 36: 0x0123 [0xCE] WAIT_LOAD_SCHEDULER_ALT4: Wait for scheduler "onmy" with entities [EventEntity, EventEntity], work=237*
 37: 0x0132 [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "ofmy" with entities [EventEntity, EventEntity], work=[237*, 0*]
 38: 0x0143 [0xCE] WAIT_LOAD_SCHEDULER_ALT4: Wait for scheduler "ofmy" with entities [EventEntity, EventEntity], work=237*
 39: 0x0152 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=16.8°*)
 40: 0x0159 [0x1C] WAIT(15* ticks)
 41: 0x015C [0x03] Work_Zone[39] = 0*
 42: 0x0161 [0x1C] WAIT(15* ticks)
 43: 0x0164 [0x01] GOTO 0x0070
 44: 0x0167 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0168  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                          03 01 00 01 80 00                ......  
```

#### Opcodes

```
  0: 0x0168 [0x03] ExtData[1]->WorkLocal[1] = 1*
  1: 0x016D [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x016E  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                            92 01                ..
0170: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x016E [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0174 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0175   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                32 12 80  1F 00 13 80 14 80 15 80       2..........
0180: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0175 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0178 [0x1F] MOVE_ENTITY: EventEntity moves to X=396.442*, Z=-454.836*, Y=1.450*
  2: 0x0180 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0182 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0183  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:          C0 01 80 00                                 ....         
```

#### Opcodes

```
  0: 0x0183 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0186 [0x00] END_REQSTACK()
```
