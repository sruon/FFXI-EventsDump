# 17318611 - Namonutice

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Abyssea - La Theine (ID: 132) |
| Block Size       | 236 bytes                     |
| Total Events     | 2                             |
| References Count | 18                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [158](#event-158)     | 0x0001       |    136 |             43 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x0032      |          50 |
|       2 | 0x1E91      |        7825 |
|       3 | 0x1E92      |        7826 |
|       4 | 0x0028      |          40 |
|       5 | 0x1E8F      |        7823 |
|       6 | 0x1E90      |        7824 |
|       7 | 0x001E      |          30 |
|       8 | 0x1E8D      |        7821 |
|       9 | 0x1E8E      |        7822 |
|      10 | 0x1E8B      |        7819 |
|      11 | 0x1E8C      |        7820 |
|      12 | 0x000A      |          10 |
|      13 | 0x1E89      |        7817 |
|      14 | 0x1E8A      |        7818 |
|      15 | 0x1E86      |        7814 |
|      16 | 0x1E87      |        7815 |
|      17 | 0x1E88      |        7816 |

## String References

- **7814**: Hmm... <Player>, you say? No, never heard that name.
- **7815**: But do good for the survivors, and they shall come to know you.
- **7816**: Once you have their trust, they will more readily turn to you for help. Just keep your head down, and your day shall come.
- **7817**: <Player>...? Hmm... I might have heard that name before. Then again, maybe not.
- **7818**: You are not yet famous. Keep your nose to the grindstone and do your part for the people. Soon, they will know you better!
- **7819**: Ah, <Player>. That is a name I often hear. People speak well of you!
- **7820**: Your deeds for the folk battling here have earned you much honor.
- **7821**: <Player>! You have become well known in these parts!
- **7822**: I hear much of your accomplishments. Keep up the good work, and greatness lies in your future.
- **7823**: Ah, <Player>! You are famous among the community of survivors!
- **7824**: Of you no ill is spoken. Give to the community and it will give to you, no?
- **7825**: <Player>! I would venture that most who've taken refuge in the plateau have heard your name!
- **7826**: And your reputation sparkles. Indeed I am proud of you. And to think I first knew you when first you came to us!

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

### Event 158

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 136 bytes |
| Instructions | 43        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 1E F0  FF FF 7F 6F 70 66 00 80   ..........opf..
0010: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 02 00 00 01  ........tlk0....
0020: 80 04 2F 00 1D 02 80 23  1D 03 80 23 01 87 00 02  ../....#...#....
0030: 00 00 04 80 04 42 00 1D  05 80 23 1D 06 80 23 01  .....B....#...#.
0040: 87 00 02 00 00 07 80 04  55 00 1D 08 80 23 1D 09  ........U....#..
0050: 80 23 01 87 00 02 00 00  00 80 04 68 00 1D 0A 80  .#.........h....
0060: 23 1D 0B 80 23 01 87 00  02 00 00 0C 80 04 7B 00  #...#.........{.
0070: 1D 0D 80 23 1D 0E 80 23  01 87 00 1D 0F 80 23 1D  ...#...#......#.
0080: 10 80 23 1D 11 80 23 21  00                       ..#...#!.       
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x000B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x001C [0x02] IF !(ExtData[1]->WorkLocal[0] < 50*) GOTO 0x002F
  6: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7825*)
    → "<Player>! I would venture that most who've taken refuge in the plateau have heard your name!"
  7: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=7826*)
    → "And your reputation sparkles. Indeed I am proud of you. And to think I first knew you when first you came to us!"
  9: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002C [0x01] GOTO 0x0087
 11: 0x002F [0x02] IF !(ExtData[1]->WorkLocal[0] < 40*) GOTO 0x0042
 12: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=7823*)
    → "Ah, <Player>! You are famous among the community of survivors!"
 13: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=7824*)
    → "Of you no ill is spoken. Give to the community and it will give to you, no?"
 15: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x003F [0x01] GOTO 0x0087
 17: 0x0042 [0x02] IF !(ExtData[1]->WorkLocal[0] < 30*) GOTO 0x0055
 18: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=7821*)
    → "<Player>! You have become well known in these parts!"
 19: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x004E [0x1D] PRINT_EVENT_MESSAGE(message_id=7822*)
    → "I hear much of your accomplishments. Keep up the good work, and greatness lies in your future."
 21: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0052 [0x01] GOTO 0x0087
 23: 0x0055 [0x02] IF !(ExtData[1]->WorkLocal[0] < 20*) GOTO 0x0068
 24: 0x005D [0x1D] PRINT_EVENT_MESSAGE(message_id=7819*)
    → "Ah, <Player>. That is a name I often hear. People speak well of you!"
 25: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0061 [0x1D] PRINT_EVENT_MESSAGE(message_id=7820*)
    → "Your deeds for the folk battling here have earned you much honor."
 27: 0x0064 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x0065 [0x01] GOTO 0x0087
 29: 0x0068 [0x02] IF !(ExtData[1]->WorkLocal[0] < 10*) GOTO 0x007B
 30: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=7817*)
    → "<Player>...? Hmm... I might have heard that name before. Then again, maybe not."
 31: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0074 [0x1D] PRINT_EVENT_MESSAGE(message_id=7818*)
    → "You are not yet famous. Keep your nose to the grindstone and do your part for the people. Soon, they will know you better!"
 33: 0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0078 [0x01] GOTO 0x0087
 35: 0x007B [0x1D] PRINT_EVENT_MESSAGE(message_id=7814*)
    → "Hmm... <Player>, you say? No, never heard that name."
 36: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x007F [0x1D] PRINT_EVENT_MESSAGE(message_id=7815*)
    → "But do good for the survivors, and they shall come to know you."
 38: 0x0082 [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x0083 [0x1D] PRINT_EVENT_MESSAGE(message_id=7816*)
    → "Once you have their trust, they will more readily turn to you for help. Just keep your head down, and your day shall come."
 40: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0087:
 41: 0x0087 [0x21] END_EVENT
 42: 0x0088 [0x00] END_REQSTACK()
```
