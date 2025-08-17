# 17142615 - Shredded Label

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Grauberg [S] (ID: 89) |
| Block Size       | 88 bytes              |
| Total Events     | 2                     |
| References Count | 4                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [22](#event-22)       | 0x0001       |     47 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2000      |        8192 |
|       1 | 0x2001      |        8193 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |

## String References

- **8192**: It appears that using the $3 here will summon forth the enemy. (Your level will be restricted to $1.)
- **8193**: Use the $3? [Yes./No.]

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

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 48 00 80 23 24 01  80 02 80 03 80 25 02 00   BH..#$......%..
0010: 10 03 80 00 1E 00 03 01  10 02 80 01 2E 00 02 00  ................
0020: 10 02 80 00 2E 00 03 01  10 03 80 01 2E 00 21 00  ..............!.
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x48] [System] [8192*]:
    → "It appears that using the $3 here will summon forth the enemy. (Your level will be restricted to $1.)"
  2: 0x0005 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0006 [0x24] CREATE_DIALOG(message_id=8193*, default_option=1*, option_flags=0*)
    → "Use the $3? [Yes./No.]"
  4: 0x000D [0x25] WAIT_DIALOG_SELECT()
  5: 0x000E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001E
  6: 0x0016 [0x03] Work_Zone[1] = 1*
  7: 0x001B [0x01] GOTO 0x002E
  8: 0x001E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x002E
  9: 0x0026 [0x03] Work_Zone[1] = 0*
 10: 0x002B [0x01] GOTO 0x002E

SUBROUTINE_002E:
 11: 0x002E [0x21] END_EVENT
 12: 0x002F [0x00] END_REQSTACK()
```
