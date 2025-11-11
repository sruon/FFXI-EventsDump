# 17719569 - Amutiyaal

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 788 bytes                     |
| Total Events     | 8                             |
| References Count | 37                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [812](#event-812)     | 0x0001       |    136 |             34 |
| [813](#event-813)     | 0x0089       |     26 |              8 |
| [814](#event-814)     | 0x00A3       |     49 |              9 |
| [815](#event-815)     | 0x00D4       |     96 |             20 |
| [816](#event-816)     | 0x0134       |     44 |              8 |
| [880](#event-880)     | 0x0160       |    138 |             24 |
| [881](#event-881)     | 0x01EA       |    102 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x002D      |          45 |
|       1 | 0x288A      |       10378 |
|       2 | 0x288B      |       10379 |
|       3 | 0x0000      |           0 |
|       4 | 0x000B      |          11 |
|       5 | 0x288C      |       10380 |
|       6 | 0x0001      |           1 |
|       7 | 0x0013      |          19 |
|       8 | 0x288D      |       10381 |
|       9 | 0x02E7      |         743 |
|      10 | 0x288E      |       10382 |
|      11 | 0x003C      |          60 |
|      12 | 0x288F      |       10383 |
|      13 | 0x001D      |          29 |
|      14 | 0x2890      |       10384 |
|      15 | 0x2891      |       10385 |
|      16 | 0x001E      |          30 |
|      17 | 0x2892      |       10386 |
|      18 | 0x2893      |       10387 |
|      19 | 0x000A      |          10 |
|      20 | 0x2894      |       10388 |
|      21 | 0x2895      |       10389 |
|      22 | 0x2896      |       10390 |
|      23 | 0x2897      |       10391 |
|      24 | 0x00C9      |         201 |
|      25 | 0x2899      |       10393 |
|      26 | 0x33F0      |       13296 |
|      27 | 0x0015      |          21 |
|      28 | 0x33F1      |       13297 |
|      29 | 0x33F2      |       13298 |
|      30 | 0x012C      |         300 |
|      31 | 0x33F3      |       13299 |
|      32 | 0x33F4      |       13300 |
|      33 | 0x33F5      |       13301 |
|      34 | 0x007A      |         122 |
|      35 | 0x0104      |         260 |
|      36 | 0x00C8      |         200 |

## String References

- **10378**: You there! Yes, you! You are one of those "adventurers"?
- **10379**: Are you an "adventurer"? [I guess I am./Not today.]
- **10380**: I knew it to be so! This badge was made for one such as you! Allow me...!
- **10381**: No!? A thousand pardons! And yet, you shall make the perfect bearer for this badge! Allow me...!
- **10382**: 6 is suddenly pinned to <Player>!
- **10383**: This is the symbol of the illustrious leader of Salaheem's Sentinels--a snarling wildcat.
- **10384**: Under the authorization of Her Imperial Majesty, Salaheem's Sentinels is a well-respected company that specializes in training and dispatching mercenaries for the defense of the Aht Urhgan Empire. We have a myriad of well-paying missions ready for any able-bodied adventurer.
- **10385**: But my speech grows overlong! My dauntless commander has bid me take ship to this bountiful kingdom and dazzle the citizenry with the Sentinels' splendor, and so I shall!
- **10386**: Oho! It is you! It would appear that more and more people are taking an interest in our humble organization. Praise be to the winds of fortune!
- **10387**: The $3 was created through the advanced alchemical techniques of my country. The wildcat's eyes are designed to flash in the presence of any who entertain thoughts of Aht Urhgan.
- **10388**: Aha! My splendid friend! You have spread the fire of fascination through the entire city! Salaheem's Sentinels is the talk of the town!
- **10389**: Hm? It appears the eyes of the $3 have lost their luster. The crystal power source must have been drained after dazzling so many people. Allow me to remove this spent trinket...
- **10390**: The $3 is taken from <Player>!
- **10391**: In return, I shall award you this bauble. It will come in handy for when you join the ranks of the Aht Urhgan mercenaries!
- **10393**: Your name will shine down through the ages as one of our finest public relations officers. Should you ever brave the seas and find yourself in the Imperial City of Al Zahbi, you simply must visit the offices of Salaheem's Sentinels. I insist!
- **13296**: Ah, if it isn't <Player>! Perchance you have come to question the authenticity of my testimony regarding the Sentinels. I do not deny that I may have possibly added a bit of color to the facts surrounding the true nature of our fine leader, but all's well that ends well, no?
- **13297**: Ah, yet you need not fret any longer, my fine friend. Our prodigal president and provider once again has proffered forth her ever-giving hands in a selfless gesture of heartwarming charity.
- **13298**: From this day forth, all employees of Salaheem's Sentinels can now teleport freely from San d'Oria to Aht Urhgan Whitegate!
- **13299**: And by freely, I mean in the sense of "free as a bird" as I will require a fee of $0 gil from those who wish to partake in my services.
- **13300**: Thank you very much, [sir/ma'am].
- **13301**: Now let us be on our merry way!

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

### Event 812

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 136 bytes |
| Instructions | 34        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 1C  00 80 1D 01 80 23 24 02   B...........#$.
0010: 80 03 80 03 80 25 02 00  10 03 80 00 34 00 6E 11  .....%......4.n.
0020: 61 0E 01 04 80 99 11 61  0E 01 1C 00 80 1D 05 80  a......a........
0030: 23 01 52 00 02 00 10 06  80 00 52 00 6E 11 61 0E  #.R.......R.n.a.
0040: 01 07 80 99 11 61 0E 01  1C 00 80 1D 08 80 23 01  .....a........#.
0050: 52 00 03 02 10 09 80 48  0A 80 1C 0B 80 1D 0C 80  R......H........
0060: 23 66 0D 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  #f..........tlk0
0070: 1D 0E 80 23 66 0D 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
0080: 6C 6B 31 1D 0F 80 23 21  00                       lk1...#!.       
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x1C] WAIT(45* ticks)
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=10378*)
    → "You there! Yes, you! You are one of those "adventurers"?"
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x24] CREATE_DIALOG(message_id=10379*, default_option=0*, option_flags=0*)
    → "Are you an "adventurer"? [I guess I am./Not today.]"
  6: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0034
  8: 0x001E [0x6E] Amutiyaal (ID: 17719569/0x010E6111) uses emote 11*
  9: 0x0025 [0x99] Wait for Amutiyaal (ID: 17719569/0x010E6111) animation to complete
 10: 0x002A [0x1C] WAIT(45* ticks)
 11: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=10380*)
    → "I knew it to be so! This badge was made for one such as you! Allow me...!"
 12: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0031 [0x01] GOTO 0x0052
 14: 0x0034 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0052
 15: 0x003C [0x6E] Amutiyaal (ID: 17719569/0x010E6111) uses emote 19*
 16: 0x0043 [0x99] Wait for Amutiyaal (ID: 17719569/0x010E6111) animation to complete
 17: 0x0048 [0x1C] WAIT(45* ticks)
 18: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=10381*)
    → "No!? A thousand pardons! And yet, you shall make the perfect bearer for this badge! Allow me...!"
 19: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x004F [0x01] GOTO 0x0052

SUBROUTINE_0052:
 21: 0x0052 [0x03] Work_Zone[2] = 743*
 22: 0x0057 [0x48] [System] [10382*]:
    → "6 is suddenly pinned to <Player>!"
 23: 0x005A [0x1C] WAIT(60* ticks)
 24: 0x005D [0x1D] PRINT_EVENT_MESSAGE(message_id=10383*)
    → "This is the symbol of the illustrious leader of Salaheem's Sentinels--a snarling wildcat."
 25: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0061 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
 27: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=10384*)
    → "Under the authorization of Her Imperial Majesty, Salaheem's Sentinels is a well-respected company that specializes in training and dispatching mercenaries for the defense of the Aht Urhgan Empire. We have a myriad of well-paying missions ready for any able-bodied adventurer."
 28: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x0074 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
 30: 0x0083 [0x1D] PRINT_EVENT_MESSAGE(message_id=10385*)
    → "But my speech grows overlong! My dauntless commander has bid me take ship to this bountiful kingdom and dazzle the citizenry with the Sentinels' splendor, and so I shall!"
 31: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0087 [0x21] END_EVENT
 33: 0x0088 [0x00] END_REQSTACK()
```

### Event 813

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             1E F0 FF FF 7F 1C 10           .......
0090: 80 6E 11 61 0E 01 04 80  99 11 61 0E 01 1D 11 80  .n.a......a.....
00A0: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0089 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x008E [0x1C] WAIT(30* ticks)
  2: 0x0091 [0x6E] Amutiyaal (ID: 17719569/0x010E6111) uses emote 11*
  3: 0x0098 [0x99] Wait for Amutiyaal (ID: 17719569/0x010E6111) animation to complete
  4: 0x009D [0x1D] PRINT_EVENT_MESSAGE(message_id=10386*)
    → "Oho! It is you! It would appear that more and more people are taking an interest in our humble organization. Praise be to the winds of fortune!"
  5: 0x00A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A1 [0x21] END_EVENT
  7: 0x00A2 [0x00] END_REQSTACK()
```

### Event 814

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 49 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          1E F0 FF FF 7F  1C 00 80 66 0D 80 F8 FF     ........f....
00B0: FF 7F F8 FF FF 7F 74 6C  6B 30 03 02 10 09 80 1D  ......tlk0......
00C0: 12 80 23 66 0D 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
00D0: 6B 31 21 00                                       k1!.            
```

#### Opcodes

```
  0: 0x00A3 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A8 [0x1C] WAIT(45* ticks)
  2: 0x00AB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  3: 0x00BA [0x03] Work_Zone[2] = 743*
  4: 0x00BF [0x1D] PRINT_EVENT_MESSAGE(message_id=10387*)
    → "The $3 was created through the advanced alchemical techniques of my country. The wildcat's eyes are designed to flash in the presence of any who entertain thoughts of Aht Urhgan."
  5: 0x00C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00C3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  7: 0x00D2 [0x21] END_EVENT
  8: 0x00D3 [0x00] END_REQSTACK()
```

### Event 815

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D4   |
| Data Size    | 96 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             42 1E F0 FF  FF 7F 1C 00 80 6E 11 61      B........n.a
00E0: 0E 01 13 80 99 11 61 0E  01 1D 14 80 23 03 02 10  ......a.....#...
00F0: 09 80 1D 15 80 23 48 16  80 1C 0B 80 66 0D 80 F8  .....#H.....f...
0100: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 17 80 23 66  .......tlk0...#f
0110: 0D 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 45 18  ..........tlk1E.
0120: 80 F0 FF FF 7F F0 FF FF  7F 71 73 74 63 03 80 1C  .........qstc...
0130: 0B 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x00D4 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00D5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00DA [0x1C] WAIT(45* ticks)
  3: 0x00DD [0x6E] Amutiyaal (ID: 17719569/0x010E6111) uses emote 10*
  4: 0x00E4 [0x99] Wait for Amutiyaal (ID: 17719569/0x010E6111) animation to complete
  5: 0x00E9 [0x1D] PRINT_EVENT_MESSAGE(message_id=10388*)
    → "Aha! My splendid friend! You have spread the fire of fascination through the entire city! Salaheem's Sentinels is the talk of the town!"
  6: 0x00EC [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00ED [0x03] Work_Zone[2] = 743*
  8: 0x00F2 [0x1D] PRINT_EVENT_MESSAGE(message_id=10389*)
    → "Hm? It appears the eyes of the $3 have lost their luster. The crystal power source must have been drained after dazzling so many people. Allow me to remove this spent trinket..."
  9: 0x00F5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00F6 [0x48] [System] [10390*]:
    → "The $3 is taken from <Player>!"
 11: 0x00F9 [0x1C] WAIT(60* ticks)
 12: 0x00FC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
 13: 0x010B [0x1D] PRINT_EVENT_MESSAGE(message_id=10391*)
    → "In return, I shall award you this bauble. It will come in handy for when you join the ranks of the Aht Urhgan mercenaries!"
 14: 0x010E [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x010F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
 16: 0x011E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 17: 0x012F [0x1C] WAIT(60* ticks)
 18: 0x0132 [0x21] END_EVENT
 19: 0x0133 [0x00] END_REQSTACK()
```

### Event 816

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0134   |
| Data Size    | 44 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:             1E F0 FF FF  7F 1C 00 80 66 0D 80 F8      ........f...
0140: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 19 80 23 66  .......tlk0...#f
0150: 0D 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 21 00  ..........tlk1!.
```

#### Opcodes

```
  0: 0x0134 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0139 [0x1C] WAIT(45* ticks)
  2: 0x013C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  3: 0x014B [0x1D] PRINT_EVENT_MESSAGE(message_id=10393*)
    → "Your name will shine down through the ages as one of our finest public relations officers. Should you ever brave the seas and find yourself in the Imperial City of Al Zahbi, you simply must visit the offices of Salaheem's Sentinels. I insist!"
  4: 0x014E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x014F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  6: 0x015E [0x21] END_EVENT
  7: 0x015F [0x00] END_REQSTACK()
```

### Event 880

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0160    |
| Data Size    | 138 bytes |
| Instructions | 24        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160: 1E F0 FF FF 7F 1C 00 80  66 0D 80 F8 FF FF 7F F8  ........f.......
0170: FF FF 7F 74 6C 6B 30 1D  1A 80 23 66 0D 80 F8 FF  ...tlk0...#f....
0180: FF 7F F8 FF FF 7F 74 6C  6B 31 6E 11 61 0E 01 1B  ......tlk1n.a...
0190: 80 99 11 61 0E 01 1D 1C  80 23 99 11 61 0E 01 66  ...a.....#..a..f
01A0: 0D 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 1D  ..........tlk0..
01B0: 80 23 03 02 10 1E 80 66  0D 80 F8 FF FF 7F F8 FF  .#.....f........
01C0: FF 7F 74 6C 6B 31 53 F8  FF FF 7F F8 FF FF 7F 74  ..tlk1S........t
01D0: 6C 6B 31 6E 11 61 0E 01  13 80 99 11 61 0E 01 1D  lk1n.a......a...
01E0: 1F 80 23 99 11 61 0E 01  21 00                    ..#..a..!.      
```

#### Opcodes

```
  0: 0x0160 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0165 [0x1C] WAIT(45* ticks)
  2: 0x0168 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  3: 0x0177 [0x1D] PRINT_EVENT_MESSAGE(message_id=13296*)
    → "Ah, if it isn't <Player>! Perchance you have come to question the authenticity of my testimony regarding the Sentinels. I do not deny that I may have possibly added a bit of color to the facts surrounding the true nature of our fine leader, but all's well that ends well, no?"
  4: 0x017A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x017B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  6: 0x018A [0x6E] Amutiyaal (ID: 17719569/0x010E6111) uses emote 21*
  7: 0x0191 [0x99] Wait for Amutiyaal (ID: 17719569/0x010E6111) animation to complete
  8: 0x0196 [0x1D] PRINT_EVENT_MESSAGE(message_id=13297*)
    → "Ah, yet you need not fret any longer, my fine friend. Our prodigal president and provider once again has proffered forth her ever-giving hands in a selfless gesture of heartwarming charity."
  9: 0x0199 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x019A [0x99] Wait for Amutiyaal (ID: 17719569/0x010E6111) animation to complete
 11: 0x019F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
 12: 0x01AE [0x1D] PRINT_EVENT_MESSAGE(message_id=13298*)
    → "From this day forth, all employees of Salaheem's Sentinels can now teleport freely from San d'Oria to Aht Urhgan Whitegate!"
 13: 0x01B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x01B2 [0x03] Work_Zone[2] = 300*
 15: 0x01B7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
 16: 0x01C6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 17: 0x01D3 [0x6E] Amutiyaal (ID: 17719569/0x010E6111) uses emote 10*
 18: 0x01DA [0x99] Wait for Amutiyaal (ID: 17719569/0x010E6111) animation to complete
 19: 0x01DF [0x1D] PRINT_EVENT_MESSAGE(message_id=13299*)
    → "And by freely, I mean in the sense of "free as a bird" as I will require a fee of $0 gil from those who wish to partake in my services."
 20: 0x01E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x01E3 [0x99] Wait for Amutiyaal (ID: 17719569/0x010E6111) animation to complete
 22: 0x01E8 [0x21] END_EVENT
 23: 0x01E9 [0x00] END_REQSTACK()
```

### Event 881

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01EA    |
| Data Size    | 102 bytes |
| Instructions | 17        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                                42 20 01 1E F0 FF            B ....
01F0: FF 7F 1C 00 80 66 0D 80  F8 FF FF 7F F8 FF FF 7F  .....f..........
0200: 74 6C 6B 30 1D 20 80 23  66 0D 80 F8 FF FF 7F F8  tlk0. .#f.......
0210: FF FF 7F 74 6C 6B 31 53  F8 FF FF 7F F8 FF FF 7F  ...tlk1S........
0220: 74 6C 6B 31 1D 21 80 03  01 10 06 80 73 22 80 11  tlk1.!......s"..
0230: 61 0E 01 F0 FF FF 7F 1C  23 80 45 24 80 F0 FF FF  a.......#.E$....
0240: 7F F0 FF FF 7F 66 64 6F  31 03 80 1C 0B 80 21 00  .....fdo1.....!.
```

#### Opcodes

```
  0: 0x01EA [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01EB [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x01ED [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x01F2 [0x1C] WAIT(45* ticks)
  4: 0x01F5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  5: 0x0204 [0x1D] PRINT_EVENT_MESSAGE(message_id=13300*)
    → "Thank you very much, [sir/ma'am]."
  6: 0x0207 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0208 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  8: 0x0217 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  9: 0x0224 [0x1D] PRINT_EVENT_MESSAGE(message_id=13301*)
    → "Now let us be on our merry way!"
 10: 0x0227 [0x03] Work_Zone[1] = 1*
 11: 0x022C [0x73] Amutiyaal (ID: 17719569/0x010E6111) casts magic 122* on LocalPlayer
 12: 0x0237 [0x1C] WAIT(260* ticks)
 13: 0x023A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x024B [0x1C] WAIT(60* ticks)
 15: 0x024E [0x21] END_EVENT
 16: 0x024F [0x00] END_REQSTACK()
```
