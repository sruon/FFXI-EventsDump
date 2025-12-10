# 17228356 - Stone Monument

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Rolanberry Fields (ID: 110) |
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
|       0 | 0x1CFD      |        7421 |
|       1 | 0x1CFE      |        7422 |
|       2 | 0x1CFF      |        7423 |
|       3 | 0x1D00      |        7424 |
|       4 | 0x1D01      |        7425 |
|       5 | 0x1D02      |        7426 |

## String References

- **7421**: You see a message engraved on the stone:
- **7422**: Here where the warm Garuda winds blow, rolanberries are cultivated in great orchards.
- **7423**: These berries are famous for their sharp, tingling tartness. And it's not just the Galka who appreciate a rolanberry pie to cleanse the palate after a meal.
- **7424**: These humble berries also warm the hearts of carnivorous beastmen, and guards have been posted against Goblin thieves and Yagudo raiders.
- **7425**: The most valuable berries are stockpiled by insects, who use a special secretion to store them. This results in an exceptionally tart preserve, popular with connoisseurs.
- **7426**: The village of Jeuno has benefited greatly from the harvests here, and the bounty of the sea. They seem well on their way to statehood. --Gwynham Ironheart, 757 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7421*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7422*]:
    → "Here where the warm Garuda winds blow, rolanberries are cultivated in great orchards."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7423*]:
    → "These berries are famous for their sharp, tingling tartness. And it's not just the Galka who appreciate a rolanberry pie to cleanse the palate after a meal."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7424*]:
    → "These humble berries also warm the hearts of carnivorous beastmen, and guards have been posted against Goblin thieves and Yagudo raiders."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7425*]:
    → "The most valuable berries are stockpiled by insects, who use a special secretion to store them. This results in an exceptionally tart preserve, popular with connoisseurs."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7426*]:
    → "The village of Jeuno has benefited greatly from the harvests here, and the bounty of the sea. They seem well on their way to statehood. --Gwynham Ironheart, 757 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
