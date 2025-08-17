# 16924797 - Dimensional Portal

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Empyreal Paradox (ID: 36) |
| Block Size       | 668 bytes                 |
| Total Events     | 3                         |
| References Count | 14                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [8](#event-8)         | 0x0001       |    132 |             23 |
| [19](#event-19)       | 0x0085       |    450 |             51 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E8D      |        7821 |
|       1 | 0x1E8E      |        7822 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0x40000000  |  1073741824 |
|       5 | 0x004B      |          75 |
|       6 | 0x00B4      |         180 |
|       7 | 0x00C9      |         201 |
|       8 | 0x00C8      |         200 |
|       9 | 0x001E      |          30 |
|      10 | 0x1EDA      |        7898 |
|      11 | 0x0004      |           4 |
|      12 | 0x0002      |           2 |
|      13 | 0x0003      |           3 |

## String References

- **7821**: This device allows teleportation to [Holla/Dem/Mea].
- **7822**: Would you like to teleport? [Ready, willing, and able./No thanks.]
- **7898**: Teleport to where? [Crag of Holla./Crag of Dem./Crag of Mea./Reisenjima Sanctorium./None of the above.]

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

### Event 8

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 132 bytes |
| Instructions | 22        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 24 01 80  02 80 03 80 25 02 00 10   H..#$......%...
0010: 02 80 00 1F 00 03 01 10  04 80 21 00 01 1F 00 42  ..........!....B
0020: 43 00 43 01 03 01 10 02  80 9F 05 80 F0 FF FF 7F  C.C.............
0030: F0 FF FF 7F 6D 61 69 6E  03 80 1C 06 80 45 07 80  ....main.....E..
0040: F8 FF FF 7F F8 FF FF 7F  77 68 6F 31 03 80 55 07  ........who1..U.
0050: 80 F8 FF FF 7F F8 FF FF  7F 77 68 6F 31 45 08 80  .........who1E..
0060: F8 FF FF 7F F8 FF FF 7F  66 64 6F 30 03 80 1C 09  ........fdo0....
0070: 80 30 45 07 80 F8 FF FF  7F F8 FF FF 7F 77 68 69  .0E..........whi
0080: 31 03 80 21 00                                    1..!.           
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7821*]:
    → "This device allows teleportation to [Holla/Dem/Mea]."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7822*, default_option=1*, option_flags=0*)
    → "Would you like to teleport? [Ready, willing, and able./No thanks.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x001F
  5: 0x0015 [0x03] Work_Zone[1] = 1073741824*
  6: 0x001A [0x21] END_EVENT
  7: 0x001B [0x00] END_REQSTACK()

SUBROUTINE_001F:
  8: 0x001F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0020 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0022 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0024 [0x03] Work_Zone[1] = 1*
 12: 0x0029 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[75*, 0*]
 13: 0x003A [0x1C] WAIT(180* ticks)
 14: 0x003D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 15: 0x004E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 16: 0x005D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 17: 0x006E [0x1C] WAIT(30* ticks)
 18: 0x0071 [0x30] SET_UCOFF_CONTINUE_ZERO()
 19: 0x0072 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 20: 0x0083 [0x21] END_EVENT
 21: 0x0084 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x001C [0x01] GOTO 0x001F
