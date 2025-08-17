# 16921072 - Cermet Portal

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | The Garden of Ru'Hmet (ID: 35) |
| Block Size       | 704 bytes                      |
| Total Events     | 4                              |
| References Count | 15                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [139](#event-139)     | 0x0001       |    209 |             39 |
| [140](#event-140)     | 0x00D2       |    200 |             36 |
| [141](#event-141)     | 0x019A       |    200 |             36 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DDD      |        7645 |
|       1 | 0x02C4      |         708 |
|       2 | 0x1DDF      |        7647 |
|       3 | 0x1DDC      |        7644 |
|       4 | 0x0001      |           1 |
|       5 | 0x0000      |           0 |
|       6 | 0x00C9      |         201 |
|       7 | 0x003C      |          60 |
|       8 | 0x0013      |          19 |
|       9 | 0x005E      |          94 |
|      10 | 0x0078      |         120 |
|      11 | 0x005A      |          90 |
|      12 | 0x00C8      |         200 |
|      13 | 0x1DDE      |        7646 |
|      14 | 0x1DD8      |        7640 |

## String References

- **7640**: Investigate the portal? [Yes./No.]
- **7644**: Hold up the $3? [Yes./No.]
- **7645**: This portal only allows passage in one direction.
- **7646**: This portal has been badly damaged...
- **7647**: The $3 is humming in response to the device...

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

### Event 139

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 209 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 48 00 80 23 03  02 10 01 80 48 02 80 23    .H..#.....H..#
0010: 24 03 80 04 80 05 80 25  02 00 10 05 80 00 BE 00  $......%........
0020: 43 00 43 01 46 01 42 45  06 80 F0 FF FF 7F F0 FF  C.C.F.BE........
0030: FF 7F 77 68 6F 31 05 80  1C 07 80 38 08 80 45 09  ..who1.....8..E.
0040: 80 F0 FF FF 7F F0 FF FF  7F 65 78 33 35 05 80 29  .........ex35..)
0050: 01 F0 FF FF 7F 14 29 01  F0 FF FF 7F 12 45 06 80  ......)......E..
0060: F0 FF FF 7F F0 FF FF 7F  77 68 69 31 05 80 1C 0A  ........whi1....
0070: 80 4C 1C 0A 80 27 01 F0  FF FF 7F 13 1C 0B 80 45  .L...'.........E
0080: 0C 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 05 80  ..........fdo1..
0090: 1C 0A 80 4D 52 09 80 F0  FF FF 7F F0 FF FF 7F 65  ...MR..........e
00A0: 78 33 35 46 00 03 01 10  04 80 45 0C 80 F0 FF FF  x35F......E.....
00B0: 7F F0 FF FF 7F 66 64 69  31 05 80 01 CE 00 02 00  .....fdi1.......
00C0: 10 04 80 00 CE 00 03 01  10 05 80 01 CE 00 20 00  .............. .
00D0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x48] [System] [7645*]:
    → "This portal only allows passage in one direction."
  2: 0x0006 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0007 [0x03] Work_Zone[2] = 708*
  4: 0x000C [0x48] [System] [7647*]:
    → "The $3 is humming in response to the device..."
  5: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0010 [0x24] CREATE_DIALOG(message_id=7644*, default_option=1*, option_flags=0*)
    → "Hold up the $3? [Yes./No.]"
  7: 0x0017 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0018 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00BE
  9: 0x0020 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0022 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0024 [0x46] CAMERA_CONTROL: Disable user control
 12: 0x0026 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 13: 0x0027 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 14: 0x0038 [0x1C] WAIT(60* ticks)
 15: 0x003B [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 16: 0x003E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ex35" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 17: 0x004F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x14)
 18: 0x0056 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x12)
 19: 0x005D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 20: 0x006E [0x1C] WAIT(120* ticks)
 21: 0x0071 [0x4C] EventEntity->StatusEvent = 8 // Open door
 22: 0x0072 [0x1C] WAIT(120* ticks)
 23: 0x0075 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x13)
 24: 0x007C [0x1C] WAIT(90* ticks)
 25: 0x007F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x0090 [0x1C] WAIT(120* ticks)
 27: 0x0093 [0x4D] EventEntity->StatusEvent = 9 // Close door
 28: 0x0094 [0x52] END_LOAD_SCHEDULER: End scheduler "ex35" with entities [LocalPlayer, LocalPlayer], work=94*
 29: 0x00A3 [0x46] CAMERA_CONTROL: Restore default settings
 30: 0x00A5 [0x03] Work_Zone[1] = 1*
 31: 0x00AA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x00BB [0x01] GOTO 0x00CE
 33: 0x00BE [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00CE
 34: 0x00C6 [0x03] Work_Zone[1] = 0*
 35: 0x00CB [0x01] GOTO 0x00CE

SUBROUTINE_00CE:
 36: 0x00CE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 37: 0x00D0 [0x21] END_EVENT
 38: 0x00D1 [0x00] END_REQSTACK()
```

### Event 140

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00D2    |
| Data Size    | 200 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:       20 01 48 0D 80 23  24 0E 80 04 80 05 80 25     .H..#$......%
00E0: 02 00 10 05 80 00 86 01  43 00 43 01 46 01 42 45  ........C.C.F.BE
00F0: 0C 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 05 80  ..........fdo1..
0100: 1C 07 80 38 08 80 45 09  80 F0 FF FF 7F F0 FF FF  ...8..E.........
0110: 7F 69 6E 33 35 05 80 29  01 F0 FF FF 7F 11 29 01  .in35..)......).
0120: F0 FF FF 7F 0F 45 0C 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0130: 66 64 69 31 05 80 1C 0A  80 4C 1C 0A 80 27 01 F0  fdi1.....L...'..
0140: FF FF 7F 10 1C 0B 80 45  0C 80 F0 FF FF 7F F0 FF  .......E........
0150: FF 7F 66 64 6F 31 05 80  1C 0A 80 4D 52 09 80 F0  ..fdo1.....MR...
0160: FF FF 7F F0 FF FF 7F 69  6E 33 35 46 00 03 01 10  .......in35F....
0170: 04 80 45 0C 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
0180: 31 05 80 01 96 01 02 00  10 04 80 00 96 01 03 01  1...............
0190: 10 05 80 01 96 01 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x00D2 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00D4 [0x48] [System] [7646*]:
    → "This portal has been badly damaged..."
  2: 0x00D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00D8 [0x24] CREATE_DIALOG(message_id=7640*, default_option=1*, option_flags=0*)
    → "Investigate the portal? [Yes./No.]"
  4: 0x00DF [0x25] WAIT_DIALOG_SELECT()
  5: 0x00E0 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0186
  6: 0x00E8 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x00EA [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x00EC [0x46] CAMERA_CONTROL: Disable user control
  9: 0x00EE [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x00EF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x0100 [0x1C] WAIT(60* ticks)
 12: 0x0103 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 13: 0x0106 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "in35" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 14: 0x0117 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x11)
 15: 0x011E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x0F)
 16: 0x0125 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x0136 [0x1C] WAIT(120* ticks)
 18: 0x0139 [0x4C] EventEntity->StatusEvent = 8 // Open door
 19: 0x013A [0x1C] WAIT(120* ticks)
 20: 0x013D [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x10)
 21: 0x0144 [0x1C] WAIT(90* ticks)
 22: 0x0147 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x0158 [0x1C] WAIT(120* ticks)
 24: 0x015B [0x4D] EventEntity->StatusEvent = 9 // Close door
 25: 0x015C [0x52] END_LOAD_SCHEDULER: End scheduler "in35" with entities [LocalPlayer, LocalPlayer], work=94*
 26: 0x016B [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x016D [0x03] Work_Zone[1] = 1*
 28: 0x0172 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 29: 0x0183 [0x01] GOTO 0x0196
 30: 0x0186 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0196
 31: 0x018E [0x03] Work_Zone[1] = 0*
 32: 0x0193 [0x01] GOTO 0x0196

SUBROUTINE_0196:
 33: 0x0196 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 34: 0x0198 [0x21] END_EVENT
 35: 0x0199 [0x00] END_REQSTACK()
```

### Event 141

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x019A    |
| Data Size    | 200 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                20 01 48 0D 80 23             .H..#
01A0: 24 0E 80 04 80 05 80 25  02 00 10 05 80 00 4E 02  $......%......N.
01B0: 43 00 43 01 46 01 42 45  0C 80 F0 FF FF 7F F0 FF  C.C.F.BE........
01C0: FF 7F 66 64 6F 31 05 80  1C 07 80 38 08 80 45 09  ..fdo1.....8..E.
01D0: 80 F0 FF FF 7F F0 FF FF  7F 65 78 33 35 05 80 29  .........ex35..)
01E0: 01 F0 FF FF 7F 14 29 01  F0 FF FF 7F 12 45 0C 80  ......)......E..
01F0: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 05 80 1C 0A  ........fdi1....
0200: 80 4C 1C 0A 80 27 01 F0  FF FF 7F 13 1C 0B 80 45  .L...'.........E
0210: 0C 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 05 80  ..........fdo1..
0220: 1C 0A 80 4D 52 09 80 F0  FF FF 7F F0 FF FF 7F 65  ...MR..........e
0230: 78 33 35 46 00 03 01 10  04 80 45 0C 80 F0 FF FF  x35F......E.....
0240: 7F F0 FF FF 7F 66 64 69  31 05 80 01 5E 02 02 00  .....fdi1...^...
0250: 10 04 80 00 5E 02 03 01  10 05 80 01 5E 02 20 00  ....^.......^. .
0260: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x019A [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x019C [0x48] [System] [7646*]:
    → "This portal has been badly damaged..."
  2: 0x019F [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01A0 [0x24] CREATE_DIALOG(message_id=7640*, default_option=1*, option_flags=0*)
    → "Investigate the portal? [Yes./No.]"
  4: 0x01A7 [0x25] WAIT_DIALOG_SELECT()
  5: 0x01A8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x024E
  6: 0x01B0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x01B2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x01B4 [0x46] CAMERA_CONTROL: Disable user control
  9: 0x01B6 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x01B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x01C8 [0x1C] WAIT(60* ticks)
 12: 0x01CB [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 13: 0x01CE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ex35" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 14: 0x01DF [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x14)
 15: 0x01E6 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x12)
 16: 0x01ED [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x01FE [0x1C] WAIT(120* ticks)
 18: 0x0201 [0x4C] EventEntity->StatusEvent = 8 // Open door
 19: 0x0202 [0x1C] WAIT(120* ticks)
 20: 0x0205 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x13)
 21: 0x020C [0x1C] WAIT(90* ticks)
 22: 0x020F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x0220 [0x1C] WAIT(120* ticks)
 24: 0x0223 [0x4D] EventEntity->StatusEvent = 9 // Close door
 25: 0x0224 [0x52] END_LOAD_SCHEDULER: End scheduler "ex35" with entities [LocalPlayer, LocalPlayer], work=94*
 26: 0x0233 [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x0235 [0x03] Work_Zone[1] = 1*
 28: 0x023A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 29: 0x024B [0x01] GOTO 0x025E
 30: 0x024E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x025E
 31: 0x0256 [0x03] Work_Zone[1] = 0*
 32: 0x025B [0x01] GOTO 0x025E

SUBROUTINE_025E:
 33: 0x025E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 34: 0x0260 [0x21] END_EVENT
 35: 0x0261 [0x00] END_REQSTACK()
```
