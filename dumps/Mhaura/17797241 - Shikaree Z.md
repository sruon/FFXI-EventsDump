# 17797241 - Shikaree Z

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 716 bytes        |
| Total Events     | 23               |
| References Count | 29               |

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
| [322](#event-322)          | 0x0044       |     12 |              3 |
| [65535.8](#event-655358)   | 0x0050       |     42 |              8 |
| [65535.9](#event-655359)   | 0x007A       |     55 |              9 |
| [65535.10](#event-6553510) | 0x00B1       |     91 |             19 |
| [65535.11](#event-6553511) | 0x010C       |     10 |              2 |
| [65535.12](#event-6553512) | 0x0116       |     26 |              7 |
| [65535.13](#event-6553513) | 0x0130       |     18 |              5 |
| [65535.14](#event-6553514) | 0x0142       |      4 |              2 |
| [65535.15](#event-6553515) | 0x0146       |     16 |              2 |
| [65535.16](#event-6553516) | 0x0156       |     16 |              2 |
| [65535.17](#event-6553517) | 0x0166       |     29 |              3 |
| [65535.18](#event-6553518) | 0x0183       |     29 |              3 |
| [65535.19](#event-6553519) | 0x01A0       |     29 |              3 |
| [65535.20](#event-6553520) | 0x01BD       |     29 |              3 |
| [65535.21](#event-6553521) | 0x01DA       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFF2C53  |  4294913107 |
|       4 | 0x7D5F      |       32095 |
|       5 | 0xFFFFC180  |  4294951296 |
|       6 | 0x0010      |          16 |
|       7 | 0x000D      |          13 |
|       8 | 0xFFFF39AC  |  4294916524 |
|       9 | 0x800E      |       32782 |
|      10 | 0x0078      |         120 |
|      11 | 0xFFFF6DB1  |  4294929841 |
|      12 | 0xC528      |       50472 |
|      13 | 0xFFFFC181  |  4294951297 |
|      14 | 0x0D9C      |        3484 |
|      15 | 0xFFFFFB50  |  4294966096 |
|      16 | 0x0055      |          85 |
|      17 | 0x04B0      |        1200 |
|      18 | 0x05DC      |        1500 |
|      19 | 0xFFFF6DAD  |  4294929837 |
|      20 | 0xC522      |       50466 |
|      21 | 0x0D9A      |        3482 |
|      22 | 0xFFFF7047  |  4294930503 |
|      23 | 0xAB48      |       43848 |
|      24 | 0xFFFF6F94  |  4294930324 |
|      25 | 0x8966      |       35174 |
|      26 | 0xFFFFD274  |  4294955636 |
|      27 | 0x0300      |         768 |
|      28 | 0x0301      |         769 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             37 03 80 04  80 05 80 06 80 A4 01 00      7...........
```

#### Opcodes

```
  0: 0x0044 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-54.189*, z=32.095*, y=-16.000*, direction=1.4°*
  1: 0x004D [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  2: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 42 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 32 07 80 31 00 08 80 09  80 05 80 0A 80 31 01 37  2..1.........1.7
0060: 0B 80 0C 80 0D 80 0E 80  03 00 00 0F 80 1A C8 00  ................
0070: 37 01 00 02 00 03 00 04  00 00                    7.........      
```

#### Opcodes

```
  0: 0x0050 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0053 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=-50.772*, Z=32.782*, Y=-16.000*, Time=120*
  2: 0x005D [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  3: 0x005F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-37.455*, z=50.472*, y=-15.999*, direction=306.2°*
  4: 0x0068 [0x03] ExtData[1]->WorkLocal[0] = 4294966096*
  5: 0x006D [0x1A] CALL_SUBROUTINE(address=0x00C8)
  6: 0x0070 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[1], z=ExtData[1]->WorkLocal[2], y=ExtData[1]->WorkLocal[3], direction=ExtData[1]->WorkLocal[4]
  7: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 55 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                45 10 80 F0 FF FF            E.....
0080: 7F F0 FF FF 7F 7A 30 30  37 00 80 55 10 80 F0 FF  .....z007..U....
0090: FF 7F F0 FF FF 7F 7A 30  30 37 32 07 80 03 00 00  ......z0072.....
00A0: 11 80 1A C8 00 1F 00 01  00 02 00 03 00 1F 01 6F  ...............o
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x007A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z007" with entities [LocalPlayer, LocalPlayer], work=[85*, 0*]
  1: 0x008B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "z007" with entities [LocalPlayer, LocalPlayer], work=85*
  2: 0x009A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x009D [0x03] ExtData[1]->WorkLocal[0] = 1200*
  4: 0x00A2 [0x1A] CALL_SUBROUTINE(address=0x00C8)
  5: 0x00A5 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  6: 0x00AD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00AF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 91 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    32 07 80 03 00 00 12  80 1A C8 00 1F 00 01 00   2..............
00C0: 02 00 03 00 1F 01 6F 00  3B F8 FF FF 7F 01 00 02  ......o.;.......
00D0: 00 03 00 3A F8 FF FF 7F  04 00 17 05 00 04 00 00  ...:............
00E0: 00 16 06 00 04 00 00 00  07 01 00 05 00 07 02 00  ................
00F0: 06 00 1B 17 05 00 04 00  00 00 16 06 00 04 00 00  ................
0100: 00 07 01 00 05 00 07 02  00 06 00 1B              ............    
```

#### Opcodes

```
  0: 0x00B1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B4 [0x03] ExtData[1]->WorkLocal[0] = 1500*
  2: 0x00B9 [0x1A] CALL_SUBROUTINE(address=0x00C8)
  3: 0x00BC [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  4: 0x00C4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00C6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00C7 [0x00] END_REQSTACK()

SUBROUTINE_00C8:
  7: 0x00C8 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  8: 0x00D3 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
  9: 0x00DA [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 10: 0x00E1 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 11: 0x00E8 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
 12: 0x00ED [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 13: 0x00F2 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00F3 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x00FA [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0101 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x0106 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x010B [0x1B] RETURN
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                      37 13 80 14              7...
0110: 80 0D 80 15 80 00                                 ......          
```

#### Opcodes

```
  0: 0x010C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-37.459*, z=50.466*, y=-15.999*, direction=306.0°*
  1: 0x0115 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0116   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   32 07  80 1F 00 16 80 17 80 05        2.........
0120: 80 1F 01 33 01 5A 00 18  80 19 80 1A 80 5A 01 00  ...3.Z.......Z..
```

#### Opcodes

```
  0: 0x0116 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0119 [0x1F] MOVE_ENTITY: EventEntity moves to X=-36.793*, Z=43.848*, Y=-16.000*
  2: 0x0121 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0123 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  4: 0x0125 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-36.972*, Z=35.174*, Y=-11.660*
  5: 0x012D [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  6: 0x012F [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0130   |
| Data Size    | 18 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130: 06 07 00 02 07 00 00 80  00 41 01 1C 01 80 01 33  .........A.....3
0140: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0130 [0x06] ExtData[1]->WorkLocal[7] = 0
  1: 0x0133 [0x02] IF !(ExtData[1]->WorkLocal[7] == 0*) GOTO 0x0141
  2: 0x013B [0x1C] WAIT(1* ticks)
  3: 0x013E [0x01] GOTO 0x0133
  4: 0x0141 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0142  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:       05 07 00 00                                   ....          
```

#### Opcodes

```
  0: 0x0142 [0x05] ExtData[1]->WorkLocal[7] = 1
  1: 0x0145 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0146   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                   5B 1B  80 F8 FF FF 7F F8 FF FF        [.........
0150: 7F 65 64 30 30 00                                 .ed00.          
```

#### Opcodes

```
  0: 0x0146 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed00" with entities [EventEntity, EventEntity], work=768*
  1: 0x0155 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0156   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   5B 1B  80 F8 FF FF 7F F8 FF FF        [.........
0160: 7F 65 64 30 31 00                                 .ed01.          
```

#### Opcodes

```
  0: 0x0156 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed01" with entities [EventEntity, EventEntity], work=768*
  1: 0x0165 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0166   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                   5B 1B  80 F8 FF FF 7F F8 FF FF        [.........
0170: 7F 65 64 30 32 53 F8 FF  FF 7F F8 FF FF 7F 65 64  .ed02S........ed
0180: 30 32 00                                          02.             
```

#### Opcodes

```
  0: 0x0166 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed02" with entities [EventEntity, EventEntity], work=768*
  1: 0x0175 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ed02" with entities [EventEntity, EventEntity]
  2: 0x0182 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0183   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:          5B 1B 80 F8 FF  FF 7F F8 FF FF 7F 65 64     [..........ed
0190: 30 33 53 F8 FF FF 7F F8  FF FF 7F 65 64 30 33 00  03S........ed03.
```

#### Opcodes

```
  0: 0x0183 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed03" with entities [EventEntity, EventEntity], work=768*
  1: 0x0192 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ed03" with entities [EventEntity, EventEntity]
  2: 0x019F [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A0   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0: 5B 1C 80 F8 FF FF 7F F8  FF FF 7F 65 64 30 34 53  [..........ed04S
01B0: F8 FF FF 7F F8 FF FF 7F  65 64 30 34 00           ........ed04.   
```

#### Opcodes

```
  0: 0x01A0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed04" with entities [EventEntity, EventEntity], work=769*
  1: 0x01AF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ed04" with entities [EventEntity, EventEntity]
  2: 0x01BC [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BD   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                         5B 1C 80               [..
01C0: F8 FF FF 7F F8 FF FF 7F  65 64 30 35 53 F8 FF FF  ........ed05S...
01D0: 7F F8 FF FF 7F 65 64 30  35 00                    .....ed05.      
```

#### Opcodes

```
  0: 0x01BD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed05" with entities [EventEntity, EventEntity], work=769*
  1: 0x01CC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ed05" with entities [EventEntity, EventEntity]
  2: 0x01D9 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01DA   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                5B 1C 80 F8 FF FF            [.....
01E0: 7F F8 FF FF 7F 65 64 30  36 00                    .....ed06.      
```

#### Opcodes

```
  0: 0x01DA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ed06" with entities [EventEntity, EventEntity], work=769*
  1: 0x01E9 [0x00] END_REQSTACK()
```
