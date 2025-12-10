# 17265242 - Stone Monument

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Meriphataud Mountains (ID: 119) |
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
|       0 | 0x1ED5      |        7893 |
|       1 | 0x1ED6      |        7894 |
|       2 | 0x1ED7      |        7895 |
|       3 | 0x1ED8      |        7896 |
|       4 | 0x1ED9      |        7897 |
|       5 | 0x1EDA      |        7898 |

## String References

- **7893**: You see a message engraved on the stone:
- **7894**: Drogaroga's Spine: Tarutaru for "Spine of the Heavenly Dragon." It is made of that same mysterious white material as the holy crags.
- **7895**: However, this is the first I've seen so exposed. A good portion of it is suspended in open space, no less.
- **7896**: In San d'Oria, the papsque claims that they were monuments built by Altana in honor of the Elvaan. All believed him, but I feel that this cannot be true.
- **7897**: This is merely conjecture, but I feel they resemble some kind of road or pipeline... But carrying what? If only I could show my father.
- **7898**: The white crags, spines, points, and lines... What did my father discover at the end of his journey? I wish I knew. --Enid Ironheart, 778 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7893*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7894*]:
    → "Drogaroga's Spine: Tarutaru for "Spine of the Heavenly Dragon." It is made of that same mysterious white material as the holy crags."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7895*]:
    → "However, this is the first I've seen so exposed. A good portion of it is suspended in open space, no less."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7896*]:
    → "In San d'Oria, the papsque claims that they were monuments built by Altana in honor of the Elvaan. All believed him, but I feel that this cannot be true."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7897*]:
    → "This is merely conjecture, but I feel they resemble some kind of road or pipeline... But carrying what? If only I could show my father."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7898*]:
    → "The white crags, spines, points, and lines... What did my father discover at the end of his journey? I wish I knew. --Enid Ironheart, 778 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
