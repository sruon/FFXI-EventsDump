# 17126152 - Merfanont

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | La Vaule [S] (ID: 85) |
| Block Size       | 628 bytes             |
| Total Events     | 19                    |
| References Count | 27                    |

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
| [1](#event-1)              | 0x0044       |      1 |              1 |
| [6](#event-6)              | 0x0045       |     21 |              2 |
| [65535.8](#event-655358)   | 0x005A       |     18 |              6 |
| [65535.9](#event-655359)   | 0x006C       |     15 |              5 |
| [65535.10](#event-6553510) | 0x007B       |     37 |              5 |
| [65535.11](#event-6553511) | 0x00A0       |    185 |             37 |
| [65535.12](#event-6553512) | 0x0159       |     19 |              3 |
| [65535.13](#event-6553513) | 0x016C       |     21 |              2 |
| [5](#event-5)              | 0x0181       |      1 |              1 |
| [65535.14](#event-6553514) | 0x0182       |     21 |              2 |
| [65535.15](#event-6553515) | 0x0197       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0004      |           4 |
|       4 | 0x0008      |           8 |
|       5 | 0x00DD      |         221 |
|       6 | 0x000D      |          13 |
|       7 | 0x00FB      |         251 |
|       8 | 0x001B      |          27 |
|       9 | 0x000F      |          15 |
|      10 | 0x34E05     |      216581 |
|      11 | 0xFFFFEEA6  |  4294962854 |
|      12 | 0xFFFFFFD9  |  4294967257 |
|      13 | 0x000A      |          10 |
|      14 | 0x42795     |      272277 |
|      15 | 0xFFFD091E  |  4294773022 |
|      16 | 0x0E9D      |        3741 |
|      17 | 0x0005      |           5 |
|      18 | 0x0002      |           2 |
|      19 | 0x0009      |           9 |
|      20 | 0x0046      |          70 |
|      21 | 0x008C      |         140 |
|      22 | 0x00D2      |         210 |
|      23 | 0x001E      |          30 |
|      24 | 0x0516      |        1302 |
|      25 | 0x0003      |           3 |
|      26 | 0x000C      |          12 |

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

### Event 1

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

### Event 6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                B6 0B 03  80 04 80 00 80 05 80 05       ...........
0050: 80 06 80 05 80 07 80 08  80 00                    ..........      
```

#### Opcodes

```
  0: 0x0045 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=8*, head=0*, body=221*, hands=221*, legs=13*, feet=221*, main=251*, sub=27*)
  1: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                1C 09 80 32 06 80            ...2..
0060: 1F 00 0A 80 0B 80 0C 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x005A [0x1C] WAIT(15* ticks)
  1: 0x005D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0060 [0x1F] MOVE_ENTITY: EventEntity moves to X=216.581*, Z=-4.442*, Y=-0.039*
  3: 0x0068 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x006A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      32 0D 80 1F              2...
0070: 00 0E 80 0F 80 10 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x006C [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x006F [0x1F] MOVE_ENTITY: EventEntity moves to X=272.277*, Z=-194.274*, Y=3.741*
  2: 0x0077 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0079 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   03 00 00 07 7F             .....
0080: 1A C5 00 66 01 00 F8 FF  FF 7F F8 FF FF 7F 73 68  ...f..........sh
0090: 61 30 53 F8 FF FF 7F F8  FF FF 7F 73 68 61 30 00  a0S........sha0.
```

#### Opcodes

```
  0: 0x007B [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0080 [0x1A] CALL_SUBROUTINE(address=0x00C5)
  2: 0x0083 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0092 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x009F [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00A0    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0: 03 00 00 07 7F 1A C5 00  66 01 00 F8 FF FF 7F F8  ........f.......
00B0: FF FF 7F 73 68 61 31 53  F8 FF FF 7F F8 FF FF 7F  ...sha1S........
00C0: 73 68 61 31 00 03 01 00  00 00 02 01 00 11 80 05  sha1............
00D0: DA 00 08 01 00 01 80 01  DF 00 08 01 00 12 80 14  ................
00E0: 01 00 0D 80 07 01 00 13  80 1B 03 01 00 00 00 02  ................
00F0: 01 00 11 80 05 FF 00 08  01 00 01 80 01 04 01 08  ................
0100: 01 00 12 80 14 01 00 0D  80 07 01 00 14 80 1B 03  ................
0110: 01 00 00 00 02 01 00 11  80 05 24 01 08 01 00 01  ..........$.....
0120: 80 01 29 01 08 01 00 12  80 14 01 00 0D 80 07 01  ..).............
0130: 00 15 80 1B 03 01 00 00  00 02 01 00 11 80 05 49  ...............I
0140: 01 08 01 00 01 80 01 4E  01 08 01 00 12 80 14 01  .......N........
0150: 00 0D 80 07 01 00 16 80  1B                       .........       
```

#### Opcodes

```
  0: 0x00A0 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x00A5 [0x1A] CALL_SUBROUTINE(address=0x00C5)
  2: 0x00A8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x00B7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x00C4 [0x00] END_REQSTACK()

SUBROUTINE_00C5:
  5: 0x00C5 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  6: 0x00CA [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00DA
  7: 0x00D2 [0x08] ExtData[1]->WorkLocal[1] -= 1*
  8: 0x00D7 [0x01] GOTO 0x00DF
  9: 0x00DA [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_00DF:
 10: 0x00DF [0x14] ExtData[1]->WorkLocal[1] *= 10*
 11: 0x00E4 [0x07] ExtData[1]->WorkLocal[1] += 9*
 12: 0x00E9 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00EA [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00EF [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00FF
     0x00F7 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00FC [0x01] GOTO 0x0104
     0x00FF [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0104 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0109 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x010E [0x1B] RETURN
     0x010F [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0114 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0124
     0x011C [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0121 [0x01] GOTO 0x0129
     0x0124 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0129 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x012E [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x0133 [0x1B] RETURN
     0x0134 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0139 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0149
     0x0141 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0146 [0x01] GOTO 0x014E
     0x0149 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x014E [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0153 [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x0158 [0x1B] RETURN
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0159   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                             1C 17 80 5B 18 80 F8           ...[...
0160: FF FF 7F F8 FF FF 7F 6C  62 74 30 00              .......lbt0.    
```

#### Opcodes

```
  0: 0x0159 [0x1C] WAIT(30* ticks)
  1: 0x015C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "lbt0" with entities [EventEntity, EventEntity], work=1302*
  2: 0x016B [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016C   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                      B6 0B 19 80              ....
0170: 04 80 05 80 06 80 05 80  06 80 05 80 07 80 08 80  ................
0180: 00                                                .               
```

#### Opcodes

```
  0: 0x016C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=8*, head=221*, body=13*, hands=221*, legs=13*, feet=221*, main=251*, sub=27*)
  1: 0x0180 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0181  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:    00                                              .              
```

#### Opcodes

```
  0: 0x0181 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0182   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:       B6 0B 19 80 13 80  08 80 06 80 05 80 06 80    ..............
0190: 1A 80 00 80 00 80 00                              .......         
```

#### Opcodes

```
  0: 0x0182 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=9*, head=27*, body=13*, hands=221*, legs=13*, feet=12*, main=0*, sub=0*)
  1: 0x0196 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0197   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                      B6  0B 19 80 04 80 05 80 06         .........
01A0: 80 05 80 06 80 05 80 07  80 08 80 00              ............    
```

#### Opcodes

```
  0: 0x0197 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=8*, head=221*, body=13*, hands=221*, legs=13*, feet=221*, main=251*, sub=27*)
  1: 0x01AB [0x00] END_REQSTACK()
```
