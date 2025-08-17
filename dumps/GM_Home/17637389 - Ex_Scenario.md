# 17637389 - Ex_Scenario

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 732 bytes         |
| Total Events     | 2                 |
| References Count | 32                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [30](#event-30)       | 0x0001       |    578 |            116 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1BE4      |        7140 |
|       1 | 0x0000      |           0 |
|       2 | 0x40000000  |  1073741824 |
|       3 | 0x0001      |           1 |
|       4 | 0x0002      |           2 |
|       5 | 0x0003      |           3 |
|       6 | 0x1BDA      |        7130 |
|       7 | 0x0004      |           4 |
|       8 | 0x0005      |           5 |
|       9 | 0x0006      |           6 |
|      10 | 0x0007      |           7 |
|      11 | 0x0008      |           8 |
|      12 | 0x0009      |           9 |
|      13 | 0x1BE5      |        7141 |
|      14 | 0x000A      |          10 |
|      15 | 0x000B      |          11 |
|      16 | 0x000C      |          12 |
|      17 | 0x000D      |          13 |
|      18 | 0x000E      |          14 |
|      19 | 0x000F      |          15 |
|      20 | 0x0010      |          16 |
|      21 | 0x0011      |          17 |
|      22 | 0x0012      |          18 |
|      23 | 0x0013      |          19 |
|      24 | 0x1BF5      |        7157 |
|      25 | 0x1BFA      |        7162 |
|      26 | 0x0020      |          32 |
|      27 | 0x0021      |          33 |
|      28 | 0x0022      |          34 |
|      29 | 0x0023      |          35 |
|      30 | 0x001E      |          30 |
|      31 | 0x001F      |          31 |

## String References

- **7130**: Zilarrrt! [Never mind.../Start up the airship to Kazham!/I've been t'Norg, mommy!/I've met Gilgamesh, daddy!/I got the key from that cat-woman!/I m'et Gravi'ton!/I've gathered all the fragments!/I beat that Altepa Boss, I did!/I met with those dawnmaidens!!/Tu'Lia is ready to go!]
- **7140**: Zilarrrt! [So what.../\`the end of the Delkfutt battle./\`the Stellar Nexus battle!/\`LIMBO!]
- **7141**: Zilarrrt! [Whatever.../Heard abot Ro'Maeve./Saw that door in the Hall of the Gods./Talked to that Mithra./Got the Hall Key./Spoke to the gatekeeper./Tu'Lia!/Crystal Warriors eliminated./To Ru'Avitau!/Celestial Nexus./Awakening.]
- **7157**: How low can you go? [No limbo for me./Dynamis Event./DEBUG ON!/DEBUG OFF!]
- **7162**: Dynamis Event Menu! [I'm not hungry./Start me from the top./4 nations conquered!/Beaucedine busted!/New Dynamis defeated!]

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

### Event 30

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 578 bytes |
| Instructions | 116       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 19   $......%.......
0010: 00 03 01 10 02 80 01 43  00 02 00 10 03 80 00 27  .......C.......'
0020: 00 1A 45 00 01 43 00 02  00 10 04 80 00 35 00 1A  ..E..C.......5..
0030: EE 00 01 43 00 02 00 10  05 80 00 43 00 1A A7 01  ...C.......C....
0040: 01 43 00 21 00 24 06 80  01 80 01 80 25 02 00 10  .C.!.$......%...
0050: 01 80 00 5D 00 03 01 10  02 80 01 ED 00 02 00 10  ...]............
0060: 03 80 00 6D 00 03 01 10  03 80 01 ED 00 02 00 10  ...m............
0070: 04 80 00 7D 00 03 01 10  04 80 01 ED 00 02 00 10  ...}............
0080: 05 80 00 8D 00 03 01 10  05 80 01 ED 00 02 00 10  ................
0090: 07 80 00 9D 00 03 01 10  07 80 01 ED 00 02 00 10  ................
00A0: 08 80 00 AD 00 03 01 10  08 80 01 ED 00 02 00 10  ................
00B0: 09 80 00 BD 00 03 01 10  09 80 01 ED 00 02 00 10  ................
00C0: 0A 80 00 CD 00 03 01 10  0A 80 01 ED 00 02 00 10  ................
00D0: 0B 80 00 DD 00 03 01 10  0B 80 01 ED 00 02 00 10  ................
00E0: 0C 80 00 ED 00 03 01 10  0C 80 01 ED 00 1B 24 0D  ..............$.
00F0: 80 01 80 01 80 25 02 00  10 01 80 00 06 01 03 01  .....%..........
0100: 10 02 80 01 A6 01 02 00  10 03 80 00 16 01 03 01  ................
0110: 10 0E 80 01 A6 01 02 00  10 04 80 00 26 01 03 01  ............&...
0120: 10 0F 80 01 A6 01 02 00  10 05 80 00 36 01 03 01  ............6...
0130: 10 10 80 01 A6 01 02 00  10 07 80 00 46 01 03 01  ............F...
0140: 10 11 80 01 A6 01 02 00  10 08 80 00 56 01 03 01  ............V...
0150: 10 12 80 01 A6 01 02 00  10 09 80 00 66 01 03 01  ............f...
0160: 10 13 80 01 A6 01 02 00  10 0A 80 00 76 01 03 01  ............v...
0170: 10 14 80 01 A6 01 02 00  10 0B 80 00 86 01 03 01  ................
0180: 10 15 80 01 A6 01 02 00  10 0C 80 00 96 01 03 01  ................
0190: 10 16 80 01 A6 01 02 00  10 0E 80 00 A6 01 03 01  ................
01A0: 10 17 80 01 A6 01 1B 24  18 80 01 80 01 80 25 02  .......$......%.
01B0: 00 10 01 80 00 BF 01 03  01 10 02 80 01 42 02 02  .............B..
01C0: 00 10 03 80 00 22 02 24  19 80 01 80 01 80 25 02  .....".$......%.
01D0: 00 10 01 80 00 DF 01 03  01 10 02 80 01 1F 02 02  ................
01E0: 00 10 03 80 00 EF 01 03  01 10 1A 80 01 1F 02 02  ................
01F0: 00 10 04 80 00 FF 01 03  01 10 1B 80 01 1F 02 02  ................
0200: 00 10 05 80 00 0F 02 03  01 10 1C 80 01 1F 02 02  ................
0210: 00 10 07 80 00 1F 02 03  01 10 1D 80 01 1F 02 01  ................
0220: 42 02 02 00 10 04 80 00  32 02 03 01 10 1E 80 01  B.......2.......
0230: 42 02 02 00 10 05 80 00  42 02 03 01 10 1F 80 01  B.......B.......
0240: 42 02 1B                                          B..             
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7140*, default_option=0*, option_flags=0*)
    → "Zilarrrt! [So what.../`the end of the Delkfutt battle./`the Stellar Nexus battle!/`LIMBO!]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0019
  3: 0x0011 [0x03] Work_Zone[1] = 1073741824*
  4: 0x0016 [0x01] GOTO 0x0043
  5: 0x0019 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0027
  6: 0x0021 [0x1A] CALL_SUBROUTINE(address=0x0045)
  7: 0x0024 [0x01] GOTO 0x0043
  8: 0x0027 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0035
  9: 0x002F [0x1A] CALL_SUBROUTINE(address=0x00EE)
 10: 0x0032 [0x01] GOTO 0x0043
 11: 0x0035 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0043
 12: 0x003D [0x1A] CALL_SUBROUTINE(address=0x01A7)
 13: 0x0040 [0x01] GOTO 0x0043

SUBROUTINE_0043:
 14: 0x0043 [0x21] END_EVENT
 15: 0x0044 [0x00] END_REQSTACK()

SUBROUTINE_0045:
 16: 0x0045 [0x24] CREATE_DIALOG(message_id=7130*, default_option=0*, option_flags=0*)
    → "Zilarrrt! [Never mind.../Start up the airship to Kazham!/I've been t'Norg, mommy!/I've met Gilgamesh, daddy!/I got the key from that cat-woman!/I m'et Gravi'ton!/I've gathered all the fragments!/I beat that Altepa Boss, I did!/I met with those dawnmaidens!!/Tu'Lia is ready to go!]"
 17: 0x004C [0x25] WAIT_DIALOG_SELECT()
 18: 0x004D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x005D
 19: 0x0055 [0x03] Work_Zone[1] = 1073741824*
 20: 0x005A [0x01] GOTO 0x00ED
 21: 0x005D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x006D
 22: 0x0065 [0x03] Work_Zone[1] = 1*
 23: 0x006A [0x01] GOTO 0x00ED
 24: 0x006D [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x007D
 25: 0x0075 [0x03] Work_Zone[1] = 2*
 26: 0x007A [0x01] GOTO 0x00ED
 27: 0x007D [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x008D
 28: 0x0085 [0x03] Work_Zone[1] = 3*
 29: 0x008A [0x01] GOTO 0x00ED
 30: 0x008D [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x009D
 31: 0x0095 [0x03] Work_Zone[1] = 4*
 32: 0x009A [0x01] GOTO 0x00ED
 33: 0x009D [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x00AD
 34: 0x00A5 [0x03] Work_Zone[1] = 5*
 35: 0x00AA [0x01] GOTO 0x00ED
 36: 0x00AD [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x00BD
 37: 0x00B5 [0x03] Work_Zone[1] = 6*
 38: 0x00BA [0x01] GOTO 0x00ED
 39: 0x00BD [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x00CD
 40: 0x00C5 [0x03] Work_Zone[1] = 7*
 41: 0x00CA [0x01] GOTO 0x00ED
 42: 0x00CD [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x00DD
 43: 0x00D5 [0x03] Work_Zone[1] = 8*
 44: 0x00DA [0x01] GOTO 0x00ED
 45: 0x00DD [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x00ED
 46: 0x00E5 [0x03] Work_Zone[1] = 9*
 47: 0x00EA [0x01] GOTO 0x00ED

SUBROUTINE_00ED:
 48: 0x00ED [0x1B] RETURN

SUBROUTINE_00EE:
 49: 0x00EE [0x24] CREATE_DIALOG(message_id=7141*, default_option=0*, option_flags=0*)
    → "Zilarrrt! [Whatever.../Heard abot Ro'Maeve./Saw that door in the Hall of the Gods./Talked to that Mithra./Got the Hall Key./Spoke to the gatekeeper./Tu'Lia!/Crystal Warriors eliminated./To Ru'Avitau!/Celestial Nexus./Awakening.]"
 50: 0x00F5 [0x25] WAIT_DIALOG_SELECT()
 51: 0x00F6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0106
 52: 0x00FE [0x03] Work_Zone[1] = 1073741824*
 53: 0x0103 [0x01] GOTO 0x01A6
 54: 0x0106 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0116
 55: 0x010E [0x03] Work_Zone[1] = 10*
 56: 0x0113 [0x01] GOTO 0x01A6
 57: 0x0116 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0126
 58: 0x011E [0x03] Work_Zone[1] = 11*
 59: 0x0123 [0x01] GOTO 0x01A6
 60: 0x0126 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0136
 61: 0x012E [0x03] Work_Zone[1] = 12*
 62: 0x0133 [0x01] GOTO 0x01A6
 63: 0x0136 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0146
 64: 0x013E [0x03] Work_Zone[1] = 13*
 65: 0x0143 [0x01] GOTO 0x01A6
 66: 0x0146 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0156
 67: 0x014E [0x03] Work_Zone[1] = 14*
 68: 0x0153 [0x01] GOTO 0x01A6
 69: 0x0156 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0166
 70: 0x015E [0x03] Work_Zone[1] = 15*
 71: 0x0163 [0x01] GOTO 0x01A6
 72: 0x0166 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0176
 73: 0x016E [0x03] Work_Zone[1] = 16*
 74: 0x0173 [0x01] GOTO 0x01A6
 75: 0x0176 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x0186
 76: 0x017E [0x03] Work_Zone[1] = 17*
 77: 0x0183 [0x01] GOTO 0x01A6
 78: 0x0186 [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x0196
 79: 0x018E [0x03] Work_Zone[1] = 18*
 80: 0x0193 [0x01] GOTO 0x01A6
 81: 0x0196 [0x02] IF !(Work_Zone[0] == 10*) GOTO 0x01A6
 82: 0x019E [0x03] Work_Zone[1] = 19*
 83: 0x01A3 [0x01] GOTO 0x01A6

SUBROUTINE_01A6:
 84: 0x01A6 [0x1B] RETURN

SUBROUTINE_01A7:
 85: 0x01A7 [0x24] CREATE_DIALOG(message_id=7157*, default_option=0*, option_flags=0*)
    → "How low can you go? [No limbo for me./Dynamis Event./DEBUG ON!/DEBUG OFF!]"
 86: 0x01AE [0x25] WAIT_DIALOG_SELECT()
 87: 0x01AF [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01BF
 88: 0x01B7 [0x03] Work_Zone[1] = 1073741824*
 89: 0x01BC [0x01] GOTO 0x0242
 90: 0x01BF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0222
 91: 0x01C7 [0x24] CREATE_DIALOG(message_id=7162*, default_option=0*, option_flags=0*)
    → "Dynamis Event Menu! [I'm not hungry./Start me from the top./4 nations conquered!/Beaucedine busted!/New Dynamis defeated!]"
 92: 0x01CE [0x25] WAIT_DIALOG_SELECT()
 93: 0x01CF [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01DF
 94: 0x01D7 [0x03] Work_Zone[1] = 1073741824*
 95: 0x01DC [0x01] GOTO 0x021F
 96: 0x01DF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01EF
 97: 0x01E7 [0x03] Work_Zone[1] = 32*
 98: 0x01EC [0x01] GOTO 0x021F
 99: 0x01EF [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x01FF
100: 0x01F7 [0x03] Work_Zone[1] = 33*
101: 0x01FC [0x01] GOTO 0x021F
102: 0x01FF [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x020F
103: 0x0207 [0x03] Work_Zone[1] = 34*
104: 0x020C [0x01] GOTO 0x021F
105: 0x020F [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x021F
106: 0x0217 [0x03] Work_Zone[1] = 35*
107: 0x021C [0x01] GOTO 0x021F

SUBROUTINE_021F:
108: 0x021F [0x01] GOTO 0x0242
109: 0x0222 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0232
110: 0x022A [0x03] Work_Zone[1] = 30*
111: 0x022F [0x01] GOTO 0x0242
112: 0x0232 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0242
113: 0x023A [0x03] Work_Zone[1] = 31*
114: 0x023F [0x01] GOTO 0x0242

SUBROUTINE_0242:
115: 0x0242 [0x1B] RETURN
```
