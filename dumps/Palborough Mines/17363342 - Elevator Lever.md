# 17363342 - Elevator Lever

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Palborough Mines (ID: 143) |
| Block Size       | 116 bytes                  |
| Total Events     | 2                          |
| References Count | 3                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [9](#event-9)         | 0x0001       |     77 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CA2      |        7330 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |

## String References

- **7330**: Pull lever? [Yes./No.]

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

### Event 9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 77 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    53 F0 FF FF 7F F0 FF  FF 7F 72 65 73 30 53 F0   S........res0S.
0010: FF FF 7F F0 FF FF 7F 72  65 73 32 4A F0 FF FF 7F  .......res2J....
0020: 8E F1 08 01 24 00 80 01  80 01 80 25 02 00 10 01  ....$......%....
0030: 80 00 3C 00 03 01 10 02  80 01 4C 00 02 00 10 02  ..<.......L.....
0040: 80 00 4C 00 03 01 10 01  80 01 4C 00 21 00        ..L.......L.!.  
```

#### Opcodes

```
  0: 0x0001 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res0" with entities [LocalPlayer, LocalPlayer]
  1: 0x000E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res2" with entities [LocalPlayer, LocalPlayer]
  2: 0x001B [0x4A] LocalPlayer looks at Elevator Lever (ID: 17363342/0x0108F18E)
  3: 0x0024 [0x24] CREATE_DIALOG(message_id=7330*, default_option=0*, option_flags=0*)
    → "Pull lever? [Yes./No.]"
  4: 0x002B [0x25] WAIT_DIALOG_SELECT()
  5: 0x002C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003C
  6: 0x0034 [0x03] Work_Zone[1] = 1*
  7: 0x0039 [0x01] GOTO 0x004C
  8: 0x003C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004C
  9: 0x0044 [0x03] Work_Zone[1] = 0*
 10: 0x0049 [0x01] GOTO 0x004C

SUBROUTINE_004C:
 11: 0x004C [0x21] END_EVENT
 12: 0x004D [0x00] END_REQSTACK()
```
