# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Crawlers' Nest [S] (ID: 171) |
| Block Size       | 364 bytes                    |
| Total Events     | 8                            |
| References Count | 8                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     24 |              4 |
| [65535.2](#event-655352) | 0x001A       |     24 |              4 |
| [65535.3](#event-655353) | 0x0032       |     37 |              5 |
| [65535.4](#event-655354) | 0x0057       |    185 |             37 |
| [65535.5](#event-655355) | 0x0110       |      6 |              2 |
| [65535.6](#event-655356) | 0x0116       |      6 |              2 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 00 00 07 7F 1A  7C 00 66 01 00 F8 FF FF    ......|.f.....
0010: 7F F8 FF FF 7F 74 6C 6B  30 00                    .....tlk0.      
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0007 [0x1A] CALL_SUBROUTINE(address=0x007C)
  2: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                03 00 00 07 7F 1A            ......
0020: 7C 00 66 01 00 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  |.f..........tlk
0030: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x001A [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x001F [0x1A] CALL_SUBROUTINE(address=0x007C)
  2: 0x0022 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       03 00 00 07 7F 1A  7C 00 66 01 00 F8 FF FF    ......|.f.....
0040: 7F F8 FF FF 7F 73 68 61  30 53 F8 FF FF 7F F8 FF  .....sha0S......
0050: FF 7F 73 68 61 30 00                              ..sha0.         
```

#### Opcodes

```
  0: 0x0032 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0037 [0x1A] CALL_SUBROUTINE(address=0x007C)
  2: 0x003A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0049 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0057    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      03  00 00 07 7F 1A 7C 00 66         ......|.f
0060: 01 00 F8 FF FF 7F F8 FF  FF 7F 73 68 61 31 53 F8  ..........sha1S.
0070: FF FF 7F F8 FF FF 7F 73  68 61 31 00 03 01 00 00  .......sha1.....
0080: 00 02 01 00 00 80 05 91  00 08 01 00 01 80 01 96  ................
0090: 00 08 01 00 02 80 14 01  00 03 80 07 01 00 04 80  ................
00A0: 1B 03 01 00 00 00 02 01  00 00 80 05 B6 00 08 01  ................
00B0: 00 01 80 01 BB 00 08 01  00 02 80 14 01 00 03 80  ................
00C0: 07 01 00 05 80 1B 03 01  00 00 00 02 01 00 00 80  ................
00D0: 05 DB 00 08 01 00 01 80  01 E0 00 08 01 00 02 80  ................
00E0: 14 01 00 03 80 07 01 00  06 80 1B 03 01 00 00 00  ................
00F0: 02 01 00 00 80 05 00 01  08 01 00 01 80 01 05 01  ................
0100: 08 01 00 02 80 14 01 00  03 80 07 01 00 07 80 1B  ................
```

#### Opcodes

```
  0: 0x0057 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x005C [0x1A] CALL_SUBROUTINE(address=0x007C)
  2: 0x005F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x006E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x007B [0x00] END_REQSTACK()

SUBROUTINE_007C:
  5: 0x007C [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  6: 0x0081 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0091
  7: 0x0089 [0x08] ExtData[1]->WorkLocal[1] -= 1*
  8: 0x008E [0x01] GOTO 0x0096
  9: 0x0091 [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_0096:
 10: 0x0096 [0x14] ExtData[1]->WorkLocal[1] *= 10*
 11: 0x009B [0x07] ExtData[1]->WorkLocal[1] += 9*
 12: 0x00A0 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00A1 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00A6 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00B6
     0x00AE [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00B3 [0x01] GOTO 0x00BB
     0x00B6 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00BB [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00C0 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x00C5 [0x1B] RETURN
     0x00C6 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00CB [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00DB
     0x00D3 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00D8 [0x01] GOTO 0x00E0
     0x00DB [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00E0 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00E5 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x00EA [0x1B] RETURN
     0x00EB [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00F0 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0100
     0x00F8 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00FD [0x01] GOTO 0x0105
     0x0100 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0105 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x010A [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x010F [0x1B] RETURN
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0110  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110: 03 02 10 07 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0110 [0x03] Work_Zone[2] = Entity->Race
  1: 0x0115 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0116  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   03 02  10 0B 7F 00                    ......    
```

#### Opcodes

```
  0: 0x0116 [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x011B [0x00] END_REQSTACK()
```
