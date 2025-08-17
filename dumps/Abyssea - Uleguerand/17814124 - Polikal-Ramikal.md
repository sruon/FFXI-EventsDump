# 17814124 - Polikal-Ramikal

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 76 bytes                       |
| Total Events     | 2                              |
| References Count | 4                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [352](#event-352)     | 0x0001       |     33 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x1F99      |        8089 |
|       2 | 0x1F9A      |        8090 |
|       3 | 0x1F9B      |        8091 |

## String References

- **8089**: Greetings, friend. Have you ever seen a spinning pile of stones as beauti-weautiful as this one? I'll bet you haven'taru.
- **8090**: We call them veridical confluxes, you see, and what makes them even more beautiful is the power of teleportation they possess. I make it a point to activate each one I come across, and I would heartily-weartily suggest you do the same.
- **8091**: To utilize their powers, you'll also need a supply of cruor. But that shouldn't presentaru a problem to one of your skills, now should it?

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

### Event 352

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 33 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  6E 6C D2 0F 01 00 80 99   .....opnl......
0010: 6C D2 0F 01 1D 01 80 23  1D 02 80 23 1D 03 80 23  l......#...#...#
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x6E] Polikal-Ramikal (ID: 17814124/0x010FD26C) uses emote 0*
  4: 0x000F [0x99] Wait for Polikal-Ramikal (ID: 17814124/0x010FD26C) animation to complete
  5: 0x0014 [0x1D] PRINT_EVENT_MESSAGE(message_id=8089*)
    → "Greetings, friend. Have you ever seen a spinning pile of stones as beauti-weautiful as this one? I'll bet you haven'taru."
  6: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=8090*)
    → "We call them veridical confluxes, you see, and what makes them even more beautiful is the power of teleportation they possess. I make it a point to activate each one I come across, and I would heartily-weartily suggest you do the same."
  8: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=8091*)
    → "To utilize their powers, you'll also need a supply of cruor. But that shouldn't presentaru a problem to one of your skills, now should it?"
 10: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0020 [0x21] END_EVENT
 12: 0x0021 [0x00] END_REQSTACK()
```
