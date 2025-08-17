# 17814108 - Gauger Trunk

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 240 bytes                      |
| Total Events     | 3                              |
| References Count | 11                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [364](#event-364)     | 0x0001       |      6 |              4 |
| [365](#event-365)     | 0x0007       |    159 |             39 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FCD      |        8141 |
|       1 | 0x48F8      |       18680 |
|       2 | 0x0005      |           5 |
|       3 | 0x1FCE      |        8142 |
|       4 | 0x1FCF      |        8143 |
|       5 | 0x1FD0      |        8144 |
|       6 | 0x0000      |           0 |
|       7 | 0x1FD1      |        8145 |
|       8 | 0x0001      |           1 |
|       9 | 0x000C      |          12 |
|      10 | 0x1FD2      |        8146 |

## String References

- **8141**: It appears sturdily built.
- **8142**: The casket is stocked with $0. A message scrawled on the lid reads: "$1 cruor a pop! No freebies!"
- **8143**: Purchase $0?
- **8144**: You have $0 cruor. Purchase? [Yes./No.]
- **8145**: Purchase how many? (Maximum purchase: 12).
- **8146**: The total fee comes to $0 cruor. Make the purchase?

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

### Event 364

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 21 00                               H..#!.         
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [8141*]:
    → "It appears sturdily built."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x21] END_EVENT
  3: 0x0006 [0x00] END_REQSTACK()
```

### Event 365

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0007    |
| Data Size    | 159 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      03  00 00 02 10 03 02 10 01         .........
0010: 80 03 03 10 02 80 48 03  80 23 48 04 80 23 03 02  ......H..#H..#..
0020: 10 00 00 24 05 80 06 80  06 80 25 02 00 10 06 80  ...$......%.....
0030: 00 96 00 48 07 80 71 10  08 80 71 11 04 10 02 04  ...H..q...q.....
0040: 10 06 80 02 90 00 02 04  10 09 80 05 8A 00 03 02  ................
0050: 10 02 80 14 02 10 04 10  48 0A 80 23 03 02 10 00  ........H..#....
0060: 00 24 05 80 06 80 06 80  25 02 00 10 06 80 00 79  .$......%......y
0070: 00 03 01 10 04 10 01 87  00 02 00 10 08 80 00 87  ................
0080: 00 06 01 10 01 87 00 01  8D 00 06 01 10 01 93 00  ................
0090: 06 01 10 01 A4 00 02 00  10 08 80 00 A4 00 06 01  ................
00A0: 10 01 A4 00 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x0007 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x000C [0x03] Work_Zone[2] = 18680*
  2: 0x0011 [0x03] Work_Zone[3] = 5*
  3: 0x0016 [0x48] [System] [8142*]:
    → "The casket is stocked with $0. A message scrawled on the lid reads: "$1 cruor a pop! No freebies!""
  4: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001A [0x48] [System] [8143*]:
    → "Purchase $0?"
  6: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001E [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
  8: 0x0023 [0x24] CREATE_DIALOG(message_id=8144*, default_option=0*, option_flags=0*)
    → "You have $0 cruor. Purchase? [Yes./No.]"
  9: 0x002A [0x25] WAIT_DIALOG_SELECT()
 10: 0x002B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0096
 11: 0x0033 [0x48] [System] [8145*]:
    → "Purchase how many? (Maximum purchase: 12)."
 12: 0x0036 [0x71] USER_INPUT_HANDLER: Open numerical input dialog (work=1*)
 13: 0x003A [0x71] USER_INPUT_HANDLER: Process numerical input A (work=Work_Zone[4])
 14: 0x003E [0x02] IF !(Work_Zone[4] <= 0*) GOTO 0x0090
 15: 0x0046 [0x02] IF !(Work_Zone[4] > 12*) GOTO 0x008A
 16: 0x004E [0x03] Work_Zone[2] = 5*
 17: 0x0053 [0x14] Work_Zone[2] *= Work_Zone[4]
 18: 0x0058 [0x48] [System] [8146*]:
    → "The total fee comes to $0 cruor. Make the purchase?"
 19: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x005C [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 21: 0x0061 [0x24] CREATE_DIALOG(message_id=8144*, default_option=0*, option_flags=0*)
    → "You have $0 cruor. Purchase? [Yes./No.]"
 22: 0x0068 [0x25] WAIT_DIALOG_SELECT()
 23: 0x0069 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0079
 24: 0x0071 [0x03] Work_Zone[1] = Work_Zone[4]
 25: 0x0076 [0x01] GOTO 0x0087
 26: 0x0079 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0087
 27: 0x0081 [0x06] Work_Zone[1] = 0
 28: 0x0084 [0x01] GOTO 0x0087

SUBROUTINE_0087:
 29: 0x0087 [0x01] GOTO 0x008D
 30: 0x008A [0x06] Work_Zone[1] = 0

SUBROUTINE_008D:
 31: 0x008D [0x01] GOTO 0x0093
 32: 0x0090 [0x06] Work_Zone[1] = 0

SUBROUTINE_0093:
 33: 0x0093 [0x01] GOTO 0x00A4
 34: 0x0096 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A4
 35: 0x009E [0x06] Work_Zone[1] = 0
 36: 0x00A1 [0x01] GOTO 0x00A4

SUBROUTINE_00A4:
 37: 0x00A4 [0x21] END_EVENT
 38: 0x00A5 [0x00] END_REQSTACK()
```
