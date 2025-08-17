# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Woh Gates (ID: 273) |
| Block Size       | 752 bytes           |
| Total Events     | 15                  |
| References Count | 31                  |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     37 |              5 |
| [65535.2](#event-655352)   | 0x0027       |    185 |             37 |
| [65535.3](#event-655353)   | 0x00E0       |     22 |              6 |
| [65535.4](#event-655354)   | 0x00F6       |     14 |              4 |
| [65535.5](#event-655355)   | 0x0104       |     14 |              4 |
| [65535.6](#event-655356)   | 0x0112       |     24 |              4 |
| [65535.7](#event-655357)   | 0x012A       |     24 |              4 |
| [65535.8](#event-655358)   | 0x0142       |     38 |              5 |
| [65535.9](#event-655359)   | 0x0168       |     38 |              5 |
| [65535.10](#event-6553510) | 0x018E       |     38 |              5 |
| [65535.11](#event-6553511) | 0x01B4       |     37 |              5 |
| [65535.12](#event-6553512) | 0x01D9       |     37 |              5 |
| [65535.13](#event-6553513) | 0x01FE       |     42 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0005      |           5 |
|       1 | 0x0001      |           1 |
|       2 | 0x0002      |           2 |
|       3 | 0x000A      |          10 |
|       4 | 0x0009      |           9 |
|       5 | 0x0046      |          70 |
|       6 | 0x008C      |         140 |
|       7 | 0x00D2      |         210 |
|       8 | 0x000D      |          13 |
|       9 | 0x7061A     |      460314 |
|      10 | 0x28BA6     |      166822 |
|      11 | 0x29C7      |       10695 |
|      12 | 0x001E      |          30 |
|      13 | 0x0028      |          40 |
|      14 | 0xFFFF1EFD  |  4294909693 |
|      15 | 0x32B1D     |      207645 |
|      16 | 0x763C      |       30268 |
|      17 | 0xFFFF40A3  |  4294918307 |
|      18 | 0x34787     |      214919 |
|      19 | 0x7723      |       30499 |
|      20 | 0x0008      |           8 |
|      21 | 0x0007      |           7 |
|      22 | 0x0091      |         145 |
|      23 | 0x004F      |          79 |
|      24 | 0x004C      |          76 |
|      25 | 0x00C9      |         201 |
|      26 | 0x0018      |          24 |
|      27 | 0x0020      |          32 |
|      28 | 0x0030      |          48 |
|      29 | 0x0040      |          64 |
|      30 | 0x003C      |          60 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 00 00 07 7F 1A  4C 00 66 01 00 F8 FF FF    ......L.f.....
0010: 7F F8 FF FF 7F 73 68 61  30 53 F8 FF FF 7F F8 FF  .....sha0S......
0020: FF 7F 73 68 61 30 00                              ..sha0.         
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0007 [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0019 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0027    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      03  00 00 07 7F 1A 4C 00 66         ......L.f
0030: 01 00 F8 FF FF 7F F8 FF  FF 7F 73 68 61 31 53 F8  ..........sha1S.
0040: FF FF 7F F8 FF FF 7F 73  68 61 31 00 03 01 00 00  .......sha1.....
0050: 00 02 01 00 00 80 05 61  00 08 01 00 01 80 01 66  .......a.......f
0060: 00 08 01 00 02 80 14 01  00 03 80 07 01 00 04 80  ................
0070: 1B 03 01 00 00 00 02 01  00 00 80 05 86 00 08 01  ................
0080: 00 01 80 01 8B 00 08 01  00 02 80 14 01 00 03 80  ................
0090: 07 01 00 05 80 1B 03 01  00 00 00 02 01 00 00 80  ................
00A0: 05 AB 00 08 01 00 01 80  01 B0 00 08 01 00 02 80  ................
00B0: 14 01 00 03 80 07 01 00  06 80 1B 03 01 00 00 00  ................
00C0: 02 01 00 00 80 05 D0 00  08 01 00 01 80 01 D5 00  ................
00D0: 08 01 00 02 80 14 01 00  03 80 07 01 00 07 80 1B  ................
```

#### Opcodes

```
  0: 0x0027 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x002C [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x002F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x003E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x004B [0x00] END_REQSTACK()

SUBROUTINE_004C:
  5: 0x004C [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  6: 0x0051 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0061
  7: 0x0059 [0x08] ExtData[1]->WorkLocal[1] -= 1*
  8: 0x005E [0x01] GOTO 0x0066
  9: 0x0061 [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_0066:
 10: 0x0066 [0x14] ExtData[1]->WorkLocal[1] *= 10*
 11: 0x006B [0x07] ExtData[1]->WorkLocal[1] += 9*
 12: 0x0070 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0071 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0076 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0086
     0x007E [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0083 [0x01] GOTO 0x008B
     0x0086 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x008B [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0090 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x0095 [0x1B] RETURN
     0x0096 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x009B [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00AB
     0x00A3 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00A8 [0x01] GOTO 0x00B0
     0x00AB [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00B0 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00B5 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x00BA [0x1B] RETURN
     0x00BB [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00C0 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00D0
     0x00C8 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00CD [0x01] GOTO 0x00D5
     0x00D0 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00D5 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00DA [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x00DF [0x1B] RETURN
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E0   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 32 08 80 1F 00 09 80 0A  80 0B 80 1F 01 1E CB 11  2...............
00F0: 11 01 1C 0C 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00E0 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00E3 [0x1F] MOVE_ENTITY: EventEntity moves to X=460.314*, Z=166.822*, Y=10.695*
  2: 0x00EB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00ED [0x1E] EventEntity looks at Arciela (ID: 17895883/0x011111CB) and starts talking
  4: 0x00F2 [0x1C] WAIT(30* ticks)
  5: 0x00F5 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F6   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                   32 0D  80 1F 00 0E 80 0F 80 10        2.........
0100: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x00F6 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00F9 [0x1F] MOVE_ENTITY: EventEntity moves to X=-57.603*, Z=207.645*, Y=30.268*
  2: 0x0101 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0103 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0104   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:             32 0D 80 1F  00 11 80 12 80 13 80 1F      2...........
0110: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0104 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0107 [0x1F] MOVE_ENTITY: EventEntity moves to X=-48.989*, Z=214.919*, Y=30.499*
  2: 0x010F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0111 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0112   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:       03 00 00 07 7F 1A  4C 00 66 01 00 F8 FF FF    ......L.f.....
0120: 7F F8 FF FF 7F 74 6C 6B  30 00                    .....tlk0.      
```

#### Opcodes

```
  0: 0x0112 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0117 [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x011A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0129 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012A   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                03 00 00 07 7F 1A            ......
0130: 4C 00 66 01 00 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  L.f..........tlk
0140: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x012A [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x012F [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x0132 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0141 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0142   |
| Data Size    | 38 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:       22 00 2F 00 F8 FF  FF 7F B6 0B 14 80 15 80    "./...........
0150: 16 80 17 80 18 80 18 80  18 80 19 80 1A 80 6C F8  ..............l.
0160: FF FF 7F 1B 80 01 80 00                           ........        
```

#### Opcodes

```
  0: 0x0142 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0144 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x014A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=7*, head=145*, body=79*, hands=76*, legs=76*, feet=76*, main=201*, sub=24*)
  3: 0x015E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=32*, fade_time=1*)
  4: 0x0167 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0168   |
| Data Size    | 38 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                          22 00 2F 00 F8 FF FF 7F          "./.....
0170: B6 0B 15 80 15 80 16 80  17 80 18 80 18 80 18 80  ................
0180: 19 80 1A 80 6C F8 FF FF  7F 1C 80 01 80 00        ....l.........  
```

#### Opcodes

```
  0: 0x0168 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x016A [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0170 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=7*, head=145*, body=79*, hands=76*, legs=76*, feet=76*, main=201*, sub=24*)
  3: 0x0184 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=48*, fade_time=1*)
  4: 0x018D [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018E   |
| Data Size    | 38 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                            22 00                ".
0190: 2F 00 F8 FF FF 7F B6 0B  00 80 15 80 16 80 17 80  /...............
01A0: 18 80 18 80 18 80 19 80  1A 80 6C F8 FF FF 7F 1D  ..........l.....
01B0: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x018E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0190 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0196 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=7*, head=145*, body=79*, hands=76*, legs=76*, feet=76*, main=201*, sub=24*)
  3: 0x01AA [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=64*, fade_time=1*)
  4: 0x01B3 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B4   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:             03 00 00 07  7F 1A 4C 00 66 01 00 F8      ......L.f...
01C0: FF FF 7F F8 FF FF 7F 73  69 74 30 53 F8 FF FF 7F  .......sit0S....
01D0: F8 FF FF 7F 73 69 74 30  00                       ....sit0.       
```

#### Opcodes

```
  0: 0x01B4 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x01B9 [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x01BC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x01CB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit0" with entities [EventEntity, EventEntity]
  4: 0x01D8 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D9   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                             03 00 00 07 7F 1A 4C           ......L
01E0: 00 66 01 00 F8 FF FF 7F  F8 FF FF 7F 73 69 74 31  .f..........sit1
01F0: 53 F8 FF FF 7F F8 FF FF  7F 73 69 74 31 00        S........sit1.  
```

#### Opcodes

```
  0: 0x01D9 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x01DE [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x01E1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x01F0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit1" with entities [EventEntity, EventEntity]
  4: 0x01FD [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01FE   |
| Data Size    | 42 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                            03 00                ..
0200: 00 07 7F 1A 4C 00 66 01  00 F8 FF FF 7F F8 FF FF  ....L.f.........
0210: 7F 74 6C 6B 30 1C 1E 80  66 01 00 F8 FF FF 7F F8  .tlk0...f.......
0220: FF FF 7F 74 6C 6B 31 00                           ...tlk1.        
```

#### Opcodes

```
  0: 0x01FE [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0203 [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x0206 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0215 [0x1C] WAIT(60* ticks)
  4: 0x0218 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  5: 0x0227 [0x00] END_REQSTACK()
```
