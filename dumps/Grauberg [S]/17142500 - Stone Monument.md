# 17142500 - Stone Monument

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Grauberg [S] (ID: 89) |
| Block Size       | 76 bytes              |
| Total Events     | 2                     |
| References Count | 6                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [900](#event-900)     | 0x0001       |     26 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E21      |        7713 |
|       1 | 0x1E22      |        7714 |
|       2 | 0x1E23      |        7715 |
|       3 | 0x1E24      |        7716 |
|       4 | 0x1E25      |        7717 |
|       5 | 0x1E26      |        7718 |

## String References

- **7713**: You see a message engraved on the stone:
- **7714**: Having never planned on surveying the inland regions, I'd had not the slightest intention of setting foot in Grauberg. A sailor first and foremost, mountain climbing was most certainly not my strong suit.
- **7715**: However, my journey relies on the financial support I receive from my homeland. I could not ignore the whims of my benefactors, no matter how foolish they seemed to me. If they wished to construct a base on this natural fortress, who was I to question?
- **7716**: It was just as I was beginning to enjoy the surprisingly pleasant trail and serenity of my surroundings, when my legs were crushed under a sudden landslide. I was halfway up a mountain, far from any semblance of civilization. Even my optimistic spirit sensed the end was near.
- **7717**: I lost consciousness from the pain, floating in oblivion for the goddess knows how long. I woke to the sound of tinkling laughter, and for the briefest of moments caught sight of tiny figures flitting through the air on insect wings. My shattered legs were completely healed. The report I sent advised against building a base in Grauberg.
- **7718**: @ --Gwynham Ironheart, 762 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7713*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7714*]:
    → "Having never planned on surveying the inland regions, I'd had not the slightest intention of setting foot in Grauberg. A sailor first and foremost, mountain climbing was most certainly not my strong suit."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7715*]:
    → "However, my journey relies on the financial support I receive from my homeland. I could not ignore the whims of my benefactors, no matter how foolish they seemed to me. If they wished to construct a base on this natural fortress, who was I to question?"
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7716*]:
    → "It was just as I was beginning to enjoy the surprisingly pleasant trail and serenity of my surroundings, when my legs were crushed under a sudden landslide. I was halfway up a mountain, far from any semblance of civilization. Even my optimistic spirit sensed the end was near."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7717*]:
    → "I lost consciousness from the pain, floating in oblivion for the goddess knows how long. I woke to the sound of tinkling laughter, and for the briefest of moments caught sight of tiny figures flitting through the air on insect wings. My shattered legs were completely healed. The report I sent advised against building a base in Grauberg."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7718*]:
    → "@ --Gwynham Ironheart, 762 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
