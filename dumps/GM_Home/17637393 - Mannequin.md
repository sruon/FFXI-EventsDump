# 17637393 - Mannequin

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 212 bytes         |
| Total Events     | 2                 |
| References Count | 10                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [42](#event-42)       | 0x0001       |    147 |             31 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1BFD      |        7165 |
|       1 | 0x1BFE      |        7166 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0002      |           2 |
|       5 | 0x0003      |           3 |
|       6 | 0x0004      |           4 |
|       7 | 0x0005      |           5 |
|       8 | 0x0006      |           6 |
|       9 | 0x0007      |           7 |

## String References

- **7165**: Select the race and sex of the mannequin that you want...
- **7166**: Well... [Hume male./Hume female./Elvaan male./Elvaan female./Tarutaru male./Tarutaru female./Mithra./Galka.]

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

### Event 42

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 147 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 24 01 80  02 80 02 80 25 02 00 10   ...#$......%...
0010: 02 80 00 1D 00 03 01 10  02 80 01 92 00 02 00 10  ................
0020: 03 80 00 2D 00 03 01 10  03 80 01 92 00 02 00 10  ...-............
0030: 04 80 00 3D 00 03 01 10  04 80 01 92 00 02 00 10  ...=............
0040: 05 80 00 4D 00 03 01 10  05 80 01 92 00 02 00 10  ...M............
0050: 06 80 00 5D 00 03 01 10  06 80 01 92 00 02 00 10  ...]............
0060: 07 80 00 6D 00 03 01 10  07 80 01 92 00 02 00 10  ...m............
0070: 08 80 00 7D 00 03 01 10  08 80 01 92 00 02 00 10  ...}............
0080: 09 80 00 8D 00 03 01 10  09 80 01 92 00 03 01 10  ................
0090: 02 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7165*)
    → "Select the race and sex of the mannequin that you want..."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7166*, default_option=0*, option_flags=0*)
    → "Well... [Hume male./Hume female./Elvaan male./Elvaan female./Tarutaru male./Tarutaru female./Mithra./Galka.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001D
  5: 0x0015 [0x03] Work_Zone[1] = 0*
  6: 0x001A [0x01] GOTO 0x0092
  7: 0x001D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x002D
  8: 0x0025 [0x03] Work_Zone[1] = 1*
  9: 0x002A [0x01] GOTO 0x0092
 10: 0x002D [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x003D
 11: 0x0035 [0x03] Work_Zone[1] = 2*
 12: 0x003A [0x01] GOTO 0x0092
 13: 0x003D [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x004D
 14: 0x0045 [0x03] Work_Zone[1] = 3*
 15: 0x004A [0x01] GOTO 0x0092
 16: 0x004D [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x005D
 17: 0x0055 [0x03] Work_Zone[1] = 4*
 18: 0x005A [0x01] GOTO 0x0092
 19: 0x005D [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x006D
 20: 0x0065 [0x03] Work_Zone[1] = 5*
 21: 0x006A [0x01] GOTO 0x0092
 22: 0x006D [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x007D
 23: 0x0075 [0x03] Work_Zone[1] = 6*
 24: 0x007A [0x01] GOTO 0x0092
 25: 0x007D [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x008D
 26: 0x0085 [0x03] Work_Zone[1] = 7*
 27: 0x008A [0x01] GOTO 0x0092
 28: 0x008D [0x03] Work_Zone[1] = 0*

SUBROUTINE_0092:
 29: 0x0092 [0x21] END_EVENT
 30: 0x0093 [0x00] END_REQSTACK()
```
