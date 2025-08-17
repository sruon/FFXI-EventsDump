# 17752146 - Zabirego-Hajigo

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 500 bytes                 |
| Total Events     | 15                        |
| References Count | 24                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [614](#event-614)        | 0x0030       |     31 |             11 |
| [688](#event-688)        | 0x004F       |     31 |             11 |
| [689](#event-689)        | 0x006E       |     27 |              9 |
| [690](#event-690)        | 0x0089       |     27 |              9 |
| [691](#event-691)        | 0x00A4       |     27 |              9 |
| [692](#event-692)        | 0x00BF       |     27 |              9 |
| [693](#event-693)        | 0x00DA       |     27 |              9 |
| [694](#event-694)        | 0x00F5       |     27 |              9 |
| [695](#event-695)        | 0x0110       |     27 |              9 |
| [784](#event-784)        | 0x012B       |     27 |              9 |
| [638](#event-638)        | 0x0146       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x22C1      |        8897 |
|       3 | 0x22C2      |        8898 |
|       4 | 0x22C3      |        8899 |
|       5 | 0x23F9      |        9209 |
|       6 | 0x23FA      |        9210 |
|       7 | 0x23FB      |        9211 |
|       8 | 0x23FC      |        9212 |
|       9 | 0x23FD      |        9213 |
|      10 | 0x23FE      |        9214 |
|      11 | 0x23FF      |        9215 |
|      12 | 0x2400      |        9216 |
|      13 | 0x2401      |        9217 |
|      14 | 0x2402      |        9218 |
|      15 | 0x2403      |        9219 |
|      16 | 0x2404      |        9220 |
|      17 | 0x2405      |        9221 |
|      18 | 0x2406      |        9222 |
|      19 | 0x2407      |        9223 |
|      20 | 0x2586      |        9606 |
|      21 | 0x2587      |        9607 |
|      22 | 0x2408      |        9224 |
|      23 | 0x2409      |        9225 |

## String References

- **8897**: It took us twenty long years to restore our town, and just when we think we have it good, along come the rumors of war again...
- **8898**: Don't tell me we need to sacrifice the lives of so many mages...not to mention the innocent lives of our wee children...?
- **8899**: If it takes some tribute offerings to the Yagudo to avoid a full-blown war, then I'm happy to offer it to them.
- **9209**: <Player>? Hmm... Sorry, but I never heard that name before.
- **9210**: Try doing some missions for Windurst. Bust you britches, and everybody'll know who you are.
- **9211**: That's when the real work starts rolling in. People won't trust you unless you give them something to trust.
- **9212**: <Player>? Hmm... Now, was that the name of the...? No, that was some other [guy/lady].
- **9213**: Either way, you're still not making much of a name of yourself here yet. Hard work and perseverence--that's what's going to put you on the map.
- **9214**: Oh, you're the <Player> that people are starting to talk about. I've heard pretty good things about you.
- **9215**: Hard work and perseverence--those are the only things that'll put you on the map.
- **9216**: Why, if it isn't <Player>! I heard some guys talking about you over their dinners at the eatery last night.
- **9217**: They had nothing but good things to say about you. Keep up the good work!
- **9218**: Hello there, <Player>! There aren't many Windurstians who don't know that name.
- **9219**: We're all proud to have you on our side! Keep up the great work!
- **9220**: [Mister/Miss] <Player>! You'd have to be living in a hole somewhere not to have heard that name.
- **9221**: All the bards in the land are singing songs of your outstanding deeds. Keep up the extraordinary work!
- **9222**: [Mister/Miss] <Player>! There isn't a soul in all of Windurst that has yet to hear the tales of your feats.
- **9223**: Why, I remember when you were just a fledgling adventurer. It seems like just yesterday...
- **9224**: [Lord/Lady] <Player>! I am honored to have the hero of Windurst in my presence.
- **9225**: Every man and woman in the country knows by heart the tales of your courage. May the Goddess shine her light of grace upon you.
- **9606**: A day doesn't go by when I fail to hear a tale of your deeds.
- **9607**: I am proud to be a citizen of the same great country as [Sir/Lady] <Player>. Keep up the marvelous work!

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5E  69 64 6C 30 1C 01 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0027 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x002C [0x1C] WAIT(30* ticks)
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 614

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 31 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 79 00 52 E0 0E 01 F0 FF  FF 7F 1D 02 80 23 1D 03  y.R..........#..
0040: 80 23 1D 04 80 23 7B 52  E0 0E 01 20 00 21 00     .#...#{R... .!. 
```

#### Opcodes

```
  0: 0x0030 [0x79] Zabirego-Hajigo (ID: 17752146/0x010EE052) looks at LocalPlayer (Basic look)
  1: 0x003A [0x1D] PRINT_EVENT_MESSAGE(message_id=8897*)
    → "It took us twenty long years to restore our town, and just when we think we have it good, along come the rumors of war again..."
  2: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=8898*)
    → "Don't tell me we need to sacrifice the lives of so many mages...not to mention the innocent lives of our wee children...?"
  4: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=8899*)
    → "If it takes some tribute offerings to the Yagudo to avoid a full-blown war, then I'm happy to offer it to them."
  6: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0046 [0x7B] Zabirego-Hajigo (ID: 17752146/0x010EE052) stops talking
  8: 0x004B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x004D [0x21] END_EVENT
 10: 0x004E [0x00] END_REQSTACK()
```

### Event 688

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 31 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               79                 y
0050: 00 52 E0 0E 01 F0 FF FF  7F 1D 05 80 23 1D 06 80  .R..........#...
0060: 23 1D 07 80 23 7B 52 E0  0E 01 20 00 21 00        #...#{R... .!.  
```

#### Opcodes

```
  0: 0x004F [0x79] Zabirego-Hajigo (ID: 17752146/0x010EE052) looks at LocalPlayer (Basic look)
  1: 0x0059 [0x1D] PRINT_EVENT_MESSAGE(message_id=9209*)
    → "<Player>? Hmm... Sorry, but I never heard that name before."
  2: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x005D [0x1D] PRINT_EVENT_MESSAGE(message_id=9210*)
    → "Try doing some missions for Windurst. Bust you britches, and everybody'll know who you are."
  4: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0061 [0x1D] PRINT_EVENT_MESSAGE(message_id=9211*)
    → "That's when the real work starts rolling in. People won't trust you unless you give them something to trust."
  6: 0x0064 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0065 [0x7B] Zabirego-Hajigo (ID: 17752146/0x010EE052) stops talking
  8: 0x006A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x006C [0x21] END_EVENT
 10: 0x006D [0x00] END_REQSTACK()
```

### Event 689

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            79 00                y.
0070: 52 E0 0E 01 F0 FF FF 7F  1D 08 80 23 1D 09 80 23  R..........#...#
0080: 7B 52 E0 0E 01 20 00 21  00                       {R... .!.       
```

#### Opcodes

```
  0: 0x006E [0x79] Zabirego-Hajigo (ID: 17752146/0x010EE052) looks at LocalPlayer (Basic look)
  1: 0x0078 [0x1D] PRINT_EVENT_MESSAGE(message_id=9212*)
    → "<Player>? Hmm... Now, was that the name of the...? No, that was some other [guy/lady]."
  2: 0x007B [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x007C [0x1D] PRINT_EVENT_MESSAGE(message_id=9213*)
    → "Either way, you're still not making much of a name of yourself here yet. Hard work and perseverence--that's what's going to put you on the map."
  4: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0080 [0x7B] Zabirego-Hajigo (ID: 17752146/0x010EE052) stops talking
  6: 0x0085 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x0087 [0x21] END_EVENT
  8: 0x0088 [0x00] END_REQSTACK()
```

### Event 690

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             79 00 52 E0 0E 01 F0           y.R....
0090: FF FF 7F 1D 0A 80 23 1D  0B 80 23 7B 52 E0 0E 01  ......#...#{R...
00A0: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0089 [0x79] Zabirego-Hajigo (ID: 17752146/0x010EE052) looks at LocalPlayer (Basic look)
  1: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=9214*)
    → "Oh, you're the <Player> that people are starting to talk about. I've heard pretty good things about you."
  2: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0097 [0x1D] PRINT_EVENT_MESSAGE(message_id=9215*)
    → "Hard work and perseverence--those are the only things that'll put you on the map."
  4: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x009B [0x7B] Zabirego-Hajigo (ID: 17752146/0x010EE052) stops talking
  6: 0x00A0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x00A2 [0x21] END_EVENT
  8: 0x00A3 [0x00] END_REQSTACK()
```

### Event 691

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             79 00 52 E0  0E 01 F0 FF FF 7F 1D 0C      y.R.........
00B0: 80 23 1D 0D 80 23 7B 52  E0 0E 01 20 00 21 00     .#...#{R... .!. 
```

#### Opcodes

```
  0: 0x00A4 [0x79] Zabirego-Hajigo (ID: 17752146/0x010EE052) looks at LocalPlayer (Basic look)
  1: 0x00AE [0x1D] PRINT_EVENT_MESSAGE(message_id=9216*)
    → "Why, if it isn't <Player>! I heard some guys talking about you over their dinners at the eatery last night."
  2: 0x00B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B2 [0x1D] PRINT_EVENT_MESSAGE(message_id=9217*)
    → "They had nothing but good things to say about you. Keep up the good work!"
  4: 0x00B5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00B6 [0x7B] Zabirego-Hajigo (ID: 17752146/0x010EE052) stops talking
  6: 0x00BB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x00BD [0x21] END_EVENT
  8: 0x00BE [0x00] END_REQSTACK()
```

### Event 692

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               79                 y
00C0: 00 52 E0 0E 01 F0 FF FF  7F 1D 0E 80 23 1D 0F 80  .R..........#...
00D0: 23 7B 52 E0 0E 01 20 00  21 00                    #{R... .!.      
```

#### Opcodes

```
  0: 0x00BF [0x79] Zabirego-Hajigo (ID: 17752146/0x010EE052) looks at LocalPlayer (Basic look)
  1: 0x00C9 [0x1D] PRINT_EVENT_MESSAGE(message_id=9218*)
    → "Hello there, <Player>! There aren't many Windurstians who don't know that name."
  2: 0x00CC [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00CD [0x1D] PRINT_EVENT_MESSAGE(message_id=9219*)
    → "We're all proud to have you on our side! Keep up the great work!"
  4: 0x00D0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00D1 [0x7B] Zabirego-Hajigo (ID: 17752146/0x010EE052) stops talking
  6: 0x00D6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x00D8 [0x21] END_EVENT
  8: 0x00D9 [0x00] END_REQSTACK()
```

### Event 693

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DA   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                79 00 52 E0 0E 01            y.R...
00E0: F0 FF FF 7F 1D 10 80 23  1D 11 80 23 7B 52 E0 0E  .......#...#{R..
00F0: 01 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x00DA [0x79] Zabirego-Hajigo (ID: 17752146/0x010EE052) looks at LocalPlayer (Basic look)
  1: 0x00E4 [0x1D] PRINT_EVENT_MESSAGE(message_id=9220*)
    → "[Mister/Miss] <Player>! You'd have to be living in a hole somewhere not to have heard that name."
  2: 0x00E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00E8 [0x1D] PRINT_EVENT_MESSAGE(message_id=9221*)
    → "All the bards in the land are singing songs of your outstanding deeds. Keep up the extraordinary work!"
  4: 0x00EB [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00EC [0x7B] Zabirego-Hajigo (ID: 17752146/0x010EE052) stops talking
  6: 0x00F1 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x00F3 [0x21] END_EVENT
  8: 0x00F4 [0x00] END_REQSTACK()
```

### Event 694

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                79 00 52  E0 0E 01 F0 FF FF 7F 1D       y.R........
0100: 12 80 23 1D 13 80 23 7B  52 E0 0E 01 20 00 21 00  ..#...#{R... .!.
```

#### Opcodes

```
  0: 0x00F5 [0x79] Zabirego-Hajigo (ID: 17752146/0x010EE052) looks at LocalPlayer (Basic look)
  1: 0x00FF [0x1D] PRINT_EVENT_MESSAGE(message_id=9222*)
    → "[Mister/Miss] <Player>! There isn't a soul in all of Windurst that has yet to hear the tales of your feats."
  2: 0x0102 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0103 [0x1D] PRINT_EVENT_MESSAGE(message_id=9223*)
    → "Why, I remember when you were just a fledgling adventurer. It seems like just yesterday..."
  4: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0107 [0x7B] Zabirego-Hajigo (ID: 17752146/0x010EE052) stops talking
  6: 0x010C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x010E [0x21] END_EVENT
  8: 0x010F [0x00] END_REQSTACK()
```

### Event 695

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0110   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110: 79 00 52 E0 0E 01 F0 FF  FF 7F 1D 14 80 23 1D 15  y.R..........#..
0120: 80 23 7B 52 E0 0E 01 20  00 21 00                 .#{R... .!.     
```

#### Opcodes

```
  0: 0x0110 [0x79] Zabirego-Hajigo (ID: 17752146/0x010EE052) looks at LocalPlayer (Basic look)
  1: 0x011A [0x1D] PRINT_EVENT_MESSAGE(message_id=9606*)
    → "A day doesn't go by when I fail to hear a tale of your deeds."
  2: 0x011D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x011E [0x1D] PRINT_EVENT_MESSAGE(message_id=9607*)
    → "I am proud to be a citizen of the same great country as [Sir/Lady] <Player>. Keep up the marvelous work!"
  4: 0x0121 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0122 [0x7B] Zabirego-Hajigo (ID: 17752146/0x010EE052) stops talking
  6: 0x0127 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x0129 [0x21] END_EVENT
  8: 0x012A [0x00] END_REQSTACK()
```

### Event 784

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012B   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   79 00 52 E0 0E             y.R..
0130: 01 F0 FF FF 7F 1D 16 80  23 1D 17 80 23 7B 52 E0  ........#...#{R.
0140: 0E 01 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x012B [0x79] Zabirego-Hajigo (ID: 17752146/0x010EE052) looks at LocalPlayer (Basic look)
  1: 0x0135 [0x1D] PRINT_EVENT_MESSAGE(message_id=9224*)
    → "[Lord/Lady] <Player>! I am honored to have the hero of Windurst in my presence."
  2: 0x0138 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0139 [0x1D] PRINT_EVENT_MESSAGE(message_id=9225*)
    → "Every man and woman in the country knows by heart the tales of your courage. May the Goddess shine her light of grace upon you."
  4: 0x013C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x013D [0x7B] Zabirego-Hajigo (ID: 17752146/0x010EE052) stops talking
  6: 0x0142 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x0144 [0x21] END_EVENT
  8: 0x0145 [0x00] END_REQSTACK()
```

### Event 638

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0146  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                   00                                    .         
```

#### Opcodes

```
  0: 0x0146 [0x00] END_REQSTACK()
```
