# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 604 bytes                  |
| Total Events     | 10                         |
| References Count | 17                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     16 |              3 |
| [65535.2](#event-655352) | 0x0012       |     41 |              5 |
| [2180](#event-2180)      | 0x003B       |    119 |             15 |
| [65535.3](#event-655353) | 0x00B2       |      6 |              2 |
| [65535.4](#event-655354) | 0x00B8       |      6 |              2 |
| [65535.5](#event-655355) | 0x00BE       |     37 |              5 |
| [65535.6](#event-655356) | 0x00E3       |     37 |              5 |
| [65535.7](#event-655357) | 0x0108       |    216 |             40 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x6AD65     |      437605 |
|       1 | 0x4E297     |      320151 |
|       2 | 0x0000      |           0 |
|       3 | 0x000A      |          10 |
|       4 | 0x0094      |         148 |
|       5 | 0x00F0      |         240 |
|       6 | 0x00C8      |         200 |
|       7 | 0x003C      |          60 |
|       8 | 0x00C9      |         201 |
|       9 | 0x0155      |         341 |
|      10 | 0x0001      |           1 |
|      11 | 0x0005      |           5 |
|      12 | 0x0002      |           2 |
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
  1: 0x0008 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=437.605*, z=320.151*, y=0.000*, direction=0.9°*
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
0010:       BB 04 80 F0 FF FF  7F 47 A2 0D 01 6D 61 69    .......G...mai
0020: 6E 02 80 1C 05 80 45 06  80 F0 FF FF 7F F0 FF FF  n.....E.........
0030: 7F 66 64 6F 31 02 80 1C  07 80 00                 .fdo1......     
```

#### Opcodes

```
  0: 0x0012 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17670727/0x010DA247)], work=[148*, 0*]
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
0040: 45 06 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 02  E..........blon.
0050: 80 45 08 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
0060: 02 80 45 06 80 F0 FF FF  7F F0 FF FF 7F 6F 76 6C  ..E..........ovl
0070: 31 02 80 45 09 80 F0 FF  FF 7F F0 FF FF 7F 77 61  1..E..........wa
0080: 72 70 02 80 BB 04 80 F0  FF FF 7F 47 A2 0D 01 6D  rp.........G...m
0090: 61 69 6E 02 80 1C 05 80  45 06 80 F0 FF FF 7F F0  ain.....E.......
00A0: FF FF 7F 66 64 6F 31 02  80 1C 07 80 46 00 20 00  ...fdo1.....F. .
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
  7: 0x0084 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17670727/0x010DA247)], work=[148*, 0*]
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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B2  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       03 02 10 07 7F 00                             ......        
```

#### Opcodes

```
  0: 0x00B2 [0x03] Work_Zone[2] = Entity->Race
  1: 0x00B7 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B8  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          03 02 10 0B 7F 00                ......  
```

#### Opcodes

```
  0: 0x00B8 [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x00BD [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BE   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            03 00                ..
00C0: 00 07 7F 1A 4C 01 66 01  00 F8 FF FF 7F F8 FF FF  ....L.f.........
00D0: 7F 74 6C 6B 30 53 F8 FF  FF 7F F8 FF FF 7F 74 6C  .tlk0S........tl
00E0: 6B 30 00                                          k0.             
```

#### Opcodes

```
  0: 0x00BE [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x00C3 [0x1A] CALL_SUBROUTINE(address=0x014C)
  2: 0x00C6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x00D5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  4: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          03 00 00 07 7F  1A 4C 01 66 01 00 F8 FF     ......L.f....
00F0: FF 7F F8 FF FF 7F 74 6C  6B 31 53 F8 FF FF 7F F8  ......tlk1S.....
0100: FF FF 7F 74 6C 6B 31 00                           ...tlk1.        
```

#### Opcodes

```
  0: 0x00E3 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x00E8 [0x1A] CALL_SUBROUTINE(address=0x014C)
  2: 0x00EB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x00FA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  4: 0x0107 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0108    |
| Data Size    | 216 bytes |
| Instructions | 16        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                          03 00 00 07 7F 1A 4C 01          ......L.
0110: 66 01 00 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 53  f..........tlk0S
0120: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1C 0A 80 66  ........tlk0...f
0130: 01 00 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 53 F8  ..........tlk1S.
0140: FF FF 7F F8 FF FF 7F 74  6C 6B 31 00 03 01 00 00  .......tlk1.....
0150: 00 02 01 00 0B 80 05 61  01 08 01 00 0A 80 01 66  .......a.......f
0160: 01 08 01 00 0C 80 14 01  00 03 80 07 01 00 0D 80  ................
0170: 1B 03 01 00 00 00 02 01  00 0B 80 05 86 01 08 01  ................
0180: 00 0A 80 01 8B 01 08 01  00 0C 80 14 01 00 03 80  ................
0190: 07 01 00 0E 80 1B 03 01  00 00 00 02 01 00 0B 80  ................
01A0: 05 AB 01 08 01 00 0A 80  01 B0 01 08 01 00 0C 80  ................
01B0: 14 01 00 03 80 07 01 00  0F 80 1B 03 01 00 00 00  ................
01C0: 02 01 00 0B 80 05 D0 01  08 01 00 0A 80 01 D5 01  ................
01D0: 08 01 00 0C 80 14 01 00  03 80 07 01 00 10 80 1B  ................
```

#### Opcodes

```
  0: 0x0108 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x010D [0x1A] CALL_SUBROUTINE(address=0x014C)
  2: 0x0110 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x011F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  4: 0x012C [0x1C] WAIT(1* ticks)
  5: 0x012F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  6: 0x013E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  7: 0x014B [0x00] END_REQSTACK()

SUBROUTINE_014C:
  8: 0x014C [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  9: 0x0151 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0161
 10: 0x0159 [0x08] ExtData[1]->WorkLocal[1] -= 1*
 11: 0x015E [0x01] GOTO 0x0166
 12: 0x0161 [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_0166:
 13: 0x0166 [0x14] ExtData[1]->WorkLocal[1] *= 10*
 14: 0x016B [0x07] ExtData[1]->WorkLocal[1] += 9*
 15: 0x0170 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0171 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0176 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0186
     0x017E [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0183 [0x01] GOTO 0x018B
     0x0186 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x018B [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0190 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x0195 [0x1B] RETURN
     0x0196 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x019B [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x01AB
     0x01A3 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x01A8 [0x01] GOTO 0x01B0
     0x01AB [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x01B0 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x01B5 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x01BA [0x1B] RETURN
     0x01BB [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x01C0 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x01D0
     0x01C8 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x01CD [0x01] GOTO 0x01D5
     0x01D0 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x01D5 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x01DA [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x01DF [0x1B] RETURN
```
