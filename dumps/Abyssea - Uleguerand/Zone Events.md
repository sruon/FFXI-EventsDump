# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 588 bytes                      |
| Total Events     | 10                             |
| References Count | 19                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     37 |              5 |
| [65535.2](#event-655352) | 0x0027       |     37 |              5 |
| [65535.3](#event-655353) | 0x004C       |     24 |              4 |
| [65535.4](#event-655354) | 0x0064       |    172 |             36 |
| [65535.5](#event-655355) | 0x0110       |      6 |              2 |
| [65535.6](#event-655356) | 0x0116       |     16 |              3 |
| [65535.7](#event-655357) | 0x0126       |     41 |              5 |
| [2180](#event-2180)      | 0x014F       |    119 |             15 |

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
|       8 | 0xFFFC7006  |  4294733830 |
|       9 | 0xFFF815B8  |  4294448568 |
|      10 | 0xFFFF643E  |  4294927422 |
|      11 | 0x07F3      |        2035 |
|      12 | 0x0094      |         148 |
|      13 | 0x0000      |           0 |
|      14 | 0x00F0      |         240 |
|      15 | 0x00C8      |         200 |
|      16 | 0x003C      |          60 |
|      17 | 0x00C9      |         201 |
|      18 | 0x0155      |         341 |

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
0000:       03 00 00 07 7F 1A  7C 00 66 01 00 F8 FF FF    ......|.f.....
0010: 7F F8 FF FF 7F 73 68 61  30 53 F8 FF FF 7F F8 FF  .....sha0S......
0020: FF 7F 73 68 61 30 00                              ..sha0.         
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0007 [0x1A] CALL_SUBROUTINE(address=0x007C)
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
0020:                      03  00 00 07 7F 1A 7C 00 66         ......|.f
0030: 01 00 F8 FF FF 7F F8 FF  FF 7F 73 68 61 31 53 F8  ..........sha1S.
0040: FF FF 7F F8 FF FF 7F 73  68 61 31 00              .......sha1.    
```

#### Opcodes

```
  0: 0x0027 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x002C [0x1A] CALL_SUBROUTINE(address=0x007C)
  2: 0x002F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x003E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      03 00 00 07              ....
0050: 7F 1A 7C 00 66 01 00 F8  FF FF 7F F8 FF FF 7F 74  ..|.f..........t
0060: 6C 6B 30 00                                       lk0.            
```

#### Opcodes

```
  0: 0x004C [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0051 [0x1A] CALL_SUBROUTINE(address=0x007C)
  2: 0x0054 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0064    |
| Data Size    | 172 bytes |
| Instructions | 12        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             03 00 00 07  7F 1A 7C 00 66 01 00 F8      ......|.f...
0070: FF FF 7F F8 FF FF 7F 74  6C 6B 31 00 03 01 00 00  .......tlk1.....
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
  0: 0x0064 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0069 [0x1A] CALL_SUBROUTINE(address=0x007C)
  2: 0x006C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x007B [0x00] END_REQSTACK()

SUBROUTINE_007C:
  4: 0x007C [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  5: 0x0081 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0091
  6: 0x0089 [0x08] ExtData[1]->WorkLocal[1] -= 1*
  7: 0x008E [0x01] GOTO 0x0096
  8: 0x0091 [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_0096:
  9: 0x0096 [0x14] ExtData[1]->WorkLocal[1] *= 10*
 10: 0x009B [0x07] ExtData[1]->WorkLocal[1] += 9*
 11: 0x00A0 [0x1B] RETURN
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
0110: 03 02 10 0B 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0110 [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x0115 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0116   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   92 01  F0 FF FF 7F 37 08 80 09        ......7...
0120: 80 0A 80 0B 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0116 [0x92] LocalPlayer->Render.Flags3 ^= 0x01
  1: 0x011C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-233.466*, z=-518.728*, y=-39.874*, direction=178.9°*
  2: 0x0125 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0126   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                   BB 0C  80 F0 FF FF 7F 47 D2 0F        .......G..
0130: 01 6D 61 69 6E 0D 80 1C  0E 80 45 0F 80 F0 FF FF  .main.....E.....
0140: 7F F0 FF FF 7F 66 64 6F  31 0D 80 1C 10 80 00     .....fdo1...... 
```

#### Opcodes

```
  0: 0x0126 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17814087/0x010FD247)], work=[148*, 0*]
  1: 0x0137 [0x1C] WAIT(240* ticks)
  2: 0x013A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x014B [0x1C] WAIT(60* ticks)
  4: 0x014E [0x00] END_REQSTACK()
```

### Event 2180

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x014F    |
| Data Size    | 119 bytes |
| Instructions | 15        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                               20                  
0150: 01 42 46 01 45 0F 80 F0  FF FF 7F F0 FF FF 7F 62  .BF.E..........b
0160: 6C 6F 6E 0D 80 45 11 80  F0 FF FF 7F F0 FF FF 7F  lon..E..........
0170: 62 6C 6F 6E 0D 80 45 0F  80 F0 FF FF 7F F0 FF FF  blon..E.........
0180: 7F 6F 76 6C 31 0D 80 45  12 80 F0 FF FF 7F F0 FF  .ovl1..E........
0190: FF 7F 77 61 72 70 0D 80  BB 0C 80 F0 FF FF 7F 47  ..warp.........G
01A0: D2 0F 01 6D 61 69 6E 0D  80 1C 0E 80 45 0F 80 F0  ...main.....E...
01B0: FF FF 7F F0 FF FF 7F 66  64 6F 31 0D 80 1C 10 80  .......fdo1.....
01C0: 46 00 20 00 21 00                                 F. .!.          
```

#### Opcodes

```
  0: 0x014F [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0151 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0152 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0154 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0165 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  5: 0x0176 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x0187 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
  7: 0x0198 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17814087/0x010FD247)], work=[148*, 0*]
  8: 0x01A9 [0x1C] WAIT(240* ticks)
  9: 0x01AC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x01BD [0x1C] WAIT(60* ticks)
 11: 0x01C0 [0x46] CAMERA_CONTROL: Restore default settings
 12: 0x01C2 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x01C4 [0x21] END_EVENT
 14: 0x01C5 [0x00] END_REQSTACK()
```
