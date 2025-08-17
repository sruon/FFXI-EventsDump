# 17318617 - Nonterene

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Abyssea - La Theine (ID: 132) |
| Block Size       | 52 bytes                      |
| Total Events     | 2                             |
| References Count | 2                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [306](#event-306)     | 0x0001       |     17 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E98      |        7832 |
|       1 | 0x1E99      |        7833 |

## String References

- **7832**: You've done well to come this far. On behalf of our leader Halver, I welcome you to the southeastern encampment. The people here are conducting biological research on the Abyssean hordes, that we might develop countermeasures against them.
- **7833**: Were you perchance able to locate the fifth veridical conflux as you journeyed here? Strike westward and you shall find it.

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

### Event 306

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 17 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 1D 01 80 23   .....op...#...#
0010: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7832*)
    → "You've done well to come this far. On behalf of our leader Halver, I welcome you to the southeastern encampment. The people here are conducting biological research on the Abyssean hordes, that we might develop countermeasures against them."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=7833*)
    → "Were you perchance able to locate the fifth veridical conflux as you journeyed here? Strike westward and you shall find it."
  6: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0010 [0x21] END_EVENT
  8: 0x0011 [0x00] END_REQSTACK()
```
