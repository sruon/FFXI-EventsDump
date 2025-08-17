# 17498604 - Bou the Righteous

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Sea Serpent Grotto (ID: 176) |
| Block Size       | 60 bytes                     |
| Total Events     | 2                            |
| References Count | 4                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [108](#event-108)     | 0x0001       |     19 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x04AD      |        1197 |
|       1 | 0x1CAF      |        7343 |
|       2 | 0x1CB0      |        7344 |
|       3 | 0x1CB1      |        7345 |

## String References

- **7343**: Something fishy... Hurr making $0 again? He as slimy as eel!
- **7344**: Thanks to him, all our good booty go to pirates!
- **7345**: He sell his people for gil! I see him again, I chop him up into sushi!

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

### Event 108

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 19 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 02 10 00 80 1D 01  80 23 1D 02 80 23 1D 03   ........#...#..
0010: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[2] = 1197*
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7343*)
    → "Something fishy... Hurr making $0 again? He as slimy as eel!"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=7344*)
    → "Thanks to him, all our good booty go to pirates!"
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=7345*)
    → "He sell his people for gil! I see him again, I chop him up into sushi!"
  6: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0012 [0x21] END_EVENT
  8: 0x0013 [0x00] END_REQSTACK()
```
