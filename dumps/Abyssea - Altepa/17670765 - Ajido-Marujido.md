# 17670765 - Ajido-Marujido

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 216 bytes                  |
| Total Events     | 3                          |
| References Count | 18                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [346](#event-346)     | 0x0001       |     13 |              7 |
| [351](#event-351)     | 0x000E       |     99 |             33 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x206D      |        8301 |
|       1 | 0x0028      |          40 |
|       2 | 0x206E      |        8302 |
|       3 | 0x0014      |          20 |
|       4 | 0x0019      |          25 |
|       5 | 0x206F      |        8303 |
|       6 | 0x2070      |        8304 |
|       7 | 0x0032      |          50 |
|       8 | 0x2071      |        8305 |
|       9 | 0x2072      |        8306 |
|      10 | 0x004B      |          75 |
|      11 | 0x2073      |        8307 |
|      12 | 0x2074      |        8308 |
|      13 | 0x0064      |         100 |
|      14 | 0x2075      |        8309 |
|      15 | 0x2076      |        8310 |
|      16 | 0x2077      |        8311 |
|      17 | 0x2078      |        8312 |

## String References

- **8301**: The earth split, the skies cracked open... Unholy monsters, bursting forth in multitudes from every crevasse... And the Star Tree... It was, it was...!
- **8302**: Curses! Why can I not remember!? Did I fail my nation? Is our beloved Windurst no more...!?
- **8303**: The fiends! They are everywhere! Just like that day when...no!
- **8304**: We must incinerate them! Annihilate them! Sear the flesh from their bones!
- **8305**: Yes! I can hear the enemy cry for mercy! Just like our people cried that day when...when...when what!?
- **8306**: Our battle has only just begun! We will teach these accursed monsters the true meaning of pain!
- **8307**: The fiends may try to run, but we shall give chase until the last one meets a grisly end! Ahahahahaha!
- **8308**: We have nothing left to lose! We live only to exact vengeance on the monsters that...that...aaaaaah!
- **8309**: The enemy cowers at our feet, begging for sweet mercy. But we have no mercy to give! Ahahaha!
- **8310**: For our heart was ripped from our chest that day when...aaaaaah! Attack! Attack! Our battle is almost won!
- **8311**: Ahahahaha! Our enemy is silent! We have won for the day.
- **8312**: But what does it matter, when our beloved Windurst is lost forever? Why!? Oh, why did I fail you!? Aaaaaah!

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

### Event 346

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 1C 01 80  1D 02 80 23 21 00         ...#......#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=8301*)
    → "The earth split, the skies cracked open... Unholy monsters, bursting forth in multitudes from every crevasse... And the Star Tree... It was, it was...!"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1C] WAIT(40* ticks)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=8302*)
    → "Curses! Why can I not remember!? Did I fail my nation? Is our beloved Windurst no more...!?"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 351

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 99 bytes |
| Instructions | 33       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            1E F0                ..
0010: FF FF 7F 1C 03 80 03 00  00 02 10 02 00 00 04 80  ................
0020: 03 2E 00 1D 05 80 23 1D  06 80 23 01 6F 00 02 00  ......#...#.o...
0030: 00 07 80 03 41 00 1D 08  80 23 1D 09 80 23 01 6F  ....A....#...#.o
0040: 00 02 00 00 0A 80 03 54  00 1D 0B 80 23 1D 0C 80  .......T....#...
0050: 23 01 6F 00 02 00 00 0D  80 03 67 00 1D 0E 80 23  #.o.......g....#
0060: 1D 0F 80 23 01 6F 00 1D  10 80 23 1D 11 80 23 21  ...#.o....#...#!
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x000E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0013 [0x1C] WAIT(20* ticks)
  2: 0x0016 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  3: 0x001B [0x02] IF !(ExtData[1]->WorkLocal[0] >= 25*) GOTO 0x002E
  4: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=8303*)
    → "The fiends! They are everywhere! Just like that day when...no!"
  5: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=8304*)
    → "We must incinerate them! Annihilate them! Sear the flesh from their bones!"
  7: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x002B [0x01] GOTO 0x006F
  9: 0x002E [0x02] IF !(ExtData[1]->WorkLocal[0] >= 50*) GOTO 0x0041
 10: 0x0036 [0x1D] PRINT_EVENT_MESSAGE(message_id=8305*)
    → "Yes! I can hear the enemy cry for mercy! Just like our people cried that day when...when...when what!?"
 11: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x003A [0x1D] PRINT_EVENT_MESSAGE(message_id=8306*)
    → "Our battle has only just begun! We will teach these accursed monsters the true meaning of pain!"
 13: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x003E [0x01] GOTO 0x006F
 15: 0x0041 [0x02] IF !(ExtData[1]->WorkLocal[0] >= 75*) GOTO 0x0054
 16: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=8307*)
    → "The fiends may try to run, but we shall give chase until the last one meets a grisly end! Ahahahahaha!"
 17: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=8308*)
    → "We have nothing left to lose! We live only to exact vengeance on the monsters that...that...aaaaaah!"
 19: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0051 [0x01] GOTO 0x006F
 21: 0x0054 [0x02] IF !(ExtData[1]->WorkLocal[0] >= 100*) GOTO 0x0067
 22: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=8309*)
    → "The enemy cowers at our feet, begging for sweet mercy. But we have no mercy to give! Ahahaha!"
 23: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=8310*)
    → "For our heart was ripped from our chest that day when...aaaaaah! Attack! Attack! Our battle is almost won!"
 25: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0064 [0x01] GOTO 0x006F
 27: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=8311*)
    → "Ahahahaha! Our enemy is silent! We have won for the day."
 28: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x006B [0x1D] PRINT_EVENT_MESSAGE(message_id=8312*)
    → "But what does it matter, when our beloved Windurst is lost forever? Why!? Oh, why did I fail you!? Aaaaaah!"
 30: 0x006E [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_006F:
 31: 0x006F [0x21] END_EVENT
 32: 0x0070 [0x00] END_REQSTACK()
```
