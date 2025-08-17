# 17195622 - Stone Monument

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
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
|       0 | 0x1D17      |        7447 |
|       1 | 0x1D18      |        7448 |
|       2 | 0x1D19      |        7449 |
|       3 | 0x1D1A      |        7450 |
|       4 | 0x1D1B      |        7451 |
|       5 | 0x1D1C      |        7452 |

## String References

- **7447**: You see a message engraved on the stone:
- **7448**: This plateau is a land of many features, but by far the most memorable is the Crag of Holla.
- **7449**: I call it a structure, for I have no other word. It is surely not a rock born of nature, nor does it seem to be a hall built by the gods, as the priestly scholars say.
- **7450**: Yet there are no seams in its bone-white surface, and it is faintly warm to the touch. But through a fortunate accident, I have found proof of its artificial origins.
- **7451**: I shall head north to the land of Valdeaunia to verify my findings. I fear this may be the longest, most perilous journey of my life.
- **7452**: I leave my daughter Enid to find her own path. May the gods watch over her in my stead. --Gwynham Ironheart, 764 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7447*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7448*]:
    → "This plateau is a land of many features, but by far the most memorable is the Crag of Holla."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7449*]:
    → "I call it a structure, for I have no other word. It is surely not a rock born of nature, nor does it seem to be a hall built by the gods, as the priestly scholars say."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7450*]:
    → "Yet there are no seams in its bone-white surface, and it is faintly warm to the touch. But through a fortunate accident, I have found proof of its artificial origins."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7451*]:
    → "I shall head north to the land of Valdeaunia to verify my findings. I fear this may be the longest, most perilous journey of my life."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7452*]:
    → "I leave my daughter Enid to find her own path. May the gods watch over her in my stead. --Gwynham Ironheart, 764 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
