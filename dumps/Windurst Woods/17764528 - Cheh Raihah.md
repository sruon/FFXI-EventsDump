# 17764528 - Cheh Raihah

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 120 bytes                |
| Total Events     | 7                        |
| References Count | 6                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [52](#event-52)       | 0x0001       |      8 |              5 |
| [53](#event-53)       | 0x0009       |      8 |              5 |
| [62](#event-62)       | 0x0011       |      8 |              5 |
| [63](#event-63)       | 0x0019       |      8 |              5 |
| [72](#event-72)       | 0x0021       |      8 |              5 |
| [73](#event-73)       | 0x0029       |      8 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D91      |        7569 |
|       1 | 0x1D92      |        7570 |
|       2 | 0x1D9B      |        7579 |
|       3 | 0x1D9C      |        7580 |
|       4 | 0x1DA5      |        7589 |
|       5 | 0x1DA6      |        7590 |

## String References

- **7569**: The food around here's purrretty good, especially with all the exotic ingrrredients available these days. My fellow Windurstians, you had better go on morrre conquests or you'll be left behind!
- **7570**: Interrrested in a knife trick? It's a special routine I worrrked out. But keep your distance, if you value your ears and moustaches as they are!
- **7579**: The food here's terrrible! C'mon, Windurstians, worrrk harder! I miss Windurstian cuisine.
- **7580**: Like to see my new knife trrrick? Oh, but keep your distance, if you value your ears and moustaches as they are!
- **7589**: It's so verrrdant here and the food is delicious. I can hardly breathe in those other countries. Keep up the good work so I can stay here longerrr!
- **7590**: Want to see my new knife trrrick? But keep your distance, if you value your ears and moustaches as they arrre!

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

### Event 52

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 20 00 21  00                        ...# .!.       
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7569*)
    → "The food around here's purrretty good, especially with all the exotic ingrrredients available these days. My fellow Windurstians, you had better go on morrre conquests or you'll be left behind!"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x0007 [0x21] END_EVENT
  4: 0x0008 [0x00] END_REQSTACK()
```

### Event 53

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             1D 01 80 23 20 00 21           ...# .!
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=7570*)
    → "Interrrested in a knife trick? It's a special routine I worrrked out. But keep your distance, if you value your ears and moustaches as they are!"
  1: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x000D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x000F [0x21] END_EVENT
  4: 0x0010 [0x00] END_REQSTACK()
```

### Event 62

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    1D 02 80 23 20 00 21  00                        ...# .!.       
```

#### Opcodes

```
  0: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7579*)
    → "The food here's terrrible! C'mon, Windurstians, worrrk harder! I miss Windurstian cuisine."
  1: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0015 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x0017 [0x21] END_EVENT
  4: 0x0018 [0x00] END_REQSTACK()
```

### Event 63

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             1D 03 80 23 20 00 21           ...# .!
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=7580*)
    → "Like to see my new knife trrrick? Oh, but keep your distance, if you value your ears and moustaches as they are!"
  1: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x001D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x001F [0x21] END_EVENT
  4: 0x0020 [0x00] END_REQSTACK()
```

### Event 72

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0021  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    1D 04 80 23 20 00 21  00                        ...# .!.       
```

#### Opcodes

```
  0: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=7589*)
    → "It's so verrrdant here and the food is delicious. I can hardly breathe in those other countries. Keep up the good work so I can stay here longerrr!"
  1: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0025 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x0027 [0x21] END_EVENT
  4: 0x0028 [0x00] END_REQSTACK()
```

### Event 73

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1D 05 80 23 20 00 21           ...# .!
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=7590*)
    → "Want to see my new knife trrrick? But keep your distance, if you value your ears and moustaches as they arrre!"
  1: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x002D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x002F [0x21] END_EVENT
  4: 0x0030 [0x00] END_REQSTACK()
```
