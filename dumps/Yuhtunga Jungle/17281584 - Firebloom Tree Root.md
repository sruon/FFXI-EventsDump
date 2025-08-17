# 17281584 - Firebloom Tree Root

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Yuhtunga Jungle (ID: 123) |
| Block Size       | 156 bytes                 |
| Total Events     | 3                         |
| References Count | 7                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [14](#event-14)       | 0x0001       |     49 |             14 |
| [18](#event-18)       | 0x0032       |     49 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DF5      |        7669 |
|       1 | 0x1DF6      |        7670 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0002      |           2 |
|       5 | 0x1DF9      |        7673 |
|       6 | 0x1DFA      |        7674 |

## String References

- **7669**: This is the Firebloom Tree.
- **7670**: Cut off a vine? [Yes./No.]
- **7673**: This is the most blessed spot on the tree.
- **7674**: Cut off a piece of wood? [Yes./No.]

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

### Event 14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 49 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 24 01 80  02 80 02 80 25 02 00 10   H..#$......%...
0010: 02 80 00 1E 00 42 03 01  10 03 80 01 2E 00 02 00  .....B..........
0020: 10 03 80 00 2E 00 03 01  10 04 80 01 2E 00 20 00  .............. .
0030: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7669*]:
    → "This is the Firebloom Tree."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7670*, default_option=0*, option_flags=0*)
    → "Cut off a vine? [Yes./No.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001E
  5: 0x0015 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x0016 [0x03] Work_Zone[1] = 1*
  7: 0x001B [0x01] GOTO 0x002E
  8: 0x001E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x002E
  9: 0x0026 [0x03] Work_Zone[1] = 2*
 10: 0x002B [0x01] GOTO 0x002E

SUBROUTINE_002E:
 11: 0x002E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0030 [0x21] END_EVENT
 13: 0x0031 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 49 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       48 05 80 23 24 06  80 02 80 02 80 25 02 00    H..#$......%..
0040: 10 02 80 00 4F 00 42 03  01 10 03 80 01 5F 00 02  ....O.B......_..
0050: 00 10 03 80 00 5F 00 03  01 10 04 80 01 5F 00 20  ....._......._. 
0060: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0032 [0x48] [System] [7673*]:
    → "This is the most blessed spot on the tree."
  1: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0036 [0x24] CREATE_DIALOG(message_id=7674*, default_option=0*, option_flags=0*)
    → "Cut off a piece of wood? [Yes./No.]"
  3: 0x003D [0x25] WAIT_DIALOG_SELECT()
  4: 0x003E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004F
  5: 0x0046 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x0047 [0x03] Work_Zone[1] = 1*
  7: 0x004C [0x01] GOTO 0x005F
  8: 0x004F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x005F
  9: 0x0057 [0x03] Work_Zone[1] = 2*
 10: 0x005C [0x01] GOTO 0x005F

SUBROUTINE_005F:
 11: 0x005F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0061 [0x21] END_EVENT
 13: 0x0062 [0x00] END_REQSTACK()
```
