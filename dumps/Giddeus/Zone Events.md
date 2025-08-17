# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Giddeus (ID: 145) |
| Block Size       | 356 bytes         |
| Total Events     | 9                 |
| References Count | 12                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [54](#event-54)          | 0x0001       |      6 |              4 |
| [55](#event-55)          | 0x0007       |      9 |              6 |
| [65534](#event-65534)    | 0x0010       |      1 |              1 |
| [65535.1](#event-655351) | 0x0011       |     27 |              5 |
| [65535.2](#event-655352) | 0x002C       |     42 |              6 |
| [65535.3](#event-655353) | 0x0056       |      7 |              3 |
| [65535.4](#event-655354) | 0x005D       |      7 |              3 |
| [65535.5](#event-655355) | 0x0064       |    154 |             34 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CCE      |        7374 |
|       1 | 0x1CCD      |        7373 |
|       2 | 0x003C      |          60 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x0005      |           5 |
|       6 | 0x0002      |           2 |
|       7 | 0x000A      |          10 |
|       8 | 0x0009      |           9 |
|       9 | 0x0046      |          70 |
|      10 | 0x008C      |         140 |
|      11 | 0x00D2      |         210 |

## String References

- **7373**: You fill your flask with water.
- **7374**: Sparkling clear water bubbles up from the ground. If you have a container, you can fill it here.

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

### Event 54

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 21 00                               H..#!.         
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7374*]:
    → "Sparkling clear water bubbles up from the ground. If you have a container, you can fill it here."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x21] END_EVENT
  3: 0x0006 [0x00] END_REQSTACK()
```

### Event 55

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 9 bytes |
| Instructions | 6       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      42  48 01 80 23 20 00 21 00         BH..# .!.
```

#### Opcodes

```
  0: 0x0007 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0008 [0x48] [System] [7373*]:
    → "You fill your flask with water."
  2: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  4: 0x000E [0x21] END_EVENT
  5: 0x000F [0x00] END_REQSTACK()
```

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 27 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    03 00 00 07 7F 1A 8F  00 0B 01 00 66 01 00 F8   ...........f...
0020: FF FF 7F F8 FF FF 7F 70  61 73 30 00              .......pas0.    
```

#### Opcodes

```
  0: 0x0011 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0016 [0x1A] CALL_SUBROUTINE(address=0x008F)
  2: 0x0019 [0x0B] ExtData[1]->WorkLocal[1]++
  3: 0x001C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  4: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 42 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      03 00 00 07              ....
0030: 7F 1A 6A 00 66 01 00 F8  FF FF 7F F8 FF FF 7F 74  ..j.f..........t
0040: 6C 6B 30 1C 02 80 66 01  00 F8 FF FF 7F F8 FF FF  lk0...f.........
0050: 7F 74 6C 6B 31 00                                 .tlk1.          
```

#### Opcodes

```
  0: 0x002C [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0031 [0x1A] CALL_SUBROUTINE(address=0x006A)
  2: 0x0034 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0043 [0x1C] WAIT(60* ticks)
  4: 0x0046 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  5: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0056  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   AB 03  AC 01 03 80 00                 .......   
```

#### Opcodes

```
  0: 0x0056 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0058 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005D  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         AC 01 04               ...
0060: 80 AB 04 00                                       ....            
```

#### Opcodes

```
  0: 0x005D [0xAC] EventEntity->StatusEvent = 0*
  1: 0x0061 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0064    |
| Data Size    | 154 bytes |
| Instructions | 2         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             03 09 10 07  7F 00 03 01 00 00 00 02      ............
0070: 01 00 05 80 05 7F 00 08  01 00 03 80 01 84 00 08  ................
0080: 01 00 06 80 14 01 00 07  80 07 01 00 08 80 1B 03  ................
0090: 01 00 00 00 02 01 00 05  80 05 A4 00 08 01 00 03  ................
00A0: 80 01 A9 00 08 01 00 06  80 14 01 00 07 80 07 01  ................
00B0: 00 09 80 1B 03 01 00 00  00 02 01 00 05 80 05 C9  ................
00C0: 00 08 01 00 03 80 01 CE  00 08 01 00 06 80 14 01  ................
00D0: 00 07 80 07 01 00 0A 80  1B 03 01 00 00 00 02 01  ................
00E0: 00 05 80 05 EE 00 08 01  00 03 80 01 F3 00 08 01  ................
00F0: 00 06 80 14 01 00 07 80  07 01 00 0B 80 1B        ..............  
```

#### Opcodes

```
  0: 0x0064 [0x03] Work_Zone[9] = Entity->Race
  1: 0x0069 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x006A [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x006F [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x007F
     0x0077 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x007C [0x01] GOTO 0x0084
     0x007F [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0084 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0089 [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x008E [0x1B] RETURN
     0x008F [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0094 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00A4
     0x009C [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00A1 [0x01] GOTO 0x00A9
     0x00A4 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00A9 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00AE [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x00B3 [0x1B] RETURN
     0x00B4 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00B9 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00C9
     0x00C1 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00C6 [0x01] GOTO 0x00CE
     0x00C9 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00CE [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00D3 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x00D8 [0x1B] RETURN
     0x00D9 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00DE [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00EE
     0x00E6 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00EB [0x01] GOTO 0x00F3
     0x00EE [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00F3 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00F8 [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x00FD [0x1B] RETURN
```
