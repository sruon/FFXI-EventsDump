# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Leujaoam Sanctum (ID: 69) |
| Block Size       | 728 bytes                 |
| Total Events     | 6                         |
| References Count | 29                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [101](#event-101)     | 0x0002       |     26 |              7 |
| [102](#event-102)     | 0x001C       |     46 |              9 |
| [50](#event-50)       | 0x004A       |      9 |              4 |
| [103](#event-103)     | 0x0053       |    486 |            108 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x00C9      |         201 |
|       4 | 0x008C      |         140 |
|       5 | 0x0001      |           1 |
|       6 | 0x1DB6      |        7606 |
|       7 | 0x1DB7      |        7607 |
|       8 | 0x03E7      |         999 |
|       9 | 0x1DBD      |        7613 |
|      10 | 0x03E6      |         998 |
|      11 | 0x1DBA      |        7610 |
|      12 | 0x1DC1      |        7617 |
|      13 | 0x1DBE      |        7614 |
|      14 | 0x1DBF      |        7615 |
|      15 | 0x03E8      |        1000 |
|      16 | 0x1DC0      |        7616 |
|      17 | 0x01F3      |         499 |
|      18 | 0x1DBB      |        7611 |
|      19 | 0x1DBC      |        7612 |
|      20 | 0x1DC2      |        7618 |
|      21 | 0x1DC5      |        7621 |
|      22 | 0x0003      |           3 |
|      23 | 0x1DC4      |        7620 |
|      24 | 0x0002      |           2 |
|      25 | 0x1DC3      |        7619 |
|      26 | 0x1DB8      |        7608 |
|      27 | 0x088B      |        2187 |
|      28 | 0x1DB9      |        7609 |

## String References

- **7607**: Throwing dice around? [Yes, let's gooo!/What yooo mean?]
- **7612**: The Qiqirn Dealer's total has exceeded 1,000!
- **7613**: You roll the dice... The result is $0.
- **7614**: Roll the dice again? [Yes, please./I'll stop here!]
- **7615**: You roll the dice again... The result is $0. Your total is now $1.
- **7616**: <Player>'s total has exceeded 1,000!
- **7617**: Current totals: You: $0 Qiqirn Dealer: $1
- **7618**: Final results: You: $0 Qiqirn Dealer: $1
- **7619**: <Player> wins!
- **7620**: <Player> loses!

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

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 42 45 00 80  F0 FF FF 7F F0 FF FF 7F     .BE..........
0010: 66 64 6F 31 01 80 1C 02  80 30 21 00              fdo1.....0!.    
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0016 [0x1C] WAIT(60* ticks)
  4: 0x0019 [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x001A [0x21] END_EVENT
  6: 0x001B [0x00] END_REQSTACK()
```

### Event 102

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 46 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      20 01 42 9F               .B.
0020: 03 80 F8 FF FF 7F F8 FF  FF 7F 6D 61 69 6E 01 80  ..........main..
0030: 1C 04 80 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0040: 6F 31 01 80 1C 02 80 30  21 00                    o1.....0!.      
```

#### Opcodes

```
  0: 0x001C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x001E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x001F [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[201*, 0*]
  3: 0x0030 [0x1C] WAIT(140* ticks)
  4: 0x0033 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x0044 [0x1C] WAIT(60* ticks)
  6: 0x0047 [0x30] SET_UCOFF_CONTINUE_ZERO()
  7: 0x0048 [0x21] END_EVENT
  8: 0x0049 [0x00] END_REQSTACK()
```

### Event 50

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 9 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                20 01 03 01 10 05             .....
0050: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x004A [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x004C [0x03] Work_Zone[1] = 1*
  2: 0x0051 [0x21] END_EVENT
  3: 0x0052 [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0053    |
| Data Size    | 486 bytes |
| Instructions | 107       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          20 01 42 2B 5A  50 04 01 06 80 23 24 07      .B+ZP....#$.
0060: 80 05 80 01 80 25 02 00  10 01 80 00 0E 02 43 00  .....%........C.
0070: 43 01 13 00 00 08 80 0B  00 00 03 02 00 00 00 03  C...............
0080: 02 10 00 00 49 5A 50 04  01 09 80 23 13 00 00 0A  ....IZP....#....
0090: 80 0B 00 00 03 01 00 00  00 03 02 10 00 00 2B 5A  ..............+Z
00A0: 50 04 01 0B 80 23 03 03  00 01 80 03 02 10 02 00  P....#..........
00B0: 03 03 10 01 00 49 5A 50  04 01 0C 80 23 24 0D 80  .....IZP....#$..
00C0: 05 80 01 80 25 02 00 10  01 80 00 EF 00 13 00 00  ....%...........
00D0: 08 80 0B 00 00 07 02 00  00 00 03 02 10 00 00 03  ................
00E0: 03 10 02 00 49 5A 50 04  01 0E 80 23 01 FF 00 02  ....IZP....#....
00F0: 00 10 05 80 00 FF 00 03  03 00 05 80 01 FF 00 02  ................
0100: 0F 80 02 00 03 12 01 49  5A 50 04 01 10 80 23 01  .......IZP....#.
0110: 8C 01 02 01 00 02 00 01  79 01 02 01 00 02 00 03  ........y.......
0120: 79 01 13 00 00 08 80 0B  00 00 03 04 00 01 00 07  y...............
0130: 04 00 00 00 02 0F 80 04  00 03 44 01 13 00 00 11  ..........D.....
0140: 80 0B 00 00 07 01 00 00  00 03 02 10 00 00 03 03  ................
0150: 10 01 00 2B 5A 50 04 01  12 80 23 02 0F 80 01 00  ...+ZP....#.....
0160: 03 6E 01 49 5A 50 04 01  13 80 23 01 79 01 02 05  .n.IZP....#.y...
0170: 80 03 00 00 79 01 01 12  01 02 01 80 03 00 00 8C  ....y...........
0180: 01 02 01 00 0F 80 05 8C  01 01 AB 00 03 02 10 02  ................
0190: 00 03 03 10 01 00 49 5A  50 04 01 14 80 23 02 01  ......IZP....#..
01A0: 00 02 00 00 B6 01 2B 5A  50 04 01 15 80 23 03 01  ......+ZP....#..
01B0: 10 16 80 01 0B 02 02 0F  80 02 00 03 CE 01 49 5A  ..............IZ
01C0: 50 04 01 17 80 23 03 01  10 18 80 01 0B 02 02 0F  P....#..........
01D0: 80 01 00 03 E6 01 49 5A  50 04 01 19 80 23 03 01  ......IZP....#..
01E0: 10 05 80 01 0B 02 02 01  00 02 00 03 FE 01 49 5A  ..............IZ
01F0: 50 04 01 19 80 23 03 01  10 05 80 01 0B 02 49 5A  P....#........IZ
0200: 50 04 01 17 80 23 03 01  10 18 80 01 35 02 02 00  P....#......5...
0210: 10 05 80 00 35 02 43 00  43 01 2B 5A 50 04 01 1A  ....5.C.C.+ZP...
0220: 80 23 03 02 10 1B 80 2B  5A 50 04 01 1C 80 23 01  .#.....+ZP....#.
0230: 5E 00 01 35 02 20 00 21  00                       ^..5. .!.       
```

#### Opcodes

```
  0: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0055 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0056 [0x2B] Qiqirn Dealer (ID: 17059930/0x0104505A) [7606*]:
    → "Clink clink! Clink clink! Make heart pound! Okay, okay! It game, then! Can play now, yes?"
  3: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x005E [0x24] CREATE_DIALOG(message_id=7607*, default_option=1*, option_flags=0*)
    → "Throwing dice around? [Yes, let's gooo!/What yooo mean?]"
  5: 0x0065 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0066 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x020E
  7: 0x006E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x0070 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0072 [0x13] ExtData[1]->WorkLocal[0] = rand() % 999*
 10: 0x0077 [0x0B] ExtData[1]->WorkLocal[0]++
 11: 0x007A [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[0]
 12: 0x007F [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 13: 0x0084 [0x49] Qiqirn Dealer (ID: 17059930/0x0104505A) (No speaker name) [7613*]:
 14: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x008C [0x13] ExtData[1]->WorkLocal[0] = rand() % 998*
 16: 0x0091 [0x0B] ExtData[1]->WorkLocal[0]++
 17: 0x0094 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
 18: 0x0099 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 19: 0x009E [0x2B] Qiqirn Dealer (ID: 17059930/0x0104505A) [7610*]:
    → "Throwing dice around and round now.t Here go for Titiroon turn... It a $0!"
 20: 0x00A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x00A6 [0x03] ExtData[1]->WorkLocal[3] = 0*
 22: 0x00AB [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
 23: 0x00B0 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[1]
 24: 0x00B5 [0x49] Qiqirn Dealer (ID: 17059930/0x0104505A) (No speaker name) [7617*]:
 25: 0x00BC [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x00BD [0x24] CREATE_DIALOG(message_id=7614*, default_option=1*, option_flags=0*)
    → "Roll the dice again? [Yes, please./I'll stop here!]"
 27: 0x00C4 [0x25] WAIT_DIALOG_SELECT()
 28: 0x00C5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00EF
 29: 0x00CD [0x13] ExtData[1]->WorkLocal[0] = rand() % 999*
 30: 0x00D2 [0x0B] ExtData[1]->WorkLocal[0]++
 31: 0x00D5 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[0]
 32: 0x00DA [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 33: 0x00DF [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[2]
 34: 0x00E4 [0x49] Qiqirn Dealer (ID: 17059930/0x0104505A) (No speaker name) [7615*]:
 35: 0x00EB [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x00EC [0x01] GOTO 0x00FF
 37: 0x00EF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00FF
 38: 0x00F7 [0x03] ExtData[1]->WorkLocal[3] = 1*
 39: 0x00FC [0x01] GOTO 0x00FF

SUBROUTINE_00FF:
 40: 0x00FF [0x02] IF !(1000* >= ExtData[1]->WorkLocal[2]) GOTO 0x0112
 41: 0x0107 [0x49] Qiqirn Dealer (ID: 17059930/0x0104505A) (No speaker name) [7616*]:
 42: 0x010E [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x010F [0x01] GOTO 0x018C

SUBROUTINE_0112:
 44: 0x0112 [0x02] IF !(ExtData[1]->WorkLocal[1] == ExtData[1]->WorkLocal[2]) GOTO 0x0179
 45: 0x011A [0x02] IF !(ExtData[1]->WorkLocal[1] >= ExtData[1]->WorkLocal[2]) GOTO 0x0179
 46: 0x0122 [0x13] ExtData[1]->WorkLocal[0] = rand() % 999*
 47: 0x0127 [0x0B] ExtData[1]->WorkLocal[0]++
 48: 0x012A [0x03] ExtData[1]->WorkLocal[4] = ExtData[1]->WorkLocal[1]
 49: 0x012F [0x07] ExtData[1]->WorkLocal[4] += ExtData[1]->WorkLocal[0]
 50: 0x0134 [0x02] IF !(1000* >= ExtData[1]->WorkLocal[4]) GOTO 0x0144
 51: 0x013C [0x13] ExtData[1]->WorkLocal[0] = rand() % 499*
 52: 0x0141 [0x0B] ExtData[1]->WorkLocal[0]++
 53: 0x0144 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[0]
 54: 0x0149 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 55: 0x014E [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[1]
 56: 0x0153 [0x2B] Qiqirn Dealer (ID: 17059930/0x0104505A) [7611*]:
    → "Okay, one more time! ...$0! Ohhh, that make $1, yes?"
 57: 0x015A [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x015B [0x02] IF !(1000* >= ExtData[1]->WorkLocal[1]) GOTO 0x016E
 59: 0x0163 [0x49] Qiqirn Dealer (ID: 17059930/0x0104505A) (No speaker name) [7612*]:
 60: 0x016A [0x23] WAIT_FOR_DIALOG_INTERACTION
 61: 0x016B [0x01] GOTO 0x0179
 62: 0x016E [0x02] IF !(1* == ExtData[1]->WorkLocal[3]) GOTO 0x0179
 63: 0x0176 [0x01] GOTO 0x0112

SUBROUTINE_0179:
 64: 0x0179 [0x02] IF !(0* == ExtData[1]->WorkLocal[3]) GOTO 0x018C
 65: 0x0181 [0x02] IF !(ExtData[1]->WorkLocal[1] > 1000*) GOTO 0x018C
 66: 0x0189 [0x01] GOTO 0x00AB

SUBROUTINE_018C:
 67: 0x018C [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
 68: 0x0191 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[1]
 69: 0x0196 [0x49] Qiqirn Dealer (ID: 17059930/0x0104505A) (No speaker name) [7618*]:
 70: 0x019D [0x23] WAIT_FOR_DIALOG_INTERACTION
 71: 0x019E [0x02] IF !(ExtData[1]->WorkLocal[1] == ExtData[1]->WorkLocal[2]) GOTO 0x01B6
 72: 0x01A6 [0x2B] Qiqirn Dealer (ID: 17059930/0x0104505A) [7621*]:
    → "Ohhh, have same luck! It tie! Will retooorn clink clink back to yooo."
 73: 0x01AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 74: 0x01AE [0x03] Work_Zone[1] = 3*
 75: 0x01B3 [0x01] GOTO 0x020B
 76: 0x01B6 [0x02] IF !(1000* >= ExtData[1]->WorkLocal[2]) GOTO 0x01CE
 77: 0x01BE [0x49] Qiqirn Dealer (ID: 17059930/0x0104505A) (No speaker name) [7620*]:
 78: 0x01C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 79: 0x01C6 [0x03] Work_Zone[1] = 2*
 80: 0x01CB [0x01] GOTO 0x020B
 81: 0x01CE [0x02] IF !(1000* >= ExtData[1]->WorkLocal[1]) GOTO 0x01E6
 82: 0x01D6 [0x49] Qiqirn Dealer (ID: 17059930/0x0104505A) (No speaker name) [7619*]:
 83: 0x01DD [0x23] WAIT_FOR_DIALOG_INTERACTION
 84: 0x01DE [0x03] Work_Zone[1] = 1*
 85: 0x01E3 [0x01] GOTO 0x020B
 86: 0x01E6 [0x02] IF !(ExtData[1]->WorkLocal[1] >= ExtData[1]->WorkLocal[2]) GOTO 0x01FE
 87: 0x01EE [0x49] Qiqirn Dealer (ID: 17059930/0x0104505A) (No speaker name) [7619*]:
 88: 0x01F5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 89: 0x01F6 [0x03] Work_Zone[1] = 1*
 90: 0x01FB [0x01] GOTO 0x020B
 91: 0x01FE [0x49] Qiqirn Dealer (ID: 17059930/0x0104505A) (No speaker name) [7620*]:
 92: 0x0205 [0x23] WAIT_FOR_DIALOG_INTERACTION
 93: 0x0206 [0x03] Work_Zone[1] = 2*

SUBROUTINE_020B:
 94: 0x020B [0x01] GOTO 0x0235
 95: 0x020E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0235
 96: 0x0216 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 97: 0x0218 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 98: 0x021A [0x2B] Qiqirn Dealer (ID: 17059930/0x0104505A) [7608*]:
    → "Throwing dice around! Yooo throw dice around all yooo want! Want get close to 1,000, okay? But if go over 1,000, then lose and so sad!"
 99: 0x0221 [0x23] WAIT_FOR_DIALOG_INTERACTION
100: 0x0222 [0x03] Work_Zone[2] = 2187*
101: 0x0227 [0x2B] Qiqirn Dealer (ID: 17059930/0x0104505A) [7609*]:
    → "If yooo win, get $0. If lose, clink clink gone! Happy, but kind of sad for yooo?"
102: 0x022E [0x23] WAIT_FOR_DIALOG_INTERACTION
103: 0x022F [0x01] GOTO 0x005E

SUBROUTINE_0235:
104: 0x0235 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
105: 0x0237 [0x21] END_EVENT
106: 0x0238 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0232 [0x01] GOTO 0x0235
```
