# 16982069 - Sharin-Garin

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 1316 bytes                    |
| Total Events     | 6                             |
| References Count | 42                            |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [140](#event-140)         | 0x0001       |     54 |              8 |
| [141](#event-141)         | 0x0037       |     54 |              8 |
| [142](#event-142)         | 0x006D       |    920 |            167 |
| [269](#event-269)         | 0x0405       |      1 |              1 |
| [65535.1](#event-65535-1) | 0x0406       |     75 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0022      |          34 |
|       1 | 0x1215      |        4629 |
|       2 | 0x1223      |        4643 |
|       3 | 0x1216      |        4630 |
|       4 | 0x0000      |           0 |
|       5 | 0x0001      |           1 |
|       6 | 0x1217      |        4631 |
|       7 | 0x030E      |         782 |
|       8 | 0x1218      |        4632 |
|       9 | 0x00C8      |         200 |
|      10 | 0x1219      |        4633 |
|      11 | 0x121A      |        4634 |
|      12 | 0x121B      |        4635 |
|      13 | 0x0028      |          40 |
|      14 | 0x1221      |        4641 |
|      15 | 0x1222      |        4642 |
|      16 | 0x1220      |        4640 |
|      17 | 0x121C      |        4636 |
|      18 | 0x003C      |          60 |
|      19 | 0x0002      |           2 |
|      20 | 0x121F      |        4639 |
|      21 | 0x0029      |          41 |
|      22 | 0x121D      |        4637 |
|      23 | 0x121E      |        4638 |
|      24 | 0x1224      |        4644 |
|      25 | 0x1225      |        4645 |
|      26 | 0x1226      |        4646 |
|      27 | 0x0003      |           3 |
|      28 | 0x1227      |        4647 |
|      29 | 0x1228      |        4648 |
|      30 | 0x122F      |        4655 |
|      31 | 0x1229      |        4649 |
|      32 | 0x122C      |        4652 |
|      33 | 0x122A      |        4650 |
|      34 | 0x0004      |           4 |
|      35 | 0x122B      |        4651 |
|      36 | 0x0005      |           5 |
|      37 | 0x122D      |        4653 |
|      38 | 0x122E      |        4654 |
|      39 | 0x001E      |          30 |
|      40 | 0x0078      |         120 |
|      41 | 0x002A      |          42 |

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

### Event 140

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 54 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 79 00 35 20 03  01 F0 FF FF 7F 66 00 80    .y.5 ......f..
0010: 35 20 03 01 35 20 03 01  74 6C 62 30 1D 01 80 23  5 ..5 ..tlb0...#
0020: 66 00 80 35 20 03 01 35  20 03 01 74 6C 62 31 27  f..5 ..5 ..tlb1'
0030: 01 35 20 03 01 03 00                              .5 ....         
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x79] Sharin-Garin (ID: 16982069/0x01032035) looks at LocalPlayer (Basic look)
  2: 0x000D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=34*
  3: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=4629*)
    → "Welcome to the Chamber of Passage.\u0007From here, you can travel to the Assault staging points. Is there anything else you wish to know?\u007F1\u0000\u0007"
  4: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0020 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=34*
  6: 0x002F [0x27] REQ_SET(priority=0x01, entity_id=Sharin-Garin (ID: 16982069/0x01032035), tag_num=0x03)
  7: 0x0036 [0x00] END_REQSTACK()
```

### Event 141

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 54 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      20  01 79 00 35 20 03 01 F0          .y.5 ...
0040: FF FF 7F 66 00 80 35 20  03 01 35 20 03 01 74 6C  ...f..5 ..5 ..tl
0050: 62 30 1D 02 80 23 66 00  80 35 20 03 01 35 20 03  b0...#f..5 ..5 .
0060: 01 74 6C 62 31 27 01 35  20 03 01 03 00           .tlb1'.5 ....   
```

#### Opcodes

```
  0: 0x0037 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0039 [0x79] Sharin-Garin (ID: 16982069/0x01032035) looks at LocalPlayer (Basic look)
  2: 0x0043 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=34*
  3: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=4643*)
    → "Is there anything else you wanted to ask?\u007F1\u0000\u0007"
  4: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0056 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=34*
  6: 0x0065 [0x27] REQ_SET(priority=0x01, entity_id=Sharin-Garin (ID: 16982069/0x01032035), tag_num=0x03)
  7: 0x006C [0x00] END_REQSTACK()
```

### Event 142

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x006D    |
| Data Size    | 920 bytes |
| Instructions | 75        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         24 03 80               $..
0070: 04 80 04 80 25 02 00 10  04 80 00 81 00 42 01 F2  ....%........B..
0080: 03 02 00 10 05 80 00 23  02 42 79 00 35 20 03 01  .......#.By.5 ..
0090: F0 FF FF 7F 66 00 80 35  20 03 01 35 20 03 01 74  ....f..5 ..5 ..t
00A0: 6C 62 30 1D 06 80 23 03  02 10 07 80 1D 08 80 23  lb0...#........#
00B0: 03 07 10 09 80 02 08 10  04 80 00 C4 00 1D 0A 80  ................
00C0: 23 01 C8 00 1D 0B 80 23  24 0C 80 05 80 04 80 25  #......#$......%
00D0: 02 00 10 04 80 00 EB 01  02 06 10 04 80 00 11 01  ................
00E0: 66 0D 80 35 20 03 01 35  20 03 01 74 68 6B 31 1D  f..5 ..5 ..thk1.
00F0: 0E 80 23 1D 0F 80 23 66  0D 80 35 20 03 01 35 20  ..#...#f..5 ..5 
0100: 03 01 74 68 6B 32 27 01  35 20 03 01 02 00 01 E8  ..thk2'.5 ......
0110: 01 02 03 10 04 80 00 46  01 66 0D 80 35 20 03 01  .......F.f..5 ..
0120: 35 20 03 01 74 68 6B 31  1D 10 80 23 66 0D 80 35  5 ..thk1...#f..5
0130: 20 03 01 35 20 03 01 74  68 6B 32 27 01 35 20 03   ..5 ..thk2'.5 .
0140: 01 02 00 01 E8 01 02 04  10 04 80 00 C5 01 02 08  ................
0150: 10 04 80 01 79 01 03 02  10 07 80 1D 11 80 23 66  ....y.........#f
0160: 0D 80 35 20 03 01 35 20  03 01 70 61 73 30 1C 12  ..5 ..5 ..pas0..
0170: 80 03 01 10 13 80 01 C2  01 02 05 10 09 80 03 A2  ................
0180: 01 66 0D 80 35 20 03 01  35 20 03 01 64 69 73 30  .f..5 ..5 ..dis0
0190: 1C 12 80 1D 14 80 23 27  01 35 20 03 01 02 00 01  ......#'.5 .....
01A0: C2 01 03 02 10 07 80 1D  11 80 23 66 0D 80 35 20  ..........#f..5 
01B0: 03 01 35 20 03 01 70 61  73 30 1C 12 80 03 01 10  ..5 ..pas0......
01C0: 05 80 01 E8 01 66 15 80  35 20 03 01 35 20 03 01  .....f..5 ..5 ..
01D0: 73 68 6B 30 1C 12 80 03  02 10 07 80 1D 16 80 23  shk0...........#
01E0: 27 01 35 20 03 01 02 00  01 20 02 02 00 10 05 80  '.5 ..... ......
01F0: 00 20 02 66 0D 80 35 20  03 01 35 20 03 01 74 68  . .f..5 ..5 ..th
0200: 6B 31 1D 17 80 23 66 0D  80 35 20 03 01 35 20 03  k1...#f..5 ..5 .
0210: 01 74 68 6B 32 27 01 35  20 03 01 02 00 01 20 02  .thk2'.5 ..... .
0220: 01 F2 03 02 00 10 13 80  00 5C 02 42 79 00 35 20  .........\.By.5 
0230: 03 01 F0 FF FF 7F 66 00  80 35 20 03 01 35 20 03  ......f..5 ..5 .
0240: 01 74 6C 62 30 1D 18 80  23 1D 19 80 23 1D 1A 80  .tlb0...#...#...
0250: 23 27 01 35 20 03 01 02  00 01 F2 03 02 00 10 1B  #'.5 ...........
0260: 80 00 C1 03 42 79 00 35  20 03 01 F0 FF FF 7F 66  ....By.5 ......f
0270: 00 80 35 20 03 01 35 20  03 01 74 6C 62 30 1D 1C  ..5 ..5 ..tlb0..
0280: 80 23 66 00 80 35 20 03  01 35 20 03 01 74 6C 62  .#f..5 ..5 ..tlb
0290: 31 24 1D 80 04 80 04 80  25 02 00 10 04 80 00 CE  1$......%.......
02A0: 02 66 0D 80 35 20 03 01  35 20 03 01 74 68 6B 31  .f..5 ..5 ..thk1
02B0: 1D 1E 80 23 66 0D 80 35  20 03 01 35 20 03 01 74  ...#f..5 ..5 ..t
02C0: 68 6B 32 27 01 35 20 03  01 02 00 01 BE 03 02 00  hk2'.5 .........
02D0: 10 05 80 00 FE 02 79 00  35 20 03 01 F0 FF FF 7F  ......y.5 ......
02E0: 66 00 80 35 20 03 01 35  20 03 01 74 6C 62 30 1D  f..5 ..5 ..tlb0.
02F0: 1F 80 23 27 01 35 20 03  01 02 00 01 BE 03 02 00  ..#'.5 .........
0300: 10 13 80 00 2E 03 79 00  35 20 03 01 F0 FF FF 7F  ......y.5 ......
0310: 66 00 80 35 20 03 01 35  20 03 01 74 6C 62 30 1D  f..5 ..5 ..tlb0.
0320: 20 80 23 27 01 35 20 03  01 02 00 01 BE 03 02 00   .#'.5 .........
0330: 10 1B 80 00 5E 03 79 00  35 20 03 01 F0 FF FF 7F  ....^.y.5 ......
0340: 66 00 80 35 20 03 01 35  20 03 01 74 6C 62 30 1D  f..5 ..5 ..tlb0.
0350: 21 80 23 27 01 35 20 03  01 02 00 01 BE 03 02 00  !.#'.5 .........
0360: 10 22 80 00 8E 03 79 00  35 20 03 01 F0 FF FF 7F  ."....y.5 ......
0370: 66 00 80 35 20 03 01 35  20 03 01 74 6C 62 30 1D  f..5 ..5 ..tlb0.
0380: 23 80 23 27 01 35 20 03  01 02 00 01 BE 03 02 00  #.#'.5 .........
0390: 10 24 80 00 BE 03 79 00  35 20 03 01 F0 FF FF 7F  .$....y.5 ......
03A0: 66 00 80 35 20 03 01 35  20 03 01 74 6C 62 30 1D  f..5 ..5 ..tlb0.
03B0: 25 80 23 27 01 35 20 03  01 02 00 01 BE 03 01 F2  %.#'.5 .........
03C0: 03 02 00 10 22 80 00 F2  03 42 79 00 35 20 03 01  ...."....By.5 ..
03D0: F0 FF FF 7F 66 00 80 35  20 03 01 35 20 03 01 74  ....f..5 ..5 ..t
03E0: 6C 62 30 1D 26 80 23 27  01 35 20 03 01 02 00 01  lb0.&.#'.5 .....
03F0: F2 03 66 00 80 35 20 03  01 35 20 03 01 74 6C 62  ..f..5 ..5 ..tlb
0400: 31 20 00 21 00                                    1 .!.           
```

#### Opcodes

```
  0: 0x006D [0x24] CREATE_DIALOG(message_id=4630*, default_option=0*, option_flags=0*)
    → "Ask about...\u0007\u000BNothing.\u0007Using runic portals.\u0007The Chamber of Passage.\u0007Staging Points.\u0007Assault.\u007F1\u0000\u0007"
  1: 0x0074 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0075 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0081
  3: 0x007D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x007E [0x01] GOTO 0x03F2
  5: 0x0081 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0223
  6: 0x0089 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x008A [0x79] Sharin-Garin (ID: 16982069/0x01032035) looks at LocalPlayer (Basic look)
  8: 0x0094 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=34*
  9: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=4631*)
    → "You may freely use the runic portals if you possess an Assault order.\u007F1\u0000\u0007"
 10: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00A7 [0x03] Work_Zone[2] = 782*
 12: 0x00AC [0x1D] PRINT_EVENT_MESSAGE(message_id=4632*)
    → "However, you must be carrying \u0001\u00056\u0002\u0000\u0000\u0000 if you are not participating in an Assault mission.\u007F1\u0000\u0007"
 13: 0x00AF [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00B0 [0x03] Work_Zone[7] = 200*
 15: 0x00B5 [0x02] IF !(Work_Zone[8] == 0*) GOTO 0x00C4
 16: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=4633*)
    → "Your Imperial Standing is currently equal to 
\u0003 points. If you wish, you can purchase \u0001\u00056\u0002\u0000\u0000\u0000 with 
\u0005 points.\u007F1\u0000\u0007"
 17: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x00C1 [0x01] GOTO 0x00C8
 19: 0x00C4 [0x1D] PRINT_EVENT_MESSAGE(message_id=4634*)
    → "Your rank of captain allows you to purchase \u0001\u00056\u0002\u0000\u0000\u0000 free of charge.\u007F1\u0000\u0007"
 20: 0x00C7 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00C8:
 21: 0x00C8 [0x24] CREATE_DIALOG(message_id=4635*, default_option=1*, option_flags=0*)
    → "Purchase \u0001\u00056\u0002\u0000\u0000\u0000?\u0007\u000BYes.\u0007No.\u007F1\u0000\u0007"
 22: 0x00CF [0x25] WAIT_DIALOG_SELECT()
 23: 0x00D0 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01EB
 24: 0x00D8 [0x02] IF !(Work_Zone[6] == 0*) GOTO 0x0111
 25: 0x00E0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=40*
 26: 0x00EF [0x1D] PRINT_EVENT_MESSAGE(message_id=4641*)
    → "Ah, the Astral Candescence is too far for its waves to reach the portals now, so we have to conserve their energy.\u007F1\u0000\u0007"
 27: 0x00F2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x00F3 [0x1D] PRINT_EVENT_MESSAGE(message_id=4642*)
    → "I'm sorry, but we have orders from the Empire forbidding us from distributing a single \u0001\u00053\u0002\u0000\u0000\u0000 until the Astral Candescence is back out of the beastmen's stronghold and safe here in town.\u007F1\u0000\u0007"
 29: 0x00F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x00F7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=40*
 31: 0x0106 [0x27] REQ_SET(priority=0x01, entity_id=Sharin-Garin (ID: 16982069/0x01032035), tag_num=0x02)
 32: 0x010D [0x00] END_REQSTACK()

SUBROUTINE_01C2:
 33: 0x01C2 [0x01] GOTO 0x01E8
 34: 0x01C5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "shk0" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=41*
 35: 0x01D4 [0x1C] WAIT(60* ticks)
 36: 0x01D7 [0x03] Work_Zone[2] = 782*
 37: 0x01DC [0x1D] PRINT_EVENT_MESSAGE(message_id=4637*)
    → "What's this? I am afraid that you already have a \u0001\u00053\u0002\u0000\u0000\u0000 in your possession.\u007F1\u0000\u0007"
 38: 0x01DF [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x01E0 [0x27] REQ_SET(priority=0x01, entity_id=Sharin-Garin (ID: 16982069/0x01032035), tag_num=0x02)
 40: 0x01E7 [0x00] END_REQSTACK()

SUBROUTINE_01E8:
 41: 0x01E8 [0x01] GOTO 0x0220
 42: 0x01EB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0220
 43: 0x01F3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=40*
 44: 0x0202 [0x1D] PRINT_EVENT_MESSAGE(message_id=4638*)
    → "Hmmm...\u007F1\u0000\u0007"
 45: 0x0205 [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x0206 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=40*
 47: 0x0215 [0x27] REQ_SET(priority=0x01, entity_id=Sharin-Garin (ID: 16982069/0x01032035), tag_num=0x02)
 48: 0x021C [0x00] END_REQSTACK()

SUBROUTINE_0220:
 49: 0x0220 [0x01] GOTO 0x03F2
 50: 0x0223 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x025C
 51: 0x022B [0x42] SET_CLI_EVENT_CANCEL_DATA()
 52: 0x022C [0x79] Sharin-Garin (ID: 16982069/0x01032035) looks at LocalPlayer (Basic look)
 53: 0x0236 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=34*
 54: 0x0245 [0x1D] PRINT_EVENT_MESSAGE(message_id=4644*)
    → "This Chamber of Passage was built so the Empire could send soldiers to Assault areas at a moment's notice.\u007F1\u0000\u0007"
 55: 0x0248 [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x0249 [0x1D] PRINT_EVENT_MESSAGE(message_id=4645*)
    → "You can use the runic portals inside to travel to a staging point in the blink of an eye.\u007F1\u0000\u0007"
 57: 0x024C [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x024D [0x1D] PRINT_EVENT_MESSAGE(message_id=4646*)
    → "You've got to open the way first by activating the portal at the staging point, though.\u007F1\u0000\u0007"
 59: 0x0250 [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x0251 [0x27] REQ_SET(priority=0x01, entity_id=Sharin-Garin (ID: 16982069/0x01032035), tag_num=0x02)
 61: 0x0258 [0x00] END_REQSTACK()

SUBROUTINE_03BE:
 62: 0x03BE [0x01] GOTO 0x03F2
 63: 0x03C1 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x03F2
 64: 0x03C9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 65: 0x03CA [0x79] Sharin-Garin (ID: 16982069/0x01032035) looks at LocalPlayer (Basic look)
 66: 0x03D4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=34*
 67: 0x03E3 [0x1D] PRINT_EVENT_MESSAGE(message_id=4654*)
    → "If you would like information on Assault, please visit the Commissions Agency, right across the way from this building.\u007F1\u0000\u0007"
 68: 0x03E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 69: 0x03E7 [0x27] REQ_SET(priority=0x01, entity_id=Sharin-Garin (ID: 16982069/0x01032035), tag_num=0x02)
 70: 0x03EE [0x00] END_REQSTACK()

SUBROUTINE_03F2:
 71: 0x03F2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [Sharin-Garin (ID: 16982069/0x01032035), Sharin-Garin (ID: 16982069/0x01032035)], work=34*
 72: 0x0401 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 73: 0x0403 [0x21] END_EVENT
 74: 0x0404 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x010E [0x01] GOTO 0x01E8
     0x0143 [0x01] GOTO 0x01E8
     0x019F [0x01] GOTO 0x01C2
# Dead code (unreachable instructions):
     0x021D [0x01] GOTO 0x0220
# Dead code (unreachable instructions):
     0x0259 [0x01] GOTO 0x03F2
     0x02CB [0x01] GOTO 0x03BE
     0x02FB [0x01] GOTO 0x03BE
     0x032B [0x01] GOTO 0x03BE
     0x035B [0x01] GOTO 0x03BE
     0x038B [0x01] GOTO 0x03BE
     0x03BB [0x01] GOTO 0x03BE
# Dead code (unreachable instructions):
     0x03EF [0x01] GOTO 0x03F2
```

### Event 269

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0405  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0400:                00                                      .          
```

#### Opcodes

```
  0: 0x0405 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0406   |
| Data Size    | 75 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0400:                   1E 30  21 03 01 1C 27 80 66 0D        .0!...'.f.
0410: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1C 28 80  .........tlk0.(.
0420: 66 0D 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 6E  f..........tlk1n
0430: 30 21 03 01 04 80 99 30  21 03 01 1C 12 80 66 29  0!.....0!.....f)
0440: 80 F8 FF FF 7F F8 FF FF  7F 62 69 6B 30 1C 12 80  .........bik0...
0450: 00                                                .               
```

#### Opcodes

```
  0: 0x0406 [0x1E] EventEntity looks at Bashraf (ID: 16982320/0x01032130) and starts talking
  1: 0x040B [0x1C] WAIT(30* ticks)
  2: 0x040E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x041D [0x1C] WAIT(120* ticks)
  4: 0x0420 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  5: 0x042F [0x6E] Bashraf (ID: 16982320/0x01032130) uses emote 0*
  6: 0x0436 [0x99] Wait for Bashraf (ID: 16982320/0x01032130) animation to complete
  7: 0x043B [0x1C] WAIT(60* ticks)
  8: 0x043E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=42*
  9: 0x044D [0x1C] WAIT(60* ticks)
 10: 0x0450 [0x00] END_REQSTACK()
```
