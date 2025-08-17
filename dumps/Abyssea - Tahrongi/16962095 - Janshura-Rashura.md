# 16962095 - Janshura-Rashura

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 100 bytes                   |
| Total Events     | 2                           |
| References Count | 5                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [400](#event-400)     | 0x0001       |     55 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FB0      |        8112 |
|       1 | 0x0028      |          40 |
|       2 | 0x1FB1      |        8113 |
|       3 | 0x1FB2      |        8114 |
|       4 | 0x1FB3      |        8115 |

## String References

- **8112**: See that curious stone structure all glowing and spinning-winning over there? That's what we call a veridical conflux.
- **8113**: Don't let it intimidataru you--it's actually the handiest pile of rocks around. You can warp from one to another in the blink of an eye, you see!
- **8114**: The only catch is that you'll need to meld-weld with a conflux before you can teleport to it. They're scattered all over the canyon, so you'll want to explore and make contactaru with as many you can. It'll make travel easy-breezy!
- **8115**: You'll also want to be sure you have cruor on hand. Otherwise your long journey will have all been for naughtaru.

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

### Event 400

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 55 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 66 01 80 F8   .....op...#f...
0010: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 02 80 23 1D  .......tlk0...#.
0020: 03 80 23 66 01 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0030: 6B 31 1D 04 80 23 21 00                           k1...#!.        
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=8112*)
    → "See that curious stone structure all glowing and spinning-winning over there? That's what we call a veridical conflux."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=8113*)
    → "Don't let it intimidataru you--it's actually the handiest pile of rocks around. You can warp from one to another in the blink of an eye, you see!"
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=8114*)
    → "The only catch is that you'll need to meld-weld with a conflux before you can teleport to it. They're scattered all over the canyon, so you'll want to explore and make contactaru with as many you can. It'll make travel easy-breezy!"
  9: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0023 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 11: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=8115*)
    → "You'll also want to be sure you have cruor on hand. Otherwise your long journey will have all been for naughtaru."
 12: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0036 [0x21] END_EVENT
 14: 0x0037 [0x00] END_REQSTACK()
```
