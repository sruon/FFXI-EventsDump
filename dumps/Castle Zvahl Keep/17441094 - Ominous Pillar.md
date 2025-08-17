# 17441094 - Ominous Pillar

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Castle Zvahl Keep (ID: 162) |
| Block Size       | 400 bytes                   |
| Total Events     | 2                           |
| References Count | 22                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [100](#event-100)     | 0x0001       |    286 |             64 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x1C63      |        7267 |
|       3 | 0x1C64      |        7268 |
|       4 | 0x0484      |        1156 |
|       5 | 0x1C65      |        7269 |
|       6 | 0x1C66      |        7270 |
|       7 | 0x1C68      |        7272 |
|       8 | 0x1C69      |        7273 |
|       9 | 0x1C6A      |        7274 |
|      10 | 0x0002      |           2 |
|      11 | 0x0003      |           3 |
|      12 | 0x0005      |           5 |
|      13 | 0x1C67      |        7271 |
|      14 | 0x0487      |        1159 |
|      15 | 0x1C6E      |        7278 |
|      16 | 0x1C6F      |        7279 |
|      17 | 0x1C70      |        7280 |
|      18 | 0x0004      |           4 |
|      19 | 0x1C71      |        7281 |
|      20 | 0x1C72      |        7282 |
|      21 | 0x1C73      |        7283 |

## String References

- **7270**: How about it? [Let's do it./Do your own job.]

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

### Event 100

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 286 bytes |
| Instructions | 64        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 03 01 10 00  80 03 00 00 02 10 03 01    .B............
0010: 00 03 10 29 80 4B 21 0A  01 06 02 00 00 01 80 80  ...).K!.........
0020: 97 00 2B 4B 21 0A 01 02  80 23 2B 4B 21 0A 01 03  ..+K!....#+K!...
0030: 80 23 03 02 10 04 80 2B  4B 21 0A 01 05 80 23 24  .#.....+K!....#$
0040: 06 80 01 80 00 80 25 02  00 10 00 80 00 81 00 2B  ......%........+
0050: 4B 21 0A 01 07 80 23 03  02 10 01 00 2B 4B 21 0A  K!....#.....+K!.
0060: 01 08 80 23 2B 4B 21 0A  01 09 80 23 40 00 80 0A  ...#+K!....#@...
0070: 80 01 10 01 80 40 0B 80  0C 80 01 10 01 00 01 94  .....@..........
0080: 00 02 00 10 01 80 00 94  00 2B 4B 21 0A 01 0D 80  .........+K!....
0090: 23 01 94 00 01 14 01 02  00 00 0A 80 80 B7 00 03  #...............
00A0: 02 10 01 00 2B 4B 21 0A  01 08 80 23 2B 4B 21 0A  ....+K!....#+K!.
00B0: 01 09 80 23 01 14 01 02  00 00 0B 80 80 DF 00 03  ...#............
00C0: 03 10 0E 80 2B 4B 21 0A  01 0F 80 23 2B 4B 21 0A  ....+K!....#+K!.
00D0: 01 10 80 23 2B 4B 21 0A  01 11 80 23 01 14 01 02  ...#+K!....#....
00E0: 00 00 12 80 80 14 01 2B  4B 21 0A 01 02 80 23 03  .......+K!....#.
00F0: 02 10 04 80 2B 4B 21 0A  01 13 80 23 03 02 10 04  ....+K!....#....
0100: 80 2B 4B 21 0A 01 14 80  23 2B 4B 21 0A 01 15 80  .+K!....#+K!....
0110: 23 01 14 01 29 80 4B 21  0A 01 07 20 00 21 00     #...).K!... .!. 
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x03] Work_Zone[1] = 0*
  3: 0x0009 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  4: 0x000E [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  5: 0x0013 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17441099/0x010A214B), tag_num=0x06)
  6: 0x001A [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0097
  7: 0x0022 [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7267*]:
    → "Greetings, friend, and welcome to the Mog Merchants Extraordinaire! Here, you can exchange your hard-earned kupons for all sorts of stupendous souvenirs!"
  8: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002A [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7268*]:
    → "...Or so we thought, kupo. Sadly, it seems that my cohorts are slacking off on the job. They're nowhere to be found!"
 10: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0032 [0x03] Work_Zone[2] = 1156*
 12: 0x0037 [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7269*]:
    → "Unless they come back, I fear that your $3 is nothing but a worthless scrap of parchment. I know! Perhaps you could help me track them down, kupo?"
 13: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x003F [0x24] CREATE_DIALOG(message_id=7270*, default_option=1*, option_flags=0*)
    → "How about it? [Let's do it./Do your own job.]"
 15: 0x0046 [0x25] WAIT_DIALOG_SELECT()
 16: 0x0047 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0081
 17: 0x004F [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7272*]:
    → "Oh, a thousand thank-yous, kind adventurer! Without my accomplices--er, associates--the boss's plans will all be for naught! I mean, our customers will be distraught, kupo!"
 18: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0057 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 20: 0x005C [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7273*]:
    → "<Ahem>! As I was saying... I'd be ever so grateful if you could find our [horticulturist/ironmonger/pyrotechnician/pawnbroker], [Kupatete/Kupignol/Kupuckl/Kupert], and escort [her/his/his/his] procrastinating moogle posterior back to work."
 21: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0064 [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7274*]:
    → "They're far too lazy to have ventured outside this keep, so you should be able to find them loafing around here somewhere, kupo."
 23: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x006C [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=2*, target=Work_Zone[1], source=1*)
 25: 0x0075 [0x40] SET_BIT_WORK_RANGE(start_bit=3*, end_bit=5*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 26: 0x007E [0x01] GOTO 0x0094
 27: 0x0081 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0094
 28: 0x0089 [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7271*]:
    → "Hmph. Fine, be that way! No fur off my nose, kupo. That's one less prize wasted on an ungrateful adventurer."
 29: 0x0090 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0091 [0x01] GOTO 0x0094

SUBROUTINE_0094:
 31: 0x0094 [0x01] GOTO 0x0114
 32: 0x0097 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x00B7
 33: 0x009F [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 34: 0x00A4 [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7273*]:
    → "<Ahem>! As I was saying... I'd be ever so grateful if you could find our [horticulturist/ironmonger/pyrotechnician/pawnbroker], [Kupatete/Kupignol/Kupuckl/Kupert], and escort [her/his/his/his] procrastinating moogle posterior back to work."
 35: 0x00AB [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x00AC [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7274*]:
    → "They're far too lazy to have ventured outside this keep, so you should be able to find them loafing around here somewhere, kupo."
 37: 0x00B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x00B4 [0x01] GOTO 0x0114
 39: 0x00B7 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x00DF
 40: 0x00BF [0x03] Work_Zone[3] = 1159*
 41: 0x00C4 [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7278*]:
    → "Just don't tell the boss I was sleeping on the job. Deal, kupo? In return, that $3 will allow you to take part in this festival's grand finale..."
 42: 0x00CB [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x00CC [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7279*]:
    → "The Mega Mog Bonanza-Rama-Palooza! Doesn't that name positively scream "excitement"!?"
 44: 0x00D3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x00D4 [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7280*]:
    → "What's even more exciting are the exclusive prizes you could win, kupo. If I were you, why, I'd flap my little wings as furiously as I could and make for the main event without delay!"
 46: 0x00DB [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x00DC [0x01] GOTO 0x0114
 48: 0x00DF [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x0114
 49: 0x00E7 [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7267*]:
    → "Greetings, friend, and welcome to the Mog Merchants Extraordinaire! Here, you can exchange your hard-earned kupons for all sorts of stupendous souvenirs!"
 50: 0x00EE [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x00EF [0x03] Work_Zone[2] = 1156*
 52: 0x00F4 [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7281*]:
    → "Welcome to the Mog Merchants Extraordinaire souvenir shop, where you can exchange that hard-earned $3 of yours for scores of spectacular prizes!"
 53: 0x00FB [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x00FC [0x03] Work_Zone[2] = 1156*
 55: 0x0101 [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7282*]:
    → "What's that? You don't have a $3!? Er...then just forget I said anything, kupo!"
 56: 0x0108 [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x0109 [0x2B] Stooge Moogle (ID: 17441099/0x010A214B) [7283*]:
    → "Or, if you fancy yourself to have nerves of darksteel...! The courage to look fear in the eye and make it your master...! You could go win yourself one at our event in the castle baileys! Do you have it in you, kupo!?"
 58: 0x0110 [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x0111 [0x01] GOTO 0x0114

SUBROUTINE_0114:
 60: 0x0114 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17441099/0x010A214B), tag_num=0x07)
 61: 0x011B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 62: 0x011D [0x21] END_EVENT
 63: 0x011E [0x00] END_REQSTACK()
```
