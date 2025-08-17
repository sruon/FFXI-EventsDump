# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | The Ashu Talif (ID: 60) |
| Block Size       | 624 bytes               |
| Total Events     | 7                       |
| References Count | 19                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [101](#event-101)     | 0x0002       |     26 |              7 |
| [102](#event-102)     | 0x001C       |    194 |             41 |
| [3](#event-3)         | 0x00DE       |     37 |              9 |
| [2](#event-2)         | 0x0103       |    219 |             25 |
| [1](#event-1)         | 0x01DE       |     25 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x00C9      |         201 |
|       4 | 0x008C      |         140 |
|       5 | 0x0005      |           5 |
|       6 | 0x0001      |           1 |
|       7 | 0x0002      |           2 |
|       8 | 0x000A      |          10 |
|       9 | 0x0009      |           9 |
|      10 | 0x0046      |          70 |
|      11 | 0x00D2      |         210 |
|      12 | 0x1DA9      |        7593 |
|      13 | 0x0013      |          19 |
|      14 | 0x00FF      |         255 |
|      15 | 0x00C2      |         194 |
|      16 | 0x0514      |        1300 |
|      17 | 0x028A      |         650 |
|      18 | 0x0258      |         600 |

## String References

- **7593**: Leave the Ashu Talif? [Yes./No.]

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

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 42 45 00 80  F0 FF FF 7F F0 FF FF 7F     .BE..........
0010: 66 64 6F 31 01 80 1C 02  80 30 21 00              fdo1.....0!.    
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0016 [0x1C] WAIT(60* ticks)
  4: 0x0019 [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x001A [0x21] END_EVENT
  6: 0x001B [0x00] END_REQSTACK()
```

### Event 102

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x001C    |
| Data Size    | 194 bytes |
| Instructions | 9         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      20 01 42 9F               .B.
0020: 03 80 F8 FF FF 7F F8 FF  FF 7F 6D 61 69 6E 01 80  ..........main..
0030: 1C 04 80 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0040: 6F 31 01 80 1C 02 80 30  21 00 03 01 00 00 00 02  o1.....0!.......
0050: 01 00 05 80 05 5F 00 08  01 00 06 80 01 64 00 08  ....._.......d..
0060: 01 00 07 80 14 01 00 08  80 07 01 00 09 80 1B 03  ................
0070: 01 00 00 00 02 01 00 05  80 05 84 00 08 01 00 06  ................
0080: 80 01 89 00 08 01 00 07  80 14 01 00 08 80 07 01  ................
0090: 00 0A 80 1B 03 01 00 00  00 02 01 00 05 80 05 A9  ................
00A0: 00 08 01 00 06 80 01 AE  00 08 01 00 07 80 14 01  ................
00B0: 00 08 80 07 01 00 04 80  1B 03 01 00 00 00 02 01  ................
00C0: 00 05 80 05 CE 00 08 01  00 06 80 01 D3 00 08 01  ................
00D0: 00 07 80 14 01 00 08 80  07 01 00 0B 80 1B        ..............  
```

#### Opcodes

```
  0: 0x001C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x001E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x001F [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[201*, 0*]
  3: 0x0030 [0x1C] WAIT(140* ticks)
  4: 0x0033 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x0044 [0x1C] WAIT(60* ticks)
  6: 0x0047 [0x30] SET_UCOFF_CONTINUE_ZERO()
  7: 0x0048 [0x21] END_EVENT
  8: 0x0049 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x004A [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x004F [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x005F
     0x0057 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x005C [0x01] GOTO 0x0064
     0x005F [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0064 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0069 [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x006E [0x1B] RETURN
     0x006F [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0074 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0084
     0x007C [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0081 [0x01] GOTO 0x0089
     0x0084 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0089 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x008E [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x0093 [0x1B] RETURN
     0x0094 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0099 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00A9
     0x00A1 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00A6 [0x01] GOTO 0x00AE
     0x00A9 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00AE [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00B3 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x00B8 [0x1B] RETURN
     0x00B9 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00BE [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00CE
     0x00C6 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00CB [0x01] GOTO 0x00D3
     0x00CE [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00D3 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00D8 [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x00DD [0x1B] RETURN
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DE   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                            24 0C                $.
00E0: 80 06 80 01 80 25 02 00  10 01 80 00 F6 00 03 01  .....%..........
00F0: 10 06 80 01 01 01 02 00  10 06 80 00 01 01 01 01  ................
0100: 01 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x00DE [0x24] CREATE_DIALOG(message_id=7593*, default_option=1*, option_flags=0*)
    → "Leave the Ashu Talif? [Yes./No.]"
  1: 0x00E5 [0x25] WAIT_DIALOG_SELECT()
  2: 0x00E6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F6
  3: 0x00EE [0x03] Work_Zone[1] = 1*
  4: 0x00F3 [0x01] GOTO 0x0101
  5: 0x00F6 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0101
  6: 0x00FE [0x01] GOTO 0x0101

SUBROUTINE_0101:
  7: 0x0101 [0x21] END_EVENT
  8: 0x0102 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0103    |
| Data Size    | 219 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:          42 45 00 80 F8  FF FF 7F F8 FF FF 7F 66     BE..........f
0110: 64 6F 31 01 80 55 00 80  F8 FF FF 7F F8 FF FF 7F  do1..U..........
0120: 66 64 6F 31 4E 01 F0 FF  FF 7F 46 01 38 0D 80 77  fdo1N.....F.8..w
0130: 0E 80 06 80 45 0F 80 F8  FF FF 7F F8 FF FF 7F 73  ....E..........s
0140: 30 30 30 01 80 1C 02 80  45 00 80 F8 FF FF 7F F8  000.....E.......
0150: FF FF 7F 66 64 69 32 01  80 1C 10 80 45 00 80 F8  ...fdi2.....E...
0160: FF FF 7F F8 FF FF 7F 6F  76 6C 31 01 80 52 0F 80  .......ovl1..R..
0170: F8 FF FF 7F F8 FF FF 7F  73 30 30 30 45 0F 80 F8  ........s000E...
0180: FF FF 7F F8 FF FF 7F 73  30 30 31 01 80 1C 11 80  .......s001.....
0190: 45 00 80 F8 FF FF 7F F8  FF FF 7F 66 64 6F 31 01  E..........fdo1.
01A0: 80 55 00 80 F8 FF FF 7F  F8 FF FF 7F 66 64 6F 31  .U..........fdo1
01B0: 52 0F 80 F8 FF FF 7F F8  FF FF 7F 73 30 30 31 4E  R..........s001N
01C0: 00 F0 FF FF 7F 78 46 00  1C 02 80 45 00 80 F8 FF  .....xF....E....
01D0: FF 7F F8 FF FF 7F 66 64  69 31 01 80 21 00        ......fdi1..!.  
```

#### Opcodes

```
  0: 0x0103 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0104 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x0115 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
  3: 0x0124 [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
  4: 0x012A [0x46] CAMERA_CONTROL: Disable user control
  5: 0x012C [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x012F [0x77] SET_EVENT_TIME_WEATHER(hour=255*, weather=1*)
  7: 0x0134 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [EventEntity, EventEntity], work=[194*, 0*]
  8: 0x0145 [0x1C] WAIT(60* ticks)
  9: 0x0148 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 10: 0x0159 [0x1C] WAIT(1300* ticks)
 11: 0x015C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 12: 0x016D [0x52] END_LOAD_SCHEDULER: End scheduler "s000" with entities [EventEntity, EventEntity], work=194*
 13: 0x017C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s001" with entities [EventEntity, EventEntity], work=[194*, 0*]
 14: 0x018D [0x1C] WAIT(650* ticks)
 15: 0x0190 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 16: 0x01A1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 17: 0x01B0 [0x52] END_LOAD_SCHEDULER: End scheduler "s001" with entities [EventEntity, EventEntity], work=194*
 18: 0x01BF [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 19: 0x01C5 [0x78] ENABLE_GAME_TIMER_RESET_WEATHER()
 20: 0x01C6 [0x46] CAMERA_CONTROL: Restore default settings
 21: 0x01C8 [0x1C] WAIT(60* ticks)
 22: 0x01CB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 23: 0x01DC [0x21] END_EVENT
 24: 0x01DD [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01DE   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                            20 01                 .
01E0: 42 45 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  BE..........fdo1
01F0: 01 80 1C 12 80 21 00                              .....!.         
```

#### Opcodes

```
  0: 0x01DE [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x01E0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x01E1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x01F2 [0x1C] WAIT(600* ticks)
  4: 0x01F5 [0x21] END_EVENT
  5: 0x01F6 [0x00] END_REQSTACK()
```
