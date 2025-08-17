# 17371595 - Altar of Offerings

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Giddeus (ID: 145) |
| Block Size       | 80 bytes          |
| Total Events     | 3                 |
| References Count | 4                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [60](#event-60)       | 0x0001       |      6 |              4 |
| [53](#event-53)       | 0x0007       |     27 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CAD      |        7341 |
|       1 | 0x1CAB      |        7339 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |

## String References

- **7339**: An offering from Windurst sits here. [Retrieve the offering./Leave it alone.]
- **7341**: There is an offering bag with the seal of Windurst on it.

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 21 00                               H..#!.         
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7341*]:
    → "There is an offering bag with the seal of Windurst on it."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x21] END_EVENT
  3: 0x0006 [0x00] END_REQSTACK()
```

### Event 53

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 27 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      42  24 01 80 02 80 03 80 25         B$......%
0010: 02 00 10 03 80 00 20 00  03 01 10 02 80 01 20 00  ...... ....... .
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0007 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0008 [0x24] CREATE_DIALOG(message_id=7339*, default_option=1*, option_flags=0*)
    → "An offering from Windurst sits here. [Retrieve the offering./Leave it alone.]"
  2: 0x000F [0x25] WAIT_DIALOG_SELECT()
  3: 0x0010 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0020
  4: 0x0018 [0x03] Work_Zone[1] = 1*
  5: 0x001D [0x01] GOTO 0x0020

SUBROUTINE_0020:
  6: 0x0020 [0x21] END_EVENT
  7: 0x0021 [0x00] END_REQSTACK()
```
