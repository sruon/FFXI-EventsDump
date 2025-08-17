# 17068442 - Speaking Tubes

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | The Colosseum (ID: 71) |
| Block Size       | 360 bytes              |
| Total Events     | 2                      |
| References Count | 17                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [60](#event-60)       | 0x0001       |    266 |             52 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CBA      |        7354 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x0002      |           2 |
|       4 | 0x0003      |           3 |
|       5 | 0x0004      |           4 |
|       6 | 0x0005      |           5 |
|       7 | 0x0006      |           6 |
|       8 | 0x0007      |           7 |
|       9 | 0x0008      |           8 |
|      10 | 0x0009      |           9 |
|      11 | 0x000A      |          10 |
|      12 | 0x000B      |          11 |
|      13 | 0x000C      |          12 |
|      14 | 0x000D      |          13 |
|      15 | 0x000E      |          14 |
|      16 | 0x000F      |          15 |

## String References

- **7354**: What are your battle orders? [Quit./You're on your own!/Think, and then think again!/Watch your opponent, then attack!/Less thinking, more striking!/Don't think, kill!/Guard! Block! Parry! Hold!/Back off a bit!/Give 'em a little more bite!/Show no mercy!!!]

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

### Event 60

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 266 bytes |
| Instructions | 52        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 19   $......%.......
0010: 00 03 01 10 01 80 01 09  01 02 00 10 02 80 00 29  ...............)
0020: 00 03 01 10 02 80 01 09  01 02 00 10 03 80 00 39  ...............9
0030: 00 03 01 10 03 80 01 09  01 02 00 10 04 80 00 49  ...............I
0040: 00 03 01 10 04 80 01 09  01 02 00 10 05 80 00 59  ...............Y
0050: 00 03 01 10 05 80 01 09  01 02 00 10 06 80 00 69  ...............i
0060: 00 03 01 10 06 80 01 09  01 02 00 10 07 80 00 79  ...............y
0070: 00 03 01 10 07 80 01 09  01 02 00 10 08 80 00 89  ................
0080: 00 03 01 10 08 80 01 09  01 02 00 10 09 80 00 99  ................
0090: 00 03 01 10 09 80 01 09  01 02 00 10 0A 80 00 A9  ................
00A0: 00 03 01 10 0A 80 01 09  01 02 00 10 0B 80 00 B9  ................
00B0: 00 03 01 10 0B 80 01 09  01 02 00 10 0C 80 00 C9  ................
00C0: 00 03 01 10 0C 80 01 09  01 02 00 10 0D 80 00 D9  ................
00D0: 00 03 01 10 0D 80 01 09  01 02 00 10 0E 80 00 E9  ................
00E0: 00 03 01 10 0E 80 01 09  01 02 00 10 0F 80 00 F9  ................
00F0: 00 03 01 10 0F 80 01 09  01 02 00 10 10 80 00 09  ................
0100: 01 03 01 10 10 80 01 09  01 21 00                 .........!.     
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7354*, default_option=0*, option_flags=0*)
    → "What are your battle orders? [Quit./You're on your own!/Think, and then think again!/Watch your opponent, then attack!/Less thinking, more striking!/Don't think, kill!/Guard! Block! Parry! Hold!/Back off a bit!/Give 'em a little more bite!/Show no mercy!!!]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0019
  3: 0x0011 [0x03] Work_Zone[1] = 0*
  4: 0x0016 [0x01] GOTO 0x0109
  5: 0x0019 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0029
  6: 0x0021 [0x03] Work_Zone[1] = 1*
  7: 0x0026 [0x01] GOTO 0x0109
  8: 0x0029 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0039
  9: 0x0031 [0x03] Work_Zone[1] = 2*
 10: 0x0036 [0x01] GOTO 0x0109
 11: 0x0039 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0049
 12: 0x0041 [0x03] Work_Zone[1] = 3*
 13: 0x0046 [0x01] GOTO 0x0109
 14: 0x0049 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0059
 15: 0x0051 [0x03] Work_Zone[1] = 4*
 16: 0x0056 [0x01] GOTO 0x0109
 17: 0x0059 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0069
 18: 0x0061 [0x03] Work_Zone[1] = 5*
 19: 0x0066 [0x01] GOTO 0x0109
 20: 0x0069 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0079
 21: 0x0071 [0x03] Work_Zone[1] = 6*
 22: 0x0076 [0x01] GOTO 0x0109
 23: 0x0079 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0089
 24: 0x0081 [0x03] Work_Zone[1] = 7*
 25: 0x0086 [0x01] GOTO 0x0109
 26: 0x0089 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x0099
 27: 0x0091 [0x03] Work_Zone[1] = 8*
 28: 0x0096 [0x01] GOTO 0x0109
 29: 0x0099 [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x00A9
 30: 0x00A1 [0x03] Work_Zone[1] = 9*
 31: 0x00A6 [0x01] GOTO 0x0109
 32: 0x00A9 [0x02] IF !(Work_Zone[0] == 10*) GOTO 0x00B9
 33: 0x00B1 [0x03] Work_Zone[1] = 10*
 34: 0x00B6 [0x01] GOTO 0x0109
 35: 0x00B9 [0x02] IF !(Work_Zone[0] == 11*) GOTO 0x00C9
 36: 0x00C1 [0x03] Work_Zone[1] = 11*
 37: 0x00C6 [0x01] GOTO 0x0109
 38: 0x00C9 [0x02] IF !(Work_Zone[0] == 12*) GOTO 0x00D9
 39: 0x00D1 [0x03] Work_Zone[1] = 12*
 40: 0x00D6 [0x01] GOTO 0x0109
 41: 0x00D9 [0x02] IF !(Work_Zone[0] == 13*) GOTO 0x00E9
 42: 0x00E1 [0x03] Work_Zone[1] = 13*
 43: 0x00E6 [0x01] GOTO 0x0109
 44: 0x00E9 [0x02] IF !(Work_Zone[0] == 14*) GOTO 0x00F9
 45: 0x00F1 [0x03] Work_Zone[1] = 14*
 46: 0x00F6 [0x01] GOTO 0x0109
 47: 0x00F9 [0x02] IF !(Work_Zone[0] == 15*) GOTO 0x0109
 48: 0x0101 [0x03] Work_Zone[1] = 15*
 49: 0x0106 [0x01] GOTO 0x0109

SUBROUTINE_0109:
 50: 0x0109 [0x21] END_EVENT
 51: 0x010A [0x00] END_REQSTACK()
```
