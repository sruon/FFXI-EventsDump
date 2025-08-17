# 16883784 - Ferchinne

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 440 bytes                   |
| Total Events     | 7                           |
| References Count | 20                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [240](#event-240)     | 0x0001       |     30 |              8 |
| [241](#event-241)     | 0x001F       |     99 |             23 |
| [242](#event-242)     | 0x0082       |     53 |             13 |
| [243](#event-243)     | 0x00B7       |     71 |             15 |
| [244](#event-244)     | 0x00FE       |     30 |              8 |
| [245](#event-245)     | 0x011C       |     29 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2A33      |       10803 |
|       1 | 0x0027      |          39 |
|       2 | 0x2A34      |       10804 |
|       3 | 0x2A35      |       10805 |
|       4 | 0x2A36      |       10806 |
|       5 | 0x2A37      |       10807 |
|       6 | 0x2A38      |       10808 |
|       7 | 0x2A39      |       10809 |
|       8 | 0x2A3A      |       10810 |
|       9 | 0x2A3B      |       10811 |
|      10 | 0x2A3C      |       10812 |
|      11 | 0x2A3D      |       10813 |
|      12 | 0x2A3E      |       10814 |
|      13 | 0x2A3F      |       10815 |
|      14 | 0x2A40      |       10816 |
|      15 | 0x00C9      |         201 |
|      16 | 0x0000      |           0 |
|      17 | 0x2A41      |       10817 |
|      18 | 0x2A42      |       10818 |
|      19 | 0x2A43      |       10819 |

## String References

- **10803**: It is not only the adults of the safehold who wish to improve our current situation--many of the younger men and women are also trying to make a difference.
- **10804**: However, what they fail to realize is that cowering behind the walls of the city won't change anything...
- **10805**: My name is Ferchinne. I was tired of seeing my people suffer, so I decided to journey forth from the confines of the safehold in order to earn the title of Dragon Slayer.
- **10806**: I trained for many months, but I feel I still lack the skills needed to defeat a truly horrifying dragon. To be a true Dragon Slayer, one must be able to soar like a dragon, not only physically, but mentally.
- **10807**: Perhaps I need wings of my own to catch the winds of the endless skies...
- **10808**: The city elders told me that once, long ago, there were knights in the Kingdom of San d'Oria that could fly as high as the clouds.
- **10809**: Brave adventurer, have you ever seen a noble bird that walks on four legs? A proud beast that has the wings of an eagle?
- **10810**: If you come across one of these mythical creatures, I would greatly appreciate it if you removed its tailfeathers and brought them back here to me.
- **10811**: It is said that while those feathers are unbelievably light, they are remarkably sturdy. If I were to bond them together with wax, I could make wings of my own!
- **10812**: Bring back two and I will reward you with something special.
- **10813**: The luster, the touch... Yes, these are the feathers that I have been searching for. Thank you so very much. Now, maybe I can fly as high as the dragons themselves!
- **10814**: Here, take this as a token of my appreciation.
- **10815**: I was given that stone by an old merchant while traveling through the Eastern empire. He told me that it had the power to dissolve the clouds and rob mighty dragons of their ability to fly.
- **10816**: But even if it does not have that power, I'm sure you can find someone who will purchase it from you for a large sum of gil.
- **10817**: <Sigh> Will I ever be able to fly... Perhaps I need more feathers...
- **10818**: I am sorry to bother you again, but if you come across any more of the legendary tailfeathers, I beg of you to bring them to me.
- **10819**: Thank you, kind [sir/adventurer].

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

### Event 240

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 66 01 80 46 A0 01   ........#f..F..
0010: 01 46 A0 01 01 74 6C 6B  30 1D 02 80 23 21 00     .F...tlk0...#!. 
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=10803*)
    → "It is not only the adults of the safehold who wish to improve our current situation--many of the younger men and women are also trying to make a difference."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Epinolle (ID: 16883782/0x0101A046), Epinolle (ID: 16883782/0x0101A046)], work=39*
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=10804*)
    → "However, what they fail to realize is that cowering behind the walls of the city won't change anything..."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x21] END_EVENT
  7: 0x001E [0x00] END_REQSTACK()
```

### Event 241

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 99 bytes |
| Instructions | 23       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               1E                 .
0020: F0 FF FF 7F 1D 03 80 23  66 01 80 48 A0 01 01 48  .......#f..H...H
0030: A0 01 01 74 68 6B 31 1D  04 80 23 1D 05 80 23 1D  ...thk1...#...#.
0040: 06 80 23 66 01 80 48 A0  01 01 48 A0 01 01 74 68  ..#f..H...H...th
0050: 6B 32 1D 07 80 23 66 01  80 48 A0 01 01 48 A0 01  k2...#f..H...H..
0060: 01 74 6C 6B 30 1D 08 80  23 1D 09 80 23 66 01 80  .tlk0...#...#f..
0070: 48 A0 01 01 48 A0 01 01  74 6C 6B 31 1D 0A 80 23  H...H...tlk1...#
0080: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x001F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=10805*)
    → "My name is Ferchinne. I was tired of seeing my people suffer, so I decided to journey forth from the confines of the safehold in order to earn the title of Dragon Slayer."
  2: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0028 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Ferchinne (ID: 16883784/0x0101A048), Ferchinne (ID: 16883784/0x0101A048)], work=39*
  4: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=10806*)
    → "I trained for many months, but I feel I still lack the skills needed to defeat a truly horrifying dragon. To be a true Dragon Slayer, one must be able to soar like a dragon, not only physically, but mentally."
  5: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=10807*)
    → "Perhaps I need wings of my own to catch the winds of the endless skies..."
  7: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=10808*)
    → "The city elders told me that once, long ago, there were knights in the Kingdom of San d'Oria that could fly as high as the clouds."
  9: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0043 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Ferchinne (ID: 16883784/0x0101A048), Ferchinne (ID: 16883784/0x0101A048)], work=39*
 11: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=10809*)
    → "Brave adventurer, have you ever seen a noble bird that walks on four legs? A proud beast that has the wings of an eagle?"
 12: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0056 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Ferchinne (ID: 16883784/0x0101A048), Ferchinne (ID: 16883784/0x0101A048)], work=39*
 14: 0x0065 [0x1D] PRINT_EVENT_MESSAGE(message_id=10810*)
    → "If you come across one of these mythical creatures, I would greatly appreciate it if you removed its tailfeathers and brought them back here to me."
 15: 0x0068 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=10811*)
    → "It is said that while those feathers are unbelievably light, they are remarkably sturdy. If I were to bond them together with wax, I could make wings of my own!"
 17: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x006D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Ferchinne (ID: 16883784/0x0101A048), Ferchinne (ID: 16883784/0x0101A048)], work=39*
 19: 0x007C [0x1D] PRINT_EVENT_MESSAGE(message_id=10812*)
    → "Bring back two and I will reward you with something special."
 20: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0080 [0x21] END_EVENT
 22: 0x0081 [0x00] END_REQSTACK()
```

### Event 242

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 53 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       1E F0 FF FF 7F 1D  07 80 23 66 01 80 48 A0    ........#f..H.
0090: 01 01 48 A0 01 01 74 6C  6B 30 1D 08 80 23 1D 09  ..H...tlk0...#..
00A0: 80 23 66 01 80 48 A0 01  01 48 A0 01 01 74 6C 6B  .#f..H...H...tlk
00B0: 31 1D 0A 80 23 21 00                              1...#!.         
```

#### Opcodes

```
  0: 0x0082 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0087 [0x1D] PRINT_EVENT_MESSAGE(message_id=10809*)
    → "Brave adventurer, have you ever seen a noble bird that walks on four legs? A proud beast that has the wings of an eagle?"
  2: 0x008A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x008B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Ferchinne (ID: 16883784/0x0101A048), Ferchinne (ID: 16883784/0x0101A048)], work=39*
  4: 0x009A [0x1D] PRINT_EVENT_MESSAGE(message_id=10810*)
    → "If you come across one of these mythical creatures, I would greatly appreciate it if you removed its tailfeathers and brought them back here to me."
  5: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x009E [0x1D] PRINT_EVENT_MESSAGE(message_id=10811*)
    → "It is said that while those feathers are unbelievably light, they are remarkably sturdy. If I were to bond them together with wax, I could make wings of my own!"
  7: 0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00A2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Ferchinne (ID: 16883784/0x0101A048), Ferchinne (ID: 16883784/0x0101A048)], work=39*
  9: 0x00B1 [0x1D] PRINT_EVENT_MESSAGE(message_id=10812*)
    → "Bring back two and I will reward you with something special."
 10: 0x00B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00B5 [0x21] END_EVENT
 12: 0x00B6 [0x00] END_REQSTACK()
