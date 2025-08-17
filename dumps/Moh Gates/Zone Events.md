# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Moh Gates (ID: 269) |
| Block Size       | 308 bytes           |
| Total Events     | 6                   |
| References Count | 8                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      6 |              2 |
| [65535.2](#event-655352) | 0x0008       |      6 |              2 |
| [65535.3](#event-655353) | 0x000E       |     37 |              5 |
| [65535.4](#event-655354) | 0x0033       |    185 |             37 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            03 00                ..
0010: 00 07 7F 1A 58 00 66 01  00 F8 FF FF 7F F8 FF FF  ....X.f.........
0020: 7F 73 68 61 30 53 F8 FF  FF 7F F8 FF FF 7F 73 68  .sha0S........sh
0030: 61 30 00                                          a0.             
```

#### Opcodes

```
  0: 0x000E [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0013 [0x1A] CALL_SUBROUTINE(address=0x0058)
  2: 0x0016 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0025 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0033    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          03 00 00 07 7F  1A 58 00 66 01 00 F8 FF     ......X.f....
0040: FF 7F F8 FF FF 7F 73 68  61 31 53 F8 FF FF 7F F8  ......sha1S.....
0050: FF FF 7F 73 68 61 31 00  03 01 00 00 00 02 01 00  ...sha1.........
0060: 00 80 05 6D 00 08 01 00  01 80 01 72 00 08 01 00  ...m.......r....
0070: 02 80 14 01 00 03 80 07  01 00 04 80 1B 03 01 00  ................
0080: 00 00 02 01 00 00 80 05  92 00 08 01 00 01 80 01  ................
0090: 97 00 08 01 00 02 80 14  01 00 03 80 07 01 00 05  ................
00A0: 80 1B 03 01 00 00 00 02  01 00 00 80 05 B7 00 08  ................
00B0: 01 00 01 80 01 BC 00 08  01 00 02 80 14 01 00 03  ................
00C0: 80 07 01 00 06 80 1B 03  01 00 00 00 02 01 00 00  ................
00D0: 80 05 DC 00 08 01 00 01  80 01 E1 00 08 01 00 02  ................
00E0: 80 14 01 00 03 80 07 01  00 07 80 1B              ............    
```

#### Opcodes

```
  0: 0x0033 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0038 [0x1A] CALL_SUBROUTINE(address=0x0058)
  2: 0x003B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x004A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x0057 [0x00] END_REQSTACK()

SUBROUTINE_0058:
  5: 0x0058 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  6: 0x005D [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x006D
  7: 0x0065 [0x08] ExtData[1]->WorkLocal[1] -= 1*
  8: 0x006A [0x01] GOTO 0x0072
  9: 0x006D [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_0072:
 10: 0x0072 [0x14] ExtData[1]->WorkLocal[1] *= 10*
 11: 0x0077 [0x07] ExtData[1]->WorkLocal[1] += 9*
 12: 0x007C [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x007D [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0082 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0092
     0x008A [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x008F [0x01] GOTO 0x0097
     0x0092 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0097 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x009C [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x00A1 [0x1B] RETURN
     0x00A2 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00A7 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00B7
     0x00AF [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00B4 [0x01] GOTO 0x00BC
     0x00B7 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00BC [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00C1 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x00C6 [0x1B] RETURN
     0x00C7 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00CC [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00DC
     0x00D4 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00D9 [0x01] GOTO 0x00E1
     0x00DC [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00E1 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00E6 [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x00EB [0x1B] RETURN
```
