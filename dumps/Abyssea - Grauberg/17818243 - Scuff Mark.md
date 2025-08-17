# 17818243 - Scuff Mark

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Grauberg (ID: 254) |
| Block Size       | 296 bytes                    |
| Total Events     | 2                            |
| References Count | 24                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [241](#event-241)     | 0x0001       |    175 |             31 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0xFFFDF220  |  4294832672 |
|       2 | 0xFFFC2C0C  |  4294716428 |
|       3 | 0xFFFF7E82  |  4294934146 |
|       4 | 0x087C      |        2172 |
|       5 | 0x0002      |           2 |
|       6 | 0x9D35D     |      643933 |
|       7 | 0xFFF9752F  |  4294538543 |
|       8 | 0x62D0      |       25296 |
|       9 | 0x0EE3      |        3811 |
|      10 | 0x0003      |           3 |
|      11 | 0xFFFE7871  |  4294867057 |
|      12 | 0xFFF4ECBD  |  4294241469 |
|      13 | 0x998C      |       39308 |
|      14 | 0x0EB0      |        3760 |
|      15 | 0x001E      |          30 |
|      16 | 0x1EF7      |        7927 |
|      17 | 0x1EF8      |        7928 |
|      18 | 0x0000      |           0 |
|      19 | 0x1FF0      |        8176 |
|      20 | 0x1FFD      |        8189 |
|      21 | 0x1FF1      |        8177 |
|      22 | 0x00E6      |         230 |
|      23 | 0x0078      |         120 |

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

### Event 241

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 175 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 2F 00 86 E2 0F 01  4E 00 86 E2 0F 01 02 03   B/.....N.......
0010: 10 00 80 80 26 00 BA 86  E2 0F 01 01 80 02 80 03  ....&...........
0020: 80 04 80 01 56 00 02 03  10 05 80 80 3E 00 BA 86  ....V.......>...
0030: E2 0F 01 06 80 07 80 08  80 09 80 01 56 00 02 03  ............V...
0040: 10 0A 80 80 56 00 BA 86  E2 0F 01 0B 80 0C 80 0D  ....V...........
0050: 80 0E 80 01 56 00 80 86  E2 0F 01 4A 86 E2 0F 01  ....V......J....
0060: F0 FF FF 7F 1C 0F 80 2B  86 E2 0F 01 10 80 23 2B  .......+......#+
0070: 86 E2 0F 01 11 80 23 02  04 10 12 80 00 8A 00 2B  ......#........+
0080: 86 E2 0F 01 13 80 23 01  92 00 2B 86 E2 0F 01 14  ......#...+.....
0090: 80 23 2B 86 E2 0F 01 15  80 23 9F 16 80 86 E2 0F  .#+......#......
00A0: 01 86 E2 0F 01 6D 61 69  6E 12 80 1C 17 80 21 00  .....main.....!.
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x2F] Ramblix (ID: 17818246/0x010FE286)->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0008 [0x4E] SET_ENTITY_HIDE_FLAG: Show Ramblix (ID: 17818246/0x010FE286)
  3: 0x000E [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x0026
  4: 0x0016 [0xBA] SET_ENTITY_POSITION(entity_id=Ramblix (ID: 17818246/0x010FE286), pos_x=-134.624*, pos_z=-250.868*, pos_y=-33.150*, direction=190.9°*)
  5: 0x0023 [0x01] GOTO 0x0056
  6: 0x0026 [0x02] IF !(Work_Zone[3] == 2*) GOTO 0x003E
  7: 0x002E [0xBA] SET_ENTITY_POSITION(entity_id=Ramblix (ID: 17818246/0x010FE286), pos_x=643.933*, pos_z=-428.753*, pos_y=25.296*, direction=334.9°*)
  8: 0x003B [0x01] GOTO 0x0056
  9: 0x003E [0x02] IF !(Work_Zone[3] == 3*) GOTO 0x0056
 10: 0x0046 [0xBA] SET_ENTITY_POSITION(entity_id=Ramblix (ID: 17818246/0x010FE286), pos_x=-100.239*, pos_z=-725.827*, pos_y=39.308*, direction=330.5°*)
 11: 0x0053 [0x01] GOTO 0x0056

SUBROUTINE_0056:
 12: 0x0056 [0x80] LOAD_WAIT(entity=Ramblix (ID: 17818246/0x010FE286))
 13: 0x005B [0x4A] Ramblix (ID: 17818246/0x010FE286) looks at LocalPlayer
 14: 0x0064 [0x1C] WAIT(30* ticks)
 15: 0x0067 [0x2B] Ramblix (ID: 17818246/0x010FE286) [7927*]:
    → "Oh my Gob! You're one of those adventurerurers, aren't ya? You got nothin' on me, [man./lady.] I was just mindin' my own businesesess, lookin' for junk an' stuff."
 16: 0x006E [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x006F [0x2B] Ramblix (ID: 17818246/0x010FE286) [7928*]:
    → "Hey, watch out. You don't wanna fight me. I'll turn you into meat jerky! Wait, how about you and me be friends instead? Sound good?"
 18: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0077 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x008A
 20: 0x007F [0x2B] Ramblix (ID: 17818246/0x010FE286) [8176*]:
    → "I travel all over the world and hear lots of differererent stories. Why, I hear stories about monsters so nasty, they'd make a grown man wet his breeches! The wyverns hereabouts are worth mentionin'--real pieces of work that've been wreakin' serious havoc in the area."
 21: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0087 [0x01] GOTO 0x0092
 23: 0x008A [0x2B] Ramblix (ID: 17818246/0x010FE286) [8189*]:
    → "I travel all over the world and hear lots of differererent stories. I recall havin' told you about particularilarily nasty wyverns. Well, here's an update on the beasties!"
 24: 0x0091 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0092:
 25: 0x0092 [0x2B] Ramblix (ID: 17818246/0x010FE286) [8177*]:
    → "Word on the highroad is, the creatures've been [waaay agitated lately, so approach at your own peril!/a tad alarmed lately./in good humor lately, if that can be believed.]"
 26: 0x0099 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x009A [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [Ramblix (ID: 17818246/0x010FE286), Ramblix (ID: 17818246/0x010FE286)], work=[230*, 0*]
 28: 0x00AB [0x1C] WAIT(120* ticks)
 29: 0x00AE [0x21] END_EVENT
 30: 0x00AF [0x00] END_REQSTACK()
```
