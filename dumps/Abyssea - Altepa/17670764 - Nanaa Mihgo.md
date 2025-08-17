# 17670764 - Nanaa Mihgo

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 224 bytes                  |
| Total Events     | 3                          |
| References Count | 18                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [347](#event-347)     | 0x0001       |     22 |             10 |
| [353](#event-353)     | 0x0017       |     99 |             33 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2084      |        8324 |
|       2 | 0x2085      |        8325 |
|       3 | 0x2086      |        8326 |
|       4 | 0x0019      |          25 |
|       5 | 0x2087      |        8327 |
|       6 | 0x2088      |        8328 |
|       7 | 0x0032      |          50 |
|       8 | 0x2089      |        8329 |
|       9 | 0x208A      |        8330 |
|      10 | 0x004B      |          75 |
|      11 | 0x208B      |        8331 |
|      12 | 0x208C      |        8332 |
|      13 | 0x0064      |         100 |
|      14 | 0x208D      |        8333 |
|      15 | 0x208E      |        8334 |
|      16 | 0x208F      |        8335 |
|      17 | 0x2090      |        8336 |

## String References

- **8324**: Who put me in charge of the Resistance here, you ask? Hmph! Is that any way to talk to your superrriors!?
- **8325**: Hey, it's a cat-eat-cat world here. A girrrl's gotta do what a girrrl's gotta do.
- **8326**: Besides, someone has to make those fiends pay for laying waste to all my hard-earrrned loot!
- **8327**: Grrrrrr! Those nasty critters have got us up against the rrropes!
- **8328**: Learrrn a thing or two from me and pick up the pace, will ya?
- **8329**: Things aren't as bad as they could be, but the fiends hold the upper hand. This is no time to be caught cat-nappin'!
- **8330**: What's with that look? You've never seen me this serious before? The Cat Burglar's always serious. The nerrrve of some people!
- **8331**: That's rrright! Look at 'em run away with their tails between their legs. Looks like we've got the upper hand.
- **8332**: You know what that means? It's time to slap 'em so silly that they never show their ugly mugs in these parrrts again. Now go get 'em!
- **8333**: Look at the fiends cowerrr at our feet! Almost makes me feel sorry for the poor things...okay, maybe not.
- **8334**: I'll make them pay for every last piece of gil they stole from me. Give 'em an extra dose of pain for me, will ya?
- **8335**: Ahaha! What's the matter, fiendies? Cat got yourrr tongue? How about that? We've completely silenced the enemy prrresence.
- **8336**: But I've seen those nasties come back too many times to rrrest easy. You'll want to keep on your guarrrd too, ya hear?

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

### Event 347

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 22 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 1D 01 80 23 1D 02 80   ...........#...
0010: 23 1D 03 80 23 21 00                              #...#!.         
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(20* ticks)
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=8324*)
    → "Who put me in charge of the Resistance here, you ask? Hmph! Is that any way to talk to your superrriors!?"
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=8325*)
    → "Hey, it's a cat-eat-cat world here. A girrrl's gotta do what a girrrl's gotta do."
  5: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=8326*)
    → "Besides, someone has to make those fiends pay for laying waste to all my hard-earrrned loot!"
  7: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0015 [0x21] END_EVENT
  9: 0x0016 [0x00] END_REQSTACK()
```

### Event 353

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 99 bytes |
| Instructions | 33       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      1E  F0 FF FF 7F 1C 00 80 03         .........
0020: 00 00 02 10 02 00 00 04  80 03 37 00 1D 05 80 23  ..........7....#
0030: 1D 06 80 23 01 78 00 02  00 00 07 80 03 4A 00 1D  ...#.x.......J..
0040: 08 80 23 1D 09 80 23 01  78 00 02 00 00 0A 80 03  ..#...#.x.......
0050: 5D 00 1D 0B 80 23 1D 0C  80 23 01 78 00 02 00 00  ]....#...#.x....
0060: 0D 80 03 70 00 1D 0E 80  23 1D 0F 80 23 01 78 00  ...p....#...#.x.
0070: 1D 10 80 23 1D 11 80 23  21 00                    ...#...#!.      
```

#### Opcodes

```
  0: 0x0017 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001C [0x1C] WAIT(20* ticks)
  2: 0x001F [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  3: 0x0024 [0x02] IF !(ExtData[1]->WorkLocal[0] >= 25*) GOTO 0x0037
  4: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=8327*)
    → "Grrrrrr! Those nasty critters have got us up against the rrropes!"
  5: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0030 [0x1D] PRINT_EVENT_MESSAGE(message_id=8328*)
    → "Learrrn a thing or two from me and pick up the pace, will ya?"
  7: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0034 [0x01] GOTO 0x0078
  9: 0x0037 [0x02] IF !(ExtData[1]->WorkLocal[0] >= 50*) GOTO 0x004A
 10: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=8329*)
    → "Things aren't as bad as they could be, but the fiends hold the upper hand. This is no time to be caught cat-nappin'!"
 11: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=8330*)
    → "What's with that look? You've never seen me this serious before? The Cat Burglar's always serious. The nerrrve of some people!"
 13: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0047 [0x01] GOTO 0x0078
 15: 0x004A [0x02] IF !(ExtData[1]->WorkLocal[0] >= 75*) GOTO 0x005D
 16: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=8331*)
    → "That's rrright! Look at 'em run away with their tails between their legs. Looks like we've got the upper hand."
 17: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=8332*)
    → "You know what that means? It's time to slap 'em so silly that they never show their ugly mugs in these parrrts again. Now go get 'em!"
 19: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x005A [0x01] GOTO 0x0078
 21: 0x005D [0x02] IF !(ExtData[1]->WorkLocal[0] >= 100*) GOTO 0x0070
 22: 0x0065 [0x1D] PRINT_EVENT_MESSAGE(message_id=8333*)
    → "Look at the fiends cowerrr at our feet! Almost makes me feel sorry for the poor things...okay, maybe not."
 23: 0x0068 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=8334*)
    → "I'll make them pay for every last piece of gil they stole from me. Give 'em an extra dose of pain for me, will ya?"
 25: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x006D [0x01] GOTO 0x0078
 27: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=8335*)
    → "Ahaha! What's the matter, fiendies? Cat got yourrr tongue? How about that? We've completely silenced the enemy prrresence."
 28: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x0074 [0x1D] PRINT_EVENT_MESSAGE(message_id=8336*)
    → "But I've seen those nasties come back too many times to rrrest easy. You'll want to keep on your guarrrd too, ya hear?"
 30: 0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0078:
 31: 0x0078 [0x21] END_EVENT
 32: 0x0079 [0x00] END_REQSTACK()
```
