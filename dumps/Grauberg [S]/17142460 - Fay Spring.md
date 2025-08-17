# 17142460 - Fay Spring

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Grauberg [S] (ID: 89) |
| Block Size       | 288 bytes             |
| Total Events     | 3                     |
| References Count | 13                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [501](#event-501)     | 0x0001       |    140 |             36 |
| [23](#event-23)       | 0x008D       |     64 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1E75      |        7797 |
|       2 | 0x0000      |           0 |
|       3 | 0x0002      |           2 |
|       4 | 0x09DD      |        2525 |
|       5 | 0x1E76      |        7798 |
|       6 | 0x0003      |           3 |
|       7 | 0x00C8      |         200 |
|       8 | 0x003C      |          60 |
|       9 | 0x048D      |        1165 |
|      10 | 0x1E77      |        7799 |
|      11 | 0x00B4      |         180 |
|      12 | 0x1E78      |        7800 |

## String References

- **7797**: The crystalline waters of this spring are rumored to have the power to purify one's soul...
- **7798**: You release the $0!
- **7799**: <Player> dipped the $3 in the tranquil waters of the Fay Spring...
- **7800**: The $3 now shimmers a brilliant shade of blue!

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

### Event 501

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 140 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 03 01  00 03 10 03 02 00 04 10   ...............
0010: 03 03 00 05 10 20 01 42  02 03 00 00 80 00 2C 00  ..... .B......,.
0020: 48 01 80 23 03 01 10 02  80 01 89 00 02 03 00 03  H..#............
0030: 80 00 89 00 02 01 00 02  80 80 48 00 03 02 10 04  ..........H.....
0040: 80 48 05 80 23 01 84 00  02 01 00 00 80 80 5C 00  .H..#.........\.
0050: 03 02 10 04 80 48 05 80  23 01 84 00 02 01 00 03  .....H..#.......
0060: 80 80 70 00 03 02 10 04  80 48 05 80 23 01 84 00  ..p......H..#...
0070: 02 01 00 06 80 80 84 00  03 02 10 04 80 48 05 80  .............H..
0080: 23 01 84 00 03 01 10 00  80 20 00 21 00           #........ .!.   
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x000B [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  3: 0x0010 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  4: 0x0015 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  5: 0x0017 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x0018 [0x02] IF !(ExtData[1]->WorkLocal[3] == 1*) GOTO 0x002C
  7: 0x0020 [0x48] [System] [7797*]:
    → "The crystalline waters of this spring are rumored to have the power to purify one's soul..."
  8: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0024 [0x03] Work_Zone[1] = 0*
 10: 0x0029 [0x01] GOTO 0x0089
 11: 0x002C [0x02] IF !(ExtData[1]->WorkLocal[3] == 2*) GOTO 0x0089
 12: 0x0034 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0048
 13: 0x003C [0x03] Work_Zone[2] = 2525*
 14: 0x0041 [0x48] [System] [7798*]:
    → "You release the $0!"
 15: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0045 [0x01] GOTO 0x0084
 17: 0x0048 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x005C
 18: 0x0050 [0x03] Work_Zone[2] = 2525*
 19: 0x0055 [0x48] [System] [7798*]:
    → "You release the $0!"
 20: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0059 [0x01] GOTO 0x0084
 22: 0x005C [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x0070
 23: 0x0064 [0x03] Work_Zone[2] = 2525*
 24: 0x0069 [0x48] [System] [7798*]:
    → "You release the $0!"
 25: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x006D [0x01] GOTO 0x0084
 27: 0x0070 [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x0084
 28: 0x0078 [0x03] Work_Zone[2] = 2525*
 29: 0x007D [0x48] [System] [7798*]:
    → "You release the $0!"
 30: 0x0080 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x0081 [0x01] GOTO 0x0084

SUBROUTINE_0084:
 32: 0x0084 [0x03] Work_Zone[1] = 1*

SUBROUTINE_0089:
 33: 0x0089 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 34: 0x008B [0x21] END_EVENT
 35: 0x008C [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 64 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         42 20 01               B .
0090: 45 07 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 02  E..........fdo1.
00A0: 80 1C 08 80 03 02 10 09  80 48 0A 80 1C 0B 80 48  .........H.....H
00B0: 0C 80 1C 08 80 45 07 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
00C0: 66 64 69 31 02 80 1C 08  80 20 00 21 00           fdi1..... .!.   
```

#### Opcodes

```
  0: 0x008D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x008E [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0090 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x00A1 [0x1C] WAIT(60* ticks)
  4: 0x00A4 [0x03] Work_Zone[2] = 1165*
  5: 0x00A9 [0x48] [System] [7799*]:
    → "<Player> dipped the $3 in the tranquil waters of the Fay Spring..."
  6: 0x00AC [0x1C] WAIT(180* ticks)
  7: 0x00AF [0x48] [System] [7800*]:
    → "The $3 now shimmers a brilliant shade of blue!"
  8: 0x00B2 [0x1C] WAIT(60* ticks)
  9: 0x00B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x00C6 [0x1C] WAIT(60* ticks)
 11: 0x00C9 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x00CB [0x21] END_EVENT
 13: 0x00CC [0x00] END_REQSTACK()
```
