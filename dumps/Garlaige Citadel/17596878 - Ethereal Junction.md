# 17596878 - Ethereal Junction

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Garlaige Citadel (ID: 200) |
| Block Size       | 1364 bytes                 |
| Total Events     | 3                          |
| References Count | 23                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [9002](#event-9002)   | 0x0001       |      4 |              2 |
| [9005](#event-9005)   | 0x0005       |   1237 |            254 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2D77      |       11639 |
|       1 | 0x2D78      |       11640 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0x0360      |         864 |
|       5 | 0x0008      |           8 |
|       6 | 0x000F      |          15 |
|       7 | 0x0002      |           2 |
|       8 | 0x0003      |           3 |
|       9 | 0x0004      |           4 |
|      10 | 0x0005      |           5 |
|      11 | 0x0006      |           6 |
|      12 | 0x0007      |           7 |
|      13 | 0x000C      |          12 |
|      14 | 0x2D89      |       11657 |
|      15 | 0x2D8A      |       11658 |
|      16 | 0x000D      |          13 |
|      17 | 0x000E      |          14 |
|      18 | 0x0010      |          16 |
|      19 | 0x0011      |          17 |
|      20 | 0x0012      |          18 |
|      21 | 0x0013      |          19 |
|      22 | 0x0014      |          20 |

## String References

- **11639**: Those who have accepted $0 must pay $1 Unity accolades to participate. The content for this Wanted battle is $2. [Ready to begin?/You do not have the appropriate object set, so your rewards will be limited.]
- **11640**: Commence the Wanted battle? ($1 acc.) [Let's go!/Not yet.]
- **11657**: You currently have multiple Wanted battle objectives set. Select which one you would like to undertake.
- **11658**: Which objective would you like to undertake? [None for now./$0./$1./$2./$3./$4./$5./$6./$7.]

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

### Event 9002

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1A 09 00 00                                     ....           
```

#### Opcodes

```
  0: 0x0001 [0x1A] CALL_SUBROUTINE(address=0x0009)
  1: 0x0004 [0x00] END_REQSTACK()
```

### Event 9005

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0005     |
| Data Size    | 1237 bytes |
| Instructions | 210        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                1A F4 00  00 03 01 00 02 10 03 00       ...........
0010: 00 03 10 48 00 80 23 03  03 10 00 00 24 01 80 02  ...H..#.....$...
0020: 80 03 80 25 02 00 10 03  80 00 E7 00 42 03 01 10  ...%........B...
0030: 03 80 02 01 00 04 80 80  46 00 40 05 80 06 80 01  ........F.@.....
0040: 10 03 80 01 D2 00 02 01  00 03 80 80 5A 00 40 05  ............Z.@.
0050: 80 06 80 01 10 02 80 01  D2 00 02 01 00 03 80 80  ................
0060: 6E 00 40 05 80 06 80 01  10 07 80 01 D2 00 02 01  n.@.............
0070: 00 03 80 80 82 00 40 05  80 06 80 01 10 08 80 01  ......@.........
0080: D2 00 02 01 00 03 80 80  96 00 40 05 80 06 80 01  ..........@.....
0090: 10 09 80 01 D2 00 02 01  00 03 80 80 AA 00 40 05  ..............@.
00A0: 80 06 80 01 10 0A 80 01  D2 00 02 01 00 03 80 80  ................
00B0: BE 00 40 05 80 06 80 01  10 0B 80 01 D2 00 02 01  ..@.............
00C0: 00 03 80 80 D2 00 40 05  80 06 80 01 10 0C 80 01  ......@.........
00D0: D2 00 40 03 80 0C 80 01  10 0D 80 43 00 43 01 03  ..@........C.C..
00E0: 01 10 02 10 01 F2 00 02  00 10 02 80 00 F2 00 01  ................
00F0: F2 00 21 1B 03 02 00 03  80 02 02 10 03 80 00 08  ..!.............
0100: 01 3C 02 00 02 80 02 80  02 03 10 03 80 00 17 01  .<..............
0110: 3C 02 00 07 80 02 80 02  04 10 03 80 00 26 01 3C  <............&.<
0120: 02 00 08 80 02 80 02 05  10 03 80 00 35 01 3C 02  ............5.<.
0130: 00 09 80 02 80 02 06 10  03 80 00 44 01 3C 02 00  ...........D.<..
0140: 0A 80 02 80 02 07 10 03  80 00 53 01 3C 02 00 0B  ..........S.<...
0150: 80 02 80 02 08 10 03 80  00 62 01 3C 02 00 0C 80  .........b.<....
0160: 02 80 02 09 10 03 80 00  71 01 3C 02 00 05 80 02  ........q.<.....
0170: 80 48 0E 80 23 24 0F 80  03 80 02 00 25 02 00 10  .H..#$......%...
0180: 03 80 00 88 01 01 D8 04  02 00 10 02 80 00 F2 01  ................
0190: 03 01 10 03 80 40 03 80  0C 80 01 10 10 80 43 00  .....@........C.
01A0: 43 01 03 00 00 03 10 48  00 80 23 03 03 10 00 00  C......H..#.....
01B0: 24 01 80 02 80 03 80 25  02 00 10 03 80 00 E4 01  $......%........
01C0: 42 03 01 10 03 80 40 05  80 06 80 01 10 03 80 40  B.....@........@
01D0: 03 80 0C 80 01 10 0D 80  43 00 43 01 03 01 10 02  ........C.C.....
01E0: 10 01 EF 01 02 00 10 02  80 00 EF 01 01 EF 01 01  ................
01F0: D8 04 02 00 10 07 80 00  5C 02 03 01 10 03 80 40  ........\......@
0200: 03 80 0C 80 01 10 11 80  43 00 43 01 03 00 00 03  ........C.C.....
0210: 10 48 00 80 23 03 03 10  00 00 24 01 80 02 80 03  .H..#.....$.....
0220: 80 25 02 00 10 03 80 00  4E 02 42 03 01 10 03 80  .%......N.B.....
0230: 40 05 80 06 80 01 10 02  80 40 03 80 0C 80 01 10  @........@......
0240: 0D 80 43 00 43 01 03 01  10 02 10 01 59 02 02 00  ..C.C.......Y...
0250: 10 02 80 00 59 02 01 59  02 01 D8 04 02 00 10 08  ....Y..Y........
0260: 80 00 C6 02 03 01 10 03  80 40 03 80 0C 80 01 10  .........@......
0270: 06 80 43 00 43 01 03 00  00 03 10 48 00 80 23 03  ..C.C......H..#.
0280: 03 10 00 00 24 01 80 02  80 03 80 25 02 00 10 03  ....$......%....
0290: 80 00 B8 02 42 03 01 10  03 80 40 05 80 06 80 01  ....B.....@.....
02A0: 10 07 80 40 03 80 0C 80  01 10 0D 80 43 00 43 01  ...@........C.C.
02B0: 03 01 10 02 10 01 C3 02  02 00 10 02 80 00 C3 02  ................
02C0: 01 C3 02 01 D8 04 02 00  10 09 80 00 30 03 03 01  ............0...
02D0: 10 03 80 40 03 80 0C 80  01 10 12 80 43 00 43 01  ...@........C.C.
02E0: 03 00 00 03 10 48 00 80  23 03 03 10 00 00 24 01  .....H..#.....$.
02F0: 80 02 80 03 80 25 02 00  10 03 80 00 22 03 42 03  .....%......".B.
0300: 01 10 03 80 40 05 80 06  80 01 10 08 80 40 03 80  ....@........@..
0310: 0C 80 01 10 0D 80 43 00  43 01 03 01 10 02 10 01  ......C.C.......
0320: 2D 03 02 00 10 02 80 00  2D 03 01 2D 03 01 D8 04  -.......-..-....
0330: 02 00 10 0A 80 00 9A 03  03 01 10 03 80 40 03 80  .............@..
0340: 0C 80 01 10 13 80 43 00  43 01 03 00 00 03 10 48  ......C.C......H
0350: 00 80 23 03 03 10 00 00  24 01 80 02 80 03 80 25  ..#.....$......%
0360: 02 00 10 03 80 00 8C 03  42 03 01 10 03 80 40 05  ........B.....@.
0370: 80 06 80 01 10 09 80 40  03 80 0C 80 01 10 0D 80  .......@........
0380: 43 00 43 01 03 01 10 02  10 01 97 03 02 00 10 02  C.C.............
0390: 80 00 97 03 01 97 03 01  D8 04 02 00 10 0B 80 00  ................
03A0: 04 04 03 01 10 03 80 40  03 80 0C 80 01 10 14 80  .......@........
03B0: 43 00 43 01 03 00 00 03  10 48 00 80 23 03 03 10  C.C......H..#...
03C0: 00 00 24 01 80 02 80 03  80 25 02 00 10 03 80 00  ..$......%......
03D0: F6 03 42 03 01 10 03 80  40 05 80 06 80 01 10 0A  ..B.....@.......
03E0: 80 40 03 80 0C 80 01 10  0D 80 43 00 43 01 03 01  .@........C.C...
03F0: 10 02 10 01 01 04 02 00  10 02 80 00 01 04 01 01  ................
0400: 04 01 D8 04 02 00 10 0C  80 00 6E 04 03 01 10 03  ..........n.....
0410: 80 40 03 80 0C 80 01 10  15 80 43 00 43 01 03 00  .@........C.C...
0420: 00 03 10 48 00 80 23 03  03 10 00 00 24 01 80 02  ...H..#.....$...
0430: 80 03 80 25 02 00 10 03  80 00 60 04 42 03 01 10  ...%......`.B...
0440: 03 80 40 05 80 06 80 01  10 0B 80 40 03 80 0C 80  ..@........@....
0450: 01 10 0D 80 43 00 43 01  03 01 10 02 10 01 6B 04  ....C.C.......k.
0460: 02 00 10 02 80 00 6B 04  01 6B 04 01 D8 04 02 00  ......k..k......
0470: 10 05 80 00 D8 04 03 01  10 03 80 40 03 80 0C 80  ...........@....
0480: 01 10 16 80 43 00 43 01  03 00 00 03 10 48 00 80  ....C.C......H..
0490: 23 03 03 10 00 00 24 01  80 02 80 03 80 25 02 00  #.....$......%..
04A0: 10 03 80 00 CA 04 42 03  01 10 03 80 40 05 80 06  ......B.....@...
04B0: 80 01 10 0C 80 40 03 80  0C 80 01 10 0D 80 43 00  .....@........C.
04C0: 43 01 03 01 10 02 10 01  D5 04 02 00 10 02 80 00  C...............
04D0: D5 04 01 D5 04 01 D8 04  21 1B                    ........!.      
```

#### Opcodes

```
  0: 0x0005 [0x1A] CALL_SUBROUTINE(address=0x00F4)
  1: 0x0008 [0x00] END_REQSTACK()

SUBROUTINE_00F4:
  2: 0x00F4 [0x03] ExtData[1]->WorkLocal[2] = 0*
  3: 0x00F9 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0108
  4: 0x0101 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=1*, condition_work_offset=1*)
  5: 0x0108 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0117
  6: 0x0110 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=2*, condition_work_offset=1*)
  7: 0x0117 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0126
  8: 0x011F [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=3*, condition_work_offset=1*)
  9: 0x0126 [0x02] IF !(Work_Zone[5] == 0*) GOTO 0x0135
 10: 0x012E [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=4*, condition_work_offset=1*)
 11: 0x0135 [0x02] IF !(Work_Zone[6] == 0*) GOTO 0x0144
 12: 0x013D [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=5*, condition_work_offset=1*)
 13: 0x0144 [0x02] IF !(Work_Zone[7] == 0*) GOTO 0x0153
 14: 0x014C [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=6*, condition_work_offset=1*)
 15: 0x0153 [0x02] IF !(Work_Zone[8] == 0*) GOTO 0x0162
 16: 0x015B [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=7*, condition_work_offset=1*)
 17: 0x0162 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x0171
 18: 0x016A [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=8*, condition_work_offset=1*)
 19: 0x0171 [0x48] [System] [11657*]:
    → "You currently have multiple Wanted battle objectives set. Select which one you would like to undertake."
 20: 0x0174 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0175 [0x24] CREATE_DIALOG(message_id=11658*, default_option=0*, option_flags=ExtData[1]->WorkLocal[2])
    → "Which objective would you like to undertake? [None for now./$0./$1./$2./$3./$4./$5./$6./$7.]"
 22: 0x017C [0x25] WAIT_DIALOG_SELECT()
 23: 0x017D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0188
 24: 0x0185 [0x01] GOTO 0x04D8
 25: 0x0188 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01F2
 26: 0x0190 [0x03] Work_Zone[1] = 0*
 27: 0x0195 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=13*)
 28: 0x019E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 29: 0x01A0 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 30: 0x01A2 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
 31: 0x01A7 [0x48] [System] [11639*]:
    → "Those who have accepted $0 must pay $1 Unity accolades to participate. The content for this Wanted battle is $2. [Ready to begin?/You do not have the appropriate object set, so your rewards will be limited.]"
 32: 0x01AA [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x01AB [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
 34: 0x01B0 [0x24] CREATE_DIALOG(message_id=11640*, default_option=1*, option_flags=0*)
    → "Commence the Wanted battle? ($1 acc.) [Let's go!/Not yet.]"
 35: 0x01B7 [0x25] WAIT_DIALOG_SELECT()
 36: 0x01B8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01E4
 37: 0x01C0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 38: 0x01C1 [0x03] Work_Zone[1] = 0*
 39: 0x01C6 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=0*)
 40: 0x01CF [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=12*)
 41: 0x01D8 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 42: 0x01DA [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 43: 0x01DC [0x03] Work_Zone[1] = Work_Zone[2]
 44: 0x01E1 [0x01] GOTO 0x01EF
 45: 0x01E4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01EF
 46: 0x01EC [0x01] GOTO 0x01EF

SUBROUTINE_01EF:
 47: 0x01EF [0x01] GOTO 0x04D8
 48: 0x01F2 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x025C
 49: 0x01FA [0x03] Work_Zone[1] = 0*
 50: 0x01FF [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=14*)
 51: 0x0208 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 52: 0x020A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 53: 0x020C [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
 54: 0x0211 [0x48] [System] [11639*]:
    → "Those who have accepted $0 must pay $1 Unity accolades to participate. The content for this Wanted battle is $2. [Ready to begin?/You do not have the appropriate object set, so your rewards will be limited.]"
 55: 0x0214 [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x0215 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
 57: 0x021A [0x24] CREATE_DIALOG(message_id=11640*, default_option=1*, option_flags=0*)
    → "Commence the Wanted battle? ($1 acc.) [Let's go!/Not yet.]"
 58: 0x0221 [0x25] WAIT_DIALOG_SELECT()
 59: 0x0222 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x024E
 60: 0x022A [0x42] SET_CLI_EVENT_CANCEL_DATA()
 61: 0x022B [0x03] Work_Zone[1] = 0*
 62: 0x0230 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=1*)
 63: 0x0239 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=12*)
 64: 0x0242 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 65: 0x0244 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 66: 0x0246 [0x03] Work_Zone[1] = Work_Zone[2]
 67: 0x024B [0x01] GOTO 0x0259
 68: 0x024E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0259
 69: 0x0256 [0x01] GOTO 0x0259

SUBROUTINE_0259:
 70: 0x0259 [0x01] GOTO 0x04D8
 71: 0x025C [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x02C6
 72: 0x0264 [0x03] Work_Zone[1] = 0*
 73: 0x0269 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=15*)
 74: 0x0272 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 75: 0x0274 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 76: 0x0276 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
 77: 0x027B [0x48] [System] [11639*]:
    → "Those who have accepted $0 must pay $1 Unity accolades to participate. The content for this Wanted battle is $2. [Ready to begin?/You do not have the appropriate object set, so your rewards will be limited.]"
 78: 0x027E [0x23] WAIT_FOR_DIALOG_INTERACTION
 79: 0x027F [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
 80: 0x0284 [0x24] CREATE_DIALOG(message_id=11640*, default_option=1*, option_flags=0*)
    → "Commence the Wanted battle? ($1 acc.) [Let's go!/Not yet.]"
 81: 0x028B [0x25] WAIT_DIALOG_SELECT()
 82: 0x028C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02B8
 83: 0x0294 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 84: 0x0295 [0x03] Work_Zone[1] = 0*
 85: 0x029A [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=2*)
 86: 0x02A3 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=12*)
 87: 0x02AC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 88: 0x02AE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 89: 0x02B0 [0x03] Work_Zone[1] = Work_Zone[2]
 90: 0x02B5 [0x01] GOTO 0x02C3
 91: 0x02B8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02C3
 92: 0x02C0 [0x01] GOTO 0x02C3

SUBROUTINE_02C3:
 93: 0x02C3 [0x01] GOTO 0x04D8
 94: 0x02C6 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0330
 95: 0x02CE [0x03] Work_Zone[1] = 0*
 96: 0x02D3 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=16*)
 97: 0x02DC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 98: 0x02DE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 99: 0x02E0 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
100: 0x02E5 [0x48] [System] [11639*]:
    → "Those who have accepted $0 must pay $1 Unity accolades to participate. The content for this Wanted battle is $2. [Ready to begin?/You do not have the appropriate object set, so your rewards will be limited.]"
101: 0x02E8 [0x23] WAIT_FOR_DIALOG_INTERACTION
102: 0x02E9 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
103: 0x02EE [0x24] CREATE_DIALOG(message_id=11640*, default_option=1*, option_flags=0*)
    → "Commence the Wanted battle? ($1 acc.) [Let's go!/Not yet.]"
104: 0x02F5 [0x25] WAIT_DIALOG_SELECT()
105: 0x02F6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0322
106: 0x02FE [0x42] SET_CLI_EVENT_CANCEL_DATA()
107: 0x02FF [0x03] Work_Zone[1] = 0*
108: 0x0304 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=3*)
109: 0x030D [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=12*)
110: 0x0316 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
111: 0x0318 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
112: 0x031A [0x03] Work_Zone[1] = Work_Zone[2]
113: 0x031F [0x01] GOTO 0x032D
114: 0x0322 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x032D
115: 0x032A [0x01] GOTO 0x032D

