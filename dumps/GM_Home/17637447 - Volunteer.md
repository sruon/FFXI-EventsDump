# 17637447 - Volunteer

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 108 bytes         |
| Total Events     | 2                 |
| References Count | 6                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [122](#event-122)     | 0x0001       |     59 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x001E      |          30 |
|       2 | 0x2333      |        9011 |
|       3 | 0x0001      |           1 |
|       4 | 0x2334      |        9012 |
|       5 | 0x2335      |        9013 |

## String References

- **9011**: Make a donation? [Yes./No.]
- **9012**: Thank you! All proceeds will benefit the Orphaned Goobbues of Vana'diel.
- **9013**: That's a shame.

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

### Event 122

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 59 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 01 10 00 80 1E  F0 FF FF 7F 1C 01 80 24   B.............$
0010: 02 80 03 80 00 80 25 02  00 10 00 80 00 2B 00 1D  ......%......+..
0020: 04 80 23 03 01 10 03 80  01 3A 00 02 00 10 03 80  ..#......:......
0030: 00 3A 00 1D 05 80 23 01  3A 00 21 00              .:....#.:.!.    
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] Work_Zone[1] = 0*
  2: 0x0007 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x000C [0x1C] WAIT(30* ticks)
  4: 0x000F [0x24] CREATE_DIALOG(message_id=9011*, default_option=1*, option_flags=0*)
    → "Make a donation? [Yes./No.]"
  5: 0x0016 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0017 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x002B
  7: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=9012*)
    → "Thank you! All proceeds will benefit the Orphaned Goobbues of Vana'diel."
  8: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0023 [0x03] Work_Zone[1] = 1*
 10: 0x0028 [0x01] GOTO 0x003A
 11: 0x002B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x003A
 12: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=9013*)
    → "That's a shame."
 13: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0037 [0x01] GOTO 0x003A

SUBROUTINE_003A:
 15: 0x003A [0x21] END_EVENT
 16: 0x003B [0x00] END_REQSTACK()
```
