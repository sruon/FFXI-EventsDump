# 17658602 - Resistance Fighter

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Attohwa (ID: 215) |
| Block Size       | 88 bytes                    |
| Total Events     | 4                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [329](#event-329)     | 0x0001       |     15 |              7 |
| [330](#event-330)     | 0x0010       |     12 |              6 |
| [331](#event-331)     | 0x001C       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F94      |        8084 |
|       1 | 0x1F95      |        8085 |
|       2 | 0x1FA4      |        8100 |
|       3 | 0x1FA5      |        8101 |

## String References

- **8084**: To think I not only dropped my linkpearl, but then swiftly proceeded to step on it too! I told them I wasn't cut out for this kind of worrrk...
- **8085**: If you come across any o' the other scouts, I'd be much obliged if you could dirrrect them this way.
- **8100**: A fresh new linkpearrrl! Is this for me?
- **8101**: Oh, thank you everrr so much! I was gettin' mighty lonely out here all by myself...

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

### Event 329

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 21 00   ........#...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=8084*)
    → "To think I not only dropped my linkpearl, but then swiftly proceeded to step on it too! I told them I wasn't cut out for this kind of worrrk..."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=8085*)
    → "If you come across any o' the other scouts, I'd be much obliged if you could dirrrect them this way."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 330

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 42 1E F0 FF FF 7F 1D 02  80 23 21 00              B........#!.    
```

#### Opcodes

```
  0: 0x0010 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=8100*)
    → "A fresh new linkpearrrl! Is this for me?"
  3: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x001A [0x21] END_EVENT
  5: 0x001B [0x00] END_REQSTACK()
```

### Event 331

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      1E F0 FF FF              ....
0020: 7F 1D 03 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x001C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=8101*)
    → "Oh, thank you everrr so much! I was gettin' mighty lonely out here all by myself..."
  2: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0025 [0x21] END_EVENT
  4: 0x0026 [0x00] END_REQSTACK()
```
