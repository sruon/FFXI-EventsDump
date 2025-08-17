# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Grauberg (ID: 254) |
| Block Size       | 504 bytes                    |
| Total Events     | 7                            |
| References Count | 15                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     37 |              5 |
| [65535.2](#event-655352) | 0x0027       |    185 |             37 |
| [65535.3](#event-655353) | 0x00E0       |     16 |              3 |
| [65535.4](#event-655354) | 0x00F0       |     41 |              5 |
| [2180](#event-2180)      | 0x0119       |    119 |             15 |

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
|       8 | 0x0000      |           0 |
|       9 | 0x0094      |         148 |
|      10 | 0x00F0      |         240 |
|      11 | 0x00C8      |         200 |
|      12 | 0x003C      |          60 |
|      13 | 0x00C9      |         201 |
|      14 | 0x0155      |         341 |

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
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 92 01 F0 FF FF 7F 37 08  80 08 80 08 80 08 80 00  ......7.........
```

#### Opcodes

```
  0: 0x00E0 [0x92] LocalPlayer->Render.Flags3 ^= 0x01
  1: 0x00E6 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=0.000*, y=0.000*, direction=0.0°*
  2: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F0   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: BB 09 80 F0 FF FF 7F 6B  E2 0F 01 6D 61 69 6E 08  .......k...main.
0100: 80 1C 0A 80 45 0B 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0110: 64 6F 31 08 80 1C 0C 80  00                       do1......       
```

#### Opcodes

```
  0: 0x00F0 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17818219/0x010FE26B)], work=[148*, 0*]
  1: 0x0101 [0x1C] WAIT(240* ticks)
  2: 0x0104 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0115 [0x1C] WAIT(60* ticks)
  4: 0x0118 [0x00] END_REQSTACK()
```

### Event 2180

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0119    |
| Data Size    | 119 bytes |
| Instructions | 15        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                             20 01 42 46 01 45 0B            .BF.E.
0120: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 6E 08 80 45  .........blon..E
0130: 0D 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 08 80  ..........blon..
0140: 45 0B 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 08  E..........ovl1.
0150: 80 45 0E 80 F0 FF FF 7F  F0 FF FF 7F 77 61 72 70  .E..........warp
0160: 08 80 BB 09 80 F0 FF FF  7F 6B E2 0F 01 6D 61 69  .........k...mai
0170: 6E 08 80 1C 0A 80 45 0B  80 F0 FF FF 7F F0 FF FF  n.....E.........
0180: 7F 66 64 6F 31 08 80 1C  0C 80 46 00 20 00 21 00  .fdo1.....F. .!.
```

#### Opcodes

```
  0: 0x0119 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x011B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x011C [0x46] CAMERA_CONTROL: Disable user control
  3: 0x011E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x012F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  5: 0x0140 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x0151 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
  7: 0x0162 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17818219/0x010FE26B)], work=[148*, 0*]
  8: 0x0173 [0x1C] WAIT(240* ticks)
  9: 0x0176 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0187 [0x1C] WAIT(60* ticks)
 11: 0x018A [0x46] CAMERA_CONTROL: Restore default settings
 12: 0x018C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x018E [0x21] END_EVENT
 14: 0x018F [0x00] END_REQSTACK()
```
