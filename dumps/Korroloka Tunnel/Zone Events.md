# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Korroloka Tunnel (ID: 173) |
| Block Size       | 388 bytes                  |
| Total Events     | 9                          |
| References Count | 17                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     37 |              5 |
| [65535.3](#event-655353) | 0x0031       |     37 |              5 |
| [65535.4](#event-655354) | 0x0056       |     14 |              4 |
| [65535.5](#event-655355) | 0x0064       |      7 |              3 |
| [65535.6](#event-655356) | 0x006B       |      7 |              3 |
| [65535.7](#event-655357) | 0x0072       |    154 |             34 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF9B4BD  |  4294554813 |
|       1 | 0x1D375     |      119669 |
|       2 | 0xFFFFFF6E  |  4294967150 |
|       3 | 0x094C      |        2380 |
|       4 | 0x000D      |          13 |
|       5 | 0xCB4B      |       52043 |
|       6 | 0x11116     |       69910 |
|       7 | 0x03CC      |         972 |
|       8 | 0x0001      |           1 |
|       9 | 0x0000      |           0 |
|      10 | 0x0005      |           5 |
|      11 | 0x0002      |           2 |
|      12 | 0x000A      |          10 |
|      13 | 0x0009      |           9 |
|      14 | 0x0046      |          70 |
|      15 | 0x008C      |         140 |
|      16 | 0x00D2      |         210 |

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-412.483*, z=119.669*, y=-0.146*, direction=209.2°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      03 00 00 07              ....
0010: 7F 1A 78 00 66 01 00 F8  FF FF 7F F8 FF FF 7F 73  ..x.f..........s
0020: 68 61 30 53 F8 FF FF 7F  F8 FF FF 7F 73 68 61 30  ha0S........sha0
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x000C [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0011 [0x1A] CALL_SUBROUTINE(address=0x0078)
  2: 0x0014 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0023 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    03 00 00 07 7F 1A 78  00 66 01 00 F8 FF FF 7F   ......x.f......
0040: F8 FF FF 7F 73 68 61 31  53 F8 FF FF 7F F8 FF FF  ....sha1S.......
0050: 7F 73 68 61 31 00                                 .sha1.          
```

#### Opcodes

```
  0: 0x0031 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0036 [0x1A] CALL_SUBROUTINE(address=0x0078)
  2: 0x0039 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0048 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   32 04  80 1F 00 05 80 06 80 07        2.........
0060: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0056 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0059 [0x1F] MOVE_ENTITY: EventEntity moves to X=52.043*, Z=69.910*, Y=0.972*
  2: 0x0061 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             AB 03 AC 01  08 80 00                     .......     
```

#### Opcodes

```
  0: 0x0064 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0066 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   AC 01 09 80 AB             .....
0070: 04 00                                             ..              
```

#### Opcodes

```
  0: 0x006B [0xAC] EventEntity->StatusEvent = 0*
  1: 0x006F [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0072    |
| Data Size    | 154 bytes |
| Instructions | 2         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       03 09 10 07 7F 00  03 01 00 00 00 02 01 00    ..............
0080: 0A 80 05 8D 00 08 01 00  08 80 01 92 00 08 01 00  ................
0090: 0B 80 14 01 00 0C 80 07  01 00 0D 80 1B 03 01 00  ................
00A0: 00 00 02 01 00 0A 80 05  B2 00 08 01 00 08 80 01  ................
00B0: B7 00 08 01 00 0B 80 14  01 00 0C 80 07 01 00 0E  ................
00C0: 80 1B 03 01 00 00 00 02  01 00 0A 80 05 D7 00 08  ................
00D0: 01 00 08 80 01 DC 00 08  01 00 0B 80 14 01 00 0C  ................
00E0: 80 07 01 00 0F 80 1B 03  01 00 00 00 02 01 00 0A  ................
00F0: 80 05 FC 00 08 01 00 08  80 01 01 01 08 01 00 0B  ................
0100: 80 14 01 00 0C 80 07 01  00 10 80 1B              ............    
```

#### Opcodes

```
  0: 0x0072 [0x03] Work_Zone[9] = Entity->Race
  1: 0x0077 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0078 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x007D [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x008D
     0x0085 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x008A [0x01] GOTO 0x0092
     0x008D [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0092 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0097 [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x009C [0x1B] RETURN
     0x009D [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00A2 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00B2
     0x00AA [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00AF [0x01] GOTO 0x00B7
     0x00B2 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00B7 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00BC [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x00C1 [0x1B] RETURN
     0x00C2 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00C7 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00D7
     0x00CF [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00D4 [0x01] GOTO 0x00DC
     0x00D7 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00DC [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00E1 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x00E6 [0x1B] RETURN
     0x00E7 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00EC [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00FC
     0x00F4 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00F9 [0x01] GOTO 0x0101
     0x00FC [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0101 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0106 [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x010B [0x1B] RETURN
```
