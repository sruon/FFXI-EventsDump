# 17248819 - Stone Monument

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 76 bytes                    |
| Total Events     | 2                           |
| References Count | 6                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [900](#event-900)     | 0x0001       |     26 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D10      |        7440 |
|       1 | 0x1D11      |        7441 |
|       2 | 0x1D12      |        7442 |
|       3 | 0x1D13      |        7443 |
|       4 | 0x1D14      |        7444 |
|       5 | 0x1D15      |        7445 |

## String References

- **7440**: You see a message engraved on the stone:
- **7441**: Now, five years after I first crossed the Jeuno Straits and began my slow southward survey of Mindartia, I have arrived at the southernmost land: the plains of Sarutabaruta.
- **7442**: The Tarutaru who live here are a kind and friendly people; it is hard to believe their ancestors plotted the conquest of the world during the age of great magic.
- **7443**: They, too, worship the Goddess Altana, yet they believe that She has a form here on Vana'diel called the Star Sibyl, who lives in a giant tree.
- **7444**: I met the Star Sibyl, and she took my hand and spoke to me of everything from the current state of our world to the unseeable future. It was a wonderful experience.
- **7445**: The Tarutaru have agreed to give me a magical ship to speed the rest of my survey. I thank the Sibyl, and her kind people. --Enid Ironheart, 778 Crystal Era.

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

### Event 900

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 48 01 80  23 48 02 80 23 48 03 80   H..#H..#H..#H..
0010: 23 48 04 80 23 48 05 80  23 21 00                 #H..#H..#!.     
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7440*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7441*]:
    → "Now, five years after I first crossed the Jeuno Straits and began my slow southward survey of Mindartia, I have arrived at the southernmost land: the plains of Sarutabaruta."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7442*]:
    → "The Tarutaru who live here are a kind and friendly people; it is hard to believe their ancestors plotted the conquest of the world during the age of great magic."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7443*]:
    → "They, too, worship the Goddess Altana, yet they believe that She has a form here on Vana'diel called the Star Sibyl, who lives in a giant tree."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7444*]:
    → "I met the Star Sibyl, and she took my hand and spoke to me of everything from the current state of our world to the unseeable future. It was a wonderful experience."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7445*]:
    → "The Tarutaru have agreed to give me a magical ship to speed the rest of my survey. I thank the Sibyl, and her kind people. --Enid Ironheart, 778 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
