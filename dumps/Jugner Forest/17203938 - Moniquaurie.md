# 17203938 - Moniquaurie

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Jugner Forest (ID: 104) |
| Block Size       | 628 bytes               |
| Total Events     | 19                      |
| References Count | 26                      |

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
| [48](#event-48)            | 0x0044       |      1 |              1 |
| [49](#event-49)            | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     25 |              3 |
| [65535.9](#event-655359)   | 0x005F       |     25 |              3 |
| [65535.10](#event-6553510) | 0x0078       |     37 |              5 |
| [65535.11](#event-6553511) | 0x009D       |    185 |             37 |
| [65535.12](#event-6553512) | 0x0156       |     15 |              5 |
| [65535.13](#event-6553513) | 0x0165       |     25 |              6 |
| [65535.14](#event-6553514) | 0x017E       |     15 |              5 |
| [65535.15](#event-6553515) | 0x018D       |     20 |              6 |
| [65535.16](#event-6553516) | 0x01A1       |     15 |              5 |

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
|      10 | 0x000D      |          13 |
|      11 | 0x395A9     |      234921 |
|      12 | 0x23D0      |        9168 |
|      13 | 0x010E      |         270 |
|      14 | 0x3A92D     |      239917 |
|      15 | 0x1F53      |        8019 |
|      16 | 0x00C7      |         199 |
|      17 | 0x000B      |          11 |
|      18 | 0x3A7BB     |      239547 |
|      19 | 0x249B      |        9371 |
|      20 | 0x010A      |         266 |
|      21 | 0x3AD7B     |      241019 |
|      22 | 0x2021      |        8225 |
|      23 | 0x00D1      |         209 |
|      24 | 0x3A748     |      239432 |
|      25 | 0x24E2      |        9442 |

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

### Event 48

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

### Event 49

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
0060: 00 00 00 4D 6F 6E 69 71  75 61 75 72 69 65 00 00  ...Moniquaurie..
0070: 00 00 00 B5 00 00 00 00                           ........        
```

#### Opcodes

```
  0: 0x005F [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Moniquaurie")
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
  0: 0x0156 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0159 [0x1F] MOVE_ENTITY: EventEntity moves to X=234.921*, Z=9.168*, Y=0.270*
  2: 0x0161 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0163 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0164 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0165   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                79 00 F8  FF FF 7F E0 82 06 01 32       y.........2
0170: 0A 80 1F 00 0E 80 0F 80  10 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x0165 [0x79] EventEntity looks at Cavernous Maw (ID: 17203936/0x010682E0) (Basic look)
  1: 0x016F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0172 [0x1F] MOVE_ENTITY: EventEntity moves to X=239.917*, Z=8.019*, Y=0.199*
  3: 0x017A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x017C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x017D [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                            32 11                2.
0180: 80 1F 00 12 80 13 80 14  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x017E [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0181 [0x1F] MOVE_ENTITY: EventEntity moves to X=239.547*, Z=9.371*, Y=0.266*
  2: 0x0189 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x018B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x018C [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018D   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                         32 0A 80               2..
0190: 1F 00 15 80 16 80 17 80  1F 01 6F 1E F0 FF FF 7F  ..........o.....
01A0: 00                                                .               
```

#### Opcodes

```
  0: 0x018D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0190 [0x1F] MOVE_ENTITY: EventEntity moves to X=241.019*, Z=8.225*, Y=0.209*
  2: 0x0198 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x019A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x019B [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x01A0 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A1   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:    32 11 80 1F 00 18 80  19 80 0D 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x01A1 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x01A4 [0x1F] MOVE_ENTITY: EventEntity moves to X=239.432*, Z=9.442*, Y=0.270*
  2: 0x01AC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01AE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01AF [0x00] END_REQSTACK()
```