```

### Event 243

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 71 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      42  1E F0 FF FF 7F 1D 0B 80         B........
00C0: 23 66 01 80 48 A0 01 01  48 A0 01 01 74 6C 6B 30  #f..H...H...tlk0
00D0: 1D 0C 80 23 1D 0D 80 23  66 01 80 48 A0 01 01 48  ...#...#f..H...H
00E0: A0 01 01 74 6C 6B 31 1D  0E 80 23 45 0F 80 F8 FF  ...tlk1...#E....
00F0: FF 7F F8 FF FF 7F 71 73  74 63 10 80 21 00        ......qstc..!.  
```

#### Opcodes

```
  0: 0x00B7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00B8 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=10813*)
    → "The luster, the touch... Yes, these are the feathers that I have been searching for. Thank you so very much. Now, maybe I can fly as high as the dragons themselves!"
  3: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00C1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Ferchinne (ID: 16883784/0x0101A048), Ferchinne (ID: 16883784/0x0101A048)], work=39*
  5: 0x00D0 [0x1D] PRINT_EVENT_MESSAGE(message_id=10814*)
    → "Here, take this as a token of my appreciation."
  6: 0x00D3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00D4 [0x1D] PRINT_EVENT_MESSAGE(message_id=10815*)
    → "I was given that stone by an old merchant while traveling through the Eastern empire. He told me that it had the power to dissolve the clouds and rob mighty dragons of their ability to fly."
  8: 0x00D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00D8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Ferchinne (ID: 16883784/0x0101A048), Ferchinne (ID: 16883784/0x0101A048)], work=39*
 10: 0x00E7 [0x1D] PRINT_EVENT_MESSAGE(message_id=10816*)
    → "But even if it does not have that power, I'm sure you can find someone who will purchase it from you for a large sum of gil."
 11: 0x00EA [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x00EB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 13: 0x00FC [0x21] END_EVENT
 14: 0x00FD [0x00] END_REQSTACK()
```

