# 17203865 - Logging Point

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Jugner Forest (ID: 104) |
| Block Size       | 232 bytes               |
| Total Events     | 2                       |
| References Count | 14                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [20](#event-20)       | 0x0001       |    150 |             36 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x03FD      |        1021 |
|       2 | 0x0000      |           0 |
|       3 | 0x1EF1      |        7921 |
|       4 | 0xFFFFFFFF  |  4294967295 |
|       5 | 0x1EF4      |        7924 |
|       6 | 0xFFFFFD1E  |  4294966558 |
|       7 | 0x1EEF      |        7919 |
|       8 | 0x0001      |           1 |
|       9 | 0x0429      |        1065 |
|      10 | 0x2EF2      |       12018 |
|      11 | 0x1EEE      |        7918 |
|      12 | 0x1EF0      |        7920 |
|      13 | 0x1EF2      |        7922 |

## String References

- **7918**: Your $7 breaks!
- **7919**: You successfully cut off $0!
- **7920**: You cut off $0, but your $7 breaks in the process.
- **7921**: You are unable to log anything.
- **7922**: You cannot carry any more items. Your inventory is full.
- **7924**: It looks like you might need two people to log here...
- **12018**: <Player> recorded survey data for $1 on the $3.

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

### Event 20

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 150 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 6E F0 FF FF 7F 00  80 99 F0 FF FF 7F 03 09   Bn.............
0010: 10 01 80 03 00 00 06 10  02 04 10 02 80 00 92 00  ................
0020: 02 03 10 02 80 00 69 00  02 02 10 02 80 00 36 00  ......i.......6.
0030: 48 03 80 01 66 00 02 02  10 04 80 00 44 00 48 05  H...f.......D.H.
0040: 80 23 21 00 02 02 10 06  80 00 4E 00 21 00 48 07  .#!.......N.!.H.
0050: 80 02 00 00 08 80 00 66  00 03 03 10 02 10 03 02  .......f........
0060: 10 09 80 48 0A 80 01 8F  00 02 02 10 02 80 00 77  ...H...........w
0070: 00 48 0B 80 01 8F 00 48  0C 80 02 00 00 08 80 00  .H.....H........
0080: 8F 00 03 03 10 02 10 03  02 10 09 80 48 0A 80 01  ............H...
0090: 95 00 48 0D 80 21 00                              ..H..!.         
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x6E] LocalPlayer uses emote 40*
  2: 0x0009 [0x99] Wait for LocalPlayer animation to complete
  3: 0x000E [0x03] Work_Zone[9] = 1021*
  4: 0x0013 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[6]
  5: 0x0018 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0092
  6: 0x0020 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0069
  7: 0x0028 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0036
  8: 0x0030 [0x48] [System] [7921*]:
    → "You are unable to log anything."
  9: 0x0033 [0x01] GOTO 0x0066
 10: 0x0036 [0x02] IF !(Work_Zone[2] == 4294967295*) GOTO 0x0044
 11: 0x003E [0x48] [System] [7924*]:
    → "It looks like you might need two people to log here..."
 12: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0042 [0x21] END_EVENT
 14: 0x0043 [0x00] END_REQSTACK()
 15: 0x0044 [0x02] IF !(Work_Zone[2] == 4294966558*) GOTO 0x004E
 16: 0x004C [0x21] END_EVENT
 17: 0x004D [0x00] END_REQSTACK()
 18: 0x004E [0x48] [System] [7919*]:
    → "You successfully cut off $0!"
 19: 0x0051 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0066
 20: 0x0059 [0x03] Work_Zone[3] = Work_Zone[2]
 21: 0x005E [0x03] Work_Zone[2] = 1065*
 22: 0x0063 [0x48] [System] [12018*]:
    → "<Player> recorded survey data for $1 on the $3."

SUBROUTINE_0066:
 23: 0x0066 [0x01] GOTO 0x008F
 24: 0x0069 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0077
 25: 0x0071 [0x48] [System] [7918*]:
    → "Your $7 breaks!"
 26: 0x0074 [0x01] GOTO 0x008F
 27: 0x0077 [0x48] [System] [7920*]:
    → "You cut off $0, but your $7 breaks in the process."
 28: 0x007A [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x008F
 29: 0x0082 [0x03] Work_Zone[3] = Work_Zone[2]
 30: 0x0087 [0x03] Work_Zone[2] = 1065*
 31: 0x008C [0x48] [System] [12018*]:
    → "<Player> recorded survey data for $1 on the $3."

SUBROUTINE_008F:
 32: 0x008F [0x01] GOTO 0x0095
 33: 0x0092 [0x48] [System] [7922*]:
    → "You cannot carry any more items. Your inventory is full."

SUBROUTINE_0095:
 34: 0x0095 [0x21] END_EVENT
 35: 0x0096 [0x00] END_REQSTACK()
```
