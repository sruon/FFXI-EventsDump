# 17199775 - Kuchi Eyjhann

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Valkurm Dunes (ID: 103) |
| Block Size       | 644 bytes               |
| Total Events     | 19                      |
| References Count | 20                      |

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
| [56](#event-56)            | 0x0044       |      1 |              1 |
| [57](#event-57)            | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     25 |              3 |
| [65535.9](#event-655359)   | 0x005F       |     25 |              3 |
| [65535.10](#event-6553510) | 0x0078       |     37 |              5 |
| [65535.11](#event-6553511) | 0x009D       |    185 |             37 |
| [65535.12](#event-6553512) | 0x0156       |     15 |              5 |
| [65535.13](#event-6553513) | 0x0165       |     20 |              6 |
| [65535.14](#event-6553514) | 0x0179       |     37 |              5 |
| [65535.15](#event-6553515) | 0x019E       |     37 |              5 |
| [65535.16](#event-6553516) | 0x01C3       |     20 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0005      |           5 |
|       4 | 0x0002      |           2 |
|       5 | 0x000A      |          10 |
|       6 | 0x0009      |           9 |
|       7 | 0x0046      |          70 |
|       8 | 0x008C      |         140 |
|       9 | 0x00D2      |         210 |
|      10 | 0x0028      |          40 |
|      11 | 0x5895E     |      362846 |
|      12 | 0xFFFE13CC  |  4294841292 |
|      13 | 0x0094      |         148 |
|      14 | 0x000B      |          11 |
|      15 | 0x58A2D     |      363053 |
|      16 | 0xFFFE20C3  |  4294844611 |
|      17 | 0x59407     |      365575 |
|      18 | 0xFFFE2670  |  4294846064 |
|      19 | 0xFFFFFF88  |  4294967176 |

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

### Event 56

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

### Event 57

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   B4 00  00 00 3F 3F 3F 00 00 00        ....???...
0050: 00 00 00 00 00 00 00 00  00 00 B5 00 00 00 00     ............... 
```

#### Opcodes

```
  0: 0x0046 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="???")
  1: 0x005A [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               B4                 .
0060: 13 00 00 4B 75 63 68 69  40 45 79 6A 68 61 6E 6E  ...Kuchi@Eyjhann
0070: 00 00 00 B5 00 00 00 00                           ........        
```

#### Opcodes

```
  0: 0x005F [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="Kuchi@Eyjhann")
  1: 0x0073 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          03 01 00 07 7F 1A C2 00          ........
0080: 66 02 00 F8 FF FF 7F F8  FF FF 7F 73 68 61 30 53  f..........sha0S
0090: F8 FF FF 7F F8 FF FF 7F  73 68 61 30 00           ........sha0.   
```

#### Opcodes

```
  0: 0x0078 [0x03] ExtData[1]->WorkLocal[1] = Entity->Race
  1: 0x007D [0x1A] CALL_SUBROUTINE(address=0x00C2)
  2: 0x0080 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  3: 0x008F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x009D    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         03 01 00               ...
00A0: 07 7F 1A C2 00 66 02 00  F8 FF FF 7F F8 FF FF 7F  .....f..........
00B0: 73 68 61 31 53 F8 FF FF  7F F8 FF FF 7F 73 68 61  sha1S........sha
00C0: 31 00 03 02 00 01 00 02  02 00 03 80 05 D7 00 08  1...............
00D0: 02 00 01 80 01 DC 00 08  02 00 04 80 14 02 00 05  ................
00E0: 80 07 02 00 06 80 1B 03  02 00 01 00 02 02 00 03  ................
00F0: 80 05 FC 00 08 02 00 01  80 01 01 01 08 02 00 04  ................
0100: 80 14 02 00 05 80 07 02  00 07 80 1B 03 02 00 01  ................
0110: 00 02 02 00 03 80 05 21  01 08 02 00 01 80 01 26  .......!.......&
0120: 01 08 02 00 04 80 14 02  00 05 80 07 02 00 08 80  ................
0130: 1B 03 02 00 01 00 02 02  00 03 80 05 46 01 08 02  ............F...
0140: 00 01 80 01 4B 01 08 02  00 04 80 14 02 00 05 80  ....K...........
0150: 07 02 00 09 80 1B                                 ......          
```

#### Opcodes

```
  0: 0x009D [0x03] ExtData[1]->WorkLocal[1] = Entity->Race
  1: 0x00A2 [0x1A] CALL_SUBROUTINE(address=0x00C2)
  2: 0x00A5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  3: 0x00B4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x00C1 [0x00] END_REQSTACK()

SUBROUTINE_00C2:
  5: 0x00C2 [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[1]
  6: 0x00C7 [0x02] IF !(ExtData[1]->WorkLocal[2] > 5*) GOTO 0x00D7
  7: 0x00CF [0x08] ExtData[1]->WorkLocal[2] -= 1*
  8: 0x00D4 [0x01] GOTO 0x00DC
  9: 0x00D7 [0x08] ExtData[1]->WorkLocal[2] -= 2*

SUBROUTINE_00DC:
 10: 0x00DC [0x14] ExtData[1]->WorkLocal[2] *= 10*
 11: 0x00E1 [0x07] ExtData[1]->WorkLocal[2] += 9*
 12: 0x00E6 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00E7 [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[1]
     0x00EC [0x02] IF !(ExtData[1]->WorkLocal[2] > 5*) GOTO 0x00FC
     0x00F4 [0x08] ExtData[1]->WorkLocal[2] -= 1*
     0x00F9 [0x01] GOTO 0x0101
     0x00FC [0x08] ExtData[1]->WorkLocal[2] -= 2*
     0x0101 [0x14] ExtData[1]->WorkLocal[2] *= 10*
     0x0106 [0x07] ExtData[1]->WorkLocal[2] += 70*
     0x010B [0x1B] RETURN
     0x010C [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[1]
     0x0111 [0x02] IF !(ExtData[1]->WorkLocal[2] > 5*) GOTO 0x0121
     0x0119 [0x08] ExtData[1]->WorkLocal[2] -= 1*
     0x011E [0x01] GOTO 0x0126
     0x0121 [0x08] ExtData[1]->WorkLocal[2] -= 2*
     0x0126 [0x14] ExtData[1]->WorkLocal[2] *= 10*
     0x012B [0x07] ExtData[1]->WorkLocal[2] += 140*
     0x0130 [0x1B] RETURN
     0x0131 [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[1]
     0x0136 [0x02] IF !(ExtData[1]->WorkLocal[2] > 5*) GOTO 0x0146
     0x013E [0x08] ExtData[1]->WorkLocal[2] -= 1*
     0x0143 [0x01] GOTO 0x014B
     0x0146 [0x08] ExtData[1]->WorkLocal[2] -= 2*
     0x014B [0x14] ExtData[1]->WorkLocal[2] *= 10*
     0x0150 [0x07] ExtData[1]->WorkLocal[2] += 210*
     0x0155 [0x1B] RETURN
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0156   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   32 0A  80 1F 00 0B 80 0C 80 0D        2.........
0160: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0156 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0159 [0x1F] MOVE_ENTITY: EventEntity moves to X=362.846*, Z=-126.004*, Y=0.148*
  2: 0x0161 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0163 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0164 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0165   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                32 0E 80  1F 00 0F 80 10 80 00 80       2..........
0170: 1F 01 6F 1E F0 FF FF 7F  00                       ..o......       
```

#### Opcodes

```
  0: 0x0165 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0168 [0x1F] MOVE_ENTITY: EventEntity moves to X=363.053*, Z=-122.685*, Y=0.000*
  2: 0x0170 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0172 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0173 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0178 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0179   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                             03 01 00 07 7F 1A C2           .......
0180: 00 66 02 00 F8 FF FF 7F  F8 FF FF 7F 73 69 74 30  .f..........sit0
0190: 53 F8 FF FF 7F F8 FF FF  7F 73 69 74 30 00        S........sit0.  
```

#### Opcodes

```
  0: 0x0179 [0x03] ExtData[1]->WorkLocal[1] = Entity->Race
  1: 0x017E [0x1A] CALL_SUBROUTINE(address=0x00C2)
  2: 0x0181 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  3: 0x0190 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit0" with entities [EventEntity, EventEntity]
  4: 0x019D [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019E   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                            03 01                ..
01A0: 00 07 7F 1A C2 00 66 02  00 F8 FF FF 7F F8 FF FF  ......f.........
01B0: 7F 73 69 74 31 53 F8 FF  FF 7F F8 FF FF 7F 73 69  .sit1S........si
01C0: 74 31 00                                          t1.             
```

#### Opcodes

```
  0: 0x019E [0x03] ExtData[1]->WorkLocal[1] = Entity->Race
  1: 0x01A3 [0x1A] CALL_SUBROUTINE(address=0x00C2)
  2: 0x01A6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  3: 0x01B5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit1" with entities [EventEntity, EventEntity]
  4: 0x01C2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C3   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:          32 0A 80 1F 00  11 80 12 80 13 80 1F 01     2............
01D0: 6F 1E F0 FF FF 7F 00                              o......         
```

#### Opcodes

```
  0: 0x01C3 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x01C6 [0x1F] MOVE_ENTITY: EventEntity moves to X=365.575*, Z=-121.232*, Y=-0.120*
  2: 0x01CE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01D0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01D1 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x01D6 [0x00] END_REQSTACK()
```
