# 17637409 - Lottery-Maker

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 160 bytes         |
| Total Events     | 2                 |
| References Count | 11                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      2 |              2 |
| [75](#event-75)       | 0x0002       |     89 |             20 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x09FF      |        2559 |
|       1 | 0x1D98      |        7576 |
|       2 | 0x0000      |           0 |
|       3 | 0x1D68      |        7528 |
|       4 | 0x0001      |           1 |
|       5 | 0x0005      |           5 |
|       6 | 0x1869F     |       99999 |
|       7 | 0x0007      |           7 |
|       8 | 0x0004      |           4 |
|       9 | 0x0008      |           8 |
|      10 | 0x001F      |          31 |

## String References

- **7528**: What number would you like?
- **7576**: What will you have issued? [#./Quit.]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 2 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00 00                                             ..              
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0001 [0x00] END_REQSTACK()
```

### Event 75

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 89 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 02 10 00 80 24  01 80 02 80 02 80 25 02    .....$......%.
0010: 00 10 02 80 00 1D 00 1A  22 00 01 20 00 06 01 10  ........".. ....
0020: 21 00 1D 03 80 23 06 01  10 71 12 04 80 05 80 71  !....#...q.....q
0030: 13 02 10 02 02 10 02 80  04 5A 00 02 02 10 06 80  .........Z......
0040: 05 5A 00 03 01 10 07 80  40 08 80 07 80 01 10 02  .Z......@.......
0050: 80 40 09 80 0A 80 01 10  02 10 1B                 .@.........     
```

#### Opcodes

```
  0: 0x0002 [0x03] Work_Zone[2] = 2559*
  1: 0x0007 [0x24] CREATE_DIALOG(message_id=7576*, default_option=0*, option_flags=0*)
    → "What will you have issued? [#./Quit.]"
  2: 0x000E [0x25] WAIT_DIALOG_SELECT()
  3: 0x000F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001D
  4: 0x0017 [0x1A] CALL_SUBROUTINE(address=0x0022)
  5: 0x001A [0x01] GOTO 0x0020
  6: 0x001D [0x06] Work_Zone[1] = 0

SUBROUTINE_0020:
  7: 0x0020 [0x21] END_EVENT
  8: 0x0021 [0x00] END_REQSTACK()

SUBROUTINE_0022:
  9: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7528*)
    → "What number would you like?"
 10: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0026 [0x06] Work_Zone[1] = 0
 12: 0x0029 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 5*])
 13: 0x002F [0x71] USER_INPUT_HANDLER: Process numerical input B (work=Work_Zone[2])
 14: 0x0033 [0x02] IF !(Work_Zone[2] < 0*) GOTO 0x005A
 15: 0x003B [0x02] IF !(Work_Zone[2] > 99999*) GOTO 0x005A
 16: 0x0043 [0x03] Work_Zone[1] = 7*
 17: 0x0048 [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=7*, target=Work_Zone[1], source=0*)
 18: 0x0051 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=31*, target=Work_Zone[1], source=Work_Zone[2])
 19: 0x005A [0x1B] RETURN
```
