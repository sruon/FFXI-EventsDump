# 16986737 - Harvesting Point

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Wajaom Woodlands (ID: 51) |
| Block Size       | 152 bytes                 |
| Total Events     | 2                         |
| References Count | 9                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [507](#event-507)     | 0x0001       |     89 |             22 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x002A      |          42 |
|       1 | 0x03FC      |        1020 |
|       2 | 0x0000      |           0 |
|       3 | 0x1D02      |        7426 |
|       4 | 0xFFFFFCF8  |  4294966520 |
|       5 | 0x1D00      |        7424 |
|       6 | 0x1CFF      |        7423 |
|       7 | 0x1D01      |        7425 |
|       8 | 0x1D03      |        7427 |

## String References

- **7423**: Your $7 breaks!
- **7424**: You successfully harvest $0!
- **7425**: You harvest $0, but your $7 breaks.
- **7426**: You are unable to harvest anything.
- **7427**: You cannot carry any more items. Your inventory is full.

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

### Event 507

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 89 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 6E F0 FF FF 7F 00  80 99 F0 FF FF 7F 03 09   Bn.............
0010: 10 01 80 02 04 10 02 80  00 55 00 02 03 10 02 80  .........U......
0020: 00 41 00 02 02 10 02 80  00 31 00 48 03 80 01 3E  .A.......1.H...>
0030: 00 02 02 10 04 80 00 3B  00 21 00 48 05 80 01 52  .......;.!.H...R
0040: 00 02 02 10 02 80 00 4F  00 48 06 80 01 52 00 48  .......O.H...R.H
0050: 07 80 01 58 00 48 08 80  21 00                    ...X.H..!.      
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x6E] LocalPlayer uses emote 42*
  2: 0x0009 [0x99] Wait for LocalPlayer animation to complete
  3: 0x000E [0x03] Work_Zone[9] = 1020*
  4: 0x0013 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0055
  5: 0x001B [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0041
  6: 0x0023 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0031
  7: 0x002B [0x48] [System] [7426*]:
    → "You are unable to harvest anything."
  8: 0x002E [0x01] GOTO 0x003E
  9: 0x0031 [0x02] IF !(Work_Zone[2] == 4294966520*) GOTO 0x003B
 10: 0x0039 [0x21] END_EVENT
 11: 0x003A [0x00] END_REQSTACK()
 12: 0x003B [0x48] [System] [7424*]:
    → "You successfully harvest $0!"

SUBROUTINE_003E:
 13: 0x003E [0x01] GOTO 0x0052
 14: 0x0041 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x004F
 15: 0x0049 [0x48] [System] [7423*]:
    → "Your $7 breaks!"
 16: 0x004C [0x01] GOTO 0x0052
 17: 0x004F [0x48] [System] [7425*]:
    → "You harvest $0, but your $7 breaks."

SUBROUTINE_0052:
 18: 0x0052 [0x01] GOTO 0x0058
 19: 0x0055 [0x48] [System] [7427*]:
    → "You cannot carry any more items. Your inventory is full."

SUBROUTINE_0058:
 20: 0x0058 [0x21] END_EVENT
 21: 0x0059 [0x00] END_REQSTACK()
```
