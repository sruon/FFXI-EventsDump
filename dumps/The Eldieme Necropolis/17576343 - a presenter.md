# 17576343 - a presenter

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | The Eldieme Necropolis (ID: 195) |
| Block Size       | 140 bytes                        |
| Total Events     | 2                                |
| References Count | 6                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [500](#event-500)     | 0x0001       |     90 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CDA      |        7386 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x0002      |           2 |
|       4 | 0x0003      |           3 |
|       5 | 0x0004      |           4 |

## String References

- **7386**: WHAT IS YOUR WISH, MASTER? [A PURPLE RIBBON, PLEASE!/QUEST REQUIREMENTS, PLEASE!/TO HAVE DEFEATED THE BOSS!/TO RESET ALL FLAGS, PLEASE!/GIMME A HEAP OF PURPLE RIBBONS!]

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

### Event 500

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 90 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 19   $......%.......
0010: 00 03 01 10 01 80 01 59  00 02 00 10 02 80 00 29  .......Y.......)
0020: 00 03 01 10 02 80 01 59  00 02 00 10 03 80 00 39  .......Y.......9
0030: 00 03 01 10 03 80 01 59  00 02 00 10 04 80 00 49  .......Y.......I
0040: 00 03 01 10 04 80 01 59  00 02 00 10 05 80 00 59  .......Y.......Y
0050: 00 03 01 10 05 80 01 59  00 21 00                 .......Y.!.     
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7386*, default_option=0*, option_flags=0*)
    → "WHAT IS YOUR WISH, MASTER? [A PURPLE RIBBON, PLEASE!/QUEST REQUIREMENTS, PLEASE!/TO HAVE DEFEATED THE BOSS!/TO RESET ALL FLAGS, PLEASE!/GIMME A HEAP OF PURPLE RIBBONS!]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0019
  3: 0x0011 [0x03] Work_Zone[1] = 0*
  4: 0x0016 [0x01] GOTO 0x0059
  5: 0x0019 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0029
  6: 0x0021 [0x03] Work_Zone[1] = 1*
  7: 0x0026 [0x01] GOTO 0x0059
  8: 0x0029 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0039
  9: 0x0031 [0x03] Work_Zone[1] = 2*
 10: 0x0036 [0x01] GOTO 0x0059
 11: 0x0039 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0049
 12: 0x0041 [0x03] Work_Zone[1] = 3*
 13: 0x0046 [0x01] GOTO 0x0059
 14: 0x0049 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0059
 15: 0x0051 [0x03] Work_Zone[1] = 4*
 16: 0x0056 [0x01] GOTO 0x0059

SUBROUTINE_0059:
 17: 0x0059 [0x21] END_EVENT
 18: 0x005A [0x00] END_REQSTACK()
```
