# 17719499 - Namonutice

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 376 bytes                     |
| Total Events     | 5                             |
| References Count | 32                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [75](#event-75)          | 0x0001       |      1 |              1 |
| [31](#event-31)          | 0x0002       |    193 |             61 |
| [888](#event-888)        | 0x00C3       |      1 |              1 |
| [65535.1](#event-655351) | 0x00C4       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x0265      |         613 |
|       2 | 0x242C      |        9260 |
|       3 | 0x242D      |        9261 |
|       4 | 0x0226      |         550 |
|       5 | 0x22E9      |        8937 |
|       6 | 0x22EA      |        8938 |
|       7 | 0x01E8      |         488 |
|       8 | 0x22E7      |        8935 |
|       9 | 0x22E8      |        8936 |
|      10 | 0x01A9      |         425 |
|      11 | 0x22E5      |        8933 |
|      12 | 0x22E6      |        8934 |
|      13 | 0x0145      |         325 |
|      14 | 0x22E3      |        8931 |
|      15 | 0x22E4      |        8932 |
|      16 | 0x00E1      |         225 |
|      17 | 0x22E1      |        8929 |
|      18 | 0x22E2      |        8930 |
|      19 | 0x007D      |         125 |
|      20 | 0x22DF      |        8927 |
|      21 | 0x22E0      |        8928 |
|      22 | 0x0032      |          50 |
|      23 | 0x22DD      |        8925 |
|      24 | 0x22DE      |        8926 |
|      25 | 0x22DA      |        8922 |
|      26 | 0x22DB      |        8923 |
|      27 | 0x22DC      |        8924 |
|      28 | 0x000D      |          13 |
|      29 | 0x14DE1     |       85473 |
|      30 | 0x1BBAE     |      113582 |
|      31 | 0x03E8      |        1000 |

## String References

- **8922**: Hmm... <Player>, you say? No, never heard that name. Do not expect me to learn the name of every recruit!
- **8923**: Do good for the Kingdom and her people, and they shall come to know you.
- **8924**: Once you have their trust, they will request your help more readily. Just keep your head down, and your day shall come.
- **8925**: <Player>...? Hmm... I might have heard that name before. Then again, maybe not.
- **8926**: You are not famous yet. Keep your nose to the grindstone and work for the people. Soon, they will know you better!
- **8927**: Ah, <Player>. That is a name I often hear. People speak well of you!
- **8928**: Your deeds for the Kingdom have earned you much honor.
- **8929**: <Player>! You have become well known in these parts!
- **8930**: I hear much of your accomplishments. Keep up the good work, and greatness lies in your future.
- **8931**: Ah, <Player>! You are famous in our kingdom!
- **8932**: Of you no ill is spoken. Give to the Kingdom and she will give to you, no?
- **8933**: <Player>! I would venture that much the Kingdom has heard your name!
- **8934**: And your reputation sparkles. Indeed I am proud of you. And to think I first knew you when you were a new recruit!
- **8935**: Hello, <Player>. Practically all of the Kingdom has heard of you now.
- **8936**: What's more, your reputation is stellar. I look forward to even greater things from you!
- **8937**: <Player>! People are talking about you! Every infant in his cradle knows your name!
- **8938**: And they hold you in highest regard! I am so proud of you! May your kind deeds continue!
- **9260**: [Sir/Lady] <Player>! There isn't a soul in the Kingdom that doesn't consider you a hero!
- **9261**: As a representative of the people of San d'Oria, I humbly ask you to continue your efforts for the good of the country. May the light of the Goddess shine upon you!

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

### Event 75

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

### Event 31

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 193 bytes |
| Instructions | 61        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 00 00 02 10 1E  F0 FF FF 7F 6F 70 66 00    ..........opf.
0010: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 02 00 00  .........tlk0...
0020: 01 80 04 30 00 1D 02 80  23 1D 03 80 23 01 C1 00  ...0....#...#...
0030: 02 00 00 04 80 04 43 00  1D 05 80 23 1D 06 80 23  ......C....#...#
0040: 01 C1 00 02 00 00 07 80  04 56 00 1D 08 80 23 1D  .........V....#.
0050: 09 80 23 01 C1 00 02 00  00 0A 80 04 69 00 1D 0B  ..#.........i...
0060: 80 23 1D 0C 80 23 01 C1  00 02 00 00 0D 80 04 7C  .#...#.........|
0070: 00 1D 0E 80 23 1D 0F 80  23 01 C1 00 02 00 00 10  ....#...#.......
0080: 80 04 8F 00 1D 11 80 23  1D 12 80 23 01 C1 00 02  .......#...#....
0090: 00 00 13 80 04 A2 00 1D  14 80 23 1D 15 80 23 01  ..........#...#.
00A0: C1 00 02 00 00 16 80 04  B5 00 1D 17 80 23 1D 18  .............#..
00B0: 80 23 01 C1 00 1D 19 80  23 1D 1A 80 23 1D 1B 80  .#......#...#...
00C0: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0007 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x000C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x001D [0x02] IF !(ExtData[1]->WorkLocal[0] < 613*) GOTO 0x0030
  6: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=9260*)
    → "[Sir/Lady] <Player>! There isn't a soul in the Kingdom that doesn't consider you a hero!"
  7: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=9261*)
    → "As a representative of the people of San d'Oria, I humbly ask you to continue your efforts for the good of the country. May the light of the Goddess shine upon you!"
  9: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002D [0x01] GOTO 0x00C1
 11: 0x0030 [0x02] IF !(ExtData[1]->WorkLocal[0] < 550*) GOTO 0x0043
 12: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=8937*)
    → "<Player>! People are talking about you! Every infant in his cradle knows your name!"
 13: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=8938*)
    → "And they hold you in highest regard! I am so proud of you! May your kind deeds continue!"
 15: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0040 [0x01] GOTO 0x00C1
 17: 0x0043 [0x02] IF !(ExtData[1]->WorkLocal[0] < 488*) GOTO 0x0056
 18: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=8935*)
    → "Hello, <Player>. Practically all of the Kingdom has heard of you now."
 19: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=8936*)
    → "What's more, your reputation is stellar. I look forward to even greater things from you!"
 21: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0053 [0x01] GOTO 0x00C1
 23: 0x0056 [0x02] IF !(ExtData[1]->WorkLocal[0] < 425*) GOTO 0x0069
 24: 0x005E [0x1D] PRINT_EVENT_MESSAGE(message_id=8933*)
    → "<Player>! I would venture that much the Kingdom has heard your name!"
 25: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0062 [0x1D] PRINT_EVENT_MESSAGE(message_id=8934*)
    → "And your reputation sparkles. Indeed I am proud of you. And to think I first knew you when you were a new recruit!"
 27: 0x0065 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x0066 [0x01] GOTO 0x00C1
 29: 0x0069 [0x02] IF !(ExtData[1]->WorkLocal[0] < 325*) GOTO 0x007C
 30: 0x0071 [0x1D] PRINT_EVENT_MESSAGE(message_id=8931*)
    → "Ah, <Player>! You are famous in our kingdom!"
 31: 0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=8932*)
    → "Of you no ill is spoken. Give to the Kingdom and she will give to you, no?"
 33: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0079 [0x01] GOTO 0x00C1
 35: 0x007C [0x02] IF !(ExtData[1]->WorkLocal[0] < 225*) GOTO 0x008F
 36: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=8929*)
    → "<Player>! You have become well known in these parts!"
 37: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=8930*)
    → "I hear much of your accomplishments. Keep up the good work, and greatness lies in your future."
 39: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 40: 0x008C [0x01] GOTO 0x00C1
 41: 0x008F [0x02] IF !(ExtData[1]->WorkLocal[0] < 125*) GOTO 0x00A2
 42: 0x0097 [0x1D] PRINT_EVENT_MESSAGE(message_id=8927*)
    → "Ah, <Player>. That is a name I often hear. People speak well of you!"
 43: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x009B [0x1D] PRINT_EVENT_MESSAGE(message_id=8928*)
    → "Your deeds for the Kingdom have earned you much honor."
 45: 0x009E [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x009F [0x01] GOTO 0x00C1
 47: 0x00A2 [0x02] IF !(ExtData[1]->WorkLocal[0] < 50*) GOTO 0x00B5
 48: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=8925*)
    → "<Player>...? Hmm... I might have heard that name before. Then again, maybe not."
 49: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x00AE [0x1D] PRINT_EVENT_MESSAGE(message_id=8926*)
    → "You are not famous yet. Keep your nose to the grindstone and work for the people. Soon, they will know you better!"
 51: 0x00B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x00B2 [0x01] GOTO 0x00C1
 53: 0x00B5 [0x1D] PRINT_EVENT_MESSAGE(message_id=8922*)
    → "Hmm... <Player>, you say? No, never heard that name. Do not expect me to learn the name of every recruit!"
 54: 0x00B8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x00B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=8923*)
    → "Do good for the Kingdom and her people, and they shall come to know you."
 56: 0x00BC [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=8924*)
    → "Once you have their trust, they will request your help more readily. Just keep your head down, and your day shall come."
 58: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00C1:
 59: 0x00C1 [0x21] END_EVENT
 60: 0x00C2 [0x00] END_REQSTACK()
```

### Event 888

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          00                                          .            
```

#### Opcodes

```
  0: 0x00C3 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C4   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:             32 1C 80 1F  00 1D 80 1E 80 1F 80 1F      2...........
00D0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x00C4 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00C7 [0x1F] MOVE_ENTITY: EventEntity moves to X=85.473*, Z=113.582*, Y=1.000*
  2: 0x00CF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D1 [0x00] END_REQSTACK()
```
