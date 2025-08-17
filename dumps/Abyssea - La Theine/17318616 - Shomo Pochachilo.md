# 17318616 - Shomo Pochachilo

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
| [305](#event-305)     | 0x0001       |     17 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E96      |        7830 |
|       1 | 0x1E97      |        7831 |

## String References

- **7830**: Welcome, frrriend, to the central encampment, serviced by veridical conflux number fourrr. With the dependable LT-05 Martello buttressing the resistance effort, peace is rrrelatively well preserved in this area.
- **7831**: The ravine-grrraven landscape of La Theine puts me in mind of my homeland... Oh, how I long for those bygone--what? Otherrr conflux locations, you ask? One's located near to a valley east of here, I believe.

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

### Event 305

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
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7830*)
    → "Welcome, frrriend, to the central encampment, serviced by veridical conflux number fourrr. With the dependable LT-05 Martello buttressing the resistance effort, peace is rrrelatively well preserved in this area."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=7831*)
    → "The ravine-grrraven landscape of La Theine puts me in mind of my homeland... Oh, how I long for those bygone--what? Otherrr conflux locations, you ask? One's located near to a valley east of here, I believe."
  6: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0010 [0x21] END_EVENT
  8: 0x0011 [0x00] END_REQSTACK()
```
