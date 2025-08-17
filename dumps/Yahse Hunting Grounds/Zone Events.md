# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Yahse Hunting Grounds (ID: 260) |
| Block Size       | 508 bytes                       |
| Total Events     | 10                              |
| References Count | 16                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     37 |              5 |
| [65535.2](#event-655352) | 0x0027       |     37 |              5 |
| [65535.3](#event-655353) | 0x004C       |     37 |              5 |
| [65535.4](#event-655354) | 0x0071       |     37 |              5 |
| [65535.5](#event-655355) | 0x0096       |     29 |              5 |
| [65535.6](#event-655356) | 0x00B3       |     29 |              5 |
| [65535.7](#event-655357) | 0x00D0       |     15 |              5 |
| [65535.8](#event-655358) | 0x00DF       |    163 |             37 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0009      |           9 |
|       1 | 0x0008      |           8 |
|       2 | 0x1EC30     |      126000 |
|       3 | 0x61A80     |      400000 |
|       4 | 0x0000      |           0 |
|       5 | 0x001E      |          30 |
|       6 | 0x1D3A2     |      119714 |
|       7 | 0x5C4A4     |      378020 |
|       8 | 0x0259      |         601 |
|       9 | 0x0005      |           5 |
|      10 | 0x0001      |           1 |
|      11 | 0x0002      |           2 |
|      12 | 0x000A      |          10 |
|      13 | 0x0046      |          70 |
|      14 | 0x008C      |         140 |
|      15 | 0x00D2      |         210 |

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
0000:       03 00 00 07 7F 1A  EE 00 66 01 00 F8 FF FF    ........f.....
0010: 7F F8 FF FF 7F 73 68 61  30 53 F8 FF FF 7F F8 FF  .....sha0S......
0020: FF 7F 73 68 61 30 00                              ..sha0.         
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0007 [0x1A] CALL_SUBROUTINE(address=0x00EE)
  2: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0019 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      03  00 00 07 7F 1A EE 00 66         ........f
0030: 01 00 F8 FF FF 7F F8 FF  FF 7F 73 68 61 31 53 F8  ..........sha1S.
0040: FF FF 7F F8 FF FF 7F 73  68 61 31 00              .......sha1.    
```

#### Opcodes

```
  0: 0x0027 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x002C [0x1A] CALL_SUBROUTINE(address=0x00EE)
  2: 0x002F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x003E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      03 00 00 07              ....
0050: 7F 1A EE 00 66 01 00 F8  FF FF 7F F8 FF FF 7F 73  ....f..........s
0060: 69 72 30 53 F8 FF FF 7F  F8 FF FF 7F 73 69 72 30  ir0S........sir0
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x004C [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0051 [0x1A] CALL_SUBROUTINE(address=0x00EE)
  2: 0x0054 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0063 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sir0" with entities [EventEntity, EventEntity]
  4: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    03 00 00 07 7F 1A EE  00 66 01 00 F8 FF FF 7F   ........f......
0080: F8 FF FF 7F 73 69 72 31  53 F8 FF FF 7F F8 FF FF  ....sir1S.......
0090: 7F 73 69 72 31 00                                 .sir1.          
```

#### Opcodes

```
  0: 0x0071 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0076 [0x1A] CALL_SUBROUTINE(address=0x00EE)
  2: 0x0079 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0088 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sir1" with entities [EventEntity, EventEntity]
  4: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0096   |
| Data Size    | 29 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   03 00  00 07 7F 1A 38 01 07 01        ......8...
00A0: 00 00 80 66 01 00 F8 FF  FF 7F F8 FF FF 7F 74 6C  ...f..........tl
00B0: 6B 30 00                                          k0.             
```

#### Opcodes

```
  0: 0x0096 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x009B [0x1A] CALL_SUBROUTINE(address=0x0138)
  2: 0x009E [0x07] ExtData[1]->WorkLocal[1] += 9*
  3: 0x00A3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  4: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 29 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          03 00 00 07 7F  1A 38 01 07 01 00 00 80     ......8......
00C0: 66 01 00 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 00  f..........tlk1.
```

#### Opcodes

```
  0: 0x00B3 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x00B8 [0x1A] CALL_SUBROUTINE(address=0x0138)
  2: 0x00BB [0x07] ExtData[1]->WorkLocal[1] += 9*
  3: 0x00C0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  4: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D0   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 32 01 80 1F 00 02 80 03  80 04 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x00D0 [0x32] ExtData[1]->MainSpeed = 8* * 0.1
  1: 0x00D3 [0x1F] MOVE_ENTITY: EventEntity moves to X=126.000*, Z=400.000*, Y=0.000*
  2: 0x00DB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00DD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00DE [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00DF    |
| Data Size    | 163 bytes |
| Instructions | 5         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                               32                 2
00E0: 05 80 1F 00 06 80 07 80  08 80 1F 01 6F 00 03 01  ............o...
00F0: 00 00 00 02 01 00 09 80  05 03 01 08 01 00 0A 80  ................
0100: 01 08 01 08 01 00 0B 80  14 01 00 0C 80 07 01 00  ................
0110: 00 80 1B 03 01 00 00 00  02 01 00 09 80 05 28 01  ..............(.
0120: 08 01 00 0A 80 01 2D 01  08 01 00 0B 80 14 01 00  ......-.........
0130: 0C 80 07 01 00 0D 80 1B  03 01 00 00 00 02 01 00  ................
0140: 09 80 05 4D 01 08 01 00  0A 80 01 52 01 08 01 00  ...M.......R....
0150: 0B 80 14 01 00 0C 80 07  01 00 0E 80 1B 03 01 00  ................
0160: 00 00 02 01 00 09 80 05  72 01 08 01 00 0A 80 01  ........r.......
0170: 77 01 08 01 00 0B 80 14  01 00 0C 80 07 01 00 0F  w...............
0180: 80 1B                                             ..              
```

#### Opcodes

```
  0: 0x00DF [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x00E2 [0x1F] MOVE_ENTITY: EventEntity moves to X=119.714*, Z=378.020*, Y=0.601*
  2: 0x00EA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00EC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00ED [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00EE [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00F3 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0103
     0x00FB [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0100 [0x01] GOTO 0x0108
     0x0103 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0108 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x010D [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x0112 [0x1B] RETURN
     0x0113 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0118 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0128
     0x0120 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0125 [0x01] GOTO 0x012D
     0x0128 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x012D [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0132 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x0137 [0x1B] RETURN
     0x0138 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x013D [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x014D
     0x0145 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x014A [0x01] GOTO 0x0152
     0x014D [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0152 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0157 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x015C [0x1B] RETURN
     0x015D [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0162 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0172
     0x016A [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x016F [0x01] GOTO 0x0177
     0x0172 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0177 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x017C [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x0181 [0x1B] RETURN
```
