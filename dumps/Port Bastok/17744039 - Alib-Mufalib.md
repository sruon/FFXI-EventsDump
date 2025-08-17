# 17744039 - Alib-Mufalib

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 708 bytes             |
| Total Events     | 9                     |
| References Count | 36                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [357](#event-357)     | 0x0001       |    140 |             32 |
| [358](#event-358)     | 0x008D       |     14 |              6 |
| [359](#event-359)     | 0x009B       |     49 |              9 |
| [360](#event-360)     | 0x00CC       |     93 |             17 |
| [361](#event-361)     | 0x0129       |     14 |              6 |
| [378](#event-378)     | 0x0137       |     95 |             21 |
| [379](#event-379)     | 0x0196       |    102 |             17 |
| [443](#event-443)     | 0x01FC       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2711      |       10001 |
|       2 | 0x2712      |       10002 |
|       3 | 0x0000      |           0 |
|       4 | 0x0028      |          40 |
|       5 | 0x2713      |       10003 |
|       6 | 0x0001      |           1 |
|       7 | 0x2714      |       10004 |
|       8 | 0x02E8      |         744 |
|       9 | 0x2715      |       10005 |
|      10 | 0x003C      |          60 |
|      11 | 0x2716      |       10006 |
|      12 | 0x2717      |       10007 |
|      13 | 0x2718      |       10008 |
|      14 | 0x2719      |       10009 |
|      15 | 0x271A      |       10010 |
|      16 | 0x271B      |       10011 |
|      17 | 0x271C      |       10012 |
|      18 | 0x271D      |       10013 |
|      19 | 0x271E      |       10014 |
|      20 | 0x271F      |       10015 |
|      21 | 0x00C9      |         201 |
|      22 | 0x2721      |       10017 |
|      23 | 0x002D      |          45 |
|      24 | 0x0020      |          32 |
|      25 | 0x3174      |       12660 |
|      26 | 0x0006      |           6 |
|      27 | 0x3175      |       12661 |
|      28 | 0x3176      |       12662 |
|      29 | 0x012C      |         300 |
|      30 | 0x3177      |       12663 |
|      31 | 0x3178      |       12664 |
|      32 | 0x3179      |       12665 |
|      33 | 0x007A      |         122 |
|      34 | 0x0104      |         260 |
|      35 | 0x00C8      |         200 |

## String References

- **10001**: Wait... Would you happen to be one of those "adventurers"?
- **10002**: Well, are you? [Yes, and proud of it!/I know you are but what am I!?]
- **10003**: Well then, I shall entrust you with this!
- **10004**: It seems I was mistaken. Oh well, I have plenty of these to spare. Take one anyway.
- **10005**: <Player> obtains $6!
- **10006**: You would like to know more about the badge, would you? Well, do you see how it is shaped like a wildcat's head? That is our company emblem. Go ahead--put it on. It won't hurt you.
- **10007**: You want to know more? Quite the bother, aren't you? Our company, "Salaheem's Sentinels," is the largest, most prestigious, and esteemed establishment in Vana'diel!
- **10008**: We have even been sanctioned by the mighty Empire of Aht Urhgan! Alright... To put it in words you might understand, we are mercenaries.
- **10009**: And...! We are currently recruiting new members! Therefore, it would be much appreciated if you could show that badge to others in this town. A bit of advertising would really help us out.
- **10010**: Oh, hello. It seems that the number of people interested in our organization has begun to increase.
- **10011**: Your $3 was created using advanced alchemy techniques. It will shine brightly near people whose thoughts are currently drifting across the vast sea towards the golden fields of Aht Urhgan.
- **10012**: Oh, it's you! Many people have expressed interest in Salaheem's Sentinels!
- **10013**: It looks like your $3 has lost its luster, so I will take it back now.
- **10014**: <Player> hands over the $3.
- **10015**: I will give you this in its place. If you ever go to Aht Urhgan, please stop by Salaheem's Sentinels.
- **10017**: Remember to visit Salaheem's Sentinels in Al Zahbi the next time you visit the Empire of Aht Urhgan!
- **12660**: That look in your eyes... I sense the fear of one frightful femme fatale flowing forth from your soul... Don't tell me... You're one of Salaheem's Sentinels!
- **12661**: Which means, I am allowed to provide you with this special offer!
- **12662**: For a small fee, I can teleport you directly to Aht Urhgan Whitegate!
- **12663**: Simply trade me $0 gil, and you'll be sipping chai with [mysterious veiled beauties/bronzed, battle-hardened warriors] before the hour is up.
- **12664**: Thank you very much, [sir/ma'am].
- **12665**: Now let us be off!

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

### Event 357

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 140 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 1C  00 80 1D 01 80 23 24 02   B...........#$.
0010: 80 03 80 03 80 25 02 00  10 03 80 00 34 00 66 04  .....%......4.f.
0020: 80 F8 FF FF 7F F8 FF FF  7F 70 61 73 30 1D 05 80  .........pas0...
0030: 23 01 52 00 02 00 10 06  80 00 52 00 66 04 80 F8  #.R.......R.f...
0040: FF FF 7F F8 FF FF 7F 70  61 73 30 1D 07 80 23 01  .......pas0...#.
0050: 52 00 03 02 10 08 80 48  09 80 1C 0A 80 1D 0B 80  R......H........
0060: 23 66 04 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  #f..........tlk0
0070: 1D 0C 80 23 1D 0D 80 23  66 04 80 F8 FF FF 7F F8  ...#...#f.......
0080: FF FF 7F 74 6C 6B 31 1D  0E 80 23 21 00           ...tlk1...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x1C] WAIT(30* ticks)
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=10001*)
    → "Wait... Would you happen to be one of those "adventurers"?"
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x24] CREATE_DIALOG(message_id=10002*, default_option=0*, option_flags=0*)
    → "Well, are you? [Yes, and proud of it!/I know you are but what am I!?]"
  6: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0034
  8: 0x001E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=40*
  9: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=10003*)
    → "Well then, I shall entrust you with this!"
 10: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0031 [0x01] GOTO 0x0052
 12: 0x0034 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0052
 13: 0x003C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=40*
 14: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=10004*)
    → "It seems I was mistaken. Oh well, I have plenty of these to spare. Take one anyway."
 15: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x004F [0x01] GOTO 0x0052

SUBROUTINE_0052:
 17: 0x0052 [0x03] Work_Zone[2] = 744*
 18: 0x0057 [0x48] [System] [10005*]:
    → "<Player> obtains $6!"
 19: 0x005A [0x1C] WAIT(60* ticks)
 20: 0x005D [0x1D] PRINT_EVENT_MESSAGE(message_id=10006*)
    → "You would like to know more about the badge, would you? Well, do you see how it is shaped like a wildcat's head? That is our company emblem. Go ahead--put it on. It won't hurt you."
 21: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0061 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
 23: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=10007*)
    → "You want to know more? Quite the bother, aren't you? Our company, "Salaheem's Sentinels," is the largest, most prestigious, and esteemed establishment in Vana'diel!"
 24: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0074 [0x1D] PRINT_EVENT_MESSAGE(message_id=10008*)
    → "We have even been sanctioned by the mighty Empire of Aht Urhgan! Alright... To put it in words you might understand, we are mercenaries."
 26: 0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0078 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 28: 0x0087 [0x1D] PRINT_EVENT_MESSAGE(message_id=10009*)
    → "And...! We are currently recruiting new members! Therefore, it would be much appreciated if you could show that badge to others in this town. A bit of advertising would really help us out."
 29: 0x008A [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x008B [0x21] END_EVENT
 31: 0x008C [0x00] END_REQSTACK()
```

### Event 358

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         1E F0 FF               ...
0090: FF 7F 1C 00 80 1D 0F 80  23 21 00                 ........#!.     
```

#### Opcodes

```
  0: 0x008D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0092 [0x1C] WAIT(30* ticks)
  2: 0x0095 [0x1D] PRINT_EVENT_MESSAGE(message_id=10010*)
    → "Oh, hello. It seems that the number of people interested in our organization has begun to increase."
  3: 0x0098 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0099 [0x21] END_EVENT
  5: 0x009A [0x00] END_REQSTACK()
```

### Event 359

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 49 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   1E F0 FF FF 7F             .....
00A0: 1C 00 80 66 04 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ...f..........tl
00B0: 6B 30 03 02 10 08 80 1D  10 80 23 66 04 80 F8 FF  k0........#f....
00C0: FF 7F F8 FF FF 7F 74 6C  6B 31 21 00              ......tlk1!.    
```

#### Opcodes

```
  0: 0x009B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A0 [0x1C] WAIT(30* ticks)
  2: 0x00A3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x00B2 [0x03] Work_Zone[2] = 744*
  4: 0x00B7 [0x1D] PRINT_EVENT_MESSAGE(message_id=10011*)
    → "Your $3 was created using advanced alchemy techniques. It will shine brightly near people whose thoughts are currently drifting across the vast sea towards the golden fields of Aht Urhgan."
  5: 0x00BA [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00BB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  7: 0x00CA [0x21] END_EVENT
  8: 0x00CB [0x00] END_REQSTACK()
```

### Event 360

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CC   |
| Data Size    | 93 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                      42 1E F0 FF              B...
00D0: FF 7F 66 04 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  ..f..........tlk
00E0: 30 1D 11 80 23 66 04 80  F8 FF FF 7F F8 FF FF 7F  0...#f..........
00F0: 74 6C 6B 31 03 02 10 08  80 1D 12 80 23 48 13 80  tlk1........#H..
0100: 66 04 80 F8 FF FF 7F F8  FF FF 7F 70 61 73 30 1D  f..........pas0.
0110: 14 80 23 45 15 80 F0 FF  FF 7F F0 FF FF 7F 71 73  ..#E..........qs
0120: 74 63 03 80 1C 0A 80 21  00                       tc.....!.       
```

#### Opcodes

```
  0: 0x00CC [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00CD [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00D2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x00E1 [0x1D] PRINT_EVENT_MESSAGE(message_id=10012*)
    → "Oh, it's you! Many people have expressed interest in Salaheem's Sentinels!"
  4: 0x00E4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00E5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  6: 0x00F4 [0x03] Work_Zone[2] = 744*
  7: 0x00F9 [0x1D] PRINT_EVENT_MESSAGE(message_id=10013*)
    → "It looks like your $3 has lost its luster, so I will take it back now."
  8: 0x00FC [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00FD [0x48] [System] [10014*]:
    → "<Player> hands over the $3."
 10: 0x0100 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=40*
 11: 0x010F [0x1D] PRINT_EVENT_MESSAGE(message_id=10015*)
    → "I will give you this in its place. If you ever go to Aht Urhgan, please stop by Salaheem's Sentinels."
 12: 0x0112 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0113 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 14: 0x0124 [0x1C] WAIT(60* ticks)
 15: 0x0127 [0x21] END_EVENT
 16: 0x0128 [0x00] END_REQSTACK()
```

### Event 361

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0129   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                             1E F0 FF FF 7F 1C 00           .......
0130: 80 1D 16 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x0129 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x012E [0x1C] WAIT(30* ticks)
  2: 0x0131 [0x1D] PRINT_EVENT_MESSAGE(message_id=10017*)
    → "Remember to visit Salaheem's Sentinels in Al Zahbi the next time you visit the Empire of Aht Urhgan!"
  3: 0x0134 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0135 [0x21] END_EVENT
  5: 0x0136 [0x00] END_REQSTACK()
```

### Event 378

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0137   |
| Data Size    | 95 bytes |
| Instructions | 21       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                      1E  F0 FF FF 7F 1C 17 80 6E         ........n
0140: A7 C0 0E 01 18 80 99 A7  C0 0E 01 1D 19 80 23 99  ..............#.
0150: A7 C0 0E 01 6E A7 C0 0E  01 1A 80 99 A7 C0 0E 01  ....n...........
0160: 1D 1B 80 23 99 A7 C0 0E  01 66 04 80 F8 FF FF 7F  ...#.....f......
0170: F8 FF FF 7F 74 6C 6B 30  1D 1C 80 23 03 02 10 1D  ....tlk0...#....
0180: 80 1D 1E 80 23 66 04 80  F8 FF FF 7F F8 FF FF 7F  ....#f..........
0190: 74 6C 6B 31 21 00                                 tlk1!.          
```

#### Opcodes

```
  0: 0x0137 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x013C [0x1C] WAIT(45* ticks)
  2: 0x013F [0x6E] Alib-Mufalib (ID: 17744039/0x010EC0A7) uses emote 32*
  3: 0x0146 [0x99] Wait for Alib-Mufalib (ID: 17744039/0x010EC0A7) animation to complete
  4: 0x014B [0x1D] PRINT_EVENT_MESSAGE(message_id=12660*)
    → "That look in your eyes... I sense the fear of one frightful femme fatale flowing forth from your soul... Don't tell me... You're one of Salaheem's Sentinels!"
  5: 0x014E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x014F [0x99] Wait for Alib-Mufalib (ID: 17744039/0x010EC0A7) animation to complete
  7: 0x0154 [0x6E] Alib-Mufalib (ID: 17744039/0x010EC0A7) uses emote 6*
  8: 0x015B [0x99] Wait for Alib-Mufalib (ID: 17744039/0x010EC0A7) animation to complete
  9: 0x0160 [0x1D] PRINT_EVENT_MESSAGE(message_id=12661*)
    → "Which means, I am allowed to provide you with this special offer!"
 10: 0x0163 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0164 [0x99] Wait for Alib-Mufalib (ID: 17744039/0x010EC0A7) animation to complete
 12: 0x0169 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
 13: 0x0178 [0x1D] PRINT_EVENT_MESSAGE(message_id=12662*)
    → "For a small fee, I can teleport you directly to Aht Urhgan Whitegate!"
 14: 0x017B [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x017C [0x03] Work_Zone[2] = 300*
 16: 0x0181 [0x1D] PRINT_EVENT_MESSAGE(message_id=12663*)
    → "Simply trade me $0 gil, and you'll be sipping chai with [mysterious veiled beauties/bronzed, battle-hardened warriors] before the hour is up."
 17: 0x0184 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0185 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 19: 0x0194 [0x21] END_EVENT
 20: 0x0195 [0x00] END_REQSTACK()
```

### Event 379

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0196    |
| Data Size    | 102 bytes |
| Instructions | 17        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                   42 20  01 1E F0 FF FF 7F 1C 17        B ........
01A0: 80 66 04 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .f..........tlk0
01B0: 1D 1F 80 23 66 04 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
01C0: 6C 6B 31 53 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 31  lk1S........tlk1
01D0: 1D 20 80 03 01 10 06 80  73 21 80 A7 C0 0E 01 F0  . ......s!......
01E0: FF FF 7F 1C 22 80 45 23  80 F0 FF FF 7F F0 FF FF  ....".E#........
01F0: 7F 66 64 6F 31 03 80 1C  0A 80 21 00              .fdo1.....!.    
```

#### Opcodes

```
  0: 0x0196 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0197 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0199 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x019E [0x1C] WAIT(45* ticks)
  4: 0x01A1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  5: 0x01B0 [0x1D] PRINT_EVENT_MESSAGE(message_id=12664*)
    → "Thank you very much, [sir/ma'am]."
  6: 0x01B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x01B4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  8: 0x01C3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  9: 0x01D0 [0x1D] PRINT_EVENT_MESSAGE(message_id=12665*)
    → "Now let us be off!"
 10: 0x01D3 [0x03] Work_Zone[1] = 1*
 11: 0x01D8 [0x73] Alib-Mufalib (ID: 17744039/0x010EC0A7) casts magic 122* on LocalPlayer
 12: 0x01E3 [0x1C] WAIT(260* ticks)
 13: 0x01E6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x01F7 [0x1C] WAIT(60* ticks)
 15: 0x01FA [0x21] END_EVENT
 16: 0x01FB [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01FC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                      00                       .   
```

#### Opcodes

```
  0: 0x01FC [0x00] END_REQSTACK()
```
