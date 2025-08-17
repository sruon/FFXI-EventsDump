# 17428977 - Old Casket

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 100 bytes                     |
| Total Events     | 2                             |
| References Count | 7                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [64](#event-64)       | 0x0001       |     47 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CB1      |        7345 |
|       1 | 0x0000      |           0 |
|       2 | 0x1CB2      |        7346 |
|       3 | 0x1CD6      |        7382 |
|       4 | 0x0110      |         272 |
|       5 | 0x1CB3      |        7347 |
|       6 | 0x0001      |           1 |

## String References

- **7345**: Use your $3 to open it? [Yes./No.]
- **7346**: You find a strange brush inside the box.
- **7347**: When the $3 projects the deepest, darkest corner of your soul onto the blank canvas...only then will the doors to rancor open.
- **7382**: A hideous voice rings in your ears...

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

### Event 64

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  01 80 25 02 00 10 01 80    .$......%.....
0010: 00 2C 00 42 48 02 80 23  48 03 80 03 02 10 04 80  .,.BH..#H.......
0020: 48 05 80 23 03 01 10 06  80 01 2C 00 20 00 21 00  H..#......,. .!.
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7345*, default_option=0*, option_flags=0*)
    → "Use your $3 to open it? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x002C
  4: 0x0013 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0014 [0x48] [System] [7346*]:
    → "You find a strange brush inside the box."
  6: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0018 [0x48] [System] [7382*]:
    → "A hideous voice rings in your ears..."
  8: 0x001B [0x03] Work_Zone[2] = 272*
  9: 0x0020 [0x48] [System] [7347*]:
    → "When the $3 projects the deepest, darkest corner of your soul onto the blank canvas...only then will the doors to rancor open."
 10: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0024 [0x03] Work_Zone[1] = 1*
 12: 0x0029 [0x01] GOTO 0x002C

SUBROUTINE_002C:
 13: 0x002C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 14: 0x002E [0x21] END_EVENT
 15: 0x002F [0x00] END_REQSTACK()
```
