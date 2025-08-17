# 17719610 - Atelloune

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 864 bytes                     |
| Total Events     | 6                             |
| References Count | 46                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [884](#event-884)     | 0x0001       |     87 |             17 |
| [890](#event-890)     | 0x0058       |    199 |             46 |
| [891](#event-891)     | 0x011F       |    216 |             47 |
| [892](#event-892)     | 0x01F7       |     79 |             16 |
| [3519](#event-3519)   | 0x0246       |     55 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x344C      |       13388 |
|       2 | 0x344D      |       13389 |
|       3 | 0x344E      |       13390 |
|       4 | 0x344F      |       13391 |
|       5 | 0x3450      |       13392 |
|       6 | 0x09CA      |        2506 |
|       7 | 0x3456      |       13398 |
|       8 | 0x3457      |       13399 |
|       9 | 0x3458      |       13400 |
|      10 | 0x3459      |       13401 |
|      11 | 0x345A      |       13402 |
|      12 | 0x345B      |       13403 |
|      13 | 0x345C      |       13404 |
|      14 | 0x345D      |       13405 |
|      15 | 0x345E      |       13406 |
|      16 | 0x345F      |       13407 |
|      17 | 0x3460      |       13408 |
|      18 | 0x3461      |       13409 |
|      19 | 0x3462      |       13410 |
|      20 | 0x3463      |       13411 |
|      21 | 0x3464      |       13412 |
|      22 | 0x3465      |       13413 |
|      23 | 0x3466      |       13414 |
|      24 | 0x3467      |       13415 |
|      25 | 0x3468      |       13416 |
|      26 | 0x3469      |       13417 |
|      27 | 0x346A      |       13418 |
|      28 | 0x346B      |       13419 |
|      29 | 0x346C      |       13420 |
|      30 | 0x346D      |       13421 |
|      31 | 0x346E      |       13422 |
|      32 | 0x346F      |       13423 |
|      33 | 0x3470      |       13424 |
|      34 | 0x3471      |       13425 |
|      35 | 0x3472      |       13426 |
|      36 | 0x3473      |       13427 |
|      37 | 0x3474      |       13428 |
|      38 | 0x3475      |       13429 |
|      39 | 0x3476      |       13430 |
|      40 | 0x3477      |       13431 |
|      41 | 0x3478      |       13432 |
|      42 | 0x3479      |       13433 |
|      43 | 0x00C9      |         201 |
|      44 | 0x0000      |           0 |
|      45 | 0x3CE2      |       15586 |

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

### Event 884

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 87 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A 3A 61 0E 01 F0 FF  FF 7F 6F 76 3A 61 0E 01   J:a......ov:a..
0010: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 2B  f..........tlk0+
0020: 3A 61 0E 01 01 80 23 2B  3A 61 0E 01 02 80 23 2B  :a....#+:a....#+
0030: 3A 61 0E 01 03 80 23 2B  3A 61 0E 01 04 80 23 2B  :a....#+:a....#+
0040: 3A 61 0E 01 05 80 23 66  00 80 F8 FF FF 7F F8 FF  :a....#f........
0050: FF 7F 74 6C 6B 31 21 00                           ..tlk1!.        
```

#### Opcodes

```
  0: 0x0001 [0x4A] Atelloune (ID: 17719610/0x010E613A) looks at LocalPlayer
  1: 0x000A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x000B [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Atelloune (ID: 17719610/0x010E613A) Render.Flags0 and Render.Flags3 conditions are met
  3: 0x0010 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x001F [0x2B] Atelloune (ID: 17719610/0x010E613A) [13388*]:
    → "Hey! You there! Adventurer! Have you ever happened to see a sandworm? You know, gigantic worm, segmented body, lives in the sand?"
  5: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0027 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13389*]:
    → "Well...hmmm... Oh! Then how about a ladybug? They're distinctive little pests with bright red, semicircular bodies, three distinctive black spots and..."
  7: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x002F [0x2B] Atelloune (ID: 17719610/0x010E613A) [13390*]:
    → "I apologize, I've gone and totally forgotten my manners! You must excuse me. It's a pleasure to make your acquaintance. I'm Atelloune, assistant to renowned biologist Professor Clauvert B Chanoix."
  9: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0037 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13391*]:
    → "To help with the professor's research, I'm searching for all kinds of specimens from Quon and Mindartia whose numbers have been dwindling in recent years."
 11: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x003F [0x2B] Atelloune (ID: 17719610/0x010E613A) [13392*]:
    → "I just thought that an adventurer such as yourself had surely seen some rare creatures on your travels...but never mind. I'm sorry for disturbing you."
 13: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0047 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=30*
 15: 0x0056 [0x21] END_EVENT
 16: 0x0057 [0x00] END_REQSTACK()
```

### Event 890

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0058    |
| Data Size    | 199 bytes |
| Instructions | 46        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          20 01 42 03 02 10 06 80           .B.....
0060: 4A 3A 61 0E 01 F0 FF FF  7F 6F 76 3A 61 0E 01 66  J:a......ov:a..f
0070: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 2B 3A  ..........tlk0+:
0080: 61 0E 01 07 80 23 2B 3A  61 0E 01 08 80 23 2B 3A  a....#+:a....#+:
0090: 61 0E 01 09 80 23 2B 3A  61 0E 01 0A 80 23 2B 3A  a....#+:a....#+:
00A0: 61 0E 01 0B 80 23 2B 3A  61 0E 01 0C 80 23 2B 3A  a....#+:a....#+:
00B0: 61 0E 01 0D 80 23 2B 3A  61 0E 01 0E 80 23 2B 3A  a....#+:a....#+:
00C0: 61 0E 01 0F 80 23 2B 3A  61 0E 01 10 80 23 2B 3A  a....#+:a....#+:
00D0: 61 0E 01 11 80 23 2B 3A  61 0E 01 12 80 23 2B 3A  a....#+:a....#+:
00E0: 61 0E 01 13 80 23 2B 3A  61 0E 01 14 80 23 2B 3A  a....#+:a....#+:
00F0: 61 0E 01 15 80 23 2B 3A  61 0E 01 16 80 23 2B 3A  a....#+:a....#+:
0100: 61 0E 01 17 80 23 2B 3A  61 0E 01 18 80 23 66 00  a....#+:a....#f.
0110: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 31 21 00     .........tlk1!. 
```

#### Opcodes

```
  0: 0x0058 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x005A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x005B [0x03] Work_Zone[2] = 2506*
  3: 0x0060 [0x4A] Atelloune (ID: 17719610/0x010E613A) looks at LocalPlayer
  4: 0x0069 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x006A [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Atelloune (ID: 17719610/0x010E613A) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x006F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  7: 0x007E [0x2B] Atelloune (ID: 17719610/0x010E613A) [13398*]:
    → "Hello, there. Say, if you have some time would you mind lending me an ear? I've got a bit of a problem..."
  8: 0x0085 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0086 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13399*]:
    → "Well, I'm not sure if you already knew or not, but I'm Atelloune, assistant to the great zoologist, Professor Clavauert B Chanoix."
 10: 0x008D [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x008E [0x2B] Atelloune (ID: 17719610/0x010E613A) [13400*]:
    → "I get a lot of mail in my line of work. You know, letters from people of all ages who are passionate about animals, asking me all sorts of questions."
 12: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0096 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13401*]:
    → "I recently came across a letter whose squiggly handwriting caught my eye."
 14: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x009E [0x2B] Atelloune (ID: 17719610/0x010E613A) [13402*]:
    → "It was sent by a young Elvaan boy who didn't give his name."
 16: 0x00A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x00A6 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13403*]:
    → ""Dear Atelloune, my grandpa says that when he was my age there were big, red, round bugs in Ronfaure."
 18: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x00AE [0x2B] Atelloune (ID: 17719610/0x010E613A) [13404*]:
    → ""But I think he's going senile, and is just thinking of an apple. Either that or a liar, and there were never any bugs like that. Please tell him he's crazy.""
 20: 0x00B5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x00B6 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13405*]:
    → "...Hmmm."
 22: 0x00BD [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x00BE [0x2B] Atelloune (ID: 17719610/0x010E613A) [13406*]:
    → "I really am sorry to bother you with this."
 24: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x00C6 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13407*]:
    → "It's just that this kid really struck a nerve with me. I mean, there isn't even a question! So irritating..."
 26: 0x00CD [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x00CE [0x2B] Atelloune (ID: 17719610/0x010E613A) [13408*]:
    → "I'm thinking that what he is referring to may be the ladybug. It was a species of vermin which inhabited the Ronfaure region before the war."
 28: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x00D6 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13409*]:
    → "You know, when I was just a little girl I mistook them for app--"
 30: 0x00DD [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x00DE [0x2B] Atelloune (ID: 17719610/0x010E613A) [13410*]:
    → "Never mind that!"
 32: 0x00E5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x00E6 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13411*]:
    → "Let's focus on the real problem here. The ladybug supposedly went extinct a long time ago."
 34: 0x00ED [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x00EE [0x2B] Atelloune (ID: 17719610/0x010E613A) [13412*]:
    → "But here's where it gets really interesting!"
 36: 0x00F5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x00F6 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13413*]:
    → "I believe that there must still be some ladybugs out there somewhere in Vana'diel! If you ever happen to see one in your travels, please try and bring me back a live specimen!"
 38: 0x00FD [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x00FE [0x2B] Atelloune (ID: 17719610/0x010E613A) [13414*]:
    → "Wait...that's going to be tough. They're actually quite large animals. And I wouldn't want to harm them... Well, if you ever chance upon the corpse of one do you think you could bring back the $0 for me? You'll know them when you see them. That's all I need."
 40: 0x0105 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x0106 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13415*]:
    → "I'd reeeally like to blow this brat's mind. And I think that would do just the trick."
 42: 0x010D [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x010E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=30*
 44: 0x011D [0x21] END_EVENT
 45: 0x011E [0x00] END_REQSTACK()
```

### Event 891

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x011F    |
| Data Size    | 216 bytes |
| Instructions | 47        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                               20                  
0120: 01 42 03 02 10 06 80 4A  3A 61 0E 01 F0 FF FF 7F  .B.....J:a......
0130: 6F 76 3A 61 0E 01 66 00  80 F8 FF FF 7F F8 FF FF  ov:a..f.........
0140: 7F 74 6C 6B 30 2B 3A 61  0E 01 19 80 23 2B 3A 61  .tlk0+:a....#+:a
0150: 0E 01 1A 80 23 2B 3A 61  0E 01 1B 80 23 2B 3A 61  ....#+:a....#+:a
0160: 0E 01 1C 80 23 2B 3A 61  0E 01 1D 80 23 2B 3A 61  ....#+:a....#+:a
0170: 0E 01 1E 80 23 2B 3A 61  0E 01 1F 80 23 2B 3A 61  ....#+:a....#+:a
0180: 0E 01 20 80 23 2B 3A 61  0E 01 21 80 23 2B 3A 61  .. .#+:a..!.#+:a
0190: 0E 01 22 80 23 2B 3A 61  0E 01 23 80 23 2B 3A 61  ..".#+:a..#.#+:a
01A0: 0E 01 24 80 23 2B 3A 61  0E 01 25 80 23 2B 3A 61  ..$.#+:a..%.#+:a
01B0: 0E 01 26 80 23 2B 3A 61  0E 01 27 80 23 2B 3A 61  ..&.#+:a..'.#+:a
01C0: 0E 01 28 80 23 2B 3A 61  0E 01 29 80 23 2B 3A 61  ..(.#+:a..).#+:a
01D0: 0E 01 2A 80 23 66 00 80  F8 FF FF 7F F8 FF FF 7F  ..*.#f..........
01E0: 74 6C 6B 31 45 2B 80 F8  FF FF 7F F8 FF FF 7F 71  tlk1E+.........q
01F0: 73 74 63 2C 80 21 00                              stc,.!.         
```

#### Opcodes

```
  0: 0x011F [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0121 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0122 [0x03] Work_Zone[2] = 2506*
  3: 0x0127 [0x4A] Atelloune (ID: 17719610/0x010E613A) looks at LocalPlayer
  4: 0x0130 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0131 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Atelloune (ID: 17719610/0x010E613A) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0136 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  7: 0x0145 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13416*]:
    → "Oh my! Is this really $0!?"
  8: 0x014C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x014D [0x2B] Atelloune (ID: 17719610/0x010E613A) [13417*]:
    → "Wow, it's even more beautiful than I imagined. Such brilliance! And this contrast between the red and black... Absolutely remarkable!"
 10: 0x0154 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0155 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13418*]:
    → "Where did you find this!?"
 12: 0x015C [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x015D [0x2B] Atelloune (ID: 17719610/0x010E613A) [13419*]:
    → "Ahhh, playing your cards tight to the vest, eh? That's fine, suit yourself."
 14: 0x0164 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0165 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13420*]:
    → "It doesn't matter. This is exactly what I need to make a believer out of that little Elvaan brat. Maybe now he'll recognize the true beauty of the ladybug!"
 16: 0x016C [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x016D [0x2B] Atelloune (ID: 17719610/0x010E613A) [13421*]:
    → "To think of that poor grandfather, being called a liar by his own grandchild! Well, this should help him sleep at night."
 18: 0x0174 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0175 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13422*]:
    → "I must say, it's all thanks to you. I'll tell you what. In return, I'll let you in on a little secret..."
 20: 0x017C [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x017D [0x2B] Atelloune (ID: 17719610/0x010E613A) [13423*]:
    → "The real reason why the ladybugs went extinct..."
 22: 0x0184 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x0185 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13424*]:
    → "To be honest, not even the most esteemed minds in the ecological field could explain why it happened. But I've come across some...other information."
 24: 0x018C [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x018D [0x2B] Atelloune (ID: 17719610/0x010E613A) [13425*]:
    → "Rumor has it that right around the time of the Great War the ladybugs were overhunted to extinction by an inconsiderate people with no regard for the natural balance."
 26: 0x0194 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0195 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13426*]:
    → "They were described as seemingly possessed, an eerie and ominous group. Obsessed with the red and black colors of the ladybug, which they could constantly be heard murmuring, as if in a trance. "Red...black...""
 28: 0x019C [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x019D [0x2B] Atelloune (ID: 17719610/0x010E613A) [13427*]:
    → "There's no doubt in my mind that these wings were in high demand for some reason or another back then."
 30: 0x01A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x01A5 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13428*]:
    → "For example, perhaps some military strategists thought up an application for this characteristic design which so effectively startles predators."
 32: 0x01AC [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x01AD [0x2B] Atelloune (ID: 17719610/0x010E613A) [13429*]:
    → "The possibilities are endless!"
 34: 0x01B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x01B5 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13430*]:
    → "..."
 36: 0x01BC [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x01BD [0x2B] Atelloune (ID: 17719610/0x010E613A) [13431*]:
    → "What? Why are you looking at me like that?"
 38: 0x01C4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x01C5 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13432*]:
    → "Don't misunderstand. I'll see to it that these wings make their way to that little Elvaan boy...just as soon as I run some tests of my own!"
 40: 0x01CC [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x01CD [0x2B] Atelloune (ID: 17719610/0x010E613A) [13433*]:
    → "Here, now take this and be on your way. And no dropping in unannounced! I have work to do..."
 42: 0x01D4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x01D5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=30*
 44: 0x01E4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 45: 0x01F5 [0x21] END_EVENT
 46: 0x01F6 [0x00] END_REQSTACK()
```

### Event 892

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F7   |
| Data Size    | 79 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                      20  01 42 4A 3A 61 0E 01 F0          .BJ:a...
0200: FF FF 7F 6F 76 3A 61 0E  01 03 02 10 06 80 66 00  ...ov:a.......f.
0210: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 2B 3A 61  .........tlk0+:a
0220: 0E 01 16 80 23 2B 3A 61  0E 01 17 80 23 2B 3A 61  ....#+:a....#+:a
0230: 0E 01 18 80 23 66 00 80  F8 FF FF 7F F8 FF FF 7F  ....#f..........
0240: 74 6C 6B 31 21 00                                 tlk1!.          
```

#### Opcodes

```
  0: 0x01F7 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x01F9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x01FA [0x4A] Atelloune (ID: 17719610/0x010E613A) looks at LocalPlayer
  3: 0x0203 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0204 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Atelloune (ID: 17719610/0x010E613A) Render.Flags0 and Render.Flags3 conditions are met
  5: 0x0209 [0x03] Work_Zone[2] = 2506*
  6: 0x020E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  7: 0x021D [0x2B] Atelloune (ID: 17719610/0x010E613A) [13413*]:
    → "I believe that there must still be some ladybugs out there somewhere in Vana'diel! If you ever happen to see one in your travels, please try and bring me back a live specimen!"
  8: 0x0224 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0225 [0x2B] Atelloune (ID: 17719610/0x010E613A) [13414*]:
    → "Wait...that's going to be tough. They're actually quite large animals. And I wouldn't want to harm them... Well, if you ever chance upon the corpse of one do you think you could bring back the $0 for me? You'll know them when you see them. That's all I need."
 10: 0x022C [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x022D [0x2B] Atelloune (ID: 17719610/0x010E613A) [13415*]:
    → "I'd reeeally like to blow this brat's mind. And I think that would do just the trick."
 12: 0x0234 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0235 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=30*
 14: 0x0244 [0x21] END_EVENT
 15: 0x0245 [0x00] END_REQSTACK()
```

### Event 3519

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0246   |
| Data Size    | 55 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                   4A 3A  61 0E 01 F0 FF FF 7F 6F        J:a......o
0250: 76 3A 61 0E 01 66 00 80  F8 FF FF 7F F8 FF FF 7F  v:a..f..........
0260: 74 6C 6B 30 2B 3A 61 0E  01 2D 80 23 66 00 80 F8  tlk0+:a..-.#f...
0270: FF FF 7F F8 FF FF 7F 74  6C 6B 31 21 00           .......tlk1!.   
```

#### Opcodes

```
  0: 0x0246 [0x4A] Atelloune (ID: 17719610/0x010E613A) looks at LocalPlayer
  1: 0x024F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0250 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Atelloune (ID: 17719610/0x010E613A) Render.Flags0 and Render.Flags3 conditions are met
  3: 0x0255 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0264 [0x2B] Atelloune (ID: 17719610/0x010E613A) [15586*]:
    → "Never in my wildest dreams did I expect to find obscure crabs in someone's Mog Garden. I must make preparations for a survey this instant."
  5: 0x026B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x026C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=30*
  7: 0x027B [0x21] END_EVENT
  8: 0x027C [0x00] END_REQSTACK()
```
