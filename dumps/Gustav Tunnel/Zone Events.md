# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Gustav Tunnel (ID: 212) |
| Block Size       | 388 bytes               |
| Total Events     | 8                       |
| References Count | 13                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      9 |              3 |
| [65535.2](#event-655352) | 0x000B       |     14 |              4 |
| [65535.3](#event-655353) | 0x0019       |     23 |              4 |
| [65535.4](#event-655354) | 0x0030       |     24 |              4 |
| [65535.5](#event-655355) | 0x0048       |     24 |              4 |
| [65535.6](#event-655356) | 0x0060       |    190 |             38 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000A      |          10 |
|       1 | 0xFFFDE900  |  4294830336 |
|       2 | 0xFFFD3492  |  4294784146 |
|       3 | 0xFFFFD9F4  |  4294957556 |
|       4 | 0x0028      |          40 |
|       5 | 0x003C      |          60 |
|       6 | 0x0005      |           5 |
|       7 | 0x0001      |           1 |
|       8 | 0x0002      |           2 |
|       9 | 0x0009      |           9 |
|      10 | 0x0046      |          70 |
|      11 | 0x008C      |         140 |
|      12 | 0x00D2      |         210 |

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
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 94 01 F8 FF  FF 7F 00                   "........     
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 00 80 1F 00             2....
0010: 01 80 02 80 03 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-136.960*, Z=-183.150*, Y=-9.740*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 23 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             79 00 F8 FF FF 7F 4F           y.....O
0020: 41 0D 01 1C 04 80 4A F8  FF FF 7F 4F 41 0D 01 00  A.....J....OA...
```

#### Opcodes

```
  0: 0x0019 [0x79] EventEntity looks at Aldo (ID: 17645903/0x010D414F) (Basic look)
  1: 0x0023 [0x1C] WAIT(40* ticks)
  2: 0x0026 [0x4A] EventEntity looks at Aldo (ID: 17645903/0x010D414F)
  3: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 03 00 00 07 7F 1A 8A 00  66 01 00 F8 FF FF 7F F8  ........f.......
0040: FF FF 7F 74 6C 6B 30 00                           ...tlk0.        
```

#### Opcodes

```
  0: 0x0030 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0035 [0x1A] CALL_SUBROUTINE(address=0x008A)
  2: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          03 00 00 07 7F 1A 8A 00          ........
0050: 66 01 00 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 00  f..........tlk1.
```

#### Opcodes

```
  0: 0x0048 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x004D [0x1A] CALL_SUBROUTINE(address=0x008A)
  2: 0x0050 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0060    |
| Data Size    | 190 bytes |
| Instructions | 14        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 03 00 00 07 7F 1A 8A 00  66 01 00 F8 FF FF 7F F8  ........f.......
0070: FF FF 7F 74 6C 6B 30 1C  05 80 66 01 00 F8 FF FF  ...tlk0...f.....
0080: 7F F8 FF FF 7F 74 6C 6B  31 00 03 01 00 00 00 02  .....tlk1.......
0090: 01 00 06 80 05 9F 00 08  01 00 07 80 01 A4 00 08  ................
00A0: 01 00 08 80 14 01 00 00  80 07 01 00 09 80 1B 03  ................
00B0: 01 00 00 00 02 01 00 06  80 05 C4 00 08 01 00 07  ................
00C0: 80 01 C9 00 08 01 00 08  80 14 01 00 00 80 07 01  ................
00D0: 00 0A 80 1B 03 01 00 00  00 02 01 00 06 80 05 E9  ................
00E0: 00 08 01 00 07 80 01 EE  00 08 01 00 08 80 14 01  ................
00F0: 00 00 80 07 01 00 0B 80  1B 03 01 00 00 00 02 01  ................
0100: 00 06 80 05 0E 01 08 01  00 07 80 01 13 01 08 01  ................
0110: 00 08 80 14 01 00 00 80  07 01 00 0C 80 1B        ..............  
```

#### Opcodes

```
  0: 0x0060 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0065 [0x1A] CALL_SUBROUTINE(address=0x008A)
  2: 0x0068 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0077 [0x1C] WAIT(60* ticks)
  4: 0x007A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  5: 0x0089 [0x00] END_REQSTACK()

SUBROUTINE_008A:
  6: 0x008A [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  7: 0x008F [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x009F
  8: 0x0097 [0x08] ExtData[1]->WorkLocal[1] -= 1*
  9: 0x009C [0x01] GOTO 0x00A4
 10: 0x009F [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_00A4:
 11: 0x00A4 [0x14] ExtData[1]->WorkLocal[1] *= 10*
 12: 0x00A9 [0x07] ExtData[1]->WorkLocal[1] += 9*
 13: 0x00AE [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00AF [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00B4 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00C4
     0x00BC [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00C1 [0x01] GOTO 0x00C9
     0x00C4 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00C9 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00CE [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x00D3 [0x1B] RETURN
     0x00D4 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00D9 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00E9
     0x00E1 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00E6 [0x01] GOTO 0x00EE
     0x00E9 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00EE [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00F3 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x00F8 [0x1B] RETURN
     0x00F9 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00FE [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x010E
     0x0106 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x010B [0x01] GOTO 0x0113
     0x010E [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0113 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0118 [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x011D [0x1B] RETURN
```
