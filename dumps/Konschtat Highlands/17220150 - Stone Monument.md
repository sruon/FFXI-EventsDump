# 17220150 - Stone Monument

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Konschtat Highlands (ID: 108) |
| Block Size       | 76 bytes                      |
| Total Events     | 2                             |
| References Count | 6                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [900](#event-900)     | 0x0001       |     26 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CF0      |        7408 |
|       1 | 0x1CF1      |        7409 |
|       2 | 0x1CF2      |        7410 |
|       3 | 0x1CF3      |        7411 |
|       4 | 0x1CF4      |        7412 |
|       5 | 0x1CF5      |        7413 |

## String References

- **7408**: You see a message engraved on the stone:
- **7409**: The wind that blows incessantly through this area is called "Odin's Wrath." Seeing its potential use, some ingenious Bastokers decided to build windmills here, a long time ago.
- **7410**: Flourmills, to be exact. In this desolate land where nothing more than potatoes can grow, the wheat brought in from San d'Oria was a true lifesaver to Bastokers.
- **7411**: San d'Oria, in turn, relied on their consumption of its surplus wheat, and also on the flour that came back from Bastok's mills. The mills became the symbols of their mutual dependence.
- **7412**: Even in times of war between the two, this trade continued. Both armies' brass were infuriated, but none tried to disrupt it lest the bread disappeared from their own tables! Ah, the irony!
- **7413**: A toast, to the merchants! --Gwynham Ironheart, 750 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7408*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7409*]:
    → "The wind that blows incessantly through this area is called "Odin's Wrath." Seeing its potential use, some ingenious Bastokers decided to build windmills here, a long time ago."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7410*]:
    → "Flourmills, to be exact. In this desolate land where nothing more than potatoes can grow, the wheat brought in from San d'Oria was a true lifesaver to Bastokers."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7411*]:
    → "San d'Oria, in turn, relied on their consumption of its surplus wheat, and also on the flour that came back from Bastok's mills. The mills became the symbols of their mutual dependence."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7412*]:
    → "Even in times of war between the two, this trade continued. Both armies' brass were infuriated, but none tried to disrupt it lest the bread disappeared from their own tables! Ah, the irony!"
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7413*]:
    → "A toast, to the merchants! --Gwynham Ironheart, 750 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