```

### Event 19

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0085    |
| Data Size    | 450 bytes |
| Instructions | 51        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                24 0A 80  0B 80 03 80 25 02 00 10       $......%...
0090: 03 80 00 F7 00 03 01 10  02 80 9F 05 80 F0 FF FF  ................
00A0: 7F F0 FF FF 7F 6D 61 69  6E 03 80 1C 06 80 45 07  .....main.....E.
00B0: 80 F8 FF FF 7F F8 FF FF  7F 77 68 6F 31 03 80 55  .........who1..U
00C0: 07 80 F8 FF FF 7F F8 FF  FF 7F 77 68 6F 31 45 08  ..........who1E.
00D0: 80 F8 FF FF 7F F8 FF FF  7F 66 64 6F 30 03 80 1C  .........fdo0...
00E0: 09 80 30 45 07 80 F8 FF  FF 7F F8 FF FF 7F 77 68  ..0E..........wh
00F0: 69 31 03 80 01 45 02 02  00 10 02 80 00 61 01 03  i1...E.......a..
0100: 01 10 0C 80 9F 05 80 F0  FF FF 7F F0 FF FF 7F 6D  ...............m
0110: 61 69 6E 03 80 1C 06 80  45 07 80 F8 FF FF 7F F8  ain.....E.......
0120: FF FF 7F 77 68 6F 31 03  80 55 07 80 F8 FF FF 7F  ...who1..U......
0130: F8 FF FF 7F 77 68 6F 31  45 08 80 F8 FF FF 7F F8  ....who1E.......
0140: FF FF 7F 66 64 6F 30 03  80 1C 09 80 30 45 07 80  ...fdo0.....0E..
0150: F8 FF FF 7F F8 FF FF 7F  77 68 69 31 03 80 01 45  ........whi1...E
0160: 02 02 00 10 0C 80 00 CB  01 03 01 10 0D 80 9F 05  ................
0170: 80 F0 FF FF 7F F0 FF FF  7F 6D 61 69 6E 03 80 1C  .........main...
0180: 06 80 45 07 80 F8 FF FF  7F F8 FF FF 7F 77 68 6F  ..E..........who
0190: 31 03 80 55 07 80 F8 FF  FF 7F F8 FF FF 7F 77 68  1..U..........wh
01A0: 6F 31 45 08 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F  o1E..........fdo
01B0: 30 03 80 1C 09 80 30 45  07 80 F8 FF FF 7F F8 FF  0.....0E........
01C0: FF 7F 77 68 69 31 03 80  01 45 02 02 00 10 0D 80  ..whi1...E......
01D0: 00 35 02 03 01 10 0B 80  9F 05 80 F0 FF FF 7F F0  .5..............
01E0: FF FF 7F 6D 61 69 6E 03  80 1C 06 80 45 07 80 F8  ...main.....E...
01F0: FF FF 7F F8 FF FF 7F 77  68 6F 31 03 80 55 07 80  .......who1..U..
0200: F8 FF FF 7F F8 FF FF 7F  77 68 6F 31 45 08 80 F8  ........who1E...
0210: FF FF 7F F8 FF FF 7F 66  64 6F 30 03 80 1C 09 80  .......fdo0.....
0220: 30 45 07 80 F8 FF FF 7F  F8 FF FF 7F 77 68 69 31  0E..........whi1
0230: 03 80 01 45 02 02 00 10  0B 80 00 45 02 03 01 10  ...E.......E....
0240: 04 80 01 45 02 21 00                              ...E.!.         
```

#### Opcodes

```
  0: 0x0085 [0x24] CREATE_DIALOG(message_id=7898*, default_option=4*, option_flags=0*)
    → "Teleport to where? [Crag of Holla./Crag of Dem./Crag of Mea./Reisenjima Sanctorium./None of the above.]"
  1: 0x008C [0x25] WAIT_DIALOG_SELECT()
  2: 0x008D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F7
  3: 0x0095 [0x03] Work_Zone[1] = 1*
  4: 0x009A [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[75*, 0*]
  5: 0x00AB [0x1C] WAIT(180* ticks)
  6: 0x00AE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
  7: 0x00BF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
  8: 0x00CE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
  9: 0x00DF [0x1C] WAIT(30* ticks)
 10: 0x00E2 [0x30] SET_UCOFF_CONTINUE_ZERO()
 11: 0x00E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 12: 0x00F4 [0x01] GOTO 0x0245
 13: 0x00F7 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0161
 14: 0x00FF [0x03] Work_Zone[1] = 2*
 15: 0x0104 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[75*, 0*]
 16: 0x0115 [0x1C] WAIT(180* ticks)
 17: 0x0118 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 18: 0x0129 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 19: 0x0138 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 20: 0x0149 [0x1C] WAIT(30* ticks)
 21: 0x014C [0x30] SET_UCOFF_CONTINUE_ZERO()
 22: 0x014D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 23: 0x015E [0x01] GOTO 0x0245
 24: 0x0161 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x01CB
 25: 0x0169 [0x03] Work_Zone[1] = 3*
 26: 0x016E [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[75*, 0*]
 27: 0x017F [0x1C] WAIT(180* ticks)
 28: 0x0182 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 29: 0x0193 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 30: 0x01A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 31: 0x01B3 [0x1C] WAIT(30* ticks)
 32: 0x01B6 [0x30] SET_UCOFF_CONTINUE_ZERO()
 33: 0x01B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 34: 0x01C8 [0x01] GOTO 0x0245
 35: 0x01CB [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0235
 36: 0x01D3 [0x03] Work_Zone[1] = 4*
 37: 0x01D8 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[75*, 0*]
 38: 0x01E9 [0x1C] WAIT(180* ticks)
 39: 0x01EC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 40: 0x01FD [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 41: 0x020C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 42: 0x021D [0x1C] WAIT(30* ticks)
 43: 0x0220 [0x30] SET_UCOFF_CONTINUE_ZERO()
 44: 0x0221 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 45: 0x0232 [0x01] GOTO 0x0245
 46: 0x0235 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0245
 47: 0x023D [0x03] Work_Zone[1] = 1073741824*
 48: 0x0242 [0x01] GOTO 0x0245

SUBROUTINE_0245:
 49: 0x0245 [0x21] END_EVENT
 50: 0x0246 [0x00] END_REQSTACK()
```
