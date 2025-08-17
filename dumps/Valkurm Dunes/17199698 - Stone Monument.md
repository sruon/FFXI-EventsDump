# 17199698 - Stone Monument

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Valkurm Dunes (ID: 103) |
| Block Size       | 76 bytes                |
| Total Events     | 2                       |
| References Count | 6                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [900](#event-900)     | 0x0001       |     26 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CCC      |        7372 |
|       1 | 0x1CCD      |        7373 |
|       2 | 0x1CCE      |        7374 |
|       3 | 0x1CCF      |        7375 |
|       4 | 0x1CD0      |        7376 |
|       5 | 0x1CD1      |        7377 |

## String References

- **7372**: You see a message engraved on the stone:
- **7373**: The view may be beautiful, but the broken grass at our feet is testimony to the inhospitality of this place. The shallows repel anchoring ships, with nothing for miles but sand. Indeed, these dunes are ill-fit for any purpose save sunbathing.
- **7374**: One day I happened upon a young swimmer struggling for air. I swam out to save her, and as a gesture of thanks she led me to a fascinating place.
- **7375**: To a small inlet she guided me, to show me dolphins, no doubt. None were there, but I noticed the bay was a natural harbor. I was a sailor in youth, so I knew this to be an important discovery!
- **7376**: The harbor I named "Selbina." Upon seeing her own name inscribed on my map, the girl clapped her hands in joy.
- **7377**: --Gwynham Ironheart, 762 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7372*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7373*]:
    → "The view may be beautiful, but the broken grass at our feet is testimony to the inhospitality of this place. The shallows repel anchoring ships, with nothing for miles but sand. Indeed, these dunes are ill-fit for any purpose save sunbathing."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7374*]:
    → "One day I happened upon a young swimmer struggling for air. I swam out to save her, and as a gesture of thanks she led me to a fascinating place."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7375*]:
    → "To a small inlet she guided me, to show me dolphins, no doubt. None were there, but I noticed the bay was a natural harbor. I was a sailor in youth, so I knew this to be an important discovery!"
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7376*]:
    → "The harbor I named "Selbina." Upon seeing her own name inscribed on my map, the girl clapped her hands in joy."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7377*]:
    → "--Gwynham Ironheart, 762 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
