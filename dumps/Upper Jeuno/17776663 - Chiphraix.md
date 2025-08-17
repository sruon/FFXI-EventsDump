# 17776663 - Chiphraix

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 128 bytes             |
| Total Events     | 4                     |
| References Count | 7                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [159](#event-159)     | 0x0001       |      1 |              1 |
| [153](#event-153)     | 0x0002       |     40 |             12 |
| [10025](#event-10025) | 0x002A       |     23 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1DA4      |        7588 |
|       2 | 0x1DA5      |        7589 |
|       3 | 0x1DA6      |        7590 |
|       4 | 0x2070      |        8304 |
|       5 | 0x2071      |        8305 |
|       6 | 0x2072      |        8306 |

## String References

- **7588**: Long ago, the Goddess Altana took pity on the barren world of Vana'diel and shed five tears. Our ancestors sprouted from each one.
- **7589**: But the god Promathia saw this, and condemned her work. He cursed all her people to eternal conflict among each other.
- **7590**: Altana would not be pleased to see us now, squabbling over our petty causes. Please, at least while you are here, shun conflict and pray for peace.
- **8304**: Unlike the unsavory rumors that have been spreading through the Duchy streets, the Elvaan girl who collapsed here was not attacked by some shady assailant.
- **8305**: While she was kneeling before the statue of the Goddess to offer a prayer, she suddenly crumpled to the floor and began convulsing violently. I attempted to cleanse her soul of the terrible demons that possessed her; however, my holy water had no effect.
- **8306**: I can only hope my prayers for her safety reach the Goddess swiftly.

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

### Event 159

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 153

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 40 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 6F  76 F8 FF FF 7F 66 00 80    .....ov....f..
0010: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 01 80 23  ........tlk0...#
0020: 1D 02 80 23 1D 03 80 23  21 00                    ...#...#!.      
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0008 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x000D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=7588*)
    → "Long ago, the Goddess Altana took pity on the barren world of Vana'diel and shed five tears. Our ancestors sprouted from each one."
  5: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=7589*)
    → "But the god Promathia saw this, and condemned her work. He cursed all her people to eternal conflict among each other."
  7: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7590*)
    → "Altana would not be pleased to see us now, squabbling over our petty causes. Please, at least while you are here, shun conflict and pray for peace."
  9: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0028 [0x21] END_EVENT
 11: 0x0029 [0x00] END_REQSTACK()
```

### Event 10025

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 23 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                1E F0 FF FF 7F 6F            .....o
0030: 70 1D 04 80 23 1D 05 80  23 1D 06 80 23 20 00 21  p...#...#...# .!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x002A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0030 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=8304*)
    → "Unlike the unsavory rumors that have been spreading through the Duchy streets, the Elvaan girl who collapsed here was not attacked by some shady assailant."
  4: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=8305*)
    → "While she was kneeling before the statue of the Goddess to offer a prayer, she suddenly crumpled to the floor and began convulsing violently. I attempted to cleanse her soul of the terrible demons that possessed her; however, my holy water had no effect."
  6: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=8306*)
    → "I can only hope my prayers for her safety reach the Goddess swiftly."
  8: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x003D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x003F [0x21] END_EVENT
 11: 0x0040 [0x00] END_REQSTACK()
```
