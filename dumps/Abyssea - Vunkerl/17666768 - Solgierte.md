# 17666768 - Solgierte

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Vunkerl (ID: 217) |
| Block Size       | 64 bytes                    |
| Total Events     | 2                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1098](#event-1098)   | 0x0001       |     23 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x20FB      |        8443 |
|       1 | 0x20FC      |        8444 |
|       2 | 0x20FD      |        8445 |
|       3 | 0x20FE      |        8446 |

## String References

- **8443**: Hey, you there! Yes, you! Have you gone and obtained visitant status from the conflux surveyor?
- **8444**: Because if you haven't, folk around here won't utter so much as a single word to you. They have trust issues, you see, and small wonder considering the trauma they've lived through.
- **8445**: On the other hand, folk will also refrain from interacting with you if they know you're actively participating in the resistance effort.
- **8446**: Any other time, though, and they'll be more than happy to trade banter with you. Keep these things in mind when you journey here, all right?

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

### Event 1098

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 23 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 1D 02   ........#...#..
0010: 80 23 1D 03 80 23 21 00                           .#...#!.        
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=8443*)
    → "Hey, you there! Yes, you! Have you gone and obtained visitant status from the conflux surveyor?"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=8444*)
    → "Because if you haven't, folk around here won't utter so much as a single word to you. They have trust issues, you see, and small wonder considering the trauma they've lived through."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=8445*)
    → "On the other hand, folk will also refrain from interacting with you if they know you're actively participating in the resistance effort."
  6: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=8446*)
    → "Any other time, though, and they'll be more than happy to trade banter with you. Keep these things in mind when you journey here, all right?"
  8: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0016 [0x21] END_EVENT
 10: 0x0017 [0x00] END_REQSTACK()
```
