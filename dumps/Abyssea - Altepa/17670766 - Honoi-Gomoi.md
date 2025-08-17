# 17670766 - Honoi-Gomoi

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 220 bytes                  |
| Total Events     | 2                          |
| References Count | 17                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [331](#event-331)     | 0x0001       |    124 |             41 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x2049      |        8265 |
|       2 | 0x204A      |        8266 |
|       3 | 0x0028      |          40 |
|       4 | 0x2047      |        8263 |
|       5 | 0x2048      |        8264 |
|       6 | 0x001E      |          30 |
|       7 | 0x2045      |        8261 |
|       8 | 0x2046      |        8262 |
|       9 | 0x0014      |          20 |
|      10 | 0x2043      |        8259 |
|      11 | 0x2044      |        8260 |
|      12 | 0x000A      |          10 |
|      13 | 0x2041      |        8257 |
|      14 | 0x2042      |        8258 |
|      15 | 0x203F      |        8255 |
|      16 | 0x2040      |        8256 |

## String References

- **8255**: ...Oh, excuse me. I was just counting my cruor. <Player>? Never heard of you.
- **8256**: If you want to make yourself useful, why don't you help that chef girl with her bean stew? I've worked up an awful-wawful appetite.
- **8257**: <Player>...? I might have heard that name somewhere.
- **8258**: [He/She] hasn't done anything for me, though, so I promptly-womptly forgotaru it!
- **8259**: So you're <Player>. Yes, I've heard the occasional rumor aboutaru you.
- **8260**: You'll have to keep working hard, though, if you want to become as wealthy--I mean, as famous--as me!
- **8261**: Ah, <Player>. Your generous deeds have won you quite a few fans around camp these days.
- **8262**: When this camp prosper-wospers, so too do my fortunes. For all of our sakes, keep up the good work!
- **8263**: Well, if it isn't <Player>. You've made quite a name for yourself, haven't you?
- **8264**: Don't you feel lucky that I picky-wicked you out of the scrap heap and set you on your way to stardom?
- **8265**: Well, look who we have here! None other than the illustrious-wustrious <Player>, [hero/heroine] of the desert!
- **8266**: Your mere presence does this humble merchantaru an honor. Why, I would trade away my entire fortune-wortune for you to always stay by our side! Er, make that half my fortune...

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

### Event 331

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 124 bytes |
| Instructions | 41        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 1E F0  FF FF 7F 6F 70 02 00 00   ..........op...
0010: 00 80 04 20 00 1D 01 80  23 1D 02 80 23 01 7B 00  ... ....#...#.{.
0020: 02 00 00 03 80 04 3A 00  27 10 F0 FF FF 7F 06 1D  ......:.'.......
0030: 04 80 23 1D 05 80 23 01  7B 00 02 00 00 06 80 04  ..#...#.{.......
0040: 4D 00 1D 07 80 23 1D 08  80 23 01 7B 00 02 00 00  M....#...#.{....
0050: 09 80 04 60 00 1D 0A 80  23 1D 0B 80 23 01 7B 00  ...`....#...#.{.
0060: 02 00 00 0C 80 04 73 00  1D 0D 80 23 1D 0E 80 23  ......s....#...#
0070: 01 7B 00 1D 0F 80 23 1D  10 80 23 21 00           .{....#...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x000B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000D [0x02] IF !(ExtData[1]->WorkLocal[0] < 50*) GOTO 0x0020
  5: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=8265*)
    → "Well, look who we have here! None other than the illustrious-wustrious <Player>, [hero/heroine] of the desert!"
  6: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=8266*)
    → "Your mere presence does this humble merchantaru an honor. Why, I would trade away my entire fortune-wortune for you to always stay by our side! Er, make that half my fortune..."
  8: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x001D [0x01] GOTO 0x007B
 10: 0x0020 [0x02] IF !(ExtData[1]->WorkLocal[0] < 40*) GOTO 0x003A
 11: 0x0028 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 12: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=8263*)
    → "Well, if it isn't <Player>. You've made quite a name for yourself, haven't you?"
 13: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=8264*)
    → "Don't you feel lucky that I picky-wicked you out of the scrap heap and set you on your way to stardom?"
 15: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0037 [0x01] GOTO 0x007B
 17: 0x003A [0x02] IF !(ExtData[1]->WorkLocal[0] < 30*) GOTO 0x004D
 18: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=8261*)
    → "Ah, <Player>. Your generous deeds have won you quite a few fans around camp these days."
 19: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=8262*)
    → "When this camp prosper-wospers, so too do my fortunes. For all of our sakes, keep up the good work!"
 21: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x004A [0x01] GOTO 0x007B
 23: 0x004D [0x02] IF !(ExtData[1]->WorkLocal[0] < 20*) GOTO 0x0060
 24: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=8259*)
    → "So you're <Player>. Yes, I've heard the occasional rumor aboutaru you."
 25: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0059 [0x1D] PRINT_EVENT_MESSAGE(message_id=8260*)
    → "You'll have to keep working hard, though, if you want to become as wealthy--I mean, as famous--as me!"
 27: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x005D [0x01] GOTO 0x007B
 29: 0x0060 [0x02] IF !(ExtData[1]->WorkLocal[0] < 10*) GOTO 0x0073
 30: 0x0068 [0x1D] PRINT_EVENT_MESSAGE(message_id=8257*)
    → "<Player>...? I might have heard that name somewhere."
 31: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x006C [0x1D] PRINT_EVENT_MESSAGE(message_id=8258*)
    → "[He/She] hasn't done anything for me, though, so I promptly-womptly forgotaru it!"
 33: 0x006F [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0070 [0x01] GOTO 0x007B
 35: 0x0073 [0x1D] PRINT_EVENT_MESSAGE(message_id=8255*)
    → "...Oh, excuse me. I was just counting my cruor. <Player>? Never heard of you."
 36: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x0077 [0x1D] PRINT_EVENT_MESSAGE(message_id=8256*)
    → "If you want to make yourself useful, why don't you help that chef girl with her bean stew? I've worked up an awful-wawful appetite."
 38: 0x007A [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_007B:
 39: 0x007B [0x21] END_EVENT
 40: 0x007C [0x00] END_REQSTACK()
```
