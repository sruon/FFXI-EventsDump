# 16962092 - Hakkuru-Rinkuru

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 96 bytes                    |
| Total Events     | 2                           |
| References Count | 6                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [403](#event-403)     | 0x0001       |     44 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FA1      |        8097 |
|       1 | 0x0031      |          49 |
|       2 | 0x1FA2      |        8098 |
|       3 | 0x1FA3      |        8099 |
|       4 | 0x1FA4      |        8100 |
|       5 | 0x1FA5      |        8101 |

## String References

- **8097**: Looking to do some shopping-wopping, eh? Well, we don't have shops per se, but there's a trader over by the banner with some provisions for sale.
- **8098**: I figure she can outfitaru you with most anything you need, so long as you've got the cruor to pay-the-day for it.
- **8099**: Gil, you say? I'm afraid there hasn't been much use for that of late.
- **8100**: Take down-with-a-frown one of those Abyssean fiends, and you'll find they drop a reddish gold dusty-crust--that's cruor. Back when the three nations still stood, the stuff was nowhere to be found, but now we literally can't live without it.
- **8101**: You'll be needing it to power the confluxes as well, so you'll want to keep a healthy-wealthy supply.

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

### Event 403

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 44 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 66 01 80 F8   .....op...#f...
0010: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 02 80 23 1D  .......tlk0...#.
0020: 03 80 23 1D 04 80 23 1D  05 80 23 21 00           ..#...#...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=8097*)
    → "Looking to do some shopping-wopping, eh? Well, we don't have shops per se, but there's a trader over by the banner with some provisions for sale."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=8098*)
    → "I figure she can outfitaru you with most anything you need, so long as you've got the cruor to pay-the-day for it."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=8099*)
    → "Gil, you say? I'm afraid there hasn't been much use for that of late."
  9: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=8100*)
    → "Take down-with-a-frown one of those Abyssean fiends, and you'll find they drop a reddish gold dusty-crust--that's cruor. Back when the three nations still stood, the stuff was nowhere to be found, but now we literally can't live without it."
 11: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=8101*)
    → "You'll be needing it to power the confluxes as well, so you'll want to keep a healthy-wealthy supply."
 13: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x002B [0x21] END_EVENT
 15: 0x002C [0x00] END_REQSTACK()
```
