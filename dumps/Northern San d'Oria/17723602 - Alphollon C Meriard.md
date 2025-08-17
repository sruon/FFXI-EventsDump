# 17723602 - Alphollon C Meriard

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 592 bytes                     |
| Total Events     | 8                             |
| References Count | 22                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [719](#event-719)        | 0x0001       |    104 |             25 |
| [720](#event-720)        | 0x0069       |    187 |             29 |
| [727](#event-727)        | 0x0124       |     25 |              6 |
| [726](#event-726)        | 0x013D       |     25 |              6 |
| [728](#event-728)        | 0x0156       |     25 |              6 |
| [38](#event-38)          | 0x016F       |      1 |              1 |
| [65535.1](#event-655351) | 0x0170       |     85 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x3329      |       13097 |
|       2 | 0x332A      |       13098 |
|       3 | 0x332B      |       13099 |
|       4 | 0x332C      |       13100 |
|       5 | 0x332D      |       13101 |
|       6 | 0x332E      |       13102 |
|       7 | 0x332F      |       13103 |
|       8 | 0x3330      |       13104 |
|       9 | 0x3334      |       13108 |
|      10 | 0x3335      |       13109 |
|      11 | 0x001E      |          30 |
|      12 | 0x3336      |       13110 |
|      13 | 0x003C      |          60 |
|      14 | 0x3337      |       13111 |
|      15 | 0x3338      |       13112 |
|      16 | 0x3331      |       13105 |
|      17 | 0x3332      |       13106 |
|      18 | 0x3339      |       13113 |
|      19 | 0x0052      |          82 |
|      20 | 0x0000      |           0 |
|      21 | 0x00C8      |         200 |

## String References

- **13097**: People are wallowing in sin... There are so many weak-spirited heathens who cannot go a day without lying, cheating, or stealing from their fellows.
- **13098**: And still there are other insatiable fools who crave forbidden fruit and violate our holy law with abandon. Yet for the Gates of Paradise to open, we must reach out a forgiving hand to these deluded wretches.
- **13099**: And now... Let us assume an item thou hast obtained in your lust for material possession has been warped by the wrath of the spirits.
- **13100**: These items are in a cursed state. Useless items that, if left to their own devices, will bring down upon thee a terrible fate. That curse shall remain until the spirits are appeased by the acquisition of an "abjuration."
- **13101**: An abjuration is the one and only key capable of quieting the spirits and removing the curse. It requires great hardship and suffering to obtain one; however, this penance is necessary for the cleansing of thy soul.
- **13102**: If thou bringst unto me a cursed item and its opposing abjuration, I shall invoke the blessing of the Goddess and remove thy curse.
- **13103**: Thou needst not hasten thy steps. When the time is right, thou shalt hear more of curses and abjurations.
- **13104**: Until that time, it is best that thou forgettest what thou hast learned and be on thy way. May the Gates of Paradise open unto thee.
- **13105**: This is most unfortunate... However, if thou hast not the appropriate abjuration to counter the curse, then I may not perform the purification ceremony. When thou hast obtained the abjuration, come once again to my side.
- **13106**: Verily, this is the abjuration that is required. Thou hast done well. If thou bringst the opposing cursed item, I shall perform the purification ceremony forthwith.
- **13108**: Praise to the Goddess! Thou hast safely returned from the trial of the spirits. Let us perform the purification ceremony at once. At my urging, raise thy hand in supplication to the heavens.
- **13109**: Great Goddess Altana. In recognition of the penance <Player> has paid, I beg thee to remove the blight upon the $0 and absolve <Player> of [his/her] sin...
- **13110**: The blight upon the $0 is weakening... It has been transformed into $1!
- **13111**: Thy suffering hath been rewarded. Proof of thy redemption lies in the $1 before thee. Thou hast been blessed, <Player>.
- **13112**: Continue thy journey into the light. May the Gates of Paradise open unto thee.
- **13113**: What is the meaning of this? Dost thou propose to insult a cardinal of Altana? If thou persists in this tomfoolery, I shall be forced to call upon the Temple Knights to teach thee some manners...

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

### Event 719

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 104 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 79 00 F8 FF FF 7F   J........y.....
0010: F0 FF FF 7F 5B 00 80 F8  FF FF 7F F8 FF FF 7F 74  ....[..........t
0020: 6C 6B 30 1D 01 80 23 1D  02 80 23 1D 03 80 23 1D  lk0...#...#...#.
0030: 04 80 23 1D 05 80 23 1D  06 80 23 1D 07 80 23 5B  ..#...#...#...#[
0040: 00 80 F8 FF FF 7F F8 FF  FF 7F 69 6E 6F 30 1D 08  ..........ino0..
0050: 80 23 53 F8 FF FF 7F F8  FF FF 7F 69 6E 6F 30 7B  .#S........ino0{
0060: F8 FF FF 7F 06 01 10 21  00                       .......!.       
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x79] EventEntity looks at LocalPlayer (Basic look)
  2: 0x0014 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  3: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=13097*)
    → "People are wallowing in sin... There are so many weak-spirited heathens who cannot go a day without lying, cheating, or stealing from their fellows."
  4: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=13098*)
    → "And still there are other insatiable fools who crave forbidden fruit and violate our holy law with abandon. Yet for the Gates of Paradise to open, we must reach out a forgiving hand to these deluded wretches."
  6: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=13099*)
    → "And now... Let us assume an item thou hast obtained in your lust for material possession has been warped by the wrath of the spirits."
  8: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=13100*)
    → "These items are in a cursed state. Useless items that, if left to their own devices, will bring down upon thee a terrible fate. That curse shall remain until the spirits are appeased by the acquisition of an "abjuration.""
 10: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=13101*)
    → "An abjuration is the one and only key capable of quieting the spirits and removing the curse. It requires great hardship and suffering to obtain one; however, this penance is necessary for the cleansing of thy soul."
 12: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=13102*)
    → "If thou bringst unto me a cursed item and its opposing abjuration, I shall invoke the blessing of the Goddess and remove thy curse."
 14: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=13103*)
    → "Thou needst not hasten thy steps. When the time is right, thou shalt hear more of curses and abjurations."
 16: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x003F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
 18: 0x004E [0x1D] PRINT_EVENT_MESSAGE(message_id=13104*)
    → "Until that time, it is best that thou forgettest what thou hast learned and be on thy way. May the Gates of Paradise open unto thee."
 19: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0052 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
 21: 0x005F [0x7B] EventEntity stops talking
 22: 0x0064 [0x06] Work_Zone[1] = 0
 23: 0x0067 [0x21] END_EVENT
 24: 0x0068 [0x00] END_REQSTACK()
