# 17371613 - Harvesting Point

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Giddeus (ID: 145) |
| Block Size       | 172 bytes         |
| Total Events     | 2                 |
| References Count | 11                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [70](#event-70)       | 0x0001       |    103 |             27 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x002A      |          42 |
|       1 | 0x03FC      |        1020 |
|       2 | 0x0000      |           0 |
|       3 | 0x1D0D      |        7437 |
|       4 | 0xFFFFFFFF  |  4294967295 |
|       5 | 0x1D10      |        7440 |
|       6 | 0xFFFFFD1F  |  4294966559 |
|       7 | 0x1D0B      |        7435 |
|       8 | 0x1D0A      |        7434 |
|       9 | 0x1D0C      |        7436 |
|      10 | 0x1D0E      |        7438 |

## String References

- **7434**: Your $7 breaks!
- **7435**: You successfully harvest $0!
- **7436**: You harvest $0, but your $7 breaks.
- **7437**: You are unable to harvest anything.
- **7438**: You cannot carry any more items. Your inventory is full.
- **7440**: It looks like you might need two people to harvest here...

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

### Event 70

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 103 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 6E F0 FF FF 7F 00  80 99 F0 FF FF 7F 03 09   Bn.............
0010: 10 01 80 02 04 10 02 80  00 63 00 02 03 10 02 80  .........c......
0020: 00 4F 00 02 02 10 02 80  00 31 00 48 03 80 01 4C  .O.......1.H...L
0030: 00 02 02 10 04 80 00 3F  00 48 05 80 23 21 00 02  .......?.H..#!..
0040: 02 10 06 80 00 49 00 21  00 48 07 80 01 60 00 02  .....I.!.H...`..
0050: 02 10 02 80 00 5D 00 48  08 80 01 60 00 48 09 80  .....].H...`.H..
0060: 01 66 00 48 0A 80 21 00                           .f.H..!.        
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x6E] LocalPlayer uses emote 42*
  2: 0x0009 [0x99] Wait for LocalPlayer animation to complete
  3: 0x000E [0x03] Work_Zone[9] = 1020*
  4: 0x0013 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0063
  5: 0x001B [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x004F
  6: 0x0023 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0031
  7: 0x002B [0x48] [System] [7437*]:
    → "You are unable to harvest anything."
  8: 0x002E [0x01] GOTO 0x004C
  9: 0x0031 [0x02] IF !(Work_Zone[2] == 4294967295*) GOTO 0x003F
 10: 0x0039 [0x48] [System] [7440*]:
    → "It looks like you might need two people to harvest here..."
 11: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x003D [0x21] END_EVENT
 13: 0x003E [0x00] END_REQSTACK()
 14: 0x003F [0x02] IF !(Work_Zone[2] == 4294966559*) GOTO 0x0049
 15: 0x0047 [0x21] END_EVENT
 16: 0x0048 [0x00] END_REQSTACK()
 17: 0x0049 [0x48] [System] [7435*]:
    → "You successfully harvest $0!"

SUBROUTINE_004C:
 18: 0x004C [0x01] GOTO 0x0060
 19: 0x004F [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x005D
 20: 0x0057 [0x48] [System] [7434*]:
    → "Your $7 breaks!"
 21: 0x005A [0x01] GOTO 0x0060
 22: 0x005D [0x48] [System] [7436*]:
    → "You harvest $0, but your $7 breaks."

SUBROUTINE_0060:
 23: 0x0060 [0x01] GOTO 0x0066
 24: 0x0063 [0x48] [System] [7438*]:
    → "You cannot carry any more items. Your inventory is full."

SUBROUTINE_0066:
 25: 0x0066 [0x21] END_EVENT
 26: 0x0067 [0x00] END_REQSTACK()
```
