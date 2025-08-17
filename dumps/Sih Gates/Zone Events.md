# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Sih Gates (ID: 268) |
| Block Size       | 1004 bytes          |
| Total Events     | 17                  |
| References Count | 40                  |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |      6 |              2 |
| [65535.2](#event-655352)   | 0x0008       |      6 |              2 |
| [65535.3](#event-655353)   | 0x000E       |      7 |              3 |
| [65535.4](#event-655354)   | 0x0015       |      7 |              3 |
| [65535.5](#event-655355)   | 0x001C       |     37 |              5 |
| [65535.6](#event-655356)   | 0x0041       |     37 |              5 |
| [65535.7](#event-655357)   | 0x0066       |     27 |              7 |
| [65535.8](#event-655358)   | 0x0081       |    366 |             43 |
| [65535.9](#event-655359)   | 0x01EF       |     14 |              4 |
| [65535.10](#event-6553510) | 0x01FD       |     14 |              4 |
| [65535.11](#event-6553511) | 0x020B       |     14 |              4 |
| [65535.12](#event-6553512) | 0x0219       |     20 |              6 |
| [65535.13](#event-6553513) | 0x022D       |     19 |              5 |
| [65535.14](#event-6553514) | 0x0240       |     29 |              5 |
| [65535.15](#event-6553515) | 0x025D       |    152 |             34 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0028      |          40 |
|       3 | 0xFFF98C0C  |  4294544396 |
|       4 | 0xFFFF187B  |  4294908027 |
|       5 | 0xFFFFB32B  |  4294947627 |
|       6 | 0x001E      |          30 |
|       7 | 0x0078      |         120 |
|       8 | 0x0095      |         149 |
|       9 | 0x0002      |           2 |
|      10 | 0x009F      |         159 |
|      11 | 0x0003      |           3 |
|      12 | 0x00A9      |         169 |
|      13 | 0x0004      |           4 |
|      14 | 0x00B3      |         179 |
|      15 | 0x0005      |           5 |
|      16 | 0x00BD      |         189 |
|      17 | 0x0006      |           6 |
|      18 | 0x0007      |           7 |
|      19 | 0x00C7      |         199 |
|      20 | 0x0008      |           8 |
|      21 | 0x00D1      |         209 |
|      22 | 0x000D      |          13 |
|      23 | 0x1970B     |      104203 |
|      24 | 0xFFFCA2E6  |  4294746854 |
|      25 | 0x00CD      |         205 |
|      26 | 0x17D5E     |       97630 |
|      27 | 0xFFFC9C6C  |  4294745196 |
|      28 | 0x01BF      |         447 |
|      29 | 0x18D67     |      101735 |
|      30 | 0xFFFC9E9C  |  4294745756 |
|      31 | 0x0233      |         563 |
|      32 | 0x17F6D     |       98157 |
|      33 | 0xFFFCA59B  |  4294747547 |
|      34 | 0x0289      |         649 |
|      35 | 0x000A      |          10 |
|      36 | 0x0009      |           9 |
|      37 | 0x0046      |          70 |
|      38 | 0x008C      |         140 |
|      39 | 0x00D2      |         210 |

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

### Event 65534

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

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 02 10 07 7F 00                             ......        
```

#### Opcodes

```
  0: 0x0002 [0x03] Work_Zone[2] = Entity->Race
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          03 02 10 0B 7F 00                ......  
```

#### Opcodes

```
  0: 0x0008 [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            AB 03                ..
0010: AC 01 00 80 00                                    .....           
```

#### Opcodes

```
  0: 0x000E [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0010 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0015  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                AC 01 01  80 AB 04 00                   .......    
```

#### Opcodes

```
  0: 0x0015 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x0019 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      03 00 00 07              ....
0020: 7F 1A 61 02 66 01 00 F8  FF FF 7F F8 FF FF 7F 73  ..a.f..........s
0030: 68 61 30 53 F8 FF FF 7F  F8 FF FF 7F 73 68 61 30  ha0S........sha0
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x001C [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0021 [0x1A] CALL_SUBROUTINE(address=0x0261)
  2: 0x0024 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0033 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    03 00 00 07 7F 1A 61  02 66 01 00 F8 FF FF 7F   ......a.f......
0050: F8 FF FF 7F 73 68 61 31  53 F8 FF FF 7F F8 FF FF  ....sha1S.......
0060: 7F 73 68 61 31 00                                 .sha1.          
```

#### Opcodes

```
  0: 0x0041 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0046 [0x1A] CALL_SUBROUTINE(address=0x0261)
  2: 0x0049 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0058 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   32 02  80 1F 00 03 80 04 80 05        2.........
0070: 80 1F 01 1E 75 C1 10 01  7B F0 FF FF 7F 1C 06 80  ....u...{.......
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0066 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0069 [0x1F] MOVE_ENTITY: EventEntity moves to X=-422.900*, Z=-59.269*, Y=-19.669*
  2: 0x0071 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0073 [0x1E] EventEntity looks at Unnamed NPC (ID: 17875317/0x0110C175) and starts talking
  4: 0x0078 [0x7B] LocalPlayer stops talking
  5: 0x007D [0x1C] WAIT(30* ticks)
  6: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0081    |
| Data Size    | 366 bytes |
| Instructions | 43        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    02 03 10 01 80 05 8E  00 03 03 10 07 80 02 02   ...............
0090: 10 00 80 80 BA 00 66 08  80 F8 FF FF 7F F8 FF FF  ......f.........
00A0: 7F 74 6C 6B 30 1C 03 10  66 08 80 F8 FF FF 7F F8  .tlk0...f.......
00B0: FF FF 7F 74 6C 6B 31 01  EE 01 02 02 10 09 80 80  ...tlk1.........
00C0: E6 00 66 0A 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  ..f..........tlk
00D0: 30 1C 03 10 66 0A 80 F8  FF FF 7F F8 FF FF 7F 74  0...f..........t
00E0: 6C 6B 31 01 EE 01 02 02  10 0B 80 80 12 01 66 0C  lk1...........f.
00F0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1C 03 10  .........tlk0...
0100: 66 0C 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 01  f..........tlk1.
0110: EE 01 02 02 10 0D 80 80  3E 01 66 0E 80 F8 FF FF  ........>.f.....
0120: 7F F8 FF FF 7F 74 6C 6B  30 1C 03 10 66 0E 80 F8  .....tlk0...f...
0130: FF FF 7F F8 FF FF 7F 74  6C 6B 31 01 EE 01 02 02  .......tlk1.....
0140: 10 0F 80 80 6A 01 66 10  80 F8 FF FF 7F F8 FF FF  ....j.f.........
0150: 7F 74 6C 6B 30 1C 03 10  66 10 80 F8 FF FF 7F F8  .tlk0...f.......
0160: FF FF 7F 74 6C 6B 31 01  EE 01 02 02 10 11 80 80  ...tlk1.........
0170: 96 01 66 10 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  ..f..........tlk
0180: 30 1C 03 10 66 10 80 F8  FF FF 7F F8 FF FF 7F 74  0...f..........t
0190: 6C 6B 31 01 EE 01 02 02  10 12 80 80 C2 01 66 13  lk1...........f.
01A0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1C 03 10  .........tlk0...
01B0: 66 13 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 01  f..........tlk1.
01C0: EE 01 02 02 10 14 80 80  EE 01 66 15 80 F8 FF FF  ..........f.....
01D0: 7F F8 FF FF 7F 74 6C 6B  30 1C 03 10 66 15 80 F8  .....tlk0...f...
01E0: FF FF 7F F8 FF FF 7F 74  6C 6B 31 01 EE 01 00     .......tlk1.... 
```

#### Opcodes

```
  0: 0x0081 [0x02] IF !(Work_Zone[3] > 0*) GOTO 0x008E
  1: 0x0089 [0x03] Work_Zone[3] = 120*
  2: 0x008E [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x00BA
  3: 0x0096 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=149*
  4: 0x00A5 [0x1C] WAIT(Work_Zone[3] ticks)
  5: 0x00A8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=149*
  6: 0x00B7 [0x01] GOTO 0x01EE
  7: 0x00BA [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x00E6
  8: 0x00C2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=159*
  9: 0x00D1 [0x1C] WAIT(Work_Zone[3] ticks)
 10: 0x00D4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=159*
 11: 0x00E3 [0x01] GOTO 0x01EE
 12: 0x00E6 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x0112
 13: 0x00EE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=169*
 14: 0x00FD [0x1C] WAIT(Work_Zone[3] ticks)
 15: 0x0100 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=169*
 16: 0x010F [0x01] GOTO 0x01EE
 17: 0x0112 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x013E
 18: 0x011A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=179*
 19: 0x0129 [0x1C] WAIT(Work_Zone[3] ticks)
 20: 0x012C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=179*
 21: 0x013B [0x01] GOTO 0x01EE
 22: 0x013E [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x016A
 23: 0x0146 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=189*
 24: 0x0155 [0x1C] WAIT(Work_Zone[3] ticks)
 25: 0x0158 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=189*
 26: 0x0167 [0x01] GOTO 0x01EE
 27: 0x016A [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x0196
 28: 0x0172 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=189*
 29: 0x0181 [0x1C] WAIT(Work_Zone[3] ticks)
 30: 0x0184 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=189*
 31: 0x0193 [0x01] GOTO 0x01EE
 32: 0x0196 [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x01C2
 33: 0x019E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=199*
 34: 0x01AD [0x1C] WAIT(Work_Zone[3] ticks)
 35: 0x01B0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=199*
 36: 0x01BF [0x01] GOTO 0x01EE
 37: 0x01C2 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x01EE
 38: 0x01CA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=209*
 39: 0x01D9 [0x1C] WAIT(Work_Zone[3] ticks)
 40: 0x01DC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=209*
 41: 0x01EB [0x01] GOTO 0x01EE

SUBROUTINE_01EE:
 42: 0x01EE [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01EF   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                                               32                 2
01F0: 16 80 1F 00 17 80 18 80  19 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x01EF [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01F2 [0x1F] MOVE_ENTITY: EventEntity moves to X=104.203*, Z=-220.442*, Y=0.205*
  2: 0x01FA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01FC [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01FD   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                         32 02 80               2..
0200: 1F 00 1A 80 1B 80 1C 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x01FD [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0200 [0x1F] MOVE_ENTITY: EventEntity moves to X=97.630*, Z=-222.100*, Y=0.447*
  2: 0x0208 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x020A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x020B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                   32 16 80 1F 00             2....
0210: 1D 80 1E 80 1F 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x020B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x020E [0x1F] MOVE_ENTITY: EventEntity moves to X=101.735*, Z=-221.540*, Y=0.563*
  2: 0x0216 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0218 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0219   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                             32 16 80 1F 00 17 80           2......
0220: 18 80 19 80 1F 01 6F 1E  7B C1 10 01 00           ......o.{....   
```

#### Opcodes

```
  0: 0x0219 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x021C [0x1F] MOVE_ENTITY: EventEntity moves to X=104.203*, Z=-220.442*, Y=0.205*
  2: 0x0224 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0226 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0227 [0x1E] EventEntity looks at Midras (ID: 17875323/0x0110C17B) and starts talking
  5: 0x022C [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x022D   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                         32 16 80               2..
0230: 1E F8 FF FF 7F 1F 00 20  80 21 80 22 80 1F 01 00  ....... .!."....
```

#### Opcodes

```
  0: 0x022D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0230 [0x1E] EventEntity looks at EventEntity and starts talking
  2: 0x0235 [0x1F] MOVE_ENTITY: EventEntity moves to X=98.157*, Z=-219.749*, Y=0.649*
  3: 0x023D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x023F [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0240   |
| Data Size    | 29 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240: 03 00 00 07 7F 1A 86 02  07 01 00 00 80 66 01 00  .............f..
0250: F8 FF FF 7F F8 FF FF 7F  70 61 73 30 00           ........pas0.   
```

#### Opcodes

```
  0: 0x0240 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0245 [0x1A] CALL_SUBROUTINE(address=0x0286)
  2: 0x0248 [0x07] ExtData[1]->WorkLocal[1] += 1*
  3: 0x024D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  4: 0x025C [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x025D    |
| Data Size    | 152 bytes |
| Instructions | 2         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:                                         1C 00 17               ...
0260: 00 03 01 00 00 00 02 01  00 0F 80 05 76 02 08 01  ............v...
0270: 00 00 80 01 7B 02 08 01  00 09 80 14 01 00 23 80  ....{.........#.
0280: 07 01 00 24 80 1B 03 01  00 00 00 02 01 00 0F 80  ...$............
0290: 05 9B 02 08 01 00 00 80  01 A0 02 08 01 00 09 80  ................
02A0: 14 01 00 23 80 07 01 00  25 80 1B 03 01 00 00 00  ...#....%.......
02B0: 02 01 00 0F 80 05 C0 02  08 01 00 00 80 01 C5 02  ................
02C0: 08 01 00 09 80 14 01 00  23 80 07 01 00 26 80 1B  ........#....&..
02D0: 03 01 00 00 00 02 01 00  0F 80 05 E5 02 08 01 00  ................
02E0: 00 80 01 EA 02 08 01 00  09 80 14 01 00 23 80 07  .............#..
02F0: 01 00 27 80 1B                                    ..'..           
```

#### Opcodes

```
  0: 0x025D [0x1C] WAIT(Work_Zone_1700[0] ticks)
  1: 0x0260 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0261 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0266 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0276
     0x026E [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0273 [0x01] GOTO 0x027B
     0x0276 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x027B [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0280 [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x0285 [0x1B] RETURN
     0x0286 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x028B [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x029B
     0x0293 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0298 [0x01] GOTO 0x02A0
     0x029B [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x02A0 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x02A5 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x02AA [0x1B] RETURN
     0x02AB [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x02B0 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x02C0
     0x02B8 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x02BD [0x01] GOTO 0x02C5
     0x02C0 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x02C5 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x02CA [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x02CF [0x1B] RETURN
     0x02D0 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x02D5 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x02E5
     0x02DD [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x02E2 [0x01] GOTO 0x02EA
     0x02E5 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x02EA [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x02EF [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x02F4 [0x1B] RETURN
```
