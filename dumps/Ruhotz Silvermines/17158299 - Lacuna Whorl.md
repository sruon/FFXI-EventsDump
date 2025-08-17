# 17158299 - Lacuna Whorl

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Ruhotz Silvermines (ID: 93) |
| Block Size       | 88 bytes                    |
| Total Events     | 2                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [3](#event-3)         | 0x0001       |     46 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D2C      |        7468 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x0002      |           2 |

## String References

- **7468**: Leave the area? [Yes./No.]

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

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 46 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  02 80 25 02 00 10 02 80    .$......%.....
0010: 00 1B 00 03 01 10 01 80  01 2B 00 02 00 10 01 80  .........+......
0020: 00 2B 00 03 01 10 03 80  01 2B 00 20 00 21 00     .+.......+. .!. 
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7468*, default_option=1*, option_flags=0*)
    → "Leave the area? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001B
  4: 0x0013 [0x03] Work_Zone[1] = 1*
  5: 0x0018 [0x01] GOTO 0x002B
  6: 0x001B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x002B
  7: 0x0023 [0x03] Work_Zone[1] = 2*
  8: 0x0028 [0x01] GOTO 0x002B

SUBROUTINE_002B:
  9: 0x002B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x002D [0x21] END_EVENT
 11: 0x002E [0x00] END_REQSTACK()
```
