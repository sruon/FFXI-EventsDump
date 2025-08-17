# 17216175 - Stone Monument

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | South Gustaberg (ID: 107) |
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
|       0 | 0x1D04      |        7428 |
|       1 | 0x1D05      |        7429 |
|       2 | 0x1D06      |        7430 |
|       3 | 0x1D07      |        7431 |
|       4 | 0x1D08      |        7432 |
|       5 | 0x1D09      |        7433 |

## String References

- **7428**: You see a message engraved on the stone:
- **7429**: I've been a sailor for over forty years, yet I cannot grasp the concept of the world as a whole. Then again, those who live in cities know even less than I.
- **7430**: They are content knowing only of the things around them. I cannot blame them for choosing to live this way, as curiosity is, more often than not, a dangerous trait.
- **7431**: But I have sworn to use the rest of my life--a life I had once thought lost when I was shipwrecked--to indulge this insatiable curiosity of mine, and to uncover the truths of Vana'diel.
- **7432**: I have decided to leave my first message here, on this hill overlooking my homeland of Bastok. It is the first record of a journey that I hope will benefit all the peoples of Vana'diel.
- **7433**: --Gwynham Ironheart, 748 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7428*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7429*]:
    → "I've been a sailor for over forty years, yet I cannot grasp the concept of the world as a whole. Then again, those who live in cities know even less than I."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7430*]:
    → "They are content knowing only of the things around them. I cannot blame them for choosing to live this way, as curiosity is, more often than not, a dangerous trait."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7431*]:
    → "But I have sworn to use the rest of my life--a life I had once thought lost when I was shipwrecked--to indulge this insatiable curiosity of mine, and to uncover the truths of Vana'diel."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7432*]:
    → "I have decided to leave my first message here, on this hill overlooking my homeland of Bastok. It is the first record of a journey that I hope will benefit all the peoples of Vana'diel."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7433*]:
    → "--Gwynham Ironheart, 748 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
