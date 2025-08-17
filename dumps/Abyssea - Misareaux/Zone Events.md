# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Abyssea - Misareaux (ID: 216) |
| Block Size       | 600 bytes                     |
| Total Events     | 11                            |
| References Count | 19                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     16 |              3 |
| [65535.2](#event-655352) | 0x0012       |     41 |              5 |
| [2180](#event-2180)      | 0x003B       |    119 |             15 |
| [65535.3](#event-655353) | 0x00B2       |     37 |              5 |
| [65535.4](#event-655354) | 0x00D7       |     37 |              5 |
| [65535.5](#event-655355) | 0x00FC       |      7 |              3 |
| [65535.6](#event-655356) | 0x0103       |      7 |              3 |
| [65535.7](#event-655357) | 0x010A       |     24 |              4 |
| [65535.8](#event-655358) | 0x0122       |    172 |             36 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xA3D03     |      670979 |
|       1 | 0x4DA3A     |      318010 |
|       2 | 0xFFFFC237  |  4294951479 |
|       3 | 0x0FA7      |        4007 |
|       4 | 0x0094      |         148 |
|       5 | 0x0000      |           0 |
|       6 | 0x00F0      |         240 |
|       7 | 0x00C8      |         200 |
|       8 | 0x003C      |          60 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0155      |         341 |
|      11 | 0x0001      |           1 |
|      12 | 0x0005      |           5 |
|      13 | 0x0002      |           2 |
|      14 | 0x000A      |          10 |
|      15 | 0x0009      |           9 |
|      16 | 0x0046      |          70 |
|      17 | 0x008C      |         140 |
|      18 | 0x00D2      |         210 |

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
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       92 01 F0 FF FF 7F  37 00 80 01 80 02 80 03    ......7.......
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0002 [0x92] LocalPlayer->Render.Flags3 ^= 0x01
  1: 0x0008 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=670.979*, z=318.010*, y=-15.817*, direction=352.2°*
  2: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       BB 04 80 F0 FF FF  7F 03 83 0D 01 6D 61 69    ...........mai
0020: 6E 05 80 1C 06 80 45 07  80 F0 FF FF 7F F0 FF FF  n.....E.........
0030: 7F 66 64 6F 31 05 80 1C  08 80 00                 .fdo1......     
```

#### Opcodes

```
  0: 0x0012 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17662723/0x010D8303)], work=[148*, 0*]
  1: 0x0023 [0x1C] WAIT(240* ticks)
  2: 0x0026 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0037 [0x1C] WAIT(60* ticks)
  4: 0x003A [0x00] END_REQSTACK()
```

### Event 2180

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x003B    |
| Data Size    | 119 bytes |
| Instructions | 15        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   20 01 42 46 01              .BF.
0040: 45 07 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 05  E..........blon.
0050: 80 45 09 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
0060: 05 80 45 07 80 F0 FF FF  7F F0 FF FF 7F 6F 76 6C  ..E..........ovl
0070: 31 05 80 45 0A 80 F0 FF  FF 7F F0 FF FF 7F 77 61  1..E..........wa
0080: 72 70 05 80 BB 04 80 F0  FF FF 7F 03 83 0D 01 6D  rp.............m
0090: 61 69 6E 05 80 1C 06 80  45 07 80 F0 FF FF 7F F0  ain.....E.......
00A0: FF FF 7F 66 64 6F 31 05  80 1C 08 80 46 00 20 00  ...fdo1.....F. .
00B0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x003B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x003D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x003E [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0040 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0051 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  5: 0x0062 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x0073 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
  7: 0x0084 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17662723/0x010D8303)], work=[148*, 0*]
  8: 0x0095 [0x1C] WAIT(240* ticks)
  9: 0x0098 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x00A9 [0x1C] WAIT(60* ticks)
 11: 0x00AC [0x46] CAMERA_CONTROL: Restore default settings
 12: 0x00AE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x00B0 [0x21] END_EVENT
 14: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       03 00 00 07 7F 1A  3A 01 66 01 00 F8 FF FF    ......:.f.....
00C0: 7F F8 FF FF 7F 73 68 61  30 53 F8 FF FF 7F F8 FF  .....sha0S......
00D0: FF 7F 73 68 61 30 00                              ..sha0.         
```

#### Opcodes

```
  0: 0x00B2 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x00B7 [0x1A] CALL_SUBROUTINE(address=0x013A)
  2: 0x00BA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x00C9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x00D6 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D7   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                      03  00 00 07 7F 1A 3A 01 66         ......:.f
00E0: 01 00 F8 FF FF 7F F8 FF  FF 7F 73 68 61 31 53 F8  ..........sha1S.
00F0: FF FF 7F F8 FF FF 7F 73  68 61 31 00              .......sha1.    
```

#### Opcodes

```
  0: 0x00D7 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x00DC [0x1A] CALL_SUBROUTINE(address=0x013A)
  2: 0x00DF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x00EE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00FC  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      AB 03 AC 01              ....
0100: 0B 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00FC [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x00FE [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0102 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0103  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:          AC 01 05 80 AB  04 00                       .......      
```

#### Opcodes

```
  0: 0x0103 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x0107 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x0109 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010A   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                03 00 00 07 7F 1A            ......
0110: 3A 01 66 01 00 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  :.f..........tlk
0120: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x010A [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x010F [0x1A] CALL_SUBROUTINE(address=0x013A)
  2: 0x0112 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0121 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0122    |
| Data Size    | 172 bytes |
| Instructions | 12        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:       03 00 00 07 7F 1A  3A 01 66 01 00 F8 FF FF    ......:.f.....
0130: 7F F8 FF FF 7F 74 6C 6B  31 00 03 01 00 00 00 02  .....tlk1.......
0140: 01 00 0C 80 05 4F 01 08  01 00 0B 80 01 54 01 08  .....O.......T..
0150: 01 00 0D 80 14 01 00 0E  80 07 01 00 0F 80 1B 03  ................
0160: 01 00 00 00 02 01 00 0C  80 05 74 01 08 01 00 0B  ..........t.....
0170: 80 01 79 01 08 01 00 0D  80 14 01 00 0E 80 07 01  ..y.............
0180: 00 10 80 1B 03 01 00 00  00 02 01 00 0C 80 05 99  ................
0190: 01 08 01 00 0B 80 01 9E  01 08 01 00 0D 80 14 01  ................
01A0: 00 0E 80 07 01 00 11 80  1B 03 01 00 00 00 02 01  ................
01B0: 00 0C 80 05 BE 01 08 01  00 0B 80 01 C3 01 08 01  ................
01C0: 00 0D 80 14 01 00 0E 80  07 01 00 12 80 1B        ..............  
```

#### Opcodes

```
  0: 0x0122 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0127 [0x1A] CALL_SUBROUTINE(address=0x013A)
  2: 0x012A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0139 [0x00] END_REQSTACK()

SUBROUTINE_013A:
  4: 0x013A [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  5: 0x013F [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x014F
  6: 0x0147 [0x08] ExtData[1]->WorkLocal[1] -= 1*
  7: 0x014C [0x01] GOTO 0x0154
  8: 0x014F [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_0154:
  9: 0x0154 [0x14] ExtData[1]->WorkLocal[1] *= 10*
 10: 0x0159 [0x07] ExtData[1]->WorkLocal[1] += 9*
 11: 0x015E [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
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