```

### Event 720

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0069    |
| Data Size    | 187 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             42 79 00 F8 FF FF 7F           By.....
0070: F0 FF FF 7F 79 00 F0 FF  FF 7F F8 FF FF 7F 5B 00  ....y.........[.
0080: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 30 1D 09 80  .........thk0...
0090: 23 4A F8 FF FF 7F F0 FF  FF 7F 4A F0 FF FF 7F F8  #J........J.....
00A0: FF FF 7F 5B 00 80 F8 FF  FF 7F F8 FF FF 7F 69 6E  ...[..........in
00B0: 6F 30 1D 0A 80 23 53 F8  FF FF 7F F8 FF FF 7F 69  o0...#S........i
00C0: 6E 6F 30 1C 0B 80 73 00  80 F0 FF FF 7F F0 FF FF  no0...s.........
00D0: 7F 48 0C 80 23 1C 0D 80  5B 00 80 F8 FF FF 7F F8  .H..#...[.......
00E0: FF FF 7F 70 61 73 30 1D  0E 80 23 53 F8 FF FF 7F  ...pas0...#S....
00F0: F8 FF FF 7F 70 61 73 30  5B 00 80 F8 FF FF 7F F8  ....pas0[.......
0100: FF FF 7F 69 6E 6F 30 1D  0F 80 23 53 F8 FF FF 7F  ...ino0...#S....
0110: F8 FF FF 7F 69 6E 6F 30  7B F8 FF FF 7F 03 01 10  ....ino0{.......
0120: 03 10 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0069 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x006A [0x79] EventEntity looks at LocalPlayer (Basic look)
  2: 0x0074 [0x79] LocalPlayer looks at EventEntity (Basic look)
  3: 0x007E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x008D [0x1D] PRINT_EVENT_MESSAGE(message_id=13108*)
    → "Praise to the Goddess! Thou hast safely returned from the trial of the spirits. Let us perform the purification ceremony at once. At my urging, raise thy hand in supplication to the heavens."
  5: 0x0090 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0091 [0x4A] EventEntity looks at LocalPlayer
  7: 0x009A [0x4A] LocalPlayer looks at EventEntity
  8: 0x00A3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
  9: 0x00B2 [0x1D] PRINT_EVENT_MESSAGE(message_id=13109*)
    → "Great Goddess Altana. In recognition of the penance <Player> has paid, I beg thee to remove the blight upon the $0 and absolve <Player> of [his/her] sin..."
 10: 0x00B5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00B6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
 12: 0x00C3 [0x1C] WAIT(30* ticks)
 13: 0x00C6 [0x73] LocalPlayer casts magic 20* on LocalPlayer
 14: 0x00D1 [0x48] [System] [13110*]:
    → "The blight upon the $0 is weakening... It has been transformed into $1!"
 15: 0x00D4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x00D5 [0x1C] WAIT(60* ticks)
 17: 0x00D8 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
 18: 0x00E7 [0x1D] PRINT_EVENT_MESSAGE(message_id=13111*)
    → "Thy suffering hath been rewarded. Proof of thy redemption lies in the $1 before thee. Thou hast been blessed, <Player>."
 19: 0x00EA [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x00EB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 21: 0x00F8 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
 22: 0x0107 [0x1D] PRINT_EVENT_MESSAGE(message_id=13112*)
    → "Continue thy journey into the light. May the Gates of Paradise open unto thee."
 23: 0x010A [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x010B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
 25: 0x0118 [0x7B] EventEntity stops talking
 26: 0x011D [0x03] Work_Zone[1] = Work_Zone[3]
 27: 0x0122 [0x21] END_EVENT
 28: 0x0123 [0x00] END_REQSTACK()
```

