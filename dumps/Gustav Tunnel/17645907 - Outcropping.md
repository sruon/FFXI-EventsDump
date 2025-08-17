# 17645907 - Outcropping

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Gustav Tunnel (ID: 212) |
| Block Size       | 88 bytes                |
| Total Events     | 2                       |
| References Count | 4                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [15](#event-15)       | 0x0001       |     46 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CDD      |        7389 |
|       1 | 0x1CDE      |        7390 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |

## String References

- **7389**: Engage in "Enemy of the Empire (II)"?
- **7390**: Engage? [Yes./No.]

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

### Event 15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 46 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 24 01 80  02 80 03 80 25 02 00 10   H..#$......%...
0010: 03 80 00 1D 00 03 01 10  02 80 01 2D 00 02 00 10  ...........-....
0020: 02 80 00 2D 00 03 01 10  03 80 01 2D 00 21 00     ...-.......-.!. 
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7389*]:
    → "Engage in "Enemy of the Empire (II)"?"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7390*, default_option=1*, option_flags=0*)
    → "Engage? [Yes./No.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001D
  5: 0x0015 [0x03] Work_Zone[1] = 1*
  6: 0x001A [0x01] GOTO 0x002D
  7: 0x001D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x002D
  8: 0x0025 [0x03] Work_Zone[1] = 0*
  9: 0x002A [0x01] GOTO 0x002D

SUBROUTINE_002D:
 10: 0x002D [0x21] END_EVENT
 11: 0x002E [0x00] END_REQSTACK()
```
