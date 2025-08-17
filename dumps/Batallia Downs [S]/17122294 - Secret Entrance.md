# 17122294 - Secret Entrance

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Batallia Downs [S] (ID: 84) |
| Block Size       | 380 bytes                   |
| Total Events     | 2                           |
| References Count | 19                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [41](#event-41)       | 0x0001       |    279 |             41 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E31      |        7729 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x0009      |           9 |
|       4 | 0x0002      |           2 |
|       5 | 0x0013      |          19 |
|       6 | 0x0003      |           3 |
|       7 | 0x001D      |          29 |
|       8 | 0x0004      |           4 |
|       9 | 0x0027      |          39 |
|      10 | 0x0005      |           5 |
|      11 | 0x0031      |          49 |
|      12 | 0x0006      |           6 |
|      13 | 0x0007      |           7 |
|      14 | 0x003B      |          59 |
|      15 | 0x0008      |           8 |
|      16 | 0x0045      |          69 |
|      17 | 0x003C      |          60 |
|      18 | 0x00C8      |         200 |

## String References

- **7729**: Enter the Eldieme Necropolis? [Yes./No.]

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

### Event 41

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 279 bytes |
| Instructions | 41        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 02 80  25 02 00 10 02 80 00 06   $......%.......
0010: 01 43 00 43 01 42 02 87  7F 01 80 80 30 00 66 03  .C.C.B......0.f.
0020: 80 F0 FF FF 7F F0 FF FF  7F 73 68 61 30 01 E6 00  .........sha0...
0030: 02 87 7F 04 80 80 4A 00  66 05 80 F0 FF FF 7F F0  ......J.f.......
0040: FF FF 7F 73 68 61 30 01  E6 00 02 87 7F 06 80 80  ...sha0.........
0050: 64 00 66 07 80 F0 FF FF  7F F0 FF FF 7F 73 68 61  d.f..........sha
0060: 30 01 E6 00 02 87 7F 08  80 80 7E 00 66 09 80 F0  0.........~.f...
0070: FF FF 7F F0 FF FF 7F 73  68 61 30 01 E6 00 02 87  .......sha0.....
0080: 7F 0A 80 80 98 00 66 0B  80 F0 FF FF 7F F0 FF FF  ......f.........
0090: 7F 73 68 61 30 01 E6 00  02 87 7F 0C 80 80 B2 00  .sha0...........
00A0: 66 0B 80 F0 FF FF 7F F0  FF FF 7F 73 68 61 30 01  f..........sha0.
00B0: E6 00 02 87 7F 0D 80 80  CC 00 66 0E 80 F0 FF FF  ..........f.....
00C0: 7F F0 FF FF 7F 73 68 61  30 01 E6 00 02 87 7F 0F  .....sha0.......
00D0: 80 80 E6 00 66 10 80 F0  FF FF 7F F0 FF FF 7F 73  ....f..........s
00E0: 68 61 30 01 E6 00 1C 11  80 45 12 80 F0 FF FF 7F  ha0......E......
00F0: F0 FF FF 7F 66 64 6F 31  02 80 1C 11 80 03 01 10  ....fdo1........
0100: 01 80 30 01 16 01 02 00  10 01 80 00 16 01 03 01  ..0.............
0110: 10 02 80 01 16 01 21 00                           ......!.        
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7729*, default_option=1*, option_flags=0*)
    → "Enter the Eldieme Necropolis? [Yes./No.]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0106
  3: 0x0011 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  4: 0x0013 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  5: 0x0015 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x0016 [0x02] IF !(LocalPlayer->Race == 1*) GOTO 0x0030
  7: 0x001E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [LocalPlayer, LocalPlayer], work=9*
  8: 0x002D [0x01] GOTO 0x00E6
  9: 0x0030 [0x02] IF !(LocalPlayer->Race == 2*) GOTO 0x004A
 10: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [LocalPlayer, LocalPlayer], work=19*
 11: 0x0047 [0x01] GOTO 0x00E6
 12: 0x004A [0x02] IF !(LocalPlayer->Race == 3*) GOTO 0x0064
 13: 0x0052 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [LocalPlayer, LocalPlayer], work=29*
 14: 0x0061 [0x01] GOTO 0x00E6
 15: 0x0064 [0x02] IF !(LocalPlayer->Race == 4*) GOTO 0x007E
 16: 0x006C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [LocalPlayer, LocalPlayer], work=39*
 17: 0x007B [0x01] GOTO 0x00E6
 18: 0x007E [0x02] IF !(LocalPlayer->Race == 5*) GOTO 0x0098
 19: 0x0086 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [LocalPlayer, LocalPlayer], work=49*
 20: 0x0095 [0x01] GOTO 0x00E6
 21: 0x0098 [0x02] IF !(LocalPlayer->Race == 6*) GOTO 0x00B2
 22: 0x00A0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [LocalPlayer, LocalPlayer], work=49*
 23: 0x00AF [0x01] GOTO 0x00E6
 24: 0x00B2 [0x02] IF !(LocalPlayer->Race == 7*) GOTO 0x00CC
 25: 0x00BA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [LocalPlayer, LocalPlayer], work=59*
 26: 0x00C9 [0x01] GOTO 0x00E6
 27: 0x00CC [0x02] IF !(LocalPlayer->Race == 8*) GOTO 0x00E6
 28: 0x00D4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [LocalPlayer, LocalPlayer], work=69*
 29: 0x00E3 [0x01] GOTO 0x00E6

SUBROUTINE_00E6:
 30: 0x00E6 [0x1C] WAIT(60* ticks)
 31: 0x00E9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x00FA [0x1C] WAIT(60* ticks)
 33: 0x00FD [0x03] Work_Zone[1] = 1*
 34: 0x0102 [0x30] SET_UCOFF_CONTINUE_ZERO()
 35: 0x0103 [0x01] GOTO 0x0116
 36: 0x0106 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0116
 37: 0x010E [0x03] Work_Zone[1] = 0*
 38: 0x0113 [0x01] GOTO 0x0116

SUBROUTINE_0116:
 39: 0x0116 [0x21] END_EVENT
 40: 0x0117 [0x00] END_REQSTACK()
```
