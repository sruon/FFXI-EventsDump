# 17044015 - Logging Point

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Mamook (ID: 65) |
| Block Size       | 144 bytes       |
| Total Events     | 2               |
| References Count | 8               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [215](#event-215)     | 0x0001       |     84 |             20 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x03FD      |        1021 |
|       2 | 0x0000      |           0 |
|       3 | 0x1D82      |        7554 |
|       4 | 0x1D80      |        7552 |
|       5 | 0x1D7F      |        7551 |
|       6 | 0x1D81      |        7553 |
|       7 | 0x1D83      |        7555 |

## String References

- **7551**: Your $7 breaks!
- **7552**: You successfully cut off $0!
- **7553**: You cut off $0, but your $7 breaks in the process.
- **7554**: You are unable to log anything.
- **7555**: You cannot carry any more items. Your inventory is full.

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

### Event 215

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 84 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 6E F0 FF FF 7F 00  80 99 F0 FF FF 7F 03 09   Bn.............
0010: 10 01 80 03 00 00 06 10  02 04 10 02 80 00 50 00  ..............P.
0020: 02 03 10 02 80 00 3C 00  02 02 10 02 80 00 36 00  ......<.......6.
0030: 48 03 80 01 39 00 48 04  80 01 4D 00 02 02 10 02  H...9.H...M.....
0040: 80 00 4A 00 48 05 80 01  4D 00 48 06 80 01 53 00  ..J.H...M.H...S.
0050: 48 07 80 21 00                                    H..!.           
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x6E] LocalPlayer uses emote 40*
  2: 0x0009 [0x99] Wait for LocalPlayer animation to complete
  3: 0x000E [0x03] Work_Zone[9] = 1021*
  4: 0x0013 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[6]
  5: 0x0018 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0050
  6: 0x0020 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x003C
  7: 0x0028 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0036
  8: 0x0030 [0x48] [System] [7554*]:
    → "You are unable to log anything."
  9: 0x0033 [0x01] GOTO 0x0039
 10: 0x0036 [0x48] [System] [7552*]:
    → "You successfully cut off $0!"

SUBROUTINE_0039:
 11: 0x0039 [0x01] GOTO 0x004D
 12: 0x003C [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x004A
 13: 0x0044 [0x48] [System] [7551*]:
    → "Your $7 breaks!"
 14: 0x0047 [0x01] GOTO 0x004D
 15: 0x004A [0x48] [System] [7553*]:
    → "You cut off $0, but your $7 breaks in the process."

SUBROUTINE_004D:
 16: 0x004D [0x01] GOTO 0x0053
 17: 0x0050 [0x48] [System] [7555*]:
    → "You cannot carry any more items. Your inventory is full."

SUBROUTINE_0053:
 18: 0x0053 [0x21] END_EVENT
 19: 0x0054 [0x00] END_REQSTACK()
```
