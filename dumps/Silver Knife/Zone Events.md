# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Silver Knife (ID: 283) |
| Block Size       | 992 bytes              |
| Total Events     | 14                     |
| References Count | 36                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |      6 |              2 |
| [65535.2](#event-655352)   | 0x0008       |     24 |              4 |
| [65535.3](#event-655353)   | 0x0020       |     24 |              4 |
| [65535.4](#event-655354)   | 0x0038       |     22 |              8 |
| [65535.5](#event-655355)   | 0x004E       |     14 |              4 |
| [65535.6](#event-655356)   | 0x005C       |     15 |              5 |
| [65535.7](#event-655357)   | 0x006B       |     15 |              5 |
| [65535.8](#event-655358)   | 0x007A       |     22 |              8 |
| [65535.9](#event-655359)   | 0x0090       |     15 |              5 |
| [65535.10](#event-6553510) | 0x009F       |    170 |             40 |
| [65535.11](#event-6553511) | 0x0149       |    222 |             26 |
| [65535.12](#event-6553512) | 0x0227       |    222 |             26 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFF65F4  |  4294927860 |
|       2 | 0x74D0      |       29904 |
|       3 | 0x053A      |        1338 |
|       4 | 0xFFFF7B8C  |  4294933388 |
|       5 | 0x618D      |       24973 |
|       6 | 0x053C      |        1340 |
|       7 | 0x0000      |           0 |
|       8 | 0x0190      |         400 |
|       9 | 0x07D0      |        2000 |
|      10 | 0x0700      |        1792 |
|      11 | 0x0579      |        1401 |
|      12 | 0xFFFFFACA  |  4294965962 |
|      13 | 0xFFFF53B5  |  4294923189 |
|      14 | 0x868B      |       34443 |
|      15 | 0x0545      |        1349 |
|      16 | 0x0005      |           5 |
|      17 | 0x0001      |           1 |
|      18 | 0x0002      |           2 |
|      19 | 0x000A      |          10 |
|      20 | 0x0009      |           9 |
|      21 | 0x0046      |          70 |
|      22 | 0x008C      |         140 |
|      23 | 0x00D2      |         210 |
|      24 | 0x0095      |         149 |
|      25 | 0x009F      |         159 |
|      26 | 0x0003      |           3 |
|      27 | 0x00A9      |         169 |
|      28 | 0x0004      |           4 |
|      29 | 0x00B3      |         179 |
|      30 | 0x00BD      |         189 |
|      31 | 0x0006      |           6 |
|      32 | 0x0007      |           7 |
|      33 | 0x00C7      |         199 |
|      34 | 0x0008      |           8 |
|      35 | 0x00D1      |         209 |

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
0000:       03 09 10 07 7F 00                             ......        
```

#### Opcodes

```
  0: 0x0002 [0x03] Work_Zone[9] = Entity->Race
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          03 00 00 07 7F 1A B5 00          ........
0010: 66 01 00 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 00  f..........tlk0.
```

#### Opcodes

```
  0: 0x0008 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x000D [0x1A] CALL_SUBROUTINE(address=0x00B5)
  2: 0x0010 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 03 00 00 07 7F 1A B5 00  66 01 00 F8 FF FF 7F F8  ........f.......
0030: FF FF 7F 74 6C 6B 31 00                           ...tlk1.        
```

#### Opcodes

```
  0: 0x0020 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0025 [0x1A] CALL_SUBROUTINE(address=0x00B5)
  2: 0x0028 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          32 00 80 1F 00 01 80 02          2.......
0040: 80 03 80 1F 01 6F 1E 1E  B0 11 01 6F 70 00        .....o.....op.  
```

#### Opcodes

```
  0: 0x0038 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=-39.436*, Z=29.904*, Y=1.338*
  2: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0045 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0046 [0x1E] EventEntity looks at Rabid Chameleon (ID: 17936414/0x0111B01E) and starts talking
  5: 0x004B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x004C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            32 00                2.
0050: 80 1F 00 04 80 05 80 06  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x004E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=-33.908*, Z=24.973*, Y=1.340*
  2: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      32 00 80 1F              2...
0060: 00 07 80 08 80 07 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x005C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=0.400*, Y=0.000*
  2: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0069 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   32 00 80 1F 00             2....
0070: 07 80 09 80 07 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x006B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006E [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=2.000*, Y=0.000*
  2: 0x0076 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0078 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                32 00 80 1F 00 0A            2.....
0080: 80 0B 80 07 80 1F 01 6F  1E 1A B0 11 01 6F 70 00  .......o.....op.
```

#### Opcodes

```
  0: 0x007A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007D [0x1F] MOVE_ENTITY: EventEntity moves to X=1.792*, Z=1.401*, Y=0.000*
  2: 0x0085 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0087 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0088 [0x1E] EventEntity looks at Skhoh Undhreh (ID: 17936410/0x0111B01A) and starts talking
  5: 0x008D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x008E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 32 00 80 1F 00 07 80 0C  80 07 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0090 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0093 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=-1.334*, Y=0.000*
  2: 0x009B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x009F    |
| Data Size    | 170 bytes |
| Instructions | 8         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               32                 2
00A0: 00 80 1F 00 0D 80 0E 80  0F 80 1F 01 6F 1E 19 B0  ............o...
00B0: 11 01 6F 70 00 03 01 00  00 00 02 01 00 10 80 05  ..op............
00C0: CA 00 08 01 00 11 80 01  CF 00 08 01 00 12 80 14  ................
00D0: 01 00 13 80 07 01 00 14  80 1B 03 01 00 00 00 02  ................
00E0: 01 00 10 80 05 EF 00 08  01 00 11 80 01 F4 00 08  ................
00F0: 01 00 12 80 14 01 00 13  80 07 01 00 15 80 1B 03  ................
0100: 01 00 00 00 02 01 00 10  80 05 14 01 08 01 00 11  ................
0110: 80 01 19 01 08 01 00 12  80 14 01 00 13 80 07 01  ................
0120: 00 16 80 1B 03 01 00 00  00 02 01 00 10 80 05 39  ...............9
0130: 01 08 01 00 11 80 01 3E  01 08 01 00 12 80 14 01  .......>........
0140: 00 13 80 07 01 00 17 80  1B                       .........       
```

#### Opcodes

```
  0: 0x009F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-44.107*, Z=34.443*, Y=1.349*
  2: 0x00AA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AD [0x1E] EventEntity looks at Oshasha (ID: 17936409/0x0111B019) and starts talking
  5: 0x00B2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00B3 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x00B4 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00B5 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00BA [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00CA
     0x00C2 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00C7 [0x01] GOTO 0x00CF
     0x00CA [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00CF [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00D4 [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x00D9 [0x1B] RETURN
     0x00DA [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00DF [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00EF
     0x00E7 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00EC [0x01] GOTO 0x00F4
     0x00EF [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00F4 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00F9 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x00FE [0x1B] RETURN
     0x00FF [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0104 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0114
     0x010C [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0111 [0x01] GOTO 0x0119
     0x0114 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0119 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x011E [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x0123 [0x1B] RETURN
     0x0124 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0129 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0139
     0x0131 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0136 [0x01] GOTO 0x013E
     0x0139 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x013E [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0143 [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x0148 [0x1B] RETURN
```

### Event 65535.11

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0149    |
| Data Size    | 222 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                             02 07 7F 11 80 80 63           ......c
0150: 01 66 18 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .f..........tlk0
0160: 01 19 02 02 07 7F 12 80  80 7D 01 66 19 80 F8 FF  .........}.f....
0170: FF 7F F8 FF FF 7F 74 6C  6B 30 01 19 02 02 07 7F  ......tlk0......
0180: 1A 80 80 97 01 66 1B 80  F8 FF FF 7F F8 FF FF 7F  .....f..........
0190: 74 6C 6B 30 01 19 02 02  07 7F 1C 80 80 B1 01 66  tlk0...........f
01A0: 1D 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 01 19  ..........tlk0..
01B0: 02 02 07 7F 10 80 80 CB  01 66 1E 80 F8 FF FF 7F  .........f......
01C0: F8 FF FF 7F 74 6C 6B 30  01 19 02 02 07 7F 1F 80  ....tlk0........
01D0: 80 E5 01 66 1E 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ...f..........tl
01E0: 6B 30 01 19 02 02 07 7F  20 80 80 FF 01 66 21 80  k0...... ....f!.
01F0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 01 19 02 02  ........tlk0....
0200: 07 7F 22 80 80 19 02 66  23 80 F8 FF FF 7F F8 FF  .."....f#.......
0210: FF 7F 74 6C 6B 30 01 19  02 53 F8 FF FF 7F F8 FF  ..tlk0...S......
0220: FF 7F 74 6C 6B 30 00                              ..tlk0.         
```

#### Opcodes

```
  0: 0x0149 [0x02] IF !(Entity->Race == 1*) GOTO 0x0163
  1: 0x0151 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=149*
  2: 0x0160 [0x01] GOTO 0x0219
  3: 0x0163 [0x02] IF !(Entity->Race == 2*) GOTO 0x017D
  4: 0x016B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=159*
  5: 0x017A [0x01] GOTO 0x0219
  6: 0x017D [0x02] IF !(Entity->Race == 3*) GOTO 0x0197
  7: 0x0185 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=169*
  8: 0x0194 [0x01] GOTO 0x0219
  9: 0x0197 [0x02] IF !(Entity->Race == 4*) GOTO 0x01B1
 10: 0x019F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=179*
 11: 0x01AE [0x01] GOTO 0x0219
 12: 0x01B1 [0x02] IF !(Entity->Race == 5*) GOTO 0x01CB
 13: 0x01B9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=189*
 14: 0x01C8 [0x01] GOTO 0x0219
 15: 0x01CB [0x02] IF !(Entity->Race == 6*) GOTO 0x01E5
 16: 0x01D3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=189*
 17: 0x01E2 [0x01] GOTO 0x0219
 18: 0x01E5 [0x02] IF !(Entity->Race == 7*) GOTO 0x01FF
 19: 0x01ED [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=199*
 20: 0x01FC [0x01] GOTO 0x0219
 21: 0x01FF [0x02] IF !(Entity->Race == 8*) GOTO 0x0219
 22: 0x0207 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=209*
 23: 0x0216 [0x01] GOTO 0x0219

SUBROUTINE_0219:
 24: 0x0219 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 25: 0x0226 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0227    |
| Data Size    | 222 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                      02  07 7F 11 80 80 41 02 66         ......A.f
0230: 18 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 01 F7  ..........tlk1..
0240: 02 02 07 7F 12 80 80 5B  02 66 19 80 F8 FF FF 7F  .......[.f......
0250: F8 FF FF 7F 74 6C 6B 31  01 F7 02 02 07 7F 1A 80  ....tlk1........
0260: 80 75 02 66 1B 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .u.f..........tl
0270: 6B 31 01 F7 02 02 07 7F  1C 80 80 8F 02 66 1D 80  k1...........f..
0280: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 01 F7 02 02  ........tlk1....
0290: 07 7F 10 80 80 A9 02 66  1E 80 F8 FF FF 7F F8 FF  .......f........
02A0: FF 7F 74 6C 6B 31 01 F7  02 02 07 7F 1F 80 80 C3  ..tlk1..........
02B0: 02 66 1E 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 31  .f..........tlk1
02C0: 01 F7 02 02 07 7F 20 80  80 DD 02 66 21 80 F8 FF  ...... ....f!...
02D0: FF 7F F8 FF FF 7F 74 6C  6B 31 01 F7 02 02 07 7F  ......tlk1......
02E0: 22 80 80 F7 02 66 23 80  F8 FF FF 7F F8 FF FF 7F  "....f#.........
02F0: 74 6C 6B 31 01 F7 02 53  F8 FF FF 7F F8 FF FF 7F  tlk1...S........
0300: 74 6C 6B 31 00                                    tlk1.           
```

#### Opcodes

```
  0: 0x0227 [0x02] IF !(Entity->Race == 1*) GOTO 0x0241
  1: 0x022F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=149*
  2: 0x023E [0x01] GOTO 0x02F7
  3: 0x0241 [0x02] IF !(Entity->Race == 2*) GOTO 0x025B
  4: 0x0249 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=159*
  5: 0x0258 [0x01] GOTO 0x02F7
  6: 0x025B [0x02] IF !(Entity->Race == 3*) GOTO 0x0275
  7: 0x0263 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=169*
  8: 0x0272 [0x01] GOTO 0x02F7
  9: 0x0275 [0x02] IF !(Entity->Race == 4*) GOTO 0x028F
 10: 0x027D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=179*
 11: 0x028C [0x01] GOTO 0x02F7
 12: 0x028F [0x02] IF !(Entity->Race == 5*) GOTO 0x02A9
 13: 0x0297 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=189*
 14: 0x02A6 [0x01] GOTO 0x02F7
 15: 0x02A9 [0x02] IF !(Entity->Race == 6*) GOTO 0x02C3
 16: 0x02B1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=189*
 17: 0x02C0 [0x01] GOTO 0x02F7
 18: 0x02C3 [0x02] IF !(Entity->Race == 7*) GOTO 0x02DD
 19: 0x02CB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=199*
 20: 0x02DA [0x01] GOTO 0x02F7
 21: 0x02DD [0x02] IF !(Entity->Race == 8*) GOTO 0x02F7
 22: 0x02E5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=209*
 23: 0x02F4 [0x01] GOTO 0x02F7

SUBROUTINE_02F7:
 24: 0x02F7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 25: 0x0304 [0x00] END_REQSTACK()
```
