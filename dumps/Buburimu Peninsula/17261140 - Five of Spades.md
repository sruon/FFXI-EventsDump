# 17261140 - Five of Spades

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Buburimu Peninsula (ID: 118) |
| Block Size       | 124 bytes                    |
| Total Events     | 2                            |
| References Count | 8                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1](#event-1)         | 0x0001       |     64 |             23 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1C5E      |        7262 |
|       2 | 0x0002      |           2 |
|       3 | 0x1C5F      |        7263 |
|       4 | 0x0003      |           3 |
|       5 | 0x1C60      |        7264 |
|       6 | 0x1C61      |        7265 |
|       7 | 0x1C62      |        7266 |

## String References

- **7262**: GiMme$26fIvE! FiVe is$26A cArdIan$26OF WiN-DuRst! FIvE$26iS On$26pA-tRol!
- **7263**: HAnG$26tEn, dOOd! FiVe is$26A cArdIan$26OF WiN-DuRst! FIvE$26iS On$26pA-tRol!
- **7264**: WASSuuuuuuP!? FiVe is$26A cArdIan$26OF WiN-DuRst! FIvE$26iS On$26pA-tRol!
- **7265**: ...? aRE yOu$26TeLLiNg fiVe$26hiS GrEEtiNg$26is iNcoRreCt?
- **7266**: ThIS$26cAnNOt bE$26tRuE! THis$26iS$26tHe fIRst$26GrEEtiNg$26tHaT$26fiVe LEaRNed...

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

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 64 bytes |
| Instructions | 23       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 02 03 10 00  80 00 13 00 1D 01 80 23    .B...........#
0010: 01 35 00 02 03 10 02 80  00 22 00 1D 03 80 23 01  .5......."....#.
0020: 35 00 02 03 10 04 80 00  31 00 1D 05 80 23 01 35  5.......1....#.5
0030: 00 1D 01 80 23 1D 06 80  23 1D 07 80 23 20 00 21  ....#...#...# .!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x0013
  3: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=7262*)
    → "GiMme$26fIvE! FiVe is$26A cArdIan$26OF WiN-DuRst! FIvE$26iS On$26pA-tRol!"
  4: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0010 [0x01] GOTO 0x0035
  6: 0x0013 [0x02] IF !(Work_Zone[3] == 2*) GOTO 0x0022
  7: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=7263*)
    → "HAnG$26tEn, dOOd! FiVe is$26A cArdIan$26OF WiN-DuRst! FIvE$26iS On$26pA-tRol!"
  8: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x001F [0x01] GOTO 0x0035
 10: 0x0022 [0x02] IF !(Work_Zone[3] == 3*) GOTO 0x0031
 11: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=7264*)
    → "WASSuuuuuuP!? FiVe is$26A cArdIan$26OF WiN-DuRst! FIvE$26iS On$26pA-tRol!"
 12: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x002E [0x01] GOTO 0x0035
 14: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=7262*)
    → "GiMme$26fIvE! FiVe is$26A cArdIan$26OF WiN-DuRst! FIvE$26iS On$26pA-tRol!"
 15: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0035:
 16: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=7265*)
    → "...? aRE yOu$26TeLLiNg fiVe$26hiS GrEEtiNg$26is iNcoRreCt?"
 17: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=7266*)
    → "ThIS$26cAnNOt bE$26tRuE! THis$26iS$26tHe fIRst$26GrEEtiNg$26tHaT$26fiVe LEaRNed..."
 19: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x003D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 21: 0x003F [0x21] END_EVENT
 22: 0x0040 [0x00] END_REQSTACK()
```
