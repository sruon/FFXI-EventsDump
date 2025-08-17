# 17162840 - Gomi-Hiroi

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 296 bytes                    |
| Total Events     | 2                            |
| References Count | 17                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [304](#event-304)     | 0x0001       |    202 |             61 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x31B3      |       12723 |
|       2 | 0x31B4      |       12724 |
|       3 | 0x31B5      |       12725 |
|       4 | 0x31B8      |       12728 |
|       5 | 0x31B9      |       12729 |
|       6 | 0x31BD      |       12733 |
|       7 | 0x0001      |           1 |
|       8 | 0x31BA      |       12730 |
|       9 | 0x0002      |           2 |
|      10 | 0x31BB      |       12731 |
|      11 | 0x0003      |           3 |
|      12 | 0x31BC      |       12732 |
|      13 | 0x0004      |           4 |
|      14 | 0x31B6      |       12726 |
|      15 | 0x0009      |           9 |
|      16 | 0x31BE      |       12734 |

## String References

- **12723**: Danger!
- **12724**: This NPC will not be used in the game.
- **12725**: In the game Mr. F's NPCs will be used at the start an end of the missions.
- **12726**: Quit mission? [Yeah./No.]
- **12728**: Set difficulty. [Rank 1./Rank 2./Rank 3./Endless Debug Hell.]
- **12729**: Rank 1 quota: 1 object.
- **12730**: Rank 2 quota: 3 objects.
- **12731**: Rank 3 quota: 5 objects.
- **12732**: Endless: No end to garbage.
- **12733**: Ready......GARBAGE!
- **12734**: You have met your quota. Good job, garbage [boy/chick]!

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

### Event 304

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 202 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 02 02 10 00 80 80  85 00 48 01 80 23 48 02   B........H..#H.
0010: 80 23 48 03 80 23 24 04  80 00 80 00 80 25 02 00  .#H..#$......%..
0020: 10 00 80 00 37 00 48 05  80 23 48 06 80 23 03 01  ....7.H..#H..#..
0030: 10 07 80 21 01 82 00 02  00 10 07 80 00 50 00 48  ...!.........P.H
0040: 08 80 23 48 06 80 23 03  01 10 09 80 21 01 82 00  ..#H..#.....!...
0050: 02 00 10 09 80 00 69 00  48 0A 80 23 48 06 80 23  ......i.H..#H..#
0060: 03 01 10 0B 80 21 01 82  00 02 00 10 0B 80 00 82  .....!..........
0070: 00 48 0C 80 23 48 06 80  23 03 01 10 0D 80 21 01  .H..#H..#.....!.
0080: 82 00 01 CA 00 02 02 10  07 80 80 B5 00 24 0E 80  .............$..
0090: 00 80 00 80 25 02 00 10  00 80 00 A6 00 03 01 10  ....%...........
00A0: 0F 80 21 01 B2 00 02 00  10 07 80 00 B2 00 21 01  ..!...........!.
00B0: B2 00 01 CA 00 02 02 10  0B 80 80 CA 00 48 10 80  .............H..
00C0: 23 03 01 10 0F 80 21 01  CA 00 00                 #.....!....     
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0085
  2: 0x000A [0x48] [System] [12723*]:
    → "Danger!"
  3: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000E [0x48] [System] [12724*]:
    → "This NPC will not be used in the game."
  5: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0012 [0x48] [System] [12725*]:
    → "In the game Mr. F's NPCs will be used at the start an end of the missions."
  7: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0016 [0x24] CREATE_DIALOG(message_id=12728*, default_option=0*, option_flags=0*)
    → "Set difficulty. [Rank 1./Rank 2./Rank 3./Endless Debug Hell.]"
  9: 0x001D [0x25] WAIT_DIALOG_SELECT()
 10: 0x001E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0037
 11: 0x0026 [0x48] [System] [12729*]:
    → "Rank 1 quota: 1 object."
 12: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x002A [0x48] [System] [12733*]:
    → "Ready......GARBAGE!"
 14: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x002E [0x03] Work_Zone[1] = 1*
 16: 0x0033 [0x21] END_EVENT

SUBROUTINE_0082:
 17: 0x0082 [0x01] GOTO 0x00CA
 18: 0x0085 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x00B5
 19: 0x008D [0x24] CREATE_DIALOG(message_id=12726*, default_option=0*, option_flags=0*)
    → "Quit mission? [Yeah./No.]"
 20: 0x0094 [0x25] WAIT_DIALOG_SELECT()
 21: 0x0095 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00A6
 22: 0x009D [0x03] Work_Zone[1] = 9*
 23: 0x00A2 [0x21] END_EVENT

SUBROUTINE_00B2:
 24: 0x00B2 [0x01] GOTO 0x00CA
 25: 0x00B5 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x00CA
 26: 0x00BD [0x48] [System] [12734*]:
    → "You have met your quota. Good job, garbage [boy/chick]!"
 27: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x00C1 [0x03] Work_Zone[1] = 9*
 29: 0x00C6 [0x21] END_EVENT

SUBROUTINE_00CA:
 30: 0x00CA [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0034 [0x01] GOTO 0x0082
     0x004D [0x01] GOTO 0x0082
     0x0066 [0x01] GOTO 0x0082
     0x007F [0x01] GOTO 0x0082
# Dead code (unreachable instructions):
     0x00A3 [0x01] GOTO 0x00B2
     0x00AF [0x01] GOTO 0x00B2
# Dead code (unreachable instructions):
     0x00C7 [0x01] GOTO 0x00CA
```
