# 17134046 - Wilhelmina

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 200 bytes                   |
| Total Events     | 4                           |
| References Count | 11                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [147](#event-147)     | 0x0001       |     33 |              9 |
| [192](#event-192)     | 0x0022       |     76 |             20 |
| [195](#event-195)     | 0x006E       |     14 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x000A      |          10 |
|       2 | 0x3013      |       12307 |
|       3 | 0x3014      |       12308 |
|       4 | 0x3370      |       13168 |
|       5 | 0x0007      |           7 |
|       6 | 0x005A      |          90 |
|       7 | 0x3371      |       13169 |
|       8 | 0x3372      |       13170 |
|       9 | 0x3373      |       13171 |
|      10 | 0x3374      |       13172 |

## String References

- **12307**: Have you heard the rumors? There have been several sightings of these so-called "maws" outside the city. People are saying they may have been unleashed by the beasthordes!
- **12308**: All accounts claim that they float just above ground, wreathing about, with gaping mouths like great voids that never shut... It gives me the chills just to think about it.
- **13168**: What? You're on the trail of Darksteel Hurricane!? Well, you don't seem to be crazy, so I gather you're either a musketeer or part of that surly military police outfit.
- **13169**: Not that that has any bearing on a law-abiding citizen like me, of course. But getting back on subject, I take it you already know that he wears a menacing scar on his forehead.
- **13170**: Those who've met a brutal end by his cruel hand have all turned up with an identical wound carved into their foreheads.
- **13171**: Speculation abounds on his motives, but if you ask me, only vengeance can so fuel a man's desire for blood.
- **13172**: Just thinking about it makes my skin crawl. You certainly won't catch me going on late-night strolls any more. Nor do I intend to linger in the presence of a Galka whose forehead I cannot see. I advise you to do the same!

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

### Event 147

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  1D 02 80 23 1D 03 80 23  ....tlk0...#...#
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=12307*)
    → "Have you heard the rumors? There have been several sightings of these so-called "maws" outside the city. People are saying they may have been unleashed by the beasthordes!"
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=12308*)
    → "All accounts claim that they float just above ground, wreathing about, with gaping mouths like great voids that never shut... It gives me the chills just to think about it."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x21] END_EVENT
  8: 0x0021 [0x00] END_REQSTACK()
```

### Event 192

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 76 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       42 1E F0 FF FF 7F  1C 00 80 1D 04 80 23 6E    B...........#n
0030: F0 FF FF 7F 05 80 99 F0  FF FF 7F 1C 06 80 66 01  ..............f.
0040: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 07 80  .........tlk0...
0050: 23 1D 08 80 23 1D 09 80  23 66 01 80 F8 FF FF 7F  #...#...#f......
0060: F8 FF FF 7F 74 6C 6B 31  1D 0A 80 23 21 00        ....tlk1...#!.  
```

#### Opcodes

```
  0: 0x0022 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0023 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0028 [0x1C] WAIT(30* ticks)
  3: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=13168*)
    → "What? You're on the trail of Darksteel Hurricane!? Well, you don't seem to be crazy, so I gather you're either a musketeer or part of that surly military police outfit."
  4: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x002F [0x6E] LocalPlayer uses emote 7*
  6: 0x0036 [0x99] Wait for LocalPlayer animation to complete
  7: 0x003B [0x1C] WAIT(90* ticks)
  8: 0x003E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
  9: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=13169*)
    → "Not that that has any bearing on a law-abiding citizen like me, of course. But getting back on subject, I take it you already know that he wears a menacing scar on his forehead."
 10: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=13170*)
    → "Those who've met a brutal end by his cruel hand have all turned up with an identical wound carved into their foreheads."
 12: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=13171*)
    → "Speculation abounds on his motives, but if you ask me, only vengeance can so fuel a man's desire for blood."
 14: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0059 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=10*
 16: 0x0068 [0x1D] PRINT_EVENT_MESSAGE(message_id=13172*)
    → "Just thinking about it makes my skin crawl. You certainly won't catch me going on late-night strolls any more. Nor do I intend to linger in the presence of a Galka whose forehead I cannot see. I advise you to do the same!"
 17: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x006C [0x21] END_EVENT
 19: 0x006D [0x00] END_REQSTACK()
```

### Event 195

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            1E F0                ..
0070: FF FF 7F 1C 00 80 1D 0A  80 23 21 00              .........#!.    
```

#### Opcodes

```
  0: 0x006E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0073 [0x1C] WAIT(30* ticks)
  2: 0x0076 [0x1D] PRINT_EVENT_MESSAGE(message_id=13172*)
    → "Just thinking about it makes my skin crawl. You certainly won't catch me going on late-night strolls any more. Nor do I intend to linger in the presence of a Galka whose forehead I cannot see. I advise you to do the same!"
  3: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x007A [0x21] END_EVENT
  5: 0x007B [0x00] END_REQSTACK()
```
