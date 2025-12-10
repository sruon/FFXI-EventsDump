# 17212049 - Stone Monument

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | North Gustaberg (ID: 106) |
| Block Size       | 76 bytes                  |
| Total Events     | 2                         |
| References Count | 6                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [900](#event-900)     | 0x0001       |     26 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D29      |        7465 |
|       1 | 0x1D2A      |        7466 |
|       2 | 0x1D2B      |        7467 |
|       3 | 0x1D2C      |        7468 |
|       4 | 0x1D2D      |        7469 |
|       5 | 0x1D2E      |        7470 |

## String References

- **7465**: You see a message engraved on the stone:
- **7466**: As I passed through this area, I heard Bastokers were building a monument honoring the pioneers who dug the Palborough Mines. Being the curious type, I went to visit the site.
- **7467**: The site itself turned out to be an old cemetery, where the tombstones were so old, the names were worn away with age.
- **7468**: It turned out that the graves were those of numerous Galka who died in an accident the day the Metalworks was completed, in a time when Bastok was still struggling to become a nation.
- **7469**: I do not know if the Palborough Pioneers are the heroes people claim they are. I, for a fact, have no doubt the Galka who lie here gave their lives bravely to settle this arid, forsaken land.
- **7470**: I decided to spend a night here, drinking to the unnamed heroes of a forgotten time. --Gwynham Ironheart, 749 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7465*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7466*]:
    → "As I passed through this area, I heard Bastokers were building a monument honoring the pioneers who dug the Palborough Mines. Being the curious type, I went to visit the site."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7467*]:
    → "The site itself turned out to be an old cemetery, where the tombstones were so old, the names were worn away with age."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7468*]:
    → "It turned out that the graves were those of numerous Galka who died in an accident the day the Metalworks was completed, in a time when Bastok was still struggling to become a nation."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7469*]:
    → "I do not know if the Palborough Pioneers are the heroes people claim they are. I, for a fact, have no doubt the Galka who lie here gave their lives bravely to settle this arid, forsaken land."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7470*]:
    → "I decided to spend a night here, drinking to the unnamed heroes of a forgotten time. --Gwynham Ironheart, 749 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
