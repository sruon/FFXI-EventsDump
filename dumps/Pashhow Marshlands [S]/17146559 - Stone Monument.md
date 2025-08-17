# 17146559 - Stone Monument

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Pashhow Marshlands [S] (ID: 90) |
| Block Size       | 76 bytes                        |
| Total Events     | 2                               |
| References Count | 6                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [900](#event-900)     | 0x0001       |     26 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E2F      |        7727 |
|       1 | 0x1E30      |        7728 |
|       2 | 0x1E31      |        7729 |
|       3 | 0x1E32      |        7730 |
|       4 | 0x1E33      |        7731 |
|       5 | 0x1E34      |        7732 |

## String References

- **7727**: You see a message engraved on the stone:
- **7728**: These marshlands belong to a savage race of beastmen called the Quadav. Many have ventured in these lands seeking fame and fortune, but were never seen again.
- **7729**: But I have vowed to make a complete map of Vana'diel--the guilt I would feel for leaving these marshlands blank far outweighed the danger of entering them.
- **7730**: During my survey, I made the mistake of building a fire and was promptly captured by the Quadav. In their village, I was dumbstruck to see that their buildings were made of wrought metal!
- **7731**: As much as we use the Tarutaru magic of fire to light our smoking-pipes, the Quadav--a barbarous tribe by any account--had secretly harnessed much of Bastok's metalworking technology.
- **7732**: When I told them of my quest, they were most eager to help, releasing me and even going so far as to give me a guided tour of their home! --Gwynham Ironheart, 763 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7727*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7728*]:
    → "These marshlands belong to a savage race of beastmen called the Quadav. Many have ventured in these lands seeking fame and fortune, but were never seen again."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7729*]:
    → "But I have vowed to make a complete map of Vana'diel--the guilt I would feel for leaving these marshlands blank far outweighed the danger of entering them."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7730*]:
    → "During my survey, I made the mistake of building a fire and was promptly captured by the Quadav. In their village, I was dumbstruck to see that their buildings were made of wrought metal!"
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7731*]:
    → "As much as we use the Tarutaru magic of fire to light our smoking-pipes, the Quadav--a barbarous tribe by any account--had secretly harnessed much of Bastok's metalworking technology."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7732*]:
    → "When I told them of my quest, they were most eager to help, releasing me and even going so far as to give me a guided tour of their home! --Gwynham Ironheart, 763 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
