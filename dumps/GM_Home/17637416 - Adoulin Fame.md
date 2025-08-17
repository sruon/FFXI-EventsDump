# 17637416 - Adoulin Fame

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 444 bytes         |
| Total Events     | 2                 |
| References Count | 14                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [18](#event-18)       | 0x0001       |    360 |             70 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0003      |           3 |
|       2 | 0x000A      |          10 |
|       3 | 0x237B      |        9083 |
|       4 | 0x0001      |           1 |
|       5 | 0x0002      |           2 |
|       6 | 0x0008      |           8 |
|       7 | 0x0009      |           9 |
|       8 | 0x237A      |        9082 |
|       9 | 0x0004      |           4 |
|      10 | 0x0005      |           5 |
|      11 | 0x0006      |           6 |
|      12 | 0x0007      |           7 |
|      13 | 0x000D      |          13 |

## String References

- **9082**: Raise fame for what? [I shall remain anonymous./Quests. ($1)/Pioneers' Coalition. ($2)/Peacekeepers' Coalition. ($3)/Coureiers' Coalition. ($4)/Scouts' Coalition. ($5)/Inventoers' Coalition. ($6)/Mummers' Coalition. ($7)]
- **9083**: Fiddle with what? [Nuthin'./Fame!/Bayld. ($1)/Mummers' Medals. ($2)]

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

### Event 18

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 360 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    40 00 80 01 80 01 10  02 80 43 00 43 01 24 03   @........C.C.$.
0010: 80 00 80 00 80 25 02 00  10 00 80 00 24 00 01 61  .....%......$..a
0020: 00 01 5A 00 02 00 10 04  80 00 32 00 01 63 00 01  ..Z.......2..c..
0030: 5A 00 02 00 10 05 80 00  46 00 40 00 80 01 80 01  Z.......F.@.....
0040: 10 06 80 01 5A 00 02 00  10 01 80 00 5A 00 40 00  ....Z.......Z.@.
0050: 80 01 80 01 10 07 80 01  5A 00 43 00 43 01 01 01  ........Z.C.C...
0060: 00 21 00 40 00 80 01 80  01 10 00 80 43 00 43 01  .!.@........C.C.
0070: 24 08 80 00 80 00 80 25  02 00 10 00 80 00 86 00  $......%........
0080: 01 01 00 01 58 01 02 00  10 04 80 00 A4 00 40 00  ....X.........@.
0090: 80 05 80 01 10 04 80 71  12 04 80 01 80 71 13 02  .......q.....q..
00A0: 10 01 58 01 02 00 10 05  80 00 C2 00 40 00 80 05  ..X.........@...
00B0: 80 01 10 05 80 71 12 04  80 09 80 71 13 02 10 01  .....q.....q....
00C0: 58 01 02 00 10 01 80 00  E0 00 40 00 80 05 80 01  X.........@.....
00D0: 10 01 80 71 12 04 80 09  80 71 13 02 10 01 58 01  ...q.....q....X.
00E0: 02 00 10 09 80 00 FE 00  40 00 80 05 80 01 10 09  ........@.......
00F0: 80 71 12 04 80 09 80 71  13 02 10 01 58 01 02 00  .q.....q....X...
0100: 10 0A 80 00 1C 01 40 00  80 05 80 01 10 0A 80 71  ......@........q
0110: 12 04 80 09 80 71 13 02  10 01 58 01 02 00 10 0B  .....q....X.....
0120: 80 00 3A 01 40 00 80 05  80 01 10 0B 80 71 12 04  ..:.@........q..
0130: 80 09 80 71 13 02 10 01  58 01 02 00 10 0C 80 00  ...q....X.......
0140: 58 01 40 00 80 05 80 01  10 0C 80 71 12 04 80 09  X.@........q....
0150: 80 71 13 02 10 01 58 01  40 09 80 0D 80 01 10 02  .q....X.@.......
0160: 10 43 00 43 01 01 63 00  00                       .C.C..c..       
```

#### Opcodes

```
  0: 0x0001 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=3*, target=Work_Zone[1], source=10*)
  1: 0x000A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  2: 0x000C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  3: 0x000E [0x24] CREATE_DIALOG(message_id=9083*, default_option=0*, option_flags=0*)
    → "Fiddle with what? [Nuthin'./Fame!/Bayld. ($1)/Mummers' Medals. ($2)]"
  4: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0024
  6: 0x001E [0x01] GOTO 0x0061

SUBROUTINE_005A:
  7: 0x005A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x005C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x005E [0x01] GOTO 0x0001

SUBROUTINE_0061:
 10: 0x0061 [0x21] END_EVENT
 11: 0x0062 [0x00] END_REQSTACK()

SUBROUTINE_0063:
 12: 0x0063 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=3*, target=Work_Zone[1], source=0*)
 13: 0x006C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 14: 0x006E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 15: 0x0070 [0x24] CREATE_DIALOG(message_id=9082*, default_option=0*, option_flags=0*)
    → "Raise fame for what? [I shall remain anonymous./Quests. ($1)/Pioneers' Coalition. ($2)/Peacekeepers' Coalition. ($3)/Coureiers' Coalition. ($4)/Scouts' Coalition. ($5)/Inventoers' Coalition. ($6)/Mummers' Coalition. ($7)]"
 16: 0x0077 [0x25] WAIT_DIALOG_SELECT()
 17: 0x0078 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0086
 18: 0x0080 [0x01] GOTO 0x0001

SUBROUTINE_0158:
 19: 0x0158 [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=13*, target=Work_Zone[1], source=Work_Zone[2])
 20: 0x0161 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 21: 0x0163 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 22: 0x0165 [0x01] GOTO 0x0063
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0021 [0x01] GOTO 0x005A
     0x002F [0x01] GOTO 0x005A
# Dead code (unreachable instructions):
     0x0083 [0x01] GOTO 0x0158
# Dead code (unreachable instructions):
     0x0168 [0x00] END_REQSTACK()
```
