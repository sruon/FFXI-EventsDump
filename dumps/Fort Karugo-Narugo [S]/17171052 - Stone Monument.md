# 17171052 - Stone Monument

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
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
|       0 | 0x1E87      |        7815 |
|       1 | 0x1E88      |        7816 |
|       2 | 0x1E89      |        7817 |
|       3 | 0x1E8A      |        7818 |
|       4 | 0x1E8B      |        7819 |
|       5 | 0x1E8C      |        7820 |

## String References

- **7815**: You see a message engraved on the stone:
- **7816**: With an unfailingly cheerful Tarutaru friend as a guide, I came to tour Fort Karugo-Narugo, the centerpiece of Windurst's defenses.
- **7817**: My invitation to the complex, indeed, the complete access I enjoyed as a San d'Orian, even considering the deep ties I had developed, had less to do with their trust in me, and more to do with their own confidence.
- **7818**: "Fivespires," as the towers within the fortress were called, had been constructed and spaced in accordance with Minister Medada's precise arcane calculations. Such a configuration was said to withstand all manner of physical and magical assaults.
- **7819**: When I broached the seemingly foolish matter of a perfect configuration being vulnerable to the slightest imperfection, I was greeted with gales of laughter. How could such a perfect construction ever be marred? I hope for their sake, they are right.
- **7820**: @ --Enid Ironheart, 778 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7815*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7816*]:
    → "With an unfailingly cheerful Tarutaru friend as a guide, I came to tour Fort Karugo-Narugo, the centerpiece of Windurst's defenses."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7817*]:
    → "My invitation to the complex, indeed, the complete access I enjoyed as a San d'Orian, even considering the deep ties I had developed, had less to do with their trust in me, and more to do with their own confidence."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7818*]:
    → ""Fivespires," as the towers within the fortress were called, had been constructed and spaced in accordance with Minister Medada's precise arcane calculations. Such a configuration was said to withstand all manner of physical and magical assaults."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7819*]:
    → "When I broached the seemingly foolish matter of a perfect configuration being vulnerable to the slightest imperfection, I was greeted with gales of laughter. How could such a perfect construction ever be marred? I hope for their sake, they are right."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7820*]:
    → "@ --Enid Ironheart, 778 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
