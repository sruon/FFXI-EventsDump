# 17670757 - Tapoh Lihzeh

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 228 bytes                  |
| Total Events     | 3                          |
| References Count | 13                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [324](#event-324)     | 0x0001       |     14 |              6 |
| [321](#event-321)     | 0x000F       |    132 |             38 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1F9E      |        8094 |
|       2 | 0x1F97      |        8087 |
|       3 | 0x1F98      |        8088 |
|       4 | 0x0000      |           0 |
|       5 | 0x1F9A      |        8090 |
|       6 | 0x0001      |           1 |
|       7 | 0x1F9B      |        8091 |
|       8 | 0x0002      |           2 |
|       9 | 0x1F99      |        8089 |
|      10 | 0x1F9C      |        8092 |
|      11 | 0x1F8C      |        8076 |
|      12 | 0x1F9D      |        8093 |

## String References

- **8076**: Hear the report again? [No need./Yes, please.]
- **8087**: My report? Why, yes, it should be rrright-- Well, that's strange. It seems a fiend has devoured it. I suppose you'll just have to pass along my findings for me.
- **8088**: I spoke with a recuperating soldier who was complaining of terrrible [chest pains/dizziness/headaches/ringing in the ears].
- **8089**: It would seem that the fiend [swooped down from the sky to attack him/ambushed him when he was resting his legs at an oasis/jumped out from behind a shadowy rock when he was on patrol/burst forth from an odd hollow in the ground].
- **8090**: [The beast was so extravagantly colored, he says he'll never forget the sight of it/The beast was so unremarkable in appearance, he almost didn't see it coming/So garishly colored was the fiend that it sent shivers up his spine/He was so hypnotized by its obsidian black luster that he got too close for comfort].
- **8091**: He fought back as best he could, but [was disarrrmed by a swipe of the fiend's jagged horns/his blade bounced harrrmlessly off the fiend's round shell/the fiend danced clear out of rrrange on its four bony legs/his blade shattered in pieces against the fiend's flat, sturrrdy jaw].
- **8092**: That's all I've got for ya. Need to hear it again?
- **8093**: Wonderful! You're a rrreal lifesaver. Tell Chumimi not to work too hard, 'kay?
- **8094**: Before the cataclysm, I was just a humble apothecary--now I'm serrrvin' on the front lines, fightin' for my life. I should be proud of myself, but deep down, it just doesn't feel right...

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

### Event 324

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 1D 01 80 23 21 00      ...........#!. 
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(20* ticks)
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=8094*)
    → "Before the cataclysm, I was just a humble apothecary--now I'm serrrvin' on the front lines, fightin' for my life. I should be proud of myself, but deep down, it just doesn't feel right..."
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x21] END_EVENT
  5: 0x000E [0x00] END_REQSTACK()
```

### Event 321

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000F    |
| Data Size    | 132 bytes |
| Instructions | 37        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               03                 .
0010: 00 00 02 10 03 01 00 03  10 03 02 00 04 10 20 01  .............. .
0020: 42 1E F0 FF FF 7F 1C 00  80 1D 02 80 23 03 02 10  B...........#...
0030: 00 00 1D 03 80 23 03 02  10 02 00 02 01 00 04 80  .....#..........
0040: 80 4A 00 1D 05 80 23 01  68 00 02 01 00 06 80 80  .J....#.h.......
0050: 59 00 1D 07 80 23 01 68  00 02 01 00 08 80 80 68  Y....#.h.......h
0060: 00 1D 09 80 23 01 68 00  1D 0A 80 23 24 0B 80 04  ....#.h....#$...
0070: 80 04 80 25 02 00 10 04  80 00 7F 00 01 8D 00 02  ...%............
0080: 00 10 06 80 00 8D 00 01  2D 00 01 8D 00 1D 0C 80  ........-.......
0090: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x000F [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0014 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x0019 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  3: 0x001E [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  4: 0x0020 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0021 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x0026 [0x1C] WAIT(20* ticks)
  7: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=8087*)
    → "My report? Why, yes, it should be rrright-- Well, that's strange. It seems a fiend has devoured it. I suppose you'll just have to pass along my findings for me."
  8: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002D [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 10: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=8088*)
    → "I spoke with a recuperating soldier who was complaining of terrrible [chest pains/dizziness/headaches/ringing in the ears]."
 11: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0036 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
 13: 0x003B [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x004A
 14: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=8090*)
    → "[The beast was so extravagantly colored, he says he'll never forget the sight of it/The beast was so unremarkable in appearance, he almost didn't see it coming/So garishly colored was the fiend that it sent shivers up his spine/He was so hypnotized by its obsidian black luster that he got too close for comfort]."
 15: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0047 [0x01] GOTO 0x0068
 17: 0x004A [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0059
 18: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=8091*)
    → "He fought back as best he could, but [was disarrrmed by a swipe of the fiend's jagged horns/his blade bounced harrrmlessly off the fiend's round shell/the fiend danced clear out of rrrange on its four bony legs/his blade shattered in pieces against the fiend's flat, sturrrdy jaw]."
 19: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0056 [0x01] GOTO 0x0068
 21: 0x0059 [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x0068
 22: 0x0061 [0x1D] PRINT_EVENT_MESSAGE(message_id=8089*)
    → "It would seem that the fiend [swooped down from the sky to attack him/ambushed him when he was resting his legs at an oasis/jumped out from behind a shadowy rock when he was on patrol/burst forth from an odd hollow in the ground]."
 23: 0x0064 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0065 [0x01] GOTO 0x0068

SUBROUTINE_0068:
 25: 0x0068 [0x1D] PRINT_EVENT_MESSAGE(message_id=8092*)
    → "That's all I've got for ya. Need to hear it again?"
 26: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x006C [0x24] CREATE_DIALOG(message_id=8076*, default_option=0*, option_flags=0*)
    → "Hear the report again? [No need./Yes, please.]"
 28: 0x0073 [0x25] WAIT_DIALOG_SELECT()
 29: 0x0074 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x007F
 30: 0x007C [0x01] GOTO 0x008D
 31: 0x007F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x008D
 32: 0x0087 [0x01] GOTO 0x002D

SUBROUTINE_008D:
 33: 0x008D [0x1D] PRINT_EVENT_MESSAGE(message_id=8093*)
    → "Wonderful! You're a rrreal lifesaver. Tell Chumimi not to work too hard, 'kay?"
 34: 0x0090 [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x0091 [0x21] END_EVENT
 36: 0x0092 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x008A [0x01] GOTO 0x008D
```
