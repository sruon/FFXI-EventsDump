# 17113888 - Stone Monument

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 76 bytes                   |
| Total Events     | 2                          |
| References Count | 6                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [900](#event-900)     | 0x0001       |     26 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E52      |        7762 |
|       1 | 0x1E53      |        7763 |
|       2 | 0x1E54      |        7764 |
|       3 | 0x1E55      |        7765 |
|       4 | 0x1E56      |        7766 |
|       5 | 0x1E57      |        7767 |

## String References

- **7762**: You see a message engraved on the stone:
- **7763**: As we pierced the gloom of Jugner Forest, my dear steed (and renowned gourmand) Morten pecked at the ground, unearthing a fine mushroom.
- **7764**: Quieting the uneasy Morten, I examined the mushroom, and found that it was none other than a King Truffle, a prized ingredient I had thought to be only a legend.
- **7765**: Relying on Morten's keen sense of smell, we searched the area, and found bushels of other mushrooms. A fine mushroom soup will grace our table tonight.
- **7766**: To all travelers who wander in this forest--should you find your supplies dwindling and your hunger growing, search for nature's bounty and be saved!
- **7767**: Just take care your chocobo does not eat them first! --Gwynham Ironheart, 755 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7762*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7763*]:
    → "As we pierced the gloom of Jugner Forest, my dear steed (and renowned gourmand) Morten pecked at the ground, unearthing a fine mushroom."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7764*]:
    → "Quieting the uneasy Morten, I examined the mushroom, and found that it was none other than a King Truffle, a prized ingredient I had thought to be only a legend."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7765*]:
    → "Relying on Morten's keen sense of smell, we searched the area, and found bushels of other mushrooms. A fine mushroom soup will grace our table tonight."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7766*]:
    → "To all travelers who wander in this forest--should you find your supplies dwindling and your hunger growing, search for nature's bounty and be saved!"
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7767*]:
    → "Just take care your chocobo does not eat them first! --Gwynham Ironheart, 755 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
