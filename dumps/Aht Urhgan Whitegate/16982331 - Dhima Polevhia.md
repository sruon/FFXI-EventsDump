# 16982331 - Dhima Polevhia

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 832 bytes                     |
| Total Events     | 9                             |
| References Count | 37                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [788](#event-788)     | 0x0001       |     15 |              7 |
| [789](#event-789)     | 0x0010       |      1 |              1 |
| [790](#event-790)     | 0x0011       |    144 |             37 |
| [795](#event-795)     | 0x00A1       |     20 |             10 |
| [796](#event-796)     | 0x00B5       |     11 |              5 |
| [791](#event-791)     | 0x00C0       |    404 |             92 |
| [792](#event-792)     | 0x0254       |     32 |              8 |
| [793](#event-793)     | 0x0274       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x175F      |        5983 |
|       1 | 0x1760      |        5984 |
|       2 | 0x0001      |           1 |
|       3 | 0x0312      |         786 |
|       4 | 0x0664      |        1636 |
|       5 | 0x06A3      |        1699 |
|       6 | 0x08F1      |        2289 |
|       7 | 0x088B      |        2187 |
|       8 | 0x1770      |        6000 |
|       9 | 0x1771      |        6001 |
|      10 | 0x0002      |           2 |
|      11 | 0x02F2      |         754 |
|      12 | 0x0335      |         821 |
|      13 | 0x0868      |        2152 |
|      14 | 0x088A      |        2186 |
|      15 | 0x0003      |           3 |
|      16 | 0x1772      |        6002 |
|      17 | 0x1773      |        6003 |
|      18 | 0x1774      |        6004 |
|      19 | 0x1775      |        6005 |
|      20 | 0x1776      |        6006 |
|      21 | 0x1779      |        6009 |
|      22 | 0x0000      |           0 |
|      23 | 0x38BB      |       14523 |
|      24 | 0x3A52      |       14930 |
|      25 | 0x3D46      |       15686 |
|      26 | 0x1768      |        5992 |
|      27 | 0x1769      |        5993 |
|      28 | 0x176A      |        5994 |
|      29 | 0x176B      |        5995 |
|      30 | 0x176D      |        5997 |
|      31 | 0x176E      |        5998 |
|      32 | 0x176C      |        5996 |
|      33 | 0x176F      |        5999 |
|      34 | 0x1777      |        6007 |
|      35 | 0x1778      |        6008 |
|      36 | 0x00C9      |         201 |

## String References

- **5983**: There's been a sudden incrrrease in the number of puppetmasters lately. There are way too many for my liking now.
- **5984**: That's why I'm picky about who I do business with. People say, "The customer is always right," don't they? But I say, the customer better be rrright, or I'm not sellin'!
- **5992**: What do you want me to make? [Nothing./#/$1/$2]
- **5995**: You're rrreally sure? [Yes, I'm sure!/Maybe not...]
- **6000**: How many times do I have to tell you? I need $4, $5, $6, and $7!
- **6001**: Oh yeah, and don't forget to throw in $8. Hop to it, now!
- **6002**: Oh yeah, and don't forget to throw in $9 $0%0 . Hop to it, now!
- **6003**: Excellent work.
- **6004**: Leave everything to me, now. Just wait until you see how beautiful and strong the final product will be!
- **6005**: I won't be able to finish it today, so you should find something else to keep you busy and leave me to work in peace.
- **6006**: What do you want? Patience is a virtue, you know.
- **6007**: Your order is ready!
- **6008**: Just let me know if you want anything else. You won't find products like this anywhere else on Urhguum, believe me.
- **6009**: Did you want anything else?

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

### Event 788

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 21 00   ........#...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=5983*)
    → "There's been a sudden incrrrease in the number of puppetmasters lately. There are way too many for my liking now."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=5984*)
    → "That's why I'm picky about who I do business with. People say, "The customer is always right," don't they? But I say, the customer better be rrright, or I'm not sellin'!"
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 789

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0010 [0x00] END_REQSTACK()
```

### Event 790

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0011    |
| Data Size    | 144 bytes |
| Instructions | 37        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    1E F0 FF FF 7F 02 05  10 02 80 80 42 00 03 06   ...........B...
0020: 10 03 80 03 07 10 04 80  03 08 10 05 80 03 09 10  ................
0030: 06 80 03 00 17 07 80 1D  08 80 23 1D 09 80 23 01  ..........#...#.
0040: 9F 00 02 05 10 0A 80 80  6E 00 03 06 10 0B 80 03  ........n.......
0050: 07 10 0C 80 03 08 10 0D  80 03 09 10 06 80 03 00  ................
0060: 17 0E 80 1D 08 80 23 1D  09 80 23 01 9F 00 02 05  ......#...#.....
0070: 10 0F 80 80 9F 00 03 06  10 0B 80 03 07 10 03 80  ................
0080: 03 08 10 0D 80 03 09 10  06 80 03 00 17 0E 80 03  ................
0090: 01 17 0A 80 1D 08 80 23  1D 10 80 23 01 9F 00 21  .......#...#...!
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0016 [0x02] IF !(Work_Zone[5] == 1*) GOTO 0x0042
  2: 0x001E [0x03] Work_Zone[6] = 786*
  3: 0x0023 [0x03] Work_Zone[7] = 1636*
  4: 0x0028 [0x03] Work_Zone[8] = 1699*
  5: 0x002D [0x03] Work_Zone[9] = 2289*
  6: 0x0032 [0x03] Work_Zone_1700[0] = 2187*
  7: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=6000*)
    → "How many times do I have to tell you? I need $4, $5, $6, and $7!"
  8: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=6001*)
    → "Oh yeah, and don't forget to throw in $8. Hop to it, now!"
 10: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x003F [0x01] GOTO 0x009F
 12: 0x0042 [0x02] IF !(Work_Zone[5] == 2*) GOTO 0x006E
 13: 0x004A [0x03] Work_Zone[6] = 754*
 14: 0x004F [0x03] Work_Zone[7] = 821*
 15: 0x0054 [0x03] Work_Zone[8] = 2152*
 16: 0x0059 [0x03] Work_Zone[9] = 2289*
 17: 0x005E [0x03] Work_Zone_1700[0] = 2186*
 18: 0x0063 [0x1D] PRINT_EVENT_MESSAGE(message_id=6000*)
    → "How many times do I have to tell you? I need $4, $5, $6, and $7!"
 19: 0x0066 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=6001*)
    → "Oh yeah, and don't forget to throw in $8. Hop to it, now!"
 21: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x006B [0x01] GOTO 0x009F
 23: 0x006E [0x02] IF !(Work_Zone[5] == 3*) GOTO 0x009F
 24: 0x0076 [0x03] Work_Zone[6] = 754*
 25: 0x007B [0x03] Work_Zone[7] = 786*
 26: 0x0080 [0x03] Work_Zone[8] = 2152*
 27: 0x0085 [0x03] Work_Zone[9] = 2289*
 28: 0x008A [0x03] Work_Zone_1700[0] = 2186*
 29: 0x008F [0x03] Work_Zone_1700[1] = 2*
 30: 0x0094 [0x1D] PRINT_EVENT_MESSAGE(message_id=6000*)
    → "How many times do I have to tell you? I need $4, $5, $6, and $7!"
 31: 0x0097 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0098 [0x1D] PRINT_EVENT_MESSAGE(message_id=6002*)
    → "Oh yeah, and don't forget to throw in $9 $0%0 . Hop to it, now!"
 33: 0x009B [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x009C [0x01] GOTO 0x009F

SUBROUTINE_009F:
 35: 0x009F [0x21] END_EVENT
 36: 0x00A0 [0x00] END_REQSTACK()
```

### Event 795

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A1   |
| Data Size    | 20 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    42 1E F0 FF FF 7F 1D  11 80 23 1D 12 80 23 1D   B........#...#.
00B0: 13 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x00A1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00A2 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00A7 [0x1D] PRINT_EVENT_MESSAGE(message_id=6003*)
    → "Excellent work."
  3: 0x00AA [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00AB [0x1D] PRINT_EVENT_MESSAGE(message_id=6004*)
    → "Leave everything to me, now. Just wait until you see how beautiful and strong the final product will be!"
  5: 0x00AE [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00AF [0x1D] PRINT_EVENT_MESSAGE(message_id=6005*)
    → "I won't be able to finish it today, so you should find something else to keep you busy and leave me to work in peace."
  7: 0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00B3 [0x21] END_EVENT
  9: 0x00B4 [0x00] END_REQSTACK()
```

### Event 796

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                1E F0 FF  FF 7F 1D 14 80 23 21 00       ........#!.
```

#### Opcodes

```
  0: 0x00B5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00BA [0x1D] PRINT_EVENT_MESSAGE(message_id=6006*)
    → "What do you want? Patience is a virtue, you know."
  2: 0x00BD [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00BE [0x21] END_EVENT
  4: 0x00BF [0x00] END_REQSTACK()
```

### Event 791

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00C0    |
| Data Size    | 404 bytes |
| Instructions | 89        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 03 00 00 03 10 1E F0 FF  FF 7F 1D 15 80 23 03 01  .............#..
00D0: 10 16 80 03 02 10 17 80  03 03 10 18 80 03 04 10  ................
00E0: 19 80 24 1A 80 16 80 00  00 25 02 00 10 16 80 00  ..$......%......
00F0: FD 00 2B 3B 21 03 01 1B  80 23 01 52 02 02 00 10  ..+;!....#.R....
0100: 02 80 00 6D 01 93 02 10  2B 3B 21 03 01 1C 80 23  ...m....+;!....#
0110: 93 16 80 24 1D 80 02 80  16 80 25 02 00 10 16 80  ...$......%.....
0120: 00 54 01 03 06 10 03 80  03 07 10 04 80 03 08 10  .T..............
0130: 05 80 03 09 10 06 80 03  00 17 07 80 2B 3B 21 03  ............+;!.
0140: 01 1E 80 23 2B 3B 21 03  01 1F 80 23 03 01 10 02  ...#+;!....#....
0150: 80 01 6A 01 02 00 10 02  80 00 6A 01 2B 3B 21 03  ..j.......j.+;!.
0160: 01 20 80 23 01 CE 00 01  6A 01 01 52 02 02 00 10  . .#....j..R....
0170: 0A 80 00 DD 01 93 03 10  2B 3B 21 03 01 1C 80 23  ........+;!....#
0180: 93 16 80 24 1D 80 02 80  16 80 25 02 00 10 16 80  ...$......%.....
0190: 00 C4 01 03 06 10 0B 80  03 07 10 0C 80 03 08 10  ................
01A0: 0D 80 03 09 10 06 80 03  00 17 0E 80 2B 3B 21 03  ............+;!.
01B0: 01 1E 80 23 2B 3B 21 03  01 1F 80 23 03 01 10 0A  ...#+;!....#....
01C0: 80 01 DA 01 02 00 10 02  80 00 DA 01 2B 3B 21 03  ............+;!.
01D0: 01 20 80 23 01 CE 00 01  DA 01 01 52 02 02 00 10  . .#.......R....
01E0: 0F 80 00 52 02 93 04 10  2B 3B 21 03 01 1C 80 23  ...R....+;!....#
01F0: 93 16 80 24 1D 80 02 80  16 80 25 02 00 10 16 80  ...$......%.....
0200: 00 39 02 03 06 10 0B 80  03 07 10 03 80 03 08 10  .9..............
0210: 0D 80 03 09 10 06 80 03  00 17 0E 80 03 01 17 0A  ................
0220: 80 2B 3B 21 03 01 1E 80  23 2B 3B 21 03 01 21 80  .+;!....#+;!..!.
0230: 23 03 01 10 0F 80 01 4F  02 02 00 10 02 80 00 4F  #......O.......O
0240: 02 2B 3B 21 03 01 20 80  23 01 CE 00 01 4F 02 01  .+;!.. .#....O..
0250: 52 02 21 00                                       R.!.            
```

#### Opcodes

```
  0: 0x00C0 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  1: 0x00C5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00CA [0x1D] PRINT_EVENT_MESSAGE(message_id=6009*)
    → "Did you want anything else?"
  3: 0x00CD [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00CE [0x03] Work_Zone[1] = 0*
  5: 0x00D3 [0x03] Work_Zone[2] = 14523*
  6: 0x00D8 [0x03] Work_Zone[3] = 14930*
  7: 0x00DD [0x03] Work_Zone[4] = 15686*
  8: 0x00E2 [0x24] CREATE_DIALOG(message_id=5992*, default_option=0*, option_flags=ExtData[1]->WorkLocal[0])
    → "What do you want me to make? [Nothing./#/$1/$2]"
  9: 0x00E9 [0x25] WAIT_DIALOG_SELECT()
 10: 0x00EA [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00FD
 11: 0x00F2 [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5993*]:
    → "Oh? Where's the fun in that?"
 12: 0x00F9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00FA [0x01] GOTO 0x0252
 14: 0x00FD [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x016D
 15: 0x0105 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[2])
 16: 0x0108 [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5994*]:
    → "You surrre?"
 17: 0x010F [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0110 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 19: 0x0113 [0x24] CREATE_DIALOG(message_id=5995*, default_option=1*, option_flags=0*)
    → "You're rrreally sure? [Yes, I'm sure!/Maybe not...]"
 20: 0x011A [0x25] WAIT_DIALOG_SELECT()
 21: 0x011B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0154
 22: 0x0123 [0x03] Work_Zone[6] = 786*
 23: 0x0128 [0x03] Work_Zone[7] = 1636*
 24: 0x012D [0x03] Work_Zone[8] = 1699*
 25: 0x0132 [0x03] Work_Zone[9] = 2289*
 26: 0x0137 [0x03] Work_Zone_1700[0] = 2187*
 27: 0x013C [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5997*]:
    → "All rrright! You'll need to bring me $4, $5, $6, and $7, then!"
 28: 0x0143 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x0144 [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5998*]:
    → "I'll also need $8 to show your appreciation for my hard work! Good luck!"
 30: 0x014B [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x014C [0x03] Work_Zone[1] = 1*
 32: 0x0151 [0x01] GOTO 0x016A
 33: 0x0154 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x016A
 34: 0x015C [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5996*]:
    → "Well then, what do ya want?"
 35: 0x0163 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x0164 [0x01] GOTO 0x00CE

SUBROUTINE_016A:
 37: 0x016A [0x01] GOTO 0x0252
 38: 0x016D [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x01DD
 39: 0x0175 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[3])
 40: 0x0178 [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5994*]:
    → "You surrre?"
 41: 0x017F [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x0180 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 43: 0x0183 [0x24] CREATE_DIALOG(message_id=5995*, default_option=1*, option_flags=0*)
    → "You're rrreally sure? [Yes, I'm sure!/Maybe not...]"
 44: 0x018A [0x25] WAIT_DIALOG_SELECT()
 45: 0x018B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01C4
 46: 0x0193 [0x03] Work_Zone[6] = 754*
 47: 0x0198 [0x03] Work_Zone[7] = 821*
 48: 0x019D [0x03] Work_Zone[8] = 2152*
 49: 0x01A2 [0x03] Work_Zone[9] = 2289*
 50: 0x01A7 [0x03] Work_Zone_1700[0] = 2186*
 51: 0x01AC [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5997*]:
    → "All rrright! You'll need to bring me $4, $5, $6, and $7, then!"
 52: 0x01B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x01B4 [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5998*]:
    → "I'll also need $8 to show your appreciation for my hard work! Good luck!"
 54: 0x01BB [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x01BC [0x03] Work_Zone[1] = 2*
 56: 0x01C1 [0x01] GOTO 0x01DA
 57: 0x01C4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01DA
 58: 0x01CC [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5996*]:
    → "Well then, what do ya want?"
 59: 0x01D3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x01D4 [0x01] GOTO 0x00CE

SUBROUTINE_01DA:
 61: 0x01DA [0x01] GOTO 0x0252
 62: 0x01DD [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0252
 63: 0x01E5 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[4])
 64: 0x01E8 [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5994*]:
    → "You surrre?"
 65: 0x01EF [0x23] WAIT_FOR_DIALOG_INTERACTION
 66: 0x01F0 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 67: 0x01F3 [0x24] CREATE_DIALOG(message_id=5995*, default_option=1*, option_flags=0*)
    → "You're rrreally sure? [Yes, I'm sure!/Maybe not...]"
 68: 0x01FA [0x25] WAIT_DIALOG_SELECT()
 69: 0x01FB [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0239
 70: 0x0203 [0x03] Work_Zone[6] = 754*
 71: 0x0208 [0x03] Work_Zone[7] = 786*
 72: 0x020D [0x03] Work_Zone[8] = 2152*
 73: 0x0212 [0x03] Work_Zone[9] = 2289*
 74: 0x0217 [0x03] Work_Zone_1700[0] = 2186*
 75: 0x021C [0x03] Work_Zone_1700[1] = 2*
 76: 0x0221 [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5997*]:
    → "All rrright! You'll need to bring me $4, $5, $6, and $7, then!"
 77: 0x0228 [0x23] WAIT_FOR_DIALOG_INTERACTION
 78: 0x0229 [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5999*]:
    → "I'll also need $9 $0%0 to show your appreciation for my hard work! Good luck!"
 79: 0x0230 [0x23] WAIT_FOR_DIALOG_INTERACTION
 80: 0x0231 [0x03] Work_Zone[1] = 3*
 81: 0x0236 [0x01] GOTO 0x024F
 82: 0x0239 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x024F
 83: 0x0241 [0x2B] Dhima Polevhia (ID: 16982331/0x0103213B) [5996*]:
    → "Well then, what do ya want?"
 84: 0x0248 [0x23] WAIT_FOR_DIALOG_INTERACTION
 85: 0x0249 [0x01] GOTO 0x00CE

SUBROUTINE_024F:
 86: 0x024F [0x01] GOTO 0x0252

SUBROUTINE_0252:
 87: 0x0252 [0x21] END_EVENT
 88: 0x0253 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0167 [0x01] GOTO 0x016A
# Dead code (unreachable instructions):
     0x01D7 [0x01] GOTO 0x01DA
# Dead code (unreachable instructions):
     0x024C [0x01] GOTO 0x024F
```

### Event 792

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0254   |
| Data Size    | 32 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:             1E F0 FF FF  7F 1D 22 80 23 1D 23 80      ......".#.#.
0260: 23 45 24 80 F8 FF FF 7F  F8 FF FF 7F 71 73 74 63  #E$.........qstc
0270: 16 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0254 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0259 [0x1D] PRINT_EVENT_MESSAGE(message_id=6007*)
    → "Your order is ready!"
  2: 0x025C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x025D [0x1D] PRINT_EVENT_MESSAGE(message_id=6008*)
    → "Just let me know if you want anything else. You won't find products like this anywhere else on Urhguum, believe me."
  4: 0x0260 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0261 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
  6: 0x0272 [0x21] END_EVENT
  7: 0x0273 [0x00] END_REQSTACK()
```

### Event 793

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0274  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:             00                                        .           
```

#### Opcodes

```
  0: 0x0274 [0x00] END_REQSTACK()
```
