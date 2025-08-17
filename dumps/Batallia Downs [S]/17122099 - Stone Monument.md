# 17122099 - Stone Monument

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Batallia Downs [S] (ID: 84) |
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
|       0 | 0x1E33      |        7731 |
|       1 | 0x1E34      |        7732 |
|       2 | 0x1E35      |        7733 |
|       3 | 0x1E36      |        7734 |
|       4 | 0x1E37      |        7735 |
|       5 | 0x1E38      |        7736 |

## String References

- **7731**: You see a message engraved on the stone:
- **7732**: I have come to a place with countless mounds of earth. According to legend, it was here that our ancestors, created by the Goddess, first descended to Vana'diel.
- **7733**: Since time immemorial, elderly Elvaan have come here to await their final rest. Many pilgrims of other races, too, have ended their journeys here, wishing to be close to the Nurturer.
- **7734**: Of course, faith and discipline are virtues. But life is to be enjoyed, and the lives of others respected. Faith can wait until these two things are accomplished.
- **7735**: I told this to a Galka friend, and he bellowed a hearty laugh. Yet I could see his point: those who only live a short while have no time for such thoughts.
- **7736**: To think of these things and wonder is the duty of the living. --Gwynham Ironheart, 759 Crystal Era

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
  0: 0x0001 [0x48] [System] [7731*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7732*]:
    → "I have come to a place with countless mounds of earth. According to legend, it was here that our ancestors, created by the Goddess, first descended to Vana'diel."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7733*]:
    → "Since time immemorial, elderly Elvaan have come here to await their final rest. Many pilgrims of other races, too, have ended their journeys here, wishing to be close to the Nurturer."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7734*]:
    → "Of course, faith and discipline are virtues. But life is to be enjoyed, and the lives of others respected. Faith can wait until these two things are accomplished."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7735*]:
    → "I told this to a Galka friend, and he bellowed a hearty laugh. Yet I could see his point: those who only live a short while have no time for such thoughts."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7736*]:
    → "To think of these things and wonder is the duty of the living. --Gwynham Ironheart, 759 Crystal Era"
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
