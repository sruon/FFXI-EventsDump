# 17752089 - Library book

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 100 bytes                 |
| Total Events     | 2                         |
| References Count | 5                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [369](#event-369)     | 0x0001       |     52 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FE5      |        8165 |
|       1 | 0x1FE6      |        8166 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x1FE7      |        8167 |

## String References

- **8165**: You hear a strange sound... It appears to be coming from this book.
- **8166**: Check out what's inside? [No way!/Take a peek.]
- **8167**: .........You simply can't open it!

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

### Event 369

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 52 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 24 01 80  02 80 02 80 25 02 00 10   H..#$......%...
0010: 02 80 00 1D 00 03 01 10  02 80 01 31 00 02 00 10  ...........1....
0020: 03 80 00 31 00 03 01 10  03 80 48 04 80 23 01 31  ...1......H..#.1
0030: 00 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [8165*]:
    → "You hear a strange sound... It appears to be coming from this book."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=8166*, default_option=0*, option_flags=0*)
    → "Check out what's inside? [No way!/Take a peek.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001D
  5: 0x0015 [0x03] Work_Zone[1] = 0*
  6: 0x001A [0x01] GOTO 0x0031
  7: 0x001D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0031
  8: 0x0025 [0x03] Work_Zone[1] = 1*
  9: 0x002A [0x48] [System] [8167*]:
    → ".........You simply can't open it!"
 10: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x002E [0x01] GOTO 0x0031

SUBROUTINE_0031:
 12: 0x0031 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0033 [0x21] END_EVENT
 14: 0x0034 [0x00] END_REQSTACK()
```
