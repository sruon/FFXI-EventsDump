# 17253065 - Stone Monument

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | East Sarutabaruta (ID: 116) |
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
|       0 | 0x1D23      |        7459 |
|       1 | 0x1D24      |        7460 |
|       2 | 0x1D25      |        7461 |
|       3 | 0x1D26      |        7462 |
|       4 | 0x1D27      |        7463 |
|       5 | 0x1D28      |        7464 |

## String References

- **7459**: You see a message engraved on the stone:
- **7460**: It is clear from my research that, in addition to the endearing Tarutaru and the unsophisticated Mithra, a third race once lived here on the plains of Sarutabaruta.
- **7461**: The ancient towers that the Tarutaru call the "Horutoto Ruins" look to have been made for people their size, but there are peculiar differences in design and style.
- **7462**: Indeed, they closely resemble the "Tower Like a Hand" in a sketch my father Gwynham once sent me.
- **7463**: Yet the tower he saw was in Valdeaunia in the north of Quon, a great distance from its counterparts here. Clearly, an advanced civilization once covered this world.
- **7464**: I believe I can still hear its echoes in Vana'diel today, or perhaps it is just my imagination running wild. --Enid Ironheart, 777 Crystal Era.

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
  0: 0x0001 [0x48] [System] [7459*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7460*]:
    → "It is clear from my research that, in addition to the endearing Tarutaru and the unsophisticated Mithra, a third race once lived here on the plains of Sarutabaruta."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7461*]:
    → "The ancient towers that the Tarutaru call the "Horutoto Ruins" look to have been made for people their size, but there are peculiar differences in design and style."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7462*]:
    → "Indeed, they closely resemble the "Tower Like a Hand" in a sketch my father Gwynham once sent me."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7463*]:
    → "Yet the tower he saw was in Valdeaunia in the north of Quon, a great distance from its counterparts here. Clearly, an advanced civilization once covered this world."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7464*]:
    → "I believe I can still hear its echoes in Vana'diel today, or perhaps it is just my imagination running wild. --Enid Ironheart, 777 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
