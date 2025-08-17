# 17670768 - Taraihi-Perunhi

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 64 bytes                   |
| Total Events     | 2                          |
| References Count | 4                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [333](#event-333)     | 0x0001       |     22 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x204B      |        8267 |
|       2 | 0x204C      |        8268 |
|       3 | 0x204D      |        8269 |

## String References

- **8267**: You look like you're new around here, so let me give you a tippy-wip. Here in Abyssea, it's all aboutaru the cruor!
- **8268**: Cruor is a most peculiar-wuliar substance that you'll find on the fiends you slay. You can use it to power those varicky-dal confloozies or whatever they're called.
- **8269**: If you amass more cruor than you know what to do with, you can exchange it for various goodies with the cruor prospector over there. Or you could give it to me. I certainly-wertainly wouldn't say no to that!

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

### Event 333

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 22 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 1D 01 80 23 1D 02 80   ...........#...
0010: 23 1D 03 80 23 21 00                              #...#!.         
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(20* ticks)
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=8267*)
    → "You look like you're new around here, so let me give you a tippy-wip. Here in Abyssea, it's all aboutaru the cruor!"
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=8268*)
    → "Cruor is a most peculiar-wuliar substance that you'll find on the fiends you slay. You can use it to power those varicky-dal confloozies or whatever they're called."
  5: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=8269*)
    → "If you amass more cruor than you know what to do with, you can exchange it for various goodies with the cruor prospector over there. Or you could give it to me. I certainly-wertainly wouldn't say no to that!"
  7: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0015 [0x21] END_EVENT
  9: 0x0016 [0x00] END_REQSTACK()
```