### Event 244

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FE   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                            1E F0                ..
0100: FF FF 7F 1D 11 80 23 66  01 80 48 A0 01 01 48 A0  ......#f..H...H.
0110: 01 01 74 6C 6B 30 1D 12  80 23 21 00              ..tlk0...#!.    
```

#### Opcodes

```
  0: 0x00FE [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0103 [0x1D] PRINT_EVENT_MESSAGE(message_id=10817*)
    → "<Sigh> Will I ever be able to fly... Perhaps I need more feathers..."
  2: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0107 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Ferchinne (ID: 16883784/0x0101A048), Ferchinne (ID: 16883784/0x0101A048)], work=39*
  4: 0x0116 [0x1D] PRINT_EVENT_MESSAGE(message_id=10818*)
    → "I am sorry to bother you again, but if you come across any more of the legendary tailfeathers, I beg of you to bring them to me."
  5: 0x0119 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x011A [0x21] END_EVENT
  7: 0x011B [0x00] END_REQSTACK()
```

### Event 245

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011C   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                      42 1E F0 FF              B...
0120: FF 7F 1D 13 80 23 45 0F  80 F8 FF FF 7F F8 FF FF  .....#E.........
0130: 7F 71 73 74 63 10 80 21  00                       .qstc..!.       
```

#### Opcodes

```
  0: 0x011C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x011D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0122 [0x1D] PRINT_EVENT_MESSAGE(message_id=10819*)
    → "Thank you, kind [sir/adventurer]."
  3: 0x0125 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0126 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
  5: 0x0137 [0x21] END_EVENT
  6: 0x0138 [0x00] END_REQSTACK()
```
