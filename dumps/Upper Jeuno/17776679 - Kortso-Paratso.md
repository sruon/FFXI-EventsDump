# 17776679 - Kortso-Paratso

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 104 bytes             |
| Total Events     | 2                     |
| References Count | 3                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [89](#event-89)       | 0x0001       |     64 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x1DAB      |        7595 |
|       2 | 0x1DAC      |        7596 |

## String References

- **7595**: You know, Wolfgang has changed so much ever since he became captain of the guard. It's like he's always wearing a mask. He never smiles anymore.
- **7596**: He even gives his old pal Monberaux the cold shoulder. Just who does he think he is!

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

### Event 89

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 64 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 76  F8 FF FF 7F 66 00 80 F8   .....ov....f...
0010: FF FF 7F F8 FF FF 7F 74  68 6B 31 1D 01 80 23 1D  .......thk1...#.
0020: 02 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 68  ..#f..........th
0030: 6B 32 53 F8 FF FF 7F F8  FF FF 7F 74 68 6B 32 21  k2S........thk2!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x000C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  4: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=7595*)
    → "You know, Wolfgang has changed so much ever since he became captain of the guard. It's like he's always wearing a mask. He never smiles anymore."
  5: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=7596*)
    → "He even gives his old pal Monberaux the cold shoulder. Just who does he think he is!"
  7: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0023 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  9: 0x0032 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
 10: 0x003F [0x21] END_EVENT
 11: 0x0040 [0x00] END_REQSTACK()
```
