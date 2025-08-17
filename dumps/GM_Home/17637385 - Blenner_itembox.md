# 17637385 - Blenner_itembox

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 212 bytes         |
| Total Events     | 2                 |
| References Count | 16                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [50](#event-50)       | 0x0001       |    123 |             25 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x14CB      |        5323 |
|       1 | 0x14CC      |        5324 |
|       2 | 0x14CD      |        5325 |
|       3 | 0x14CE      |        5326 |
|       4 | 0xFC00      |       64512 |
|       5 | 0x1BA9      |        7081 |
|       6 | 0x0000      |           0 |
|       7 | 0x0010      |          16 |
|       8 | 0x1BAA      |        7082 |
|       9 | 0x0018      |          24 |
|      10 | 0x000A      |          10 |
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

### Event 50

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 123 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 02 10 00 80 03 03  10 01 80 03 04 10 02 80   ...............
0010: 03 05 10 03 80 03 01 00  04 80 24 05 80 06 80 01  ..........$.....
0020: 00 25 02 00 10 06 80 00  2D 00 01 50 00 02 00 10  .%......-..P....
0030: 07 80 00 50 00 24 08 80  06 80 06 80 25 02 00 10  ...P.$......%...
0040: 09 80 00 48 00 01 4D 00  07 00 10 0A 80 01 50 00  ...H..M.......P.
0050: 40 07 80 0B 80 01 10 00  10 24 0C 80 06 80 06 80  @........$......
0060: 25 02 00 10 0D 80 00 71  00 03 01 10 0E 80 01 7A  %......q.......z
0070: 00 40 06 80 0F 80 01 10  00 10 21 00              .@........!.    
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[2] = 5323*
  1: 0x0006 [0x03] Work_Zone[3] = 5324*
  2: 0x000B [0x03] Work_Zone[4] = 5325*
  3: 0x0010 [0x03] Work_Zone[5] = 5326*
  4: 0x0015 [0x03] ExtData[1]->WorkLocal[1] = 64512*
  5: 0x001A [0x24] CREATE_DIALOG(message_id=7081*, default_option=0*, option_flags=ExtData[1]->WorkLocal[1])
    → "Whaddya want this time, cheater? [Current $0./Next $0./Previous $0./Current $1./Next $1./Previous $1./Current $2./Previous $2./Current $3./Previous $3./Current $4./Previous $4./Next $4./Current $5./Previous $5./Next $5./More $5./Forget it.]"
  6: 0x0021 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0022 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x002D
  8: 0x002A [0x01] GOTO 0x0050
  9: 0x002D [0x02] IF !(Work_Zone[0] == 16*) GOTO 0x0050
 10: 0x0035 [0x24] CREATE_DIALOG(message_id=7082*, default_option=0*, option_flags=0*)
    → "Which $0 do you want? [After phase 1./After phase 2./After phase 3./After phase 4./After phase 5./After phase 6./After phase 7./After phase 8./After phase 9./After phase 10./After phase 11./After phase 12./After phase 13./After phase 14./After phase 15./After phase 16./After phase 17./After phase 18./After phase 19./After phase 20./After phase 21./After phase 22./After phase 23./After phase 24./Nevermind.]"
 11: 0x003C [0x25] WAIT_DIALOG_SELECT()
 12: 0x003D [0x02] IF !(Work_Zone[0] == 24*) GOTO 0x0048
 13: 0x0045 [0x01] GOTO 0x004D
 14: 0x0048 [0x07] Work_Zone[0] += 10*

SUBROUTINE_004D:
 15: 0x004D [0x01] GOTO 0x0050

SUBROUTINE_0050:
 16: 0x0050 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=Work_Zone[0])
 17: 0x0059 [0x24] CREATE_DIALOG(message_id=7083*, default_option=0*, option_flags=0*)
    → "Level limit? [No limits./60./50./40."0."0./10./Nevermind.]"
 18: 0x0060 [0x25] WAIT_DIALOG_SELECT()
 19: 0x0061 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0071
 20: 0x0069 [0x03] Work_Zone[1] = 1073741824*
 21: 0x006E [0x01] GOTO 0x007A
 22: 0x0071 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=Work_Zone[0])

SUBROUTINE_007A:
 23: 0x007A [0x21] END_EVENT
 24: 0x007B [0x00] END_REQSTACK()
```
