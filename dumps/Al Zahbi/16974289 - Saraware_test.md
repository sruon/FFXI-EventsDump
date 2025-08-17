# 16974289 - Saraware_test

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al Zahbi (ID: 48) |
| Block Size       | 268 bytes         |
| Total Events     | 2                 |
| References Count | 13                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [99](#event-99)       | 0x0001       |    188 |             38 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E8F      |        7823 |
|       1 | 0x0000      |           0 |
|       2 | 0x0014      |          20 |
|       3 | 0x0001      |           1 |
|       4 | 0x0002      |           2 |
|       5 | 0x0003      |           3 |
|       6 | 0x0004      |           4 |
|       7 | 0x0005      |           5 |
|       8 | 0x0006      |           6 |
|       9 | 0x0007      |           7 |
|      10 | 0x0008      |           8 |
|      11 | 0x0009      |           9 |
|      12 | 0x000A      |          10 |

## String References

- **7823**: DEBUG: Whaddaya want? [All NPCs released!/All areas./Block A./Block B./Block C./Sky general down!/Flame general down!/Spring general down!/Stone general down!/Gale general down!/Saved all the prisoners!]

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

### Event 99

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 188 bytes |
| Instructions | 38        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  01 80 25 02 00 10 01 80    .$......%.....
0010: 00 1B 00 03 01 10 02 80  01 BB 00 02 00 10 03 80  ................
0020: 00 2B 00 03 01 10 03 80  01 BB 00 02 00 10 04 80  .+..............
0030: 00 3B 00 03 01 10 04 80  01 BB 00 02 00 10 05 80  .;..............
0040: 00 4B 00 03 01 10 05 80  01 BB 00 02 00 10 06 80  .K..............
0050: 00 5B 00 03 01 10 06 80  01 BB 00 02 00 10 07 80  .[..............
0060: 00 6B 00 03 01 10 07 80  01 BB 00 02 00 10 08 80  .k..............
0070: 00 7B 00 03 01 10 08 80  01 BB 00 02 00 10 09 80  .{..............
0080: 00 8B 00 03 01 10 09 80  01 BB 00 02 00 10 0A 80  ................
0090: 00 9B 00 03 01 10 0A 80  01 BB 00 02 00 10 0B 80  ................
00A0: 00 AB 00 03 01 10 0B 80  01 BB 00 02 00 10 0C 80  ................
00B0: 00 BB 00 03 01 10 0C 80  01 BB 00 21 00           ...........!.   
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7823*, default_option=0*, option_flags=0*)
    → "DEBUG: Whaddaya want? [All NPCs released!/All areas./Block A./Block B./Block C./Sky general down!/Flame general down!/Spring general down!/Stone general down!/Gale general down!/Saved all the prisoners!]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001B
  4: 0x0013 [0x03] Work_Zone[1] = 20*
  5: 0x0018 [0x01] GOTO 0x00BB
  6: 0x001B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x002B
  7: 0x0023 [0x03] Work_Zone[1] = 1*
  8: 0x0028 [0x01] GOTO 0x00BB
  9: 0x002B [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x003B
 10: 0x0033 [0x03] Work_Zone[1] = 2*
 11: 0x0038 [0x01] GOTO 0x00BB
 12: 0x003B [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x004B
 13: 0x0043 [0x03] Work_Zone[1] = 3*
 14: 0x0048 [0x01] GOTO 0x00BB
 15: 0x004B [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x005B
 16: 0x0053 [0x03] Work_Zone[1] = 4*
 17: 0x0058 [0x01] GOTO 0x00BB
 18: 0x005B [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x006B
 19: 0x0063 [0x03] Work_Zone[1] = 5*
 20: 0x0068 [0x01] GOTO 0x00BB
 21: 0x006B [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x007B
 22: 0x0073 [0x03] Work_Zone[1] = 6*
 23: 0x0078 [0x01] GOTO 0x00BB
 24: 0x007B [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x008B
 25: 0x0083 [0x03] Work_Zone[1] = 7*
 26: 0x0088 [0x01] GOTO 0x00BB
 27: 0x008B [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x009B
 28: 0x0093 [0x03] Work_Zone[1] = 8*
 29: 0x0098 [0x01] GOTO 0x00BB
 30: 0x009B [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x00AB
 31: 0x00A3 [0x03] Work_Zone[1] = 9*
 32: 0x00A8 [0x01] GOTO 0x00BB
 33: 0x00AB [0x02] IF !(Work_Zone[0] == 10*) GOTO 0x00BB
 34: 0x00B3 [0x03] Work_Zone[1] = 10*
 35: 0x00B8 [0x01] GOTO 0x00BB

SUBROUTINE_00BB:
 36: 0x00BB [0x21] END_EVENT
 37: 0x00BC [0x00] END_REQSTACK()
```
