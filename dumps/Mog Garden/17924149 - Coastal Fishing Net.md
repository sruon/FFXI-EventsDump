# 17924149 - Coastal Fishing Net

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Mog Garden (ID: 280) |
| Block Size       | 540 bytes            |
| Total Events     | 5                    |
| References Count | 22                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [1004](#event-1004)      | 0x0002       |     92 |             26 |
| [1005](#event-1005)      | 0x005E       |    317 |             58 |
| [65535.1](#event-655351) | 0x019B       |      5 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x1CE7      |        7399 |
|       2 | 0x40000000  |  1073741824 |
|       3 | 0x1CE4      |        7396 |
|       4 | 0x1CE5      |        7397 |
|       5 | 0x1CE6      |        7398 |
|       6 | 0x0001      |           1 |
|       7 | 0x1CEC      |        7404 |
|       8 | 0x1CEA      |        7402 |
|       9 | 0x1CE1      |        7393 |
|      10 | 0x003C      |          60 |
|      11 | 0x00C8      |         200 |
|      12 | 0x0017      |          23 |
|      13 | 0x0078      |         120 |
|      14 | 0x0005      |           5 |
|      15 | 0x0002      |           2 |
|      16 | 0x000A      |          10 |
|      17 | 0x0009      |           9 |
|      18 | 0x0046      |          70 |
|      19 | 0x008C      |         140 |
|      20 | 0x00D2      |         210 |
|      21 | 0x0064      |         100 |

## String References

- **7393**: Raise the net? [Yes./No.]
- **7396**: You have already baited the net with $1. Use $0 instead?
- **7397**: Use $0? [Yes./No.]
- **7398**: You baited the net with $0.
- **7399**: You cannot use that here.
- **7402**: $1 is being used as bait.
- **7404**: This net is rank $0.

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

### Event 1004

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 92 bytes |
| Instructions | 26       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       02 02 10 00 80 00  16 00 48 01 80 23 03 01    ........H..#..
0010: 10 02 80 01 5C 00 02 03  10 00 80 01 52 00 48 03  ....\.......R.H.
0020: 80 23 24 04 80 00 80 00  80 25 02 00 10 00 80 00  .#$......%......
0030: 3F 00 42 03 01 10 00 80  48 05 80 23 01 4F 00 02  ?.B.....H..#.O..
0040: 00 10 06 80 00 4F 00 03  01 10 02 80 01 4F 00 01  .....O.......O..
0050: 5C 00 42 48 05 80 23 03  01 10 00 80 21 00        \.BH..#.....!.  
```

#### Opcodes

```
  0: 0x0002 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0016
  1: 0x000A [0x48] [System] [7399*]:
    → "You cannot use that here."
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x03] Work_Zone[1] = 1073741824*
  4: 0x0013 [0x01] GOTO 0x005C
  5: 0x0016 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0052
  6: 0x001E [0x48] [System] [7396*]:
    → "You have already baited the net with $1. Use $0 instead?"
  7: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0022 [0x24] CREATE_DIALOG(message_id=7397*, default_option=0*, option_flags=0*)
    → "Use $0? [Yes./No.]"
  9: 0x0029 [0x25] WAIT_DIALOG_SELECT()
 10: 0x002A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003F
 11: 0x0032 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 12: 0x0033 [0x03] Work_Zone[1] = 0*
 13: 0x0038 [0x48] [System] [7398*]:
    → "You baited the net with $0."
 14: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x003C [0x01] GOTO 0x004F
 16: 0x003F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004F
 17: 0x0047 [0x03] Work_Zone[1] = 1073741824*
 18: 0x004C [0x01] GOTO 0x004F

SUBROUTINE_004F:
 19: 0x004F [0x01] GOTO 0x005C
 20: 0x0052 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 21: 0x0053 [0x48] [System] [7398*]:
    → "You baited the net with $0."
 22: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x0057 [0x03] Work_Zone[1] = 0*

SUBROUTINE_005C:
 24: 0x005C [0x21] END_EVENT
 25: 0x005D [0x00] END_REQSTACK()
```

### Event 1005

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x005E    |
| Data Size    | 317 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            4A F0                J.
0060: FF FF 7F F8 FF FF 7F 48  07 80 23 02 03 10 00 80  .......H..#.....
0070: 01 77 00 48 08 80 23 24  09 80 00 80 00 80 25 02  .w.H..#$......%.
0080: 00 10 06 80 00 8F 00 03  01 10 02 80 01 05 01 02  ................
0090: 00 10 00 80 00 05 01 42  27 80 F0 FF FF 7F 25 1C  .......B'.....%.
00A0: 0A 80 45 0B 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
00B0: 31 00 80 55 0B 80 F0 FF  FF 7F F0 FF FF 7F 66 64  1..U..........fd
00C0: 6F 31 45 0C 80 F8 FF FF  7F F8 FF FF 7F 63 70 6E  o1E..........cpn
00D0: 30 00 80 27 80 F0 FF FF  7F 26 1C 0D 80 45 0B 80  0..'.....&...E..
00E0: F0 FF FF 7F F0 FF FF 7F  66 64 69 32 00 80 55 0B  ........fdi2..U.
00F0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 32 03 01 10  .........fdi2...
0100: 00 80 01 05 01 21 00 03  01 00 00 00 02 01 00 0E  .....!..........
0110: 80 05 1C 01 08 01 00 06  80 01 21 01 08 01 00 0F  ..........!.....
0120: 80 14 01 00 10 80 07 01  00 11 80 1B 03 01 00 00  ................
0130: 00 02 01 00 0E 80 05 41  01 08 01 00 06 80 01 46  .......A.......F
0140: 01 08 01 00 0F 80 14 01  00 10 80 07 01 00 12 80  ................
0150: 1B 03 01 00 00 00 02 01  00 0E 80 05 66 01 08 01  ............f...
0160: 00 06 80 01 6B 01 08 01  00 0F 80 14 01 00 10 80  ....k...........
0170: 07 01 00 13 80 1B 03 01  00 00 00 02 01 00 0E 80  ................
0180: 05 8B 01 08 01 00 06 80  01 90 01 08 01 00 0F 80  ................
0190: 14 01 00 10 80 07 01 00  14 80 1B                 ...........     
```

#### Opcodes

```
  0: 0x005E [0x4A] LocalPlayer looks at EventEntity
  1: 0x0067 [0x48] [System] [7404*]:
    → "This net is rank $0."
  2: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x006B [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0077
  4: 0x0073 [0x48] [System] [7402*]:
    → "$1 is being used as bait."
  5: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0077 [0x24] CREATE_DIALOG(message_id=7393*, default_option=0*, option_flags=0*)
    → "Raise the net? [Yes./No.]"
  7: 0x007E [0x25] WAIT_DIALOG_SELECT()
  8: 0x007F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x008F
  9: 0x0087 [0x03] Work_Zone[1] = 1073741824*
 10: 0x008C [0x01] GOTO 0x0105
 11: 0x008F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0105
 12: 0x0097 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 13: 0x0098 [0x27] REQ_SET(priority=0x80, entity_id=LocalPlayer, tag_num=0x25)
 14: 0x009F [0x1C] WAIT(60* ticks)
 15: 0x00A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x00B3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 17: 0x00C2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cpn0" with entities [EventEntity, EventEntity], work=[23*, 0*]
 18: 0x00D3 [0x27] REQ_SET(priority=0x80, entity_id=LocalPlayer, tag_num=0x26)
 19: 0x00DA [0x1C] WAIT(120* ticks)
 20: 0x00DD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x00EE [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=200*
 22: 0x00FD [0x03] Work_Zone[1] = 0*
 23: 0x0102 [0x01] GOTO 0x0105

SUBROUTINE_0105:
 24: 0x0105 [0x21] END_EVENT
 25: 0x0106 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0107 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x010C [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x011C
     0x0114 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0119 [0x01] GOTO 0x0121
     0x011C [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0121 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0126 [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x012B [0x1B] RETURN
     0x012C [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0131 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0141
     0x0139 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x013E [0x01] GOTO 0x0146
     0x0141 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0146 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x014B [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x0150 [0x1B] RETURN
     0x0151 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0156 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0166
     0x015E [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0163 [0x01] GOTO 0x016B
     0x0166 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x016B [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0170 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x0175 [0x1B] RETURN
     0x0176 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x017B [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x018B
     0x0183 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0188 [0x01] GOTO 0x0190
     0x018B [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0190 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0195 [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x019A [0x1B] RETURN
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x019B  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                   B6 0F 15 80 00             .....
```

#### Opcodes

```
  0: 0x019B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=100*)
  1: 0x019F [0x00] END_REQSTACK()
```
