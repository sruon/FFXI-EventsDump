# 17637623 - Unity Master

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 740 bytes         |
| Total Events     | 2                 |
| References Count | 20                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [184](#event-184)     | 0x0001       |    632 |            138 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x23CE      |        9166 |
|       1 | 0x0000      |           0 |
|       2 | 0x23CF      |        9167 |
|       3 | 0x000A      |          10 |
|       4 | 0x000B      |          11 |
|       5 | 0x0001      |           1 |
|       6 | 0x0003      |           3 |
|       7 | 0x0004      |           4 |
|       8 | 0x0009      |           9 |
|       9 | 0x23D0      |        9168 |
|      10 | 0x000C      |          12 |
|      11 | 0x23D1      |        9169 |
|      12 | 0x0014      |          20 |
|      13 | 0x23D2      |        9170 |
|      14 | 0x001E      |          30 |
|      15 | 0x23D3      |        9171 |
|      16 | 0x0028      |          40 |
|      17 | 0x0002      |           2 |
|      18 | 0x23D5      |        9173 |
|      19 | 0x0008      |           8 |

## String References

- **9166**: Check message. (Current: [No Unity/Pieuje/Ayame/Invincible Shield/Apururu/Maat/Aldo/Jakoh Wahcondalo/Naja Salaheem/Flaviria/Yoran-Oran/Sylvie]j [Designate message ID (current Unity only)/Random. (Last mesID: $5/$6/$7)/Change Unity./Nothing.]
- **9167**: Display designated message (11-20) [1: Monday rank: First.": Monday rank: 2nd to 5th.": Monday Rank: 6th or worse./4: Monday Rank: Last./5: Tues.-Sat. Rank: First./6: Tues.-Sat. Rank: 2nd to 5th./7: Tues.-Sat. Rank: 6th or worse/8: Tues.-Sat. Rank: Last./9: Sunday rank: First./10: Sunday rank: 2nd to 5th./Next./Main menu.]
- **9168**: Display designated message (11-20). [Back./11: Sunday rank: 6th or worse./12: Sunday rank: Last./13: (Reserve)./14: (Reserve)./15: (Reserve)./16: GMbit New Years'/17: GMbit Valentione/18: GMbit Doll Festival/19: GMbit Egg Hunt"0: GMbit Feast of Swords/Next./Main Menu.]
- **9169**: Display designated message (21-30). [Back."1: GMbit Adv. Appreciation."2: GMbit Celestial Nights."3: GMbit Mumor."4: GMbit Blazing Buffaloes."5: GMbit Halloween."6: GMbit 11/11 Anniversary."7: GMbit Celestial Nights."8: GMbit Double Accolades."9: XI Anniversary."0: XI Anniversary Lottery./Next./Main Menu.]
- **9170**: Display designated message (31-40). [Back."1: Chatter 1"2: Chatter 2"3: Chatter 3"4: Chatter 4"5: Chatter 5"6: Chatter 6"7: Chatter 7"8: Chatter 8"9: Chatter 9/40: Chatter 10/Next./Main menu.]
- **9171**: Display designated message (41-50). [Back./41: (Reserve)./42: (Reserve)./43: (Reserve)./44: Escha RNM No. Vanquished./45: Escha RNM trash spawn./46: Escha RNM spawn prediction./47: Escha RNM spawn./48: Escha RNM HP info./49: Escha RNM despawn (vanquished)./50: Escha RNM despawn (failed)./Main Menu.]
- **9173**: Change Unity. Current: [No Unity/Pieuje/Ayame/Invincible Shield/Apururu/Maat/Aldo/Jakoh Wahcondalo/Naja Salaheem/Flaviria/Yoran-Oran/Sylvie] [Back./Pieuje./Ayame./Invincible Shield./Apururu./Maat./Aldo./Jakoh Wahcondalo./Naja Salaheem./Flaviria./Yoran-Oran./Sylvie.]

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

### Event 184

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 632 bytes |
| Instructions | 38        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    06 01 00 06 02 00 03  00 00 02 10 06 01 10 03   ...............
0010: 02 10 00 00 24 00 80 01  00 01 80 25 02 00 10 01  ....$......%....
0020: 80 00 F0 01 03 01 00 00  10 06 02 00 06 04 00 24  ...............$
0030: 02 80 02 00 01 80 25 02  00 10 03 80 00 48 00 06  ......%......H..
0040: 02 00 01 7E 00 01 7E 00  02 00 10 04 80 00 56 00  ...~..~.......V.
0050: 01 0C 00 01 7E 00 03 04  00 05 80 07 04 00 00 10  ....~...........
0060: 40 01 80 06 80 01 10 05  80 40 07 80 08 80 01 10  @........@......
0070: 04 00 03 02 00 00 10 43  00 43 01 01 2F 00 24 09  .......C.C../.$.
0080: 80 02 00 01 80 25 02 00  10 01 80 00 97 00 06 02  .....%..........
0090: 00 01 2F 00 01 DE 00 02  00 10 04 80 00 A8 00 06  ../.............
00A0: 02 00 01 DE 00 01 DE 00  02 00 10 0A 80 00 B6 00  ................
00B0: 01 0C 00 01 DE 00 03 04  00 03 80 07 04 00 00 10  ................
00C0: 40 01 80 06 80 01 10 05  80 40 07 80 08 80 01 10  @........@......
00D0: 04 00 03 02 00 00 10 43  00 43 01 01 7E 00 24 0B  .......C.C..~.$.
00E0: 80 02 00 01 80 25 02 00  10 01 80 00 F7 00 06 02  .....%..........
00F0: 00 01 7E 00 01 3E 01 02  00 10 04 80 00 08 01 06  ..~..>..........
0100: 02 00 01 3E 01 01 3E 01  02 00 10 0A 80 00 16 01  ...>..>.........
0110: 01 0C 00 01 3E 01 03 04  00 0C 80 07 04 00 00 10  ....>...........
0120: 40 01 80 06 80 01 10 05  80 40 07 80 08 80 01 10  @........@......
0130: 04 00 03 02 00 00 10 43  00 43 01 01 DE 00 24 0D  .......C.C....$.
0140: 80 02 00 01 80 25 02 00  10 01 80 00 57 01 06 02  .....%......W...
0150: 00 01 DE 00 01 9E 01 02  00 10 04 80 00 68 01 06  .............h..
0160: 02 00 01 9E 01 01 9E 01  02 00 10 0A 80 00 76 01  ..............v.
0170: 01 0C 00 01 9E 01 03 04  00 0E 80 07 04 00 00 10  ................
0180: 40 01 80 06 80 01 10 05  80 40 07 80 08 80 01 10  @........@......
0190: 04 00 03 02 00 00 10 43  00 43 01 01 3E 01 24 0F  .......C.C..>.$.
01A0: 80 02 00 01 80 25 02 00  10 01 80 00 B7 01 06 02  .....%..........
01B0: 00 01 3E 01 01 ED 01 02  00 10 04 80 00 C5 01 01  ..>.............
01C0: 0C 00 01 ED 01 03 04 00  10 80 07 04 00 00 10 40  ...............@
01D0: 01 80 06 80 01 10 05 80  40 07 80 08 80 01 10 04  ........@.......
01E0: 00 03 02 00 00 10 43 00  43 01 01 9E 01 01 77 02  ......C.C.....w.
01F0: 02 00 10 05 80 00 10 02  03 01 00 00 10 40 01 80  .............@..
0200: 06 80 01 10 11 80 43 00  43 01 01 0C 00 01 77 02  ......C.C.....w.
0210: 02 00 10 11 80 00 63 02  03 01 00 00 10 06 03 00  ......c.........
0220: 3C 03 00 00 00 05 80 03  02 10 00 00 24 12 80 01  <...........$...
0230: 80 03 00 25 02 00 10 01  80 00 42 02 01 0C 00 01  ...%......B.....
0240: 60 02 40 01 80 06 80 01  10 06 80 40 07 80 13 80  `.@........@....
0250: 01 10 00 10 03 00 00 00  10 43 00 43 01 01 0C 00  .........C.C....
0260: 01 77 02 02 00 10 06 80  00 77 02 40 01 80 06 80  .w.......w.@....
0270: 01 10 01 80 01 77 02 21  00                       .....w.!.       
```

#### Opcodes

```
  0: 0x0001 [0x06] ExtData[1]->WorkLocal[1] = 0
  1: 0x0004 [0x06] ExtData[1]->WorkLocal[2] = 0
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  3: 0x000C [0x06] Work_Zone[1] = 0
  4: 0x000F [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
  5: 0x0014 [0x24] CREATE_DIALOG(message_id=9166*, default_option=ExtData[1]->WorkLocal[1], option_flags=0*)
    → "Check message. (Current: [No Unity/Pieuje/Ayame/Invincible Shield/Apururu/Maat/Aldo/Jakoh Wahcondalo/Naja Salaheem/Flaviria/Yoran-Oran/Sylvie]j [Designate message ID (current Unity only)/Random. (Last mesID: $5/$6/$7)/Change Unity./Nothing.]"
  6: 0x001B [0x25] WAIT_DIALOG_SELECT()
  7: 0x001C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01F0
  8: 0x0024 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[0]
  9: 0x0029 [0x06] ExtData[1]->WorkLocal[2] = 0
 10: 0x002C [0x06] ExtData[1]->WorkLocal[4] = 0
 11: 0x002F [0x24] CREATE_DIALOG(message_id=9167*, default_option=ExtData[1]->WorkLocal[2], option_flags=0*)
    → "Display designated message (11-20) [1: Monday rank: First.": Monday rank: 2nd to 5th.": Monday Rank: 6th or worse./4: Monday Rank: Last./5: Tues.-Sat. Rank: First./6: Tues.-Sat. Rank: 2nd to 5th./7: Tues.-Sat. Rank: 6th or worse/8: Tues.-Sat. Rank: Last./9: Sunday rank: First./10: Sunday rank: 2nd to 5th./Next./Main menu.]"
 12: 0x0036 [0x25] WAIT_DIALOG_SELECT()
 13: 0x0037 [0x02] IF !(Work_Zone[0] == 10*) GOTO 0x0048
 14: 0x003F [0x06] ExtData[1]->WorkLocal[2] = 0
 15: 0x0042 [0x01] GOTO 0x007E

SUBROUTINE_007E:
 16: 0x007E [0x24] CREATE_DIALOG(message_id=9168*, default_option=ExtData[1]->WorkLocal[2], option_flags=0*)
    → "Display designated message (11-20). [Back./11: Sunday rank: 6th or worse./12: Sunday rank: Last./13: (Reserve)./14: (Reserve)./15: (Reserve)./16: GMbit New Years'/17: GMbit Valentione/18: GMbit Doll Festival/19: GMbit Egg Hunt"0: GMbit Feast of Swords/Next./Main Menu.]"
 17: 0x0085 [0x25] WAIT_DIALOG_SELECT()
 18: 0x0086 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0097
 19: 0x008E [0x06] ExtData[1]->WorkLocal[2] = 0
 20: 0x0091 [0x01] GOTO 0x002F

SUBROUTINE_00DE:
 21: 0x00DE [0x24] CREATE_DIALOG(message_id=9169*, default_option=ExtData[1]->WorkLocal[2], option_flags=0*)
    → "Display designated message (21-30). [Back."1: GMbit Adv. Appreciation."2: GMbit Celestial Nights."3: GMbit Mumor."4: GMbit Blazing Buffaloes."5: GMbit Halloween."6: GMbit 11/11 Anniversary."7: GMbit Celestial Nights."8: GMbit Double Accolades."9: XI Anniversary."0: XI Anniversary Lottery./Next./Main Menu.]"
 22: 0x00E5 [0x25] WAIT_DIALOG_SELECT()
 23: 0x00E6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F7
 24: 0x00EE [0x06] ExtData[1]->WorkLocal[2] = 0
 25: 0x00F1 [0x01] GOTO 0x007E

SUBROUTINE_013E:
 26: 0x013E [0x24] CREATE_DIALOG(message_id=9170*, default_option=ExtData[1]->WorkLocal[2], option_flags=0*)
    → "Display designated message (31-40). [Back."1: Chatter 1"2: Chatter 2"3: Chatter 3"4: Chatter 4"5: Chatter 5"6: Chatter 6"7: Chatter 7"8: Chatter 8"9: Chatter 9/40: Chatter 10/Next./Main menu.]"
 27: 0x0145 [0x25] WAIT_DIALOG_SELECT()
 28: 0x0146 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0157
 29: 0x014E [0x06] ExtData[1]->WorkLocal[2] = 0
 30: 0x0151 [0x01] GOTO 0x00DE

SUBROUTINE_019E:
 31: 0x019E [0x24] CREATE_DIALOG(message_id=9171*, default_option=ExtData[1]->WorkLocal[2], option_flags=0*)
    → "Display designated message (41-50). [Back./41: (Reserve)./42: (Reserve)./43: (Reserve)./44: Escha RNM No. Vanquished./45: Escha RNM trash spawn./46: Escha RNM spawn prediction./47: Escha RNM spawn./48: Escha RNM HP info./49: Escha RNM despawn (vanquished)./50: Escha RNM despawn (failed)./Main Menu.]"
 32: 0x01A5 [0x25] WAIT_DIALOG_SELECT()
 33: 0x01A6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01B7
 34: 0x01AE [0x06] ExtData[1]->WorkLocal[2] = 0
 35: 0x01B1 [0x01] GOTO 0x013E

SUBROUTINE_0277:
 36: 0x0277 [0x21] END_EVENT
 37: 0x0278 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0045 [0x01] GOTO 0x007E
     0x0053 [0x01] GOTO 0x007E
# Dead code (unreachable instructions):
     0x0094 [0x01] GOTO 0x00DE
     0x00A5 [0x01] GOTO 0x00DE
     0x00B3 [0x01] GOTO 0x00DE
# Dead code (unreachable instructions):
     0x00F4 [0x01] GOTO 0x013E
     0x0105 [0x01] GOTO 0x013E
     0x0113 [0x01] GOTO 0x013E
# Dead code (unreachable instructions):
     0x0154 [0x01] GOTO 0x019E
     0x0165 [0x01] GOTO 0x019E
     0x0173 [0x01] GOTO 0x019E
# Dead code (unreachable instructions):
     0x01B4 [0x01] GOTO 0x01ED
     0x01C2 [0x01] GOTO 0x01ED
     0x01ED [0x01] GOTO 0x0277
     0x020D [0x01] GOTO 0x0277
     0x023F [0x01] GOTO 0x0260
     0x0260 [0x01] GOTO 0x0277
```
