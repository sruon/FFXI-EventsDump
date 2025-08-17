# 17167163 - Harvesting Point

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 136 bytes                      |
| Total Events     | 2                              |
| References Count | 8                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [901](#event-901)     | 0x0001       |     79 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x002A      |          42 |
|       1 | 0x03FC      |        1020 |
|       2 | 0x0000      |           0 |
|       3 | 0x1BB5      |        7093 |
|       4 | 0x1BB3      |        7091 |
|       5 | 0x1BB2      |        7090 |
|       6 | 0x1BB4      |        7092 |
|       7 | 0x1BB6      |        7094 |

## String References

- **7090**: Your $7 breaks!
- **7091**: You successfully harvest $0!
- **7092**: You harvest $0, but your $7 breaks.
- **7093**: You are unable to harvest anything.
- **7094**: You cannot carry any more items. Your inventory is full.

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

### Event 901

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 79 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 6E F0 FF FF 7F 00  80 99 F0 FF FF 7F 03 09   Bn.............
0010: 10 01 80 02 04 10 02 80  00 4B 00 02 03 10 02 80  .........K......
0020: 00 37 00 02 02 10 02 80  00 31 00 48 03 80 01 34  .7.......1.H...4
0030: 00 48 04 80 01 48 00 02  02 10 02 80 00 45 00 48  .H...H.......E.H
0040: 05 80 01 48 00 48 06 80  01 4E 00 48 07 80 21 00  ...H.H...N.H..!.
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x6E] LocalPlayer uses emote 42*
  2: 0x0009 [0x99] Wait for LocalPlayer animation to complete
  3: 0x000E [0x03] Work_Zone[9] = 1020*
  4: 0x0013 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x004B
  5: 0x001B [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0037
  6: 0x0023 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0031
  7: 0x002B [0x48] [System] [7093*]:
    → "You are unable to harvest anything."
  8: 0x002E [0x01] GOTO 0x0034
  9: 0x0031 [0x48] [System] [7091*]:
    → "You successfully harvest $0!"

SUBROUTINE_0034:
 10: 0x0034 [0x01] GOTO 0x0048
 11: 0x0037 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0045
 12: 0x003F [0x48] [System] [7090*]:
    → "Your $7 breaks!"
 13: 0x0042 [0x01] GOTO 0x0048
 14: 0x0045 [0x48] [System] [7092*]:
    → "You harvest $0, but your $7 breaks."

SUBROUTINE_0048:
 15: 0x0048 [0x01] GOTO 0x004E
 16: 0x004B [0x48] [System] [7094*]:
    → "You cannot carry any more items. Your inventory is full."

SUBROUTINE_004E:
 17: 0x004E [0x21] END_EVENT
 18: 0x004F [0x00] END_REQSTACK()
```