### Event 727

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0124   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:             4A F8 FF FF  7F F0 FF FF 7F 79 00 F8      J........y..
0130: FF FF 7F F0 FF FF 7F 1D  10 80 23 21 00           ..........#!.   
```

#### Opcodes

```
  0: 0x0124 [0x4A] EventEntity looks at LocalPlayer
  1: 0x012D [0x79] EventEntity looks at LocalPlayer (Basic look)
  2: 0x0137 [0x1D] PRINT_EVENT_MESSAGE(message_id=13105*)
    → "This is most unfortunate... However, if thou hast not the appropriate abjuration to counter the curse, then I may not perform the purification ceremony. When thou hast obtained the abjuration, come once again to my side."
  3: 0x013A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x013B [0x21] END_EVENT
  5: 0x013C [0x00] END_REQSTACK()
```

### Event 726

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013D   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                         4A F8 FF               J..
0140: FF 7F F0 FF FF 7F 79 00  F8 FF FF 7F F0 FF FF 7F  ......y.........
0150: 1D 11 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x013D [0x4A] EventEntity looks at LocalPlayer
  1: 0x0146 [0x79] EventEntity looks at LocalPlayer (Basic look)
  2: 0x0150 [0x1D] PRINT_EVENT_MESSAGE(message_id=13106*)
    → "Verily, this is the abjuration that is required. Thou hast done well. If thou bringst the opposing cursed item, I shall perform the purification ceremony forthwith."
  3: 0x0153 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0154 [0x21] END_EVENT
  5: 0x0155 [0x00] END_REQSTACK()
```

### Event 728

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0156   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   4A F8  FF FF 7F F0 FF FF 7F 79        J........y
0160: 00 F8 FF FF 7F F0 FF FF  7F 1D 12 80 23 21 00     ............#!. 
```

#### Opcodes

```
  0: 0x0156 [0x4A] EventEntity looks at LocalPlayer
  1: 0x015F [0x79] EventEntity looks at LocalPlayer (Basic look)
  2: 0x0169 [0x1D] PRINT_EVENT_MESSAGE(message_id=13113*)
    → "What is the meaning of this? Dost thou propose to insult a cardinal of Altana? If thou persists in this tomfoolery, I shall be forced to call upon the Temple Knights to teach thee some manners..."
  3: 0x016C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x016D [0x21] END_EVENT
  5: 0x016E [0x00] END_REQSTACK()
```

### Event 38

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x016F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                               00                 .
```

#### Opcodes

```
  0: 0x016F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0170   |
| Data Size    | 85 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170: 45 13 80 F0 FF FF 7F F0  FF FF 7F 78 30 30 62 14  E..........x00b.
0180: 80 1C 15 80 52 13 80 F0  FF FF 7F F0 FF FF 7F 78  ....R..........x
0190: 30 30 62 45 15 80 F0 FF  FF 7F F0 FF FF 7F 6F 76  00bE..........ov
01A0: 6C 31 14 80 45 13 80 F0  FF FF 7F F0 FF FF 7F 78  l1..E..........x
01B0: 30 30 32 14 80 55 13 80  F0 FF FF 7F F0 FF FF 7F  002..U..........
01C0: 78 30 30 32 00                                    x002.           
```

#### Opcodes

```
  0: 0x0170 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "x00b" with entities [LocalPlayer, LocalPlayer], work=[82*, 0*]
  1: 0x0181 [0x1C] WAIT(200* ticks)
  2: 0x0184 [0x52] END_LOAD_SCHEDULER: End scheduler "x00b" with entities [LocalPlayer, LocalPlayer], work=82*
  3: 0x0193 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x01A4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "x002" with entities [LocalPlayer, LocalPlayer], work=[82*, 0*]
  5: 0x01B5 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "x002" with entities [LocalPlayer, LocalPlayer], work=82*
  6: 0x01C4 [0x00] END_REQSTACK()
```
