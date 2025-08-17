# 17093430 - Rune of Transfer

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Nyzul Isle (ID: 77) |
| Block Size       | 744 bytes           |
| Total Events     | 3                   |
| References Count | 50                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [94](#event-94)       | 0x0001       |    424 |             86 |
| [96](#event-96)       | 0x01A9       |     89 |             20 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D35      |        7477 |
|       1 | 0x1D41      |        7489 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0002      |           2 |
|       5 | 0x01F4      |         500 |
|       6 | 0x0003      |           3 |
|       7 | 0x0226      |         550 |
|       8 | 0x0004      |           4 |
|       9 | 0x0258      |         600 |
|      10 | 0x0005      |           5 |
|      11 | 0x028A      |         650 |
|      12 | 0x0006      |           6 |
|      13 | 0x02BC      |         700 |
|      14 | 0x0007      |           7 |
|      15 | 0x02EE      |         750 |
|      16 | 0x0008      |           8 |
|      17 | 0x0320      |         800 |
|      18 | 0x0009      |           9 |
|      19 | 0x0352      |         850 |
|      20 | 0x000A      |          10 |
|      21 | 0x0384      |         900 |
|      22 | 0x000B      |          11 |
|      23 | 0x03E8      |        1000 |
|      24 | 0x000C      |          12 |
|      25 | 0x044C      |        1100 |
|      26 | 0x000D      |          13 |
|      27 | 0x04B0      |        1200 |
|      28 | 0x000E      |          14 |
|      29 | 0x0514      |        1300 |
|      30 | 0x000F      |          15 |
|      31 | 0x0578      |        1400 |
|      32 | 0x0010      |          16 |
|      33 | 0x05DC      |        1500 |
|      34 | 0x0011      |          17 |
|      35 | 0x0640      |        1600 |
|      36 | 0x0012      |          18 |
|      37 | 0x06A4      |        1700 |
|      38 | 0x0013      |          19 |
|      39 | 0x0708      |        1800 |
|      40 | 0x0014      |          20 |
|      41 | 0x076C      |        1900 |
|      42 | 0x1D44      |        7492 |
|      43 | 0x1D45      |        7493 |
|      44 | 0x1D42      |        7490 |
|      45 | 0x1D43      |        7491 |
|      46 | 0x1D36      |        7478 |
|      47 | 0x1D40      |        7488 |
|      48 | 0x001F      |          31 |
|      49 | 0x1D37      |        7479 |

## String References

- **7477**: 3 confirmed. Please select a floor number.
- **7478**: 3 confirmed. Please select your destination floor.
- **7479**: Final destination set to Floor $0. Travel to Floor 1?
- **7488**: Select a floor. [None."0./40./60./80./100.]
- **7489**: Select a floor. [None./1./6./11./16."1."6."1."6./41./46./51./56./61./66./71./76./81./86./91./96.]
- **7490**: Transfer to Floor $0 requires $1 [token/tokens].
- **7491**: Use $1 [token/tokens] to travel to Floor $0? [Yes./No.]
- **7492**: Commencing transfer to Floor 1.
- **7493**: Travel to Floor 1? [Yes./No.]

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

### Event 94

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 424 bytes |
| Instructions | 86        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 24 01 80  02 80 09 10 25 02 00 10   H..#$......%...
0010: 03 80 00 18 00 01 48 01  02 00 10 04 80 00 28 00  ......H.......(.
0020: 03 03 10 05 80 01 48 01  02 00 10 06 80 00 38 00  ......H.......8.
0030: 03 03 10 07 80 01 48 01  02 00 10 08 80 00 48 00  ......H.......H.
0040: 03 03 10 09 80 01 48 01  02 00 10 0A 80 00 58 00  ......H.......X.
0050: 03 03 10 0B 80 01 48 01  02 00 10 0C 80 00 68 00  ......H.......h.
0060: 03 03 10 0D 80 01 48 01  02 00 10 0E 80 00 78 00  ......H.......x.
0070: 03 03 10 0F 80 01 48 01  02 00 10 10 80 00 88 00  ......H.........
0080: 03 03 10 11 80 01 48 01  02 00 10 12 80 00 98 00  ......H.........
0090: 03 03 10 13 80 01 48 01  02 00 10 14 80 00 A8 00  ......H.........
00A0: 03 03 10 15 80 01 48 01  02 00 10 16 80 00 B8 00  ......H.........
00B0: 03 03 10 17 80 01 48 01  02 00 10 18 80 00 C8 00  ......H.........
00C0: 03 03 10 19 80 01 48 01  02 00 10 1A 80 00 D8 00  ......H.........
00D0: 03 03 10 1B 80 01 48 01  02 00 10 1C 80 00 E8 00  ......H.........
00E0: 03 03 10 1D 80 01 48 01  02 00 10 1E 80 00 F8 00  ......H.........
00F0: 03 03 10 1F 80 01 48 01  02 00 10 20 80 00 08 01  ......H.... ....
0100: 03 03 10 21 80 01 48 01  02 00 10 22 80 00 18 01  ...!..H...."....
0110: 03 03 10 23 80 01 48 01  02 00 10 24 80 00 28 01  ...#..H....$..(.
0120: 03 03 10 25 80 01 48 01  02 00 10 26 80 00 38 01  ...%..H....&..8.
0130: 03 03 10 27 80 01 48 01  02 00 10 28 80 00 48 01  ...'..H....(..H.
0140: 03 03 10 29 80 01 48 01  03 01 10 00 10 03 02 10  ...)..H.........
0150: 00 10 14 02 10 0A 80 08  02 10 08 80 02 00 10 02  ................
0160: 80 01 A7 01 02 00 10 03  80 00 8B 01 48 2A 80 23  ............H*.#
0170: 24 2B 80 03 80 02 80 25  02 00 10 03 80 00 88 01  $+.....%........
0180: 03 01 10 02 80 01 88 01  01 A7 01 48 2C 80 23 24  ...........H,.#$
0190: 2D 80 03 80 02 80 25 02  00 10 03 80 00 A7 01 03  -.....%.........
01A0: 01 10 02 80 01 A7 01 21  00                       .......!.       
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7477*]:
    → "3 confirmed. Please select a floor number."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7489*, default_option=0*, option_flags=Work_Zone[9])
    → "Select a floor. [None./1./6./11./16."1."6."1."6./41./46./51./56./61./66./71./76./81./86./91./96.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0018
  5: 0x0015 [0x01] GOTO 0x0148
  6: 0x0018 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0028
  7: 0x0020 [0x03] Work_Zone[3] = 500*
  8: 0x0025 [0x01] GOTO 0x0148
  9: 0x0028 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0038
 10: 0x0030 [0x03] Work_Zone[3] = 550*
 11: 0x0035 [0x01] GOTO 0x0148
 12: 0x0038 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0048
 13: 0x0040 [0x03] Work_Zone[3] = 600*
 14: 0x0045 [0x01] GOTO 0x0148
 15: 0x0048 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0058
 16: 0x0050 [0x03] Work_Zone[3] = 650*
 17: 0x0055 [0x01] GOTO 0x0148
 18: 0x0058 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0068
 19: 0x0060 [0x03] Work_Zone[3] = 700*
 20: 0x0065 [0x01] GOTO 0x0148
 21: 0x0068 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0078
 22: 0x0070 [0x03] Work_Zone[3] = 750*
 23: 0x0075 [0x01] GOTO 0x0148
 24: 0x0078 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x0088
 25: 0x0080 [0x03] Work_Zone[3] = 800*
 26: 0x0085 [0x01] GOTO 0x0148
 27: 0x0088 [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x0098
 28: 0x0090 [0x03] Work_Zone[3] = 850*
 29: 0x0095 [0x01] GOTO 0x0148
 30: 0x0098 [0x02] IF !(Work_Zone[0] == 10*) GOTO 0x00A8
 31: 0x00A0 [0x03] Work_Zone[3] = 900*
 32: 0x00A5 [0x01] GOTO 0x0148
 33: 0x00A8 [0x02] IF !(Work_Zone[0] == 11*) GOTO 0x00B8
 34: 0x00B0 [0x03] Work_Zone[3] = 1000*
 35: 0x00B5 [0x01] GOTO 0x0148
 36: 0x00B8 [0x02] IF !(Work_Zone[0] == 12*) GOTO 0x00C8
 37: 0x00C0 [0x03] Work_Zone[3] = 1100*
 38: 0x00C5 [0x01] GOTO 0x0148
 39: 0x00C8 [0x02] IF !(Work_Zone[0] == 13*) GOTO 0x00D8
 40: 0x00D0 [0x03] Work_Zone[3] = 1200*
 41: 0x00D5 [0x01] GOTO 0x0148
 42: 0x00D8 [0x02] IF !(Work_Zone[0] == 14*) GOTO 0x00E8
 43: 0x00E0 [0x03] Work_Zone[3] = 1300*
 44: 0x00E5 [0x01] GOTO 0x0148
 45: 0x00E8 [0x02] IF !(Work_Zone[0] == 15*) GOTO 0x00F8
 46: 0x00F0 [0x03] Work_Zone[3] = 1400*
 47: 0x00F5 [0x01] GOTO 0x0148
 48: 0x00F8 [0x02] IF !(Work_Zone[0] == 16*) GOTO 0x0108
 49: 0x0100 [0x03] Work_Zone[3] = 1500*
 50: 0x0105 [0x01] GOTO 0x0148
 51: 0x0108 [0x02] IF !(Work_Zone[0] == 17*) GOTO 0x0118
 52: 0x0110 [0x03] Work_Zone[3] = 1600*
 53: 0x0115 [0x01] GOTO 0x0148
 54: 0x0118 [0x02] IF !(Work_Zone[0] == 18*) GOTO 0x0128
 55: 0x0120 [0x03] Work_Zone[3] = 1700*
 56: 0x0125 [0x01] GOTO 0x0148
 57: 0x0128 [0x02] IF !(Work_Zone[0] == 19*) GOTO 0x0138
 58: 0x0130 [0x03] Work_Zone[3] = 1800*
 59: 0x0135 [0x01] GOTO 0x0148
 60: 0x0138 [0x02] IF !(Work_Zone[0] == 20*) GOTO 0x0148
 61: 0x0140 [0x03] Work_Zone[3] = 1900*
 62: 0x0145 [0x01] GOTO 0x0148

SUBROUTINE_0148:
 63: 0x0148 [0x03] Work_Zone[1] = Work_Zone[0]
 64: 0x014D [0x03] Work_Zone[2] = Work_Zone[0]
 65: 0x0152 [0x14] Work_Zone[2] *= 5*
 66: 0x0157 [0x08] Work_Zone[2] -= 4*
 67: 0x015C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01A7
 68: 0x0164 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x018B
 69: 0x016C [0x48] [System] [7492*]:
    → "Commencing transfer to Floor 1."
 70: 0x016F [0x23] WAIT_FOR_DIALOG_INTERACTION
 71: 0x0170 [0x24] CREATE_DIALOG(message_id=7493*, default_option=1*, option_flags=0*)
    → "Travel to Floor 1? [Yes./No.]"
 72: 0x0177 [0x25] WAIT_DIALOG_SELECT()
 73: 0x0178 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0188
 74: 0x0180 [0x03] Work_Zone[1] = 0*
 75: 0x0185 [0x01] GOTO 0x0188

SUBROUTINE_0188:
 76: 0x0188 [0x01] GOTO 0x01A7
 77: 0x018B [0x48] [System] [7490*]:
    → "Transfer to Floor $0 requires $1 [token/tokens]."
 78: 0x018E [0x23] WAIT_FOR_DIALOG_INTERACTION
 79: 0x018F [0x24] CREATE_DIALOG(message_id=7491*, default_option=1*, option_flags=0*)
    → "Use $1 [token/tokens] to travel to Floor $0? [Yes./No.]"
 80: 0x0196 [0x25] WAIT_DIALOG_SELECT()
 81: 0x0197 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01A7
 82: 0x019F [0x03] Work_Zone[1] = 0*
 83: 0x01A4 [0x01] GOTO 0x01A7

SUBROUTINE_01A7:
 84: 0x01A7 [0x21] END_EVENT
 85: 0x01A8 [0x00] END_REQSTACK()
```

### Event 96

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A9   |
| Data Size    | 89 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                             48 2E 80 23 24 2F 80           H..#$/.
01B0: 02 80 02 80 25 02 00 10  02 80 00 C0 01 01 C0 01  ....%...........
01C0: 40 02 80 1E 80 01 10 00  10 03 02 10 00 10 14 02  @...............
01D0: 10 28 80 02 00 10 02 80  01 00 02 40 20 80 30 80  .(.........@ .0.
01E0: 01 10 03 80 48 31 80 23  24 2B 80 03 80 02 80 25  ....H1.#$+.....%
01F0: 02 00 10 03 80 00 00 02  03 01 10 02 80 01 00 02  ................
0200: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x01A9 [0x48] [System] [7478*]:
    → "3 confirmed. Please select your destination floor."
  1: 0x01AC [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x01AD [0x24] CREATE_DIALOG(message_id=7488*, default_option=0*, option_flags=0*)
    → "Select a floor. [None."0./40./60./80./100.]"
  3: 0x01B4 [0x25] WAIT_DIALOG_SELECT()
  4: 0x01B5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01C0
  5: 0x01BD [0x01] GOTO 0x01C0

SUBROUTINE_01C0:
  6: 0x01C0 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=Work_Zone[0])
  7: 0x01C9 [0x03] Work_Zone[2] = Work_Zone[0]
  8: 0x01CE [0x14] Work_Zone[2] *= 20*
  9: 0x01D3 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0200
 10: 0x01DB [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=1*)
 11: 0x01E4 [0x48] [System] [7479*]:
    → "Final destination set to Floor $0. Travel to Floor 1?"
 12: 0x01E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x01E8 [0x24] CREATE_DIALOG(message_id=7493*, default_option=1*, option_flags=0*)
    → "Travel to Floor 1? [Yes./No.]"
 14: 0x01EF [0x25] WAIT_DIALOG_SELECT()
 15: 0x01F0 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0200
 16: 0x01F8 [0x03] Work_Zone[1] = 0*
 17: 0x01FD [0x01] GOTO 0x0200

SUBROUTINE_0200:
 18: 0x0200 [0x21] END_EVENT
 19: 0x0201 [0x00] END_REQSTACK()
```
