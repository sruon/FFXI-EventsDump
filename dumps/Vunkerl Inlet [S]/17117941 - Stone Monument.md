# 17117941 - Stone Monument

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Vunkerl Inlet [S] (ID: 83) |
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
|       0 | 0x1E1A      |        7706 |
|       1 | 0x1E1B      |        7707 |
|       2 | 0x1E1C      |        7708 |
|       3 | 0x1E1D      |        7709 |
|       4 | 0x1E1E      |        7710 |
|       5 | 0x1E1F      |        7711 |

## String References

- **7706**: You see a message engraved on the stone:
- **7707**: My sojourn into Vunkerl Inlet was naturally motivated by cartography rather than simple curiosity. But I must be honest. There was another desire that quickened my stride.
- **7708**: The waters of this inlet are fed by both the warm currents of the Bastore Sea and the cold currents of the Sea of Shu'Meyo. Perhaps you now understand my excitement. To the best of my knowledge, Vunkerl Inlet is second-to-none as a fishing paradise.
- **7709**: My mounting excitement was cruelly dashed by footfalls that echoed like peals of thunder. I ducked under cover in time to witness several Gigas pass right before my hiding spot. I guessed these to be brigands from the north, landed here to plunder and pillage.
- **7710**: The Gigas wore a number of round shields hanging from their waists, of curiously small proportion to their size. My thoughts ran to the vikings rumored to inhabit the islands in the northern ocean. There would be no fishing for me here.
- **7711**: @ --Gwynham Ironheart, 758 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7706*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7707*]:
    → "My sojourn into Vunkerl Inlet was naturally motivated by cartography rather than simple curiosity. But I must be honest. There was another desire that quickened my stride."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7708*]:
    → "The waters of this inlet are fed by both the warm currents of the Bastore Sea and the cold currents of the Sea of Shu'Meyo. Perhaps you now understand my excitement. To the best of my knowledge, Vunkerl Inlet is second-to-none as a fishing paradise."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7709*]:
    → "My mounting excitement was cruelly dashed by footfalls that echoed like peals of thunder. I ducked under cover in time to witness several Gigas pass right before my hiding spot. I guessed these to be brigands from the north, landed here to plunder and pillage."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7710*]:
    → "The Gigas wore a number of round shields hanging from their waists, of curiously small proportion to their size. My thoughts ran to the vikings rumored to inhabit the islands in the northern ocean. There would be no fishing for me here."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7711*]:
    → "@ --Gwynham Ironheart, 758 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
