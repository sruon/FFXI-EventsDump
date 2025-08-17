# 17924147 - Pond Dredger

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Mog Garden (ID: 280) |
| Block Size       | 520 bytes            |
| Total Events     | 3                    |
| References Count | 21                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1002](#event-1002)   | 0x0001       |     87 |             25 |
| [1003](#event-1003)   | 0x0058       |    317 |             58 |

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
|       7 | 0x1CE0      |        7392 |
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

## String References

- **7392**: The net that sits in the middle of this pond is rank $0.
- **7393**: Raise the net? [Yes./No.]
- **7396**: You have already baited the net with $1. Use $0 instead?
- **7397**: Use $0? [Yes./No.]
- **7398**: You baited the net with $0.
- **7399**: You cannot use that here.
- **7402**: $1 is being used as bait.

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

### Event 1002

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 87 bytes |
| Instructions | 25       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    02 02 10 00 80 00 15  00 48 01 80 23 03 01 10   ........H..#...
0010: 02 80 01 56 00 02 03 10  00 80 01 4C 00 48 03 80  ...V.......L.H..
0020: 23 24 04 80 00 80 00 80  25 02 00 10 00 80 00 39  #$......%......9
0030: 00 42 48 05 80 23 01 49  00 02 00 10 06 80 00 49  .BH..#.I.......I
0040: 00 03 01 10 02 80 01 49  00 01 56 00 42 48 05 80  .......I..V.BH..
0050: 23 03 01 10 00 80 21 00                           #.....!.        
```

#### Opcodes

```
  0: 0x0001 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0015
  1: 0x0009 [0x48] [System] [7399*]:
    → "You cannot use that here."
  2: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000D [0x03] Work_Zone[1] = 1073741824*
  4: 0x0012 [0x01] GOTO 0x0056
  5: 0x0015 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x004C
  6: 0x001D [0x48] [System] [7396*]:
    → "You have already baited the net with $1. Use $0 instead?"
  7: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0021 [0x24] CREATE_DIALOG(message_id=7397*, default_option=0*, option_flags=0*)
    → "Use $0? [Yes./No.]"
  9: 0x0028 [0x25] WAIT_DIALOG_SELECT()
 10: 0x0029 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0039
 11: 0x0031 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 12: 0x0032 [0x48] [System] [7398*]:
    → "You baited the net with $0."
 13: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0036 [0x01] GOTO 0x0049
 15: 0x0039 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0049
 16: 0x0041 [0x03] Work_Zone[1] = 1073741824*
 17: 0x0046 [0x01] GOTO 0x0049

SUBROUTINE_0049:
 18: 0x0049 [0x01] GOTO 0x0056
 19: 0x004C [0x42] SET_CLI_EVENT_CANCEL_DATA()
 20: 0x004D [0x48] [System] [7398*]:
    → "You baited the net with $0."
 21: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0051 [0x03] Work_Zone[1] = 0*

SUBROUTINE_0056:
 23: 0x0056 [0x21] END_EVENT
 24: 0x0057 [0x00] END_REQSTACK()
```

### Event 1003

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0058    |
| Data Size    | 317 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          4A F0 FF FF 7F F8 FF FF          J.......
0060: 7F 48 07 80 23 02 03 10  00 80 01 71 00 48 08 80  .H..#......q.H..
0070: 23 24 09 80 00 80 00 80  25 02 00 10 06 80 00 89  #$......%.......
0080: 00 03 01 10 02 80 01 FF  00 02 00 10 00 80 00 FF  ................
0090: 00 42 27 80 F0 FF FF 7F  25 1C 0A 80 45 0B 80 F0  .B'.....%...E...
00A0: FF FF 7F F0 FF FF 7F 66  64 6F 31 00 80 55 0B 80  .......fdo1..U..
00B0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 45 0C 80 F8  ........fdo1E...
00C0: FF FF 7F F8 FF FF 7F 63  70 6E 30 00 80 27 80 F0  .......cpn0..'..
00D0: FF FF 7F 26 1C 0D 80 45  0B 80 F0 FF FF 7F F0 FF  ...&...E........
00E0: FF 7F 66 64 69 32 00 80  55 0B 80 F0 FF FF 7F F0  ..fdi2..U.......
00F0: FF FF 7F 66 64 69 32 03  01 10 00 80 01 FF 00 21  ...fdi2........!
0100: 00 03 01 00 00 00 02 01  00 0E 80 05 16 01 08 01  ................
0110: 00 06 80 01 1B 01 08 01  00 0F 80 14 01 00 10 80  ................
0120: 07 01 00 11 80 1B 03 01  00 00 00 02 01 00 0E 80  ................
0130: 05 3B 01 08 01 00 06 80  01 40 01 08 01 00 0F 80  .;.......@......
0140: 14 01 00 10 80 07 01 00  12 80 1B 03 01 00 00 00  ................
0150: 02 01 00 0E 80 05 60 01  08 01 00 06 80 01 65 01  ......`.......e.
0160: 08 01 00 0F 80 14 01 00  10 80 07 01 00 13 80 1B  ................
0170: 03 01 00 00 00 02 01 00  0E 80 05 85 01 08 01 00  ................
0180: 06 80 01 8A 01 08 01 00  0F 80 14 01 00 10 80 07  ................
0190: 01 00 14 80 1B                                    .....           
```

#### Opcodes

```
  0: 0x0058 [0x4A] LocalPlayer looks at EventEntity
  1: 0x0061 [0x48] [System] [7392*]:
    → "The net that sits in the middle of this pond is rank $0."
  2: 0x0064 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0065 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0071
  4: 0x006D [0x48] [System] [7402*]:
    → "$1 is being used as bait."
  5: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0071 [0x24] CREATE_DIALOG(message_id=7393*, default_option=0*, option_flags=0*)
    → "Raise the net? [Yes./No.]"
  7: 0x0078 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0079 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0089
  9: 0x0081 [0x03] Work_Zone[1] = 1073741824*
 10: 0x0086 [0x01] GOTO 0x00FF
 11: 0x0089 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00FF
 12: 0x0091 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 13: 0x0092 [0x27] REQ_SET(priority=0x80, entity_id=LocalPlayer, tag_num=0x25)
 14: 0x0099 [0x1C] WAIT(60* ticks)
 15: 0x009C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x00AD [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 17: 0x00BC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cpn0" with entities [EventEntity, EventEntity], work=[23*, 0*]
 18: 0x00CD [0x27] REQ_SET(priority=0x80, entity_id=LocalPlayer, tag_num=0x26)
 19: 0x00D4 [0x1C] WAIT(120* ticks)
 20: 0x00D7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x00E8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=200*
 22: 0x00F7 [0x03] Work_Zone[1] = 0*
 23: 0x00FC [0x01] GOTO 0x00FF

SUBROUTINE_00FF:
 24: 0x00FF [0x21] END_EVENT
 25: 0x0100 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0101 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0106 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0116
     0x010E [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0113 [0x01] GOTO 0x011B
     0x0116 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x011B [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0120 [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x0125 [0x1B] RETURN
     0x0126 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x012B [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x013B
     0x0133 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0138 [0x01] GOTO 0x0140
     0x013B [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0140 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0145 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x014A [0x1B] RETURN
     0x014B [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0150 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0160
     0x0158 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x015D [0x01] GOTO 0x0165
     0x0160 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0165 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x016A [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x016F [0x1B] RETURN
     0x0170 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0175 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0185
     0x017D [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0182 [0x01] GOTO 0x018A
     0x0185 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x018A [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x018F [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x0194 [0x1B] RETURN
```
