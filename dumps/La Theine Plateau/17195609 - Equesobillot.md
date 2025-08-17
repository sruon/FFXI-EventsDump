# 17195609 - Equesobillot

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 168 bytes                   |
| Total Events     | 3                           |
| References Count | 6                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [101](#event-101)     | 0x0001       |     36 |             10 |
| [112](#event-112)     | 0x0025       |     78 |             18 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1CEE      |        7406 |
|       2 | 0x001E      |          30 |
|       3 | 0x1D01      |        7425 |
|       4 | 0x1D02      |        7426 |
|       5 | 0x1D03      |        7427 |

## String References

- **7406**: Head down here if you wish to take part in the rescue drill.
- **7425**: Ruillont's sword? Yes, I was keeping it for him during training.
- **7426**: What, Ruillont's stuck in a cave? How typical of him to refuse your help...
- **7427**: Yes, I believe you; I'm sure it's him. Take this to him in there, would you? We'll keep it between you and me.

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

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 5E 69 64 6C 30  ...tlk0...#^idl0
0020: 1C 02 80 21 00                                    ...!.           
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7406*)
    → "Head down here if you wish to take part in the rescue drill."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0020 [0x1C] WAIT(30* ticks)
  8: 0x0023 [0x21] END_EVENT
  9: 0x0024 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 78 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                1E F0 FF  FF 7F 6F 70 66 00 80 F8       .....opf...
0030: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 03 80 23 1C  .......tlk0...#.
0040: 02 80 1D 04 80 23 5E 69  64 6C 30 1C 02 80 66 00  .....#^idl0...f.
0050: 80 F8 FF FF 7F F8 FF FF  7F 70 61 73 30 1D 05 80  .........pas0...
0060: 23 53 F8 FF FF 7F F8 FF  FF 7F 70 61 73 30 1C 02  #S........pas0..
0070: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0025 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x002B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=7425*)
    → "Ruillont's sword? Yes, I was keeping it for him during training."
  5: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003F [0x1C] WAIT(30* ticks)
  7: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=7426*)
    → "What, Ruillont's stuck in a cave? How typical of him to refuse your help..."
  8: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0046 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 10: 0x004B [0x1C] WAIT(30* ticks)
 11: 0x004E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
 12: 0x005D [0x1D] PRINT_EVENT_MESSAGE(message_id=7427*)
    → "Yes, I believe you; I'm sure it's him. Take this to him in there, would you? We'll keep it between you and me."
 13: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0061 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 15: 0x006E [0x1C] WAIT(30* ticks)
 16: 0x0071 [0x21] END_EVENT
 17: 0x0072 [0x00] END_REQSTACK()
```
