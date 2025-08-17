# 17658599 - Resistance Fighter

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Attohwa (ID: 215) |
| Block Size       | 104 bytes                   |
| Total Events     | 4                           |
| References Count | 6                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [320](#event-320)     | 0x0001       |     19 |              9 |
| [321](#event-321)     | 0x0014       |     16 |              8 |
| [322](#event-322)     | 0x0024       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F8A      |        8074 |
|       1 | 0x1F8B      |        8075 |
|       2 | 0x1F8C      |        8076 |
|       3 | 0x1F9A      |        8090 |
|       4 | 0x1F9B      |        8091 |
|       5 | 0x1F9C      |        8092 |

## String References

- **8074**: Oh, curse and criminy! So close to my destination, and this damnable smoke obscures my path!
- **8075**: I was serving as the rearguard of our regiment--a most important duty, I assure you!
- **8076**: And serving admirably I was, until this accursed smoke appeared before me, separating me from my comrades to the fore. Come to think of it, why have they not returned to search for me...?
- **8090**: Are mine eyes to be believed? Are those rations you carry!? And a new linkpearl! Oh, joyous day!
- **8091**: My own accursed pearl seems only to work in one direction. I receive transmissions from camp, but try as I might, my voice falls on deaf ears.
- **8092**: Nor have I heard from my fellow scouts recently... I do hope they've not met an untimely demise.

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

### Event 320

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 19 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 1D 02   ........#...#..
0010: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=8074*)
    → "Oh, curse and criminy! So close to my destination, and this damnable smoke obscures my path!"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=8075*)
    → "I was serving as the rearguard of our regiment--a most important duty, I assure you!"
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=8076*)
    → "And serving admirably I was, until this accursed smoke appeared before me, separating me from my comrades to the fore. Come to think of it, why have they not returned to search for me...?"
  6: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0012 [0x21] END_EVENT
  8: 0x0013 [0x00] END_REQSTACK()
```

### Event 321

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 16 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             42 1E F0 FF  FF 7F 1D 03 80 23 1D 04      B........#..
0020: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0014 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0015 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=8090*)
    → "Are mine eyes to be believed? Are those rations you carry!? And a new linkpearl! Oh, joyous day!"
  3: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=8091*)
    → "My own accursed pearl seems only to work in one direction. I receive transmissions from camp, but try as I might, my voice falls on deaf ears."
  5: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0022 [0x21] END_EVENT
  7: 0x0023 [0x00] END_REQSTACK()
```

### Event 322

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             1E F0 FF FF  7F 1D 05 80 23 21 00         ........#!. 
```

#### Opcodes

```
  0: 0x0024 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=8092*)
    → "Nor have I heard from my fellow scouts recently... I do hope they've not met an untimely demise."
  2: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x002D [0x21] END_EVENT
  4: 0x002E [0x00] END_REQSTACK()
```