SUBROUTINE_032D:
116: 0x032D [0x01] GOTO 0x04D8
117: 0x0330 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x039A
118: 0x0338 [0x03] Work_Zone[1] = 0*
119: 0x033D [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=17*)
120: 0x0346 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
121: 0x0348 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
122: 0x034A [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
123: 0x034F [0x48] [System] [11639*]:
    → "Those who have accepted $0 must pay $1 Unity accolades to participate. The content for this Wanted battle is $2. [Ready to begin?/You do not have the appropriate object set, so your rewards will be limited.]"
124: 0x0352 [0x23] WAIT_FOR_DIALOG_INTERACTION
125: 0x0353 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
126: 0x0358 [0x24] CREATE_DIALOG(message_id=11640*, default_option=1*, option_flags=0*)
    → "Commence the Wanted battle? ($1 acc.) [Let's go!/Not yet.]"
127: 0x035F [0x25] WAIT_DIALOG_SELECT()
128: 0x0360 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x038C
129: 0x0368 [0x42] SET_CLI_EVENT_CANCEL_DATA()
130: 0x0369 [0x03] Work_Zone[1] = 0*
131: 0x036E [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=4*)
132: 0x0377 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=12*)
133: 0x0380 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
134: 0x0382 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
135: 0x0384 [0x03] Work_Zone[1] = Work_Zone[2]
136: 0x0389 [0x01] GOTO 0x0397
137: 0x038C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0397
138: 0x0394 [0x01] GOTO 0x0397

