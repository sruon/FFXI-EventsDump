# 17637598 - menace_aug

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 160 bytes         |
| Total Events     | 2                 |
| References Count | 13                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [167](#event-167)     | 0x0001       |     81 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2416      |        9238 |
|       1 | 0x0001      |           1 |
|       2 | 0x0005      |           5 |
|       3 | 0x0000      |           0 |
|       4 | 0x0003      |           3 |
|       5 | 0x2417      |        9239 |
|       6 | 0x2418      |        9240 |
|       7 | 0x0002      |           2 |
|       8 | 0x000F      |          15 |
|       9 | 0x0010      |          16 |
|      10 | 0x0011      |          17 |
|      11 | 0x0012      |          18 |
|      12 | 0x0016      |          22 |

## String References

- **9238**: No
- **9239**: Type($0-$1)
- **9240**: Lv

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

### Event 167

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 81 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 71 12 01  80 02 80 71 13 00 00 03   ...#q.....q....
0010: 02 10 03 80 03 03 10 04  80 1D 05 80 23 71 12 01  ............#q..
0020: 80 01 80 71 13 01 00 1D  06 80 23 71 12 01 80 07  ...q......#q....
0030: 80 71 13 02 00 40 03 80  08 80 01 10 00 00 40 09  .q...@........@.
0040: 80 0A 80 01 10 01 00 40  0B 80 0C 80 01 10 02 00  .......@........
0050: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=9238*)
    → "No"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 5*])
  3: 0x000B [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
  4: 0x000F [0x03] Work_Zone[2] = 0*
  5: 0x0014 [0x03] Work_Zone[3] = 3*
  6: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=9239*)
    → "Type($0-$1)"
  7: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001D [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 1*])
  9: 0x0023 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[1])
 10: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=9240*)
    → "Lv"
 11: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x002B [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 13: 0x0031 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[2])
 14: 0x0035 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 15: 0x003E [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=17*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 16: 0x0047 [0x40] SET_BIT_WORK_RANGE(start_bit=18*, end_bit=22*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
 17: 0x0050 [0x21] END_EVENT
 18: 0x0051 [0x00] END_REQSTACK()
```
