# 17670752 - Oiheaurese

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 332 bytes                  |
| Total Events     | 8                          |
| References Count | 20                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [282](#event-282)     | 0x0001       |     26 |              8 |
| [285](#event-285)     | 0x001B       |     41 |             17 |
| [286](#event-286)     | 0x0044       |     19 |              7 |
| [287](#event-287)     | 0x0057       |     27 |             11 |
| [288](#event-288)     | 0x0072       |     23 |              9 |
| [289](#event-289)     | 0x0089       |     53 |             15 |
| [290](#event-290)     | 0x00BE       |     14 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FE1      |        8161 |
|       1 | 0x0014      |          20 |
|       2 | 0x1FE2      |        8162 |
|       3 | 0x1FE3      |        8163 |
|       4 | 0x1FE4      |        8164 |
|       5 | 0x1FE5      |        8165 |
|       6 | 0x06E2      |        1762 |
|       7 | 0x1FE6      |        8166 |
|       8 | 0x1FE7      |        8167 |
|       9 | 0x1FF4      |        8180 |
|      10 | 0x1FF5      |        8181 |
|      11 | 0x1FF6      |        8182 |
|      12 | 0x06E3      |        1763 |
|      13 | 0x1FF7      |        8183 |
|      14 | 0x1FF8      |        8184 |
|      15 | 0x1FF9      |        8185 |
|      16 | 0x1FFA      |        8186 |
|      17 | 0x00C9      |         201 |
|      18 | 0x0000      |           0 |
|      19 | 0x1FFB      |        8187 |

## String References

- **8161**: Curses! Curse it all!
- **8163**: That face! Could you perchance be the <Player> I've heard rumors about? Oh, this is a fortunate day indeed!
- **8164**: I am a researcher of wyverns, and one of no small repute. That day when the hordes took the Kingdom, I was in my laboratory, having just received a report from a reliable source that a dragon egg had been sighted in the sands of Altepa.
- **8165**: Somehow, by the Goddess's good graces, my life was spared from the onslaught. I regained my senses, and where do I find myself but the very land to which I was planning my next research expedition!
- **8166**: But alas, there is always a rub. Search though I might, the $3 I seek seems to have been buried deep beneath the shifting sands... 'Tis small surprise, given the unstable conditions these days.
- **8167**: I am a mere academic, hardly suited for traipsing across this wasteland on a wild $3 chase. But you--you have powers the rest of us could never hope to possess! Please, you must help me find it!
- **8180**: The dragon's rightful home!? Wherever did you hear that from?
- **8181**: The tales say that the $3 will hatch if laid to rest on Drogaroga's Spine in the Meriphataud Mountains.
- **8182**: But alas... Ever since the earthquakes disfigured the land, I fear that no road will take you there...
- **8183**: Why, that is... It couldn't be! 6? Does this mean that...
- **8184**: So the $3 has already hatched. Ah, for shame that I could not be there to witness this historic moment!
- **8185**: Still, I feel some measure of solace in knowing that the creature has returned to its rightful home. Doubtless you've done the wyvern a great kindness.
- **8186**: Consider this yours, as a humble token of my gratitude.
- **8187**: Doubtless you've done the wyvern a great kindness, friend. You have my gratitude.

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

### Event 282

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 4A 61 A2  0D 01 F0 FF FF 7F 1C 01   ...#Ja.........
0010: 80 2B 61 A2 0D 01 02 80  23 21 00                 .+a.....#!.     
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=8161*)
    → "Curses! Curse it all!"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x4A] Morjean (ID: 17670753/0x010DA261) looks at LocalPlayer
  3: 0x000E [0x1C] WAIT(20* ticks)
  4: 0x0011 [0x2B] Morjean (ID: 17670753/0x010DA261) [8162*]:
    → "As you can see, the doctor's a bit out of sorts at the moment. Pray leave him be, stranger."
  5: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0019 [0x21] END_EVENT
  7: 0x001A [0x00] END_REQSTACK()
```

### Event 285

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 41 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1E F0 FF FF 7F             .....
0020: 1C 01 80 1D 03 80 23 1D  04 80 23 1D 05 80 23 03  ......#...#...#.
0030: 02 10 06 80 1D 07 80 23  42 03 02 10 06 80 1D 08  .......#B.......
0040: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x001B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0020 [0x1C] WAIT(20* ticks)
  2: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=8163*)
    → "That face! Could you perchance be the <Player> I've heard rumors about? Oh, this is a fortunate day indeed!"
  3: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=8164*)
    → "I am a researcher of wyverns, and one of no small repute. That day when the hordes took the Kingdom, I was in my laboratory, having just received a report from a reliable source that a dragon egg had been sighted in the sands of Altepa."
  5: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=8165*)
    → "Somehow, by the Goddess's good graces, my life was spared from the onslaught. I regained my senses, and where do I find myself but the very land to which I was planning my next research expedition!"
  7: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x002F [0x03] Work_Zone[2] = 1762*
  9: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=8166*)
    → "But alas, there is always a rub. Search though I might, the $3 I seek seems to have been buried deep beneath the shifting sands... 'Tis small surprise, given the unstable conditions these days."
 10: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0038 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 12: 0x0039 [0x03] Work_Zone[2] = 1762*
 13: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=8167*)
    → "I am a mere academic, hardly suited for traipsing across this wasteland on a wild $3 chase. But you--you have powers the rest of us could never hope to possess! Please, you must help me find it!"
 14: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0042 [0x21] END_EVENT
 16: 0x0043 [0x00] END_REQSTACK()
```

### Event 286

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 19 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             1E F0 FF FF  7F 1C 01 80 03 02 10 06      ............
0050: 80 1D 08 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x0044 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0049 [0x1C] WAIT(20* ticks)
  2: 0x004C [0x03] Work_Zone[2] = 1762*
  3: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=8167*)
    → "I am a mere academic, hardly suited for traipsing across this wasteland on a wild $3 chase. But you--you have powers the rest of us could never hope to possess! Please, you must help me find it!"
  4: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0055 [0x21] END_EVENT
  6: 0x0056 [0x00] END_REQSTACK()
```

### Event 287

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 27 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      1E  F0 FF FF 7F 1C 01 80 1D         .........
0060: 09 80 23 03 02 10 06 80  1D 0A 80 23 1D 0B 80 23  ..#........#...#
0070: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0057 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005C [0x1C] WAIT(20* ticks)
  2: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=8180*)
    → "The dragon's rightful home!? Wherever did you hear that from?"
  3: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0063 [0x03] Work_Zone[2] = 1762*
  5: 0x0068 [0x1D] PRINT_EVENT_MESSAGE(message_id=8181*)
    → "The tales say that the $3 will hatch if laid to rest on Drogaroga's Spine in the Meriphataud Mountains."
  6: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x006C [0x1D] PRINT_EVENT_MESSAGE(message_id=8182*)
    → "But alas... Ever since the earthquakes disfigured the land, I fear that no road will take you there..."
  8: 0x006F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0070 [0x21] END_EVENT
 10: 0x0071 [0x00] END_REQSTACK()
```

### Event 288

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 23 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       1E F0 FF FF 7F 1C  01 80 03 02 10 06 80 1D    ..............
0080: 0A 80 23 1D 0B 80 23 21  00                       ..#...#!.       
```

#### Opcodes

```
  0: 0x0072 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0077 [0x1C] WAIT(20* ticks)
  2: 0x007A [0x03] Work_Zone[2] = 1762*
  3: 0x007F [0x1D] PRINT_EVENT_MESSAGE(message_id=8181*)
    → "The tales say that the $3 will hatch if laid to rest on Drogaroga's Spine in the Meriphataud Mountains."
  4: 0x0082 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0083 [0x1D] PRINT_EVENT_MESSAGE(message_id=8182*)
    → "But alas... Ever since the earthquakes disfigured the land, I fear that no road will take you there..."
  6: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0087 [0x21] END_EVENT
  8: 0x0088 [0x00] END_REQSTACK()
```

### Event 289

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 53 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             1E F0 FF FF 7F 1C 01           .......
0090: 80 03 02 10 0C 80 1D 0D  80 23 03 03 10 06 80 1D  .........#......
00A0: 0E 80 23 1D 0F 80 23 1D  10 80 23 45 11 80 F0 FF  ..#...#...#E....
00B0: FF 7F F0 FF FF 7F 71 73  74 63 12 80 21 00        ......qstc..!.  
```

#### Opcodes

```
  0: 0x0089 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x008E [0x1C] WAIT(20* ticks)
  2: 0x0091 [0x03] Work_Zone[2] = 1763*
  3: 0x0096 [0x1D] PRINT_EVENT_MESSAGE(message_id=8183*)
    → "Why, that is... It couldn't be! 6? Does this mean that..."
  4: 0x0099 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x009A [0x03] Work_Zone[3] = 1762*
  6: 0x009F [0x1D] PRINT_EVENT_MESSAGE(message_id=8184*)
    → "So the $3 has already hatched. Ah, for shame that I could not be there to witness this historic moment!"
  7: 0x00A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8185*)
    → "Still, I feel some measure of solace in knowing that the creature has returned to its rightful home. Doubtless you've done the wyvern a great kindness."
  9: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00A7 [0x1D] PRINT_EVENT_MESSAGE(message_id=8186*)
    → "Consider this yours, as a humble token of my gratitude."
 11: 0x00AA [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x00AB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 13: 0x00BC [0x21] END_EVENT
 14: 0x00BD [0x00] END_REQSTACK()
```

### Event 290

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BE   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            1E F0                ..
00C0: FF FF 7F 1C 01 80 1D 13  80 23 21 00              .........#!.    
```

#### Opcodes

```
  0: 0x00BE [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00C3 [0x1C] WAIT(20* ticks)
  2: 0x00C6 [0x1D] PRINT_EVENT_MESSAGE(message_id=8187*)
    → "Doubtless you've done the wyvern a great kindness, friend. You have my gratitude."
  3: 0x00C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00CA [0x21] END_EVENT
  5: 0x00CB [0x00] END_REQSTACK()
```