SUBROUTINE_0397:
139: 0x0397 [0x01] GOTO 0x04D8
140: 0x039A [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0404
141: 0x03A2 [0x03] Work_Zone[1] = 0*
142: 0x03A7 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=18*)
143: 0x03B0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
144: 0x03B2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
145: 0x03B4 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
146: 0x03B9 [0x48] [System] [11639*]:
    → "Those who have accepted $0 must pay $1 Unity accolades to participate. The content for this Wanted battle is $2. [Ready to begin?/You do not have the appropriate object set, so your rewards will be limited.]"
147: 0x03BC [0x23] WAIT_FOR_DIALOG_INTERACTION
148: 0x03BD [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
149: 0x03C2 [0x24] CREATE_DIALOG(message_id=11640*, default_option=1*, option_flags=0*)
    → "Commence the Wanted battle? ($1 acc.) [Let's go!/Not yet.]"
150: 0x03C9 [0x25] WAIT_DIALOG_SELECT()
151: 0x03CA [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03F6
152: 0x03D2 [0x42] SET_CLI_EVENT_CANCEL_DATA()
153: 0x03D3 [0x03] Work_Zone[1] = 0*
154: 0x03D8 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=5*)
155: 0x03E1 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=12*)
156: 0x03EA [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
157: 0x03EC [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
158: 0x03EE [0x03] Work_Zone[1] = Work_Zone[2]
159: 0x03F3 [0x01] GOTO 0x0401
160: 0x03F6 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0401
161: 0x03FE [0x01] GOTO 0x0401

SUBROUTINE_0401:
162: 0x0401 [0x01] GOTO 0x04D8
163: 0x0404 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x046E
164: 0x040C [0x03] Work_Zone[1] = 0*
165: 0x0411 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=19*)
166: 0x041A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
167: 0x041C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
168: 0x041E [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
169: 0x0423 [0x48] [System] [11639*]:
    → "Those who have accepted $0 must pay $1 Unity accolades to participate. The content for this Wanted battle is $2. [Ready to begin?/You do not have the appropriate object set, so your rewards will be limited.]"
170: 0x0426 [0x23] WAIT_FOR_DIALOG_INTERACTION
171: 0x0427 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
172: 0x042C [0x24] CREATE_DIALOG(message_id=11640*, default_option=1*, option_flags=0*)
    → "Commence the Wanted battle? ($1 acc.) [Let's go!/Not yet.]"
173: 0x0433 [0x25] WAIT_DIALOG_SELECT()
174: 0x0434 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0460
175: 0x043C [0x42] SET_CLI_EVENT_CANCEL_DATA()
176: 0x043D [0x03] Work_Zone[1] = 0*
177: 0x0442 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=6*)
178: 0x044B [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=12*)
179: 0x0454 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
180: 0x0456 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
181: 0x0458 [0x03] Work_Zone[1] = Work_Zone[2]
182: 0x045D [0x01] GOTO 0x046B
183: 0x0460 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x046B
184: 0x0468 [0x01] GOTO 0x046B

SUBROUTINE_046B:
185: 0x046B [0x01] GOTO 0x04D8
186: 0x046E [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x04D8
187: 0x0476 [0x03] Work_Zone[1] = 0*
188: 0x047B [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=20*)
189: 0x0484 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
190: 0x0486 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
191: 0x0488 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
192: 0x048D [0x48] [System] [11639*]:
    → "Those who have accepted $0 must pay $1 Unity accolades to participate. The content for this Wanted battle is $2. [Ready to begin?/You do not have the appropriate object set, so your rewards will be limited.]"
193: 0x0490 [0x23] WAIT_FOR_DIALOG_INTERACTION
194: 0x0491 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
195: 0x0496 [0x24] CREATE_DIALOG(message_id=11640*, default_option=1*, option_flags=0*)
    → "Commence the Wanted battle? ($1 acc.) [Let's go!/Not yet.]"
196: 0x049D [0x25] WAIT_DIALOG_SELECT()
197: 0x049E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x04CA
198: 0x04A6 [0x42] SET_CLI_EVENT_CANCEL_DATA()
199: 0x04A7 [0x03] Work_Zone[1] = 0*
200: 0x04AC [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=7*)
201: 0x04B5 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=12*)
202: 0x04BE [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
203: 0x04C0 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
204: 0x04C2 [0x03] Work_Zone[1] = Work_Zone[2]
205: 0x04C7 [0x01] GOTO 0x04D5
206: 0x04CA [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x04D5
207: 0x04D2 [0x01] GOTO 0x04D5

SUBROUTINE_04D5:
208: 0x04D5 [0x01] GOTO 0x04D8

SUBROUTINE_04D8:
209: 0x04D8 [0x21] END_EVENT
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0009 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
     0x000E [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
     0x0013 [0x48] [System] [11639*]:
    → "Those who have accepted $0 must pay $1 Unity accolades to participate. The content for this Wanted battle is $2. [Ready to begin?/You do not have the appropriate object set, so your rewards will be limited.]"
     0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0017 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
     0x001C [0x24] CREATE_DIALOG(message_id=11640*, default_option=1*, option_flags=0*)
    → "Commence the Wanted battle? ($1 acc.) [Let's go!/Not yet.]"
     0x0023 [0x25] WAIT_DIALOG_SELECT()
     0x0024 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00E7
     0x002C [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x002D [0x03] Work_Zone[1] = 0*
     0x0032 [0x02] IF !(ExtData[1]->WorkLocal[1] == 864*) GOTO 0x0046
     0x003A [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=0*)
     0x0043 [0x01] GOTO 0x00D2
     0x0046 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x005A
     0x004E [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=1*)
     0x0057 [0x01] GOTO 0x00D2
     0x005A [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x006E
     0x0062 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=2*)
     0x006B [0x01] GOTO 0x00D2
     0x006E [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0082
     0x0076 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=3*)
     0x007F [0x01] GOTO 0x00D2
     0x0082 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0096
     0x008A [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=4*)
     0x0093 [0x01] GOTO 0x00D2
     0x0096 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00AA
     0x009E [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=5*)
     0x00A7 [0x01] GOTO 0x00D2
     0x00AA [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00BE
     0x00B2 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=6*)
     0x00BB [0x01] GOTO 0x00D2
     0x00BE [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00D2
     0x00C6 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=7*)
     0x00CF [0x01] GOTO 0x00D2
     0x00D2 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=12*)
     0x00DB [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x00DD [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x00DF [0x03] Work_Zone[1] = Work_Zone[2]
     0x00E4 [0x01] GOTO 0x00F2
     0x00E7 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00F2
     0x00EF [0x01] GOTO 0x00F2
     0x00F2 [0x21] END_EVENT
     0x00F3 [0x1B] RETURN
# Dead code (unreachable instructions):
     0x04D9 [0x1B] RETURN
```
