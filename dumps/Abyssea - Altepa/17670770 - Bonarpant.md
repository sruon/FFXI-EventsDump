# 17670770 - Bonarpant

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 72 bytes                   |
| Total Events     | 2                          |
| References Count | 5                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [336](#event-336)     | 0x0001       |     26 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2051      |        8273 |
|       2 | 0x2052      |        8274 |
|       3 | 0x2053      |        8275 |
|       4 | 0x2054      |        8276 |

## String References

- **8273**: Oh, woe is me! Had I only known that Abyssean fiends had individual weaknesses, I might have saved my beloved from their vile clutches!
- **8274**: After all, by striking those vile creatures where they're vulnerable, one can stagger them so forcefully that they will forget their most formidable attacks, or even freeze dead in their tracks! Oh, Prietta, forgive me!
- **8275**: And if I had known that the monsters summon more and more powerful reinforcements if you fight them in the same place for too long, I would have fled before we got overwhelmed! <Sob>...
- **8276**: The hordes possess an intelligence that only a fool would ignore. We must fight on, and fight wisely, that no more...<sniff>...victims will be claimed...

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

### Event 336

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 1D 01 80 23 1D 02 80   ...........#...
0010: 23 1D 03 80 23 1D 04 80  23 21 00                 #...#...#!.     
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(20* ticks)
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=8273*)
    → "Oh, woe is me! Had I only known that Abyssean fiends had individual weaknesses, I might have saved my beloved from their vile clutches!"
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=8274*)
    → "After all, by striking those vile creatures where they're vulnerable, one can stagger them so forcefully that they will forget their most formidable attacks, or even freeze dead in their tracks! Oh, Prietta, forgive me!"
  5: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=8275*)
    → "And if I had known that the monsters summon more and more powerful reinforcements if you fight them in the same place for too long, I would have fled before we got overwhelmed! <Sob>..."
  7: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=8276*)
    → "The hordes possess an intelligence that only a fool would ignore. We must fight on, and fight wisely, that no more...<sniff>...victims will be claimed..."
  9: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0019 [0x21] END_EVENT
 11: 0x001A [0x00] END_REQSTACK()
```
