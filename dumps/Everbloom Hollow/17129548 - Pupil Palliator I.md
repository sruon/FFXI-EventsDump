# 17129548 - Pupil Palliator I

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Everbloom Hollow (ID: 86) |
| Block Size       | 188 bytes                 |
| Total Events     | 2                         |
| References Count | 9                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [4](#event-4)         | 0x0001       |    125 |             26 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CAE      |        7342 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x1CAF      |        7343 |
|       4 | 0x0002      |           2 |
|       5 | 0x0003      |           3 |
|       6 | 0x0004      |           4 |
|       7 | 0x0005      |           5 |
|       8 | 0x0006      |           6 |

## String References

- **7342**: Give the physician orders. [Commence healing, stat!/Specify healing methods./Offer moral support./Rest and recover./Issue no orders.]
- **7343**: Prescribe what type of treatment? [Cures and physical healing./Status ailment recovery.]

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

### Event 4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 125 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 19   $......%.......
0010: 00 03 01 10 02 80 01 7C  00 02 00 10 02 80 00 4C  .......|.......L
0020: 00 24 03 80 01 80 01 80  25 02 00 10 01 80 00 39  .$......%......9
0030: 00 03 01 10 04 80 01 49  00 02 00 10 02 80 00 49  .......I.......I
0040: 00 03 01 10 05 80 01 49  00 01 7C 00 02 00 10 04  .......I..|.....
0050: 80 00 5C 00 03 01 10 06  80 01 7C 00 02 00 10 05  ..\.......|.....
0060: 80 00 6C 00 03 01 10 07  80 01 7C 00 02 00 10 06  ..l.......|.....
0070: 80 00 7C 00 03 01 10 08  80 01 7C 00 21 00        ..|.......|.!.  
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7342*, default_option=0*, option_flags=0*)
    → "Give the physician orders. [Commence healing, stat!/Specify healing methods./Offer moral support./Rest and recover./Issue no orders.]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0019
  3: 0x0011 [0x03] Work_Zone[1] = 1*
  4: 0x0016 [0x01] GOTO 0x007C
  5: 0x0019 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004C
  6: 0x0021 [0x24] CREATE_DIALOG(message_id=7343*, default_option=0*, option_flags=0*)
    → "Prescribe what type of treatment? [Cures and physical healing./Status ailment recovery.]"
  7: 0x0028 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0029 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0039
  9: 0x0031 [0x03] Work_Zone[1] = 2*
 10: 0x0036 [0x01] GOTO 0x0049
 11: 0x0039 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0049
 12: 0x0041 [0x03] Work_Zone[1] = 3*
 13: 0x0046 [0x01] GOTO 0x0049

SUBROUTINE_0049:
 14: 0x0049 [0x01] GOTO 0x007C
 15: 0x004C [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x005C
 16: 0x0054 [0x03] Work_Zone[1] = 4*
 17: 0x0059 [0x01] GOTO 0x007C
 18: 0x005C [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x006C
 19: 0x0064 [0x03] Work_Zone[1] = 5*
 20: 0x0069 [0x01] GOTO 0x007C
 21: 0x006C [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x007C
 22: 0x0074 [0x03] Work_Zone[1] = 6*
 23: 0x0079 [0x01] GOTO 0x007C

SUBROUTINE_007C:
 24: 0x007C [0x21] END_EVENT
 25: 0x007D [0x00] END_REQSTACK()
```
