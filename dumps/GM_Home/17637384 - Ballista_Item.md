# 17637384 - Ballista_Item

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 220 bytes         |
| Total Events     | 2                 |
| References Count | 16                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [27](#event-27)       | 0x0001       |    128 |             26 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x14B4      |        5300 |
|       1 | 0x14B5      |        5301 |
|       2 | 0x14B6      |        5302 |
|       3 | 0x14B7      |        5303 |
|       4 | 0x0468      |        1128 |
|       5 | 0x0469      |        1129 |
|       6 | 0x1BA9      |        7081 |
|       7 | 0x0000      |           0 |
|       8 | 0x0010      |          16 |
|       9 | 0x1BAA      |        7082 |
|      10 | 0x0018      |          24 |
|      11 | 0x001F      |          31 |
|      12 | 0x1BAB      |        7083 |
|      13 | 0x0007      |           7 |
|      14 | 0x40000000  |  1073741824 |
|      15 | 0x000F      |          15 |

## String References

- **7081**: Whaddya want this time, cheater? [Current $0./Next $0./Previous $0./Current $1./Next $1./Previous $1./Current $2./Previous $2./Current $3./Previous $3./Current $4./Previous $4./Next $4./Current $5./Previous $5./Next $5./More $5./Forget it.]
- **7082**: Which $0 do you want? [After phase 1./After phase 2./After phase 3./After phase 4./After phase 5./After phase 6./After phase 7./After phase 8./After phase 9./After phase 10./After phase 11./After phase 12./After phase 13./After phase 14./After phase 15./After phase 16./After phase 17./After phase 18./After phase 19./After phase 20./After phase 21./After phase 22./After phase 23./After phase 24./Nevermind.]
- **7083**: Level limit? [No limits./60./50./40."0."0./10./Nevermind.]

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

### Event 27

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 128 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 02 10 00 80 03 03  10 01 80 03 04 10 02 80   ...............
0010: 03 05 10 03 80 03 06 10  04 80 03 07 10 05 80 24  ...............$
0020: 06 80 07 80 07 80 25 02  00 10 07 80 00 32 00 01  ......%......2..
0030: 55 00 02 00 10 08 80 00  55 00 24 09 80 07 80 07  U.......U.$.....
0040: 80 25 02 00 10 0A 80 00  4D 00 01 52 00 07 00 10  .%......M..R....
0050: 08 80 01 55 00 40 08 80  0B 80 01 10 00 10 24 0C  ...U.@........$.
0060: 80 07 80 07 80 25 02 00  10 0D 80 00 76 00 03 01  .....%......v...
0070: 10 0E 80 01 7F 00 40 07  80 0F 80 01 10 00 10 21  ......@........!
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[2] = 5300*
  1: 0x0006 [0x03] Work_Zone[3] = 5301*
  2: 0x000B [0x03] Work_Zone[4] = 5302*
  3: 0x0010 [0x03] Work_Zone[5] = 5303*
  4: 0x0015 [0x03] Work_Zone[6] = 1128*
  5: 0x001A [0x03] Work_Zone[7] = 1129*
  6: 0x001F [0x24] CREATE_DIALOG(message_id=7081*, default_option=0*, option_flags=0*)
    → "Whaddya want this time, cheater? [Current $0./Next $0./Previous $0./Current $1./Next $1./Previous $1./Current $2./Previous $2./Current $3./Previous $3./Current $4./Previous $4./Next $4./Current $5./Previous $5./Next $5./More $5./Forget it.]"
  7: 0x0026 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0027 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0032
  9: 0x002F [0x01] GOTO 0x0055
 10: 0x0032 [0x02] IF !(Work_Zone[0] == 16*) GOTO 0x0055
 11: 0x003A [0x24] CREATE_DIALOG(message_id=7082*, default_option=0*, option_flags=0*)
    → "Which $0 do you want? [After phase 1./After phase 2./After phase 3./After phase 4./After phase 5./After phase 6./After phase 7./After phase 8./After phase 9./After phase 10./After phase 11./After phase 12./After phase 13./After phase 14./After phase 15./After phase 16./After phase 17./After phase 18./After phase 19./After phase 20./After phase 21./After phase 22./After phase 23./After phase 24./Nevermind.]"
 12: 0x0041 [0x25] WAIT_DIALOG_SELECT()
 13: 0x0042 [0x02] IF !(Work_Zone[0] == 24*) GOTO 0x004D
 14: 0x004A [0x01] GOTO 0x0052
 15: 0x004D [0x07] Work_Zone[0] += 16*

SUBROUTINE_0052:
 16: 0x0052 [0x01] GOTO 0x0055

SUBROUTINE_0055:
 17: 0x0055 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=Work_Zone[0])
 18: 0x005E [0x24] CREATE_DIALOG(message_id=7083*, default_option=0*, option_flags=0*)
    → "Level limit? [No limits./60./50./40."0."0./10./Nevermind.]"
 19: 0x0065 [0x25] WAIT_DIALOG_SELECT()
 20: 0x0066 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0076
 21: 0x006E [0x03] Work_Zone[1] = 1073741824*
 22: 0x0073 [0x01] GOTO 0x007F
 23: 0x0076 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=Work_Zone[0])

SUBROUTINE_007F:
 24: 0x007F [0x21] END_EVENT
 25: 0x0080 [0x00] END_REQSTACK()
```
