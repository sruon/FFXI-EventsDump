# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Crawlers' Nest (ID: 197) |
| Block Size       | 548 bytes                |
| Total Events     | 7                        |
| References Count | 20                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     37 |              5 |
| [65535.2](#event-655352) | 0x0027       |    185 |             37 |
| [4](#event-4)            | 0x00E0       |     42 |             12 |
| [5](#event-5)            | 0x010A       |     19 |              3 |
| [6](#event-6)            | 0x011D       |    138 |             19 |

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
|       8 | 0x00C6      |         198 |
|       9 | 0x00C9      |         201 |
|      10 | 0x1C71      |        7281 |
|      11 | 0x0000      |           0 |
|      12 | 0x5C9EB     |      379371 |
|      13 | 0x07D5      |        2005 |
|      14 | 0xFFFF8214  |  4294935060 |
|      15 | 0x0359      |         857 |
|      16 | 0x0013      |          19 |
|      17 | 0x00C8      |         200 |
|      18 | 0x00B4      |         180 |
|      19 | 0x1C7A      |        7290 |

## String References

- **7281**: Bury $3 & $3? [Yes./No.]

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

### Event 4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E0   |
| Data Size    | 42 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 20 01 42 06 01 10 03 02  10 08 80 03 03 10 09 80   .B.............
00F0: 24 0A 80 01 80 0B 80 25  02 00 10 0B 80 00 08 01  $......%........
0100: 03 01 10 01 80 01 08 01  21 00                    ........!.      
```

#### Opcodes

```
  0: 0x00E0 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00E2 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00E3 [0x06] Work_Zone[1] = 0
  3: 0x00E6 [0x03] Work_Zone[2] = 198*
  4: 0x00EB [0x03] Work_Zone[3] = 201*
  5: 0x00F0 [0x24] CREATE_DIALOG(message_id=7281*, default_option=1*, option_flags=0*)
    → "Bury $3 & $3? [Yes./No.]"
  6: 0x00F7 [0x25] WAIT_DIALOG_SELECT()
  7: 0x00F8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0108
  8: 0x0100 [0x03] Work_Zone[1] = 1*
  9: 0x0105 [0x01] GOTO 0x0108

SUBROUTINE_0108:
 10: 0x0108 [0x21] END_EVENT
 11: 0x0109 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010A   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                45 09 80 F0 FF FF            E.....
0110: 7F F0 FF FF 7F 71 73 74  63 0B 80 21 00           .....qstc..!.   
```

#### Opcodes

```
  0: 0x010A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  1: 0x011B [0x21] END_EVENT
  2: 0x011C [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x011D    |
| Data Size    | 138 bytes |
| Instructions | 19        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                         42 20 01               B .
0120: 46 01 45 02 80 F0 FF FF  7F F0 FF FF 7F 73 30 33  F.E..........s03
0130: 39 0B 80 4E 00 5F 51 0C  01 22 00 37 0C 80 0D 80  9..N._Q..".7....
0140: 0E 80 0F 80 38 10 80 45  11 80 F0 FF FF 7F F0 FF  ....8..E........
0150: FF 7F 66 64 69 31 0B 80  1C 12 80 2B 5F 51 0C 01  ..fdi1.....+_Q..
0160: 13 80 23 45 11 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ..#E..........fd
0170: 6F 32 0B 80 55 11 80 F0  FF FF 7F F0 FF FF 7F 66  o2..U..........f
0180: 64 6F 32 46 00 52 02 80  F0 FF FF 7F F0 FF FF 7F  do2F.R..........
0190: 73 30 33 39 45 11 80 F0  FF FF 7F F0 FF FF 7F 66  s039E..........f
01A0: 64 69 31 0B 80 21 00                              di1..!.         
```

#### Opcodes

```
  0: 0x011D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x011E [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0120 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0122 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s039" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
  4: 0x0133 [0x4E] SET_ENTITY_HIDE_FLAG: Show Olavia (ID: 17584479/0x010C515F)
  5: 0x0139 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  6: 0x013B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=379.371*, z=2.005*, y=-32.236*, direction=75.3°*
  7: 0x0144 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x0147 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0158 [0x1C] WAIT(180* ticks)
 10: 0x015B [0x2B] Olavia (ID: 17584479/0x010C515F) [7290*]:
    → "So, you're the [guy/lady] they sent to escort me through this place. I was wondering when you'd show up. Come on. Follow me."
 11: 0x0162 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0163 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0174 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 14: 0x0183 [0x46] CAMERA_CONTROL: Restore default settings
 15: 0x0185 [0x52] END_LOAD_SCHEDULER: End scheduler "s039" with entities [LocalPlayer, LocalPlayer], work=2*
 16: 0x0194 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x01A5 [0x21] END_EVENT
 18: 0x01A6 [0x00] END_REQSTACK()
```
