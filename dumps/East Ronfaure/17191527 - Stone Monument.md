# 17191527 - Stone Monument

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | East Ronfaure (ID: 101) |
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
|       0 | 0x1D2B      |        7467 |
|       1 | 0x1D2C      |        7468 |
|       2 | 0x1D2D      |        7469 |
|       3 | 0x1D2E      |        7470 |
|       4 | 0x1D2F      |        7471 |
|       5 | 0x1D30      |        7472 |

## String References

- **7467**: You see a message engraved on the stone:
- **7468**: These woods of Ronfaure have long been hunting grounds of the Elvaan royalty, and as such are maintained well.
- **7469**: I came here to see the bravery of the participants in the great autumn hunt, but sadly it was a somber ceremonial affair with little to see.
- **7470**: I am certain that this stems from the choice of quarry: no longer do they hunt fowl or deer. Rather, giant sheep are released expressly for the hunt.
- **7471**: As I write this, I pray that the gluttonous grazing of these voracious sheep does not destroy the delicate balance of life in these woods.
- **7472**: --Gwynham Ironheart, 751 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7467*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7468*]:
    → "These woods of Ronfaure have long been hunting grounds of the Elvaan royalty, and as such are maintained well."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7469*]:
    → "I came here to see the bravery of the participants in the great autumn hunt, but sadly it was a somber ceremonial affair with little to see."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7470*]:
    → "I am certain that this stems from the choice of quarry: no longer do they hunt fowl or deer. Rather, giant sheep are released expressly for the hunt."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7471*]:
    → "As I write this, I pray that the gluttonous grazing of these voracious sheep does not destroy the delicate balance of life in these woods."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7472*]:
    → "--Gwynham Ironheart, 751 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
