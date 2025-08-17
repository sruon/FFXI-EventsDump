# 16962101 - Zahsa Syalmhaia

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 52 bytes                    |
| Total Events     | 2                           |
| References Count | 2                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [408](#event-408)     | 0x0001       |     17 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FC6      |        8134 |
|       1 | 0x1FC7      |        8135 |

## String References

- **8134**: Look at those fools, trrraipsing about without a care in the world. We didn't fight tooth and nail to save their worrrthless hides just so they could throw them away like this!
- **8135**: That goes for you too! If you've got any sense, you'll stay quiet, and stay on guarrrd. Grrr...sometimes I wonder if that teleportation accident transported everyone's brains into one o' those fissures...

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

### Event 408

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
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=8134*)
    → "Look at those fools, trrraipsing about without a care in the world. We didn't fight tooth and nail to save their worrrthless hides just so they could throw them away like this!"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=8135*)
    → "That goes for you too! If you've got any sense, you'll stay quiet, and stay on guarrrd. Grrr...sometimes I wonder if that teleportation accident transported everyone's brains into one o' those fissures..."
  6: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0010 [0x21] END_EVENT
  8: 0x0011 [0x00] END_REQSTACK()
```
