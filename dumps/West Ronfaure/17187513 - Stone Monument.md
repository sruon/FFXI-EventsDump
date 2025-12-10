# 17187513 - Stone Monument

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | West Ronfaure (ID: 100) |
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
|       0 | 0x1D06      |        7430 |
|       1 | 0x1D07      |        7431 |
|       2 | 0x1D08      |        7432 |
|       3 | 0x1D09      |        7433 |
|       4 | 0x1D0A      |        7434 |
|       5 | 0x1D0B      |        7435 |

## String References

- **7430**: You see a message engraved on the stone:
- **7431**: It has been a full ten years since I last visited this land, yet I am shocked to see Orcish warriors roaming this far south!
- **7432**: I saw many here in this forest, the very lap of the Kingdom, but the proud Elvaan knights don't consider them a threat.
- **7433**: Mark my words! Someday, hundreds--no--thousands of Orcs will bring war upon this beautiful kingdom.
- **7434**: I write this in hope that brave knights will prove me wrong.
- **7435**: --Gwynham Ironheart, 761 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7430*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7431*]:
    → "It has been a full ten years since I last visited this land, yet I am shocked to see Orcish warriors roaming this far south!"
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7432*]:
    → "I saw many here in this forest, the very lap of the Kingdom, but the proud Elvaan knights don't consider them a threat."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7433*]:
    → "Mark my words! Someday, hundreds--no--thousands of Orcs will bring war upon this beautiful kingdom."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7434*]:
    → "I write this in hope that brave knights will prove me wrong."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7435*]:
    → "--Gwynham Ironheart, 761 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
