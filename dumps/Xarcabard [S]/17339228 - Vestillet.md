# 17339228 - Vestillet

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 700 bytes               |
| Total Events     | 20                      |
| References Count | 35                      |

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
| [65535.8](#event-655358)   | 0x0044       |     29 |              6 |
| [65535.9](#event-655359)   | 0x0061       |     35 |              6 |
| [65535.10](#event-6553510) | 0x0084       |     29 |              6 |
| [23](#event-23)            | 0x00A1       |      1 |              1 |
| [39](#event-39)            | 0x00A2       |      1 |              1 |
| [18](#event-18)            | 0x00A3       |      1 |              1 |
| [65535.11](#event-6553511) | 0x00A4       |     37 |              5 |
| [65535.12](#event-6553512) | 0x00C9       |     37 |              5 |
| [41](#event-41)            | 0x00EE       |     27 |              3 |
| [65535.13](#event-6553513) | 0x0109       |     21 |              2 |
| [65535.14](#event-6553514) | 0x011E       |     14 |              4 |
| [65535.15](#event-6553515) | 0x012C       |    162 |             36 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFFD7772  |  4294801266 |
|       5 | 0xFFFF6DE2  |  4294929890 |
|       6 | 0xFFFFA462  |  4294943842 |
|       7 | 0xFFFD7F9B  |  4294803355 |
|       8 | 0xFFFF7919  |  4294932761 |
|       9 | 0xFFFFA295  |  4294943381 |
|      10 | 0x001D      |          29 |
|      11 | 0xFFFD8CC7  |  4294806727 |
|      12 | 0xFFFF7B4A  |  4294933322 |
|      13 | 0xFFFFA324  |  4294943524 |
|      14 | 0x0003      |           3 |
|      15 | 0x00DD      |         221 |
|      16 | 0x000C      |          12 |
|      17 | 0x00FB      |         251 |
|      18 | 0x001B      |          27 |
|      19 | 0x0002      |           2 |
|      20 | 0x00D9      |         217 |
|      21 | 0x00FA      |         250 |
|      22 | 0x0028      |          40 |
|      23 | 0xFFFDC279  |  4294820473 |
|      24 | 0xFFFFF24F  |  4294963791 |
|      25 | 0xFFFFC381  |  4294951809 |
|      26 | 0xFFFDAD83  |  4294815107 |
|      27 | 0xFFFFF1ED  |  4294963693 |
|      28 | 0xFFFFC23D  |  4294951485 |
|      29 | 0x0005      |           5 |
|      30 | 0x000A      |          10 |
|      31 | 0x0009      |           9 |
|      32 | 0x0046      |          70 |
|      33 | 0x008C      |         140 |
|      34 | 0x00D2      |         210 |

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

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             59 04 F8 FF  FF 7F 03 80 1F 00 04 80      Y...........
0050: 05 80 06 80 1F 01 6F 4A  F8 FF FF 7F 5A 93 08 01  ......oJ....Z...
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0044 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=-166.030*, Z=-37.406*, Y=-23.454*
  2: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0057 [0x4A] EventEntity looks at Ragelise (ID: 17339226/0x0108935A)
  5: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 35 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    59 04 F8 FF FF 7F 03  80 1F 00 07 80 08 80 09   Y..............
0070: 80 1F 01 6F 66 0A 80 F8  FF FF 7F F8 FF FF 7F 74  ...of..........t
0080: 77 62 30 00                                       wb0.            
```

#### Opcodes

```
  0: 0x0061 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x0069 [0x1F] MOVE_ENTITY: EventEntity moves to X=-163.941*, Z=-34.535*, Y=-23.915*
  2: 0x0071 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0073 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0074 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twb0" with entities [EventEntity, EventEntity], work=29*
  5: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             59 04 F8 FF  FF 7F 03 80 1F 00 0B 80      Y...........
0090: 0C 80 0D 80 1F 01 6F 4A  F8 FF FF 7F 5A 93 08 01  ......oJ....Z...
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0084 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x008C [0x1F] MOVE_ENTITY: EventEntity moves to X=-160.569*, Z=-33.974*, Y=-23.772*
  2: 0x0094 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0096 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0097 [0x4A] EventEntity looks at Ragelise (ID: 17339226/0x0108935A)
  5: 0x00A0 [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    00                                              .              
```

#### Opcodes

```
  0: 0x00A1 [0x00] END_REQSTACK()
```

### Event 39

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       00                                            .             
```

#### Opcodes

```
  0: 0x00A2 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          00                                          .            
```

#### Opcodes

```
  0: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             03 00 00 07  7F 1A 3A 01 66 01 00 F8      ......:.f...
00B0: FF FF 7F F8 FF FF 7F 73  68 61 30 53 F8 FF FF 7F  .......sha0S....
00C0: F8 FF FF 7F 73 68 61 30  00                       ....sha0.       
```

#### Opcodes

```
  0: 0x00A4 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x00A9 [0x1A] CALL_SUBROUTINE(address=0x013A)
  2: 0x00AC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x00BB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             03 00 00 07 7F 1A 3A           ......:
00D0: 01 66 01 00 F8 FF FF 7F  F8 FF FF 7F 73 68 61 31  .f..........sha1
00E0: 53 F8 FF FF 7F F8 FF FF  7F 73 68 61 31 00        S........sha1.  
```

#### Opcodes

```
  0: 0x00C9 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x00CE [0x1A] CALL_SUBROUTINE(address=0x013A)
  2: 0x00D1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x00E0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x00ED [0x00] END_REQSTACK()
```

### Event 41

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EE   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                            92 01                ..
00F0: F8 FF FF 7F B6 0B 0E 80  03 80 03 80 0F 80 03 80  ................
0100: 10 80 0F 80 11 80 12 80  00                       .........       
```

#### Opcodes

```
  0: 0x00EE [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00F4 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=13*, head=13*, body=221*, hands=13*, legs=12*, feet=221*, main=251*, sub=27*)
  2: 0x0108 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0109   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                             B6 0B 0E 80 13 80 00           .......
0110: 80 14 80 03 80 10 80 0F  80 15 80 12 80 00        ..............  
```

#### Opcodes

```
  0: 0x0109 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=0*, body=217*, hands=13*, legs=12*, feet=221*, main=250*, sub=27*)
  1: 0x011D [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                            32 16                2.
0120: 80 1F 00 17 80 18 80 19  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x011E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0121 [0x1F] MOVE_ENTITY: EventEntity moves to X=-146.823*, Z=-3.505*, Y=-15.487*
  2: 0x0129 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x012B [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x012C    |
| Data Size    | 162 bytes |
| Instructions | 4         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                      32 16 80 1F              2...
0130: 00 1A 80 1B 80 1C 80 1F  01 00 03 01 00 00 00 02  ................
0140: 01 00 1D 80 05 4F 01 08  01 00 01 80 01 54 01 08  .....O.......T..
0150: 01 00 13 80 14 01 00 1E  80 07 01 00 1F 80 1B 03  ................
0160: 01 00 00 00 02 01 00 1D  80 05 74 01 08 01 00 01  ..........t.....
0170: 80 01 79 01 08 01 00 13  80 14 01 00 1E 80 07 01  ..y.............
0180: 00 20 80 1B 03 01 00 00  00 02 01 00 1D 80 05 99  . ..............
0190: 01 08 01 00 01 80 01 9E  01 08 01 00 13 80 14 01  ................
01A0: 00 1E 80 07 01 00 21 80  1B 03 01 00 00 00 02 01  ......!.........
01B0: 00 1D 80 05 BE 01 08 01  00 01 80 01 C3 01 08 01  ................
01C0: 00 13 80 14 01 00 1E 80  07 01 00 22 80 1B        ..........."..  
```

#### Opcodes

```
  0: 0x012C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x012F [0x1F] MOVE_ENTITY: EventEntity moves to X=-152.189*, Z=-3.603*, Y=-15.811*
  2: 0x0137 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0139 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x013A [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x013F [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x014F
     0x0147 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x014C [0x01] GOTO 0x0154
     0x014F [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0154 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0159 [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x015E [0x1B] RETURN
     0x015F [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0164 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0174
     0x016C [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0171 [0x01] GOTO 0x0179
     0x0174 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0179 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x017E [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x0183 [0x1B] RETURN
     0x0184 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0189 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0199
     0x0191 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0196 [0x01] GOTO 0x019E
     0x0199 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x019E [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x01A3 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x01A8 [0x1B] RETURN
     0x01A9 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x01AE [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x01BE
     0x01B6 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x01BB [0x01] GOTO 0x01C3
     0x01BE [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x01C3 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x01C8 [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x01CD [0x1B] RETURN
```
