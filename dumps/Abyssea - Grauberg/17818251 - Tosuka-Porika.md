# 17818251 - Tosuka-Porika

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Grauberg (ID: 254) |
| Block Size       | 236 bytes                    |
| Total Events     | 3                            |
| References Count | 17                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [275](#event-275)     | 0x0001       |     33 |              9 |
| [268](#event-268)     | 0x0022       |    105 |             31 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0151      |         337 |
|       2 | 0x203E      |        8254 |
|       3 | 0x203F      |        8255 |
|       4 | 0x0064      |         100 |
|       5 | 0x2048      |        8264 |
|       6 | 0x004B      |          75 |
|       7 | 0x2046      |        8262 |
|       8 | 0x2047      |        8263 |
|       9 | 0x0032      |          50 |
|      10 | 0x2044      |        8260 |
|      11 | 0x2045      |        8261 |
|      12 | 0x0019      |          25 |
|      13 | 0x2042      |        8258 |
|      14 | 0x2043      |        8259 |
|      15 | 0x2040      |        8256 |
|      16 | 0x2041      |        8257 |

## String References

- **8254**: Hrrrm... I say, however did an academic such as me end up at the helm of a military outfit?
- **8255**: Well, perhaps it's to the good. Knowing is half the battle, after all, and knowledge is something I do not want for. Now, I just require strapping young fighters like you to take to the front line.
- **8256**: Hrrrm! Our forces are on the receiving end of heavy punishment!
- **8257**: You! Don't just stand there looking like a tree! Jump into the fray and fell a fiend or three! That's an order!
- **8258**: The Abyssean hordes harry us still, but I'm observing some wariness in their movements.
- **8259**: This is a golden chance to shift out of our defensive posture and repay the enemy in kind!
- **8260**: We've managed to gain a footing with the Abyssean hordes. The time is come for us to show our true steel!
- **8261**: Go forth, my loyal minions, and show the enemy no quarter!
- **8262**: Mwahaha! We have the Abyssean fiends cowering at the mere sound of our approach!
- **8263**: Victory is no longer a question of if, but when. Go forth, my loyal minions, and lay waste to our foes!
- **8264**: Mwahaha! The Abyssean fiends are completely at our mercy! Squirm though they might, there will be no escaping my iron grip of subjugation! Heaheaheaheahhh!

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

### Event 275

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 5B 01 80 F8 FF FF 7F   ........[......
0010: F8 FF FF 7F 74 6C 6B 30  1D 02 80 23 1D 03 80 23  ....tlk0...#...#
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=337*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=8254*)
    → "Hrrrm... I say, however did an academic such as me end up at the helm of a military outfit?"
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=8255*)
    → "Well, perhaps it's to the good. Knowing is half the battle, after all, and knowledge is something I do not want for. Now, I just require strapping young fighters like you to take to the front line."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x21] END_EVENT
  8: 0x0021 [0x00] END_REQSTACK()
```

### Event 268

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0022    |
| Data Size    | 105 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       1E F0 FF FF 7F 1C  00 80 5B 01 80 F8 FF FF    ........[.....
0030: 7F F8 FF FF 7F 74 6C 6B  30 02 02 10 04 80 00 48  .....tlk0......H
0040: 00 1D 05 80 23 01 89 00  02 02 10 06 80 04 5B 00  ....#.........[.
0050: 1D 07 80 23 1D 08 80 23  01 89 00 02 02 10 09 80  ...#...#........
0060: 04 6E 00 1D 0A 80 23 1D  0B 80 23 01 89 00 02 02  .n....#...#.....
0070: 10 0C 80 04 81 00 1D 0D  80 23 1D 0E 80 23 01 89  .........#...#..
0080: 00 1D 0F 80 23 1D 10 80  23 21 00                 ....#...#!.     
```

#### Opcodes

```
  0: 0x0022 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0027 [0x1C] WAIT(30* ticks)
  2: 0x002A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=337*
  3: 0x0039 [0x02] IF !(Work_Zone[2] == 100*) GOTO 0x0048
  4: 0x0041 [0x1D] PRINT_EVENT_MESSAGE(message_id=8264*)
    → "Mwahaha! The Abyssean fiends are completely at our mercy! Squirm though they might, there will be no escaping my iron grip of subjugation! Heaheaheaheahhh!"
  5: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0045 [0x01] GOTO 0x0089
  7: 0x0048 [0x02] IF !(Work_Zone[2] < 75*) GOTO 0x005B
  8: 0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=8262*)
    → "Mwahaha! We have the Abyssean fiends cowering at the mere sound of our approach!"
  9: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=8263*)
    → "Victory is no longer a question of if, but when. Go forth, my loyal minions, and lay waste to our foes!"
 11: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0058 [0x01] GOTO 0x0089
 13: 0x005B [0x02] IF !(Work_Zone[2] < 50*) GOTO 0x006E
 14: 0x0063 [0x1D] PRINT_EVENT_MESSAGE(message_id=8260*)
    → "We've managed to gain a footing with the Abyssean hordes. The time is come for us to show our true steel!"
 15: 0x0066 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=8261*)
    → "Go forth, my loyal minions, and show the enemy no quarter!"
 17: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x006B [0x01] GOTO 0x0089
 19: 0x006E [0x02] IF !(Work_Zone[2] < 25*) GOTO 0x0081
 20: 0x0076 [0x1D] PRINT_EVENT_MESSAGE(message_id=8258*)
    → "The Abyssean hordes harry us still, but I'm observing some wariness in their movements."
 21: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x007A [0x1D] PRINT_EVENT_MESSAGE(message_id=8259*)
    → "This is a golden chance to shift out of our defensive posture and repay the enemy in kind!"
 23: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x007E [0x01] GOTO 0x0089
 25: 0x0081 [0x1D] PRINT_EVENT_MESSAGE(message_id=8256*)
    → "Hrrrm! Our forces are on the receiving end of heavy punishment!"
 26: 0x0084 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=8257*)
    → "You! Don't just stand there looking like a tree! Jump into the fray and fell a fiend or three! That's an order!"
 28: 0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0089:
 29: 0x0089 [0x21] END_EVENT
 30: 0x008A [0x00] END_REQSTACK()
```
