# 17064121 - Rhind Mhikkrol

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Chocobo Circuit (ID: 70) |
| Block Size       | 100 bytes                |
| Total Events     | 4                        |
| References Count | 4                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [365](#event-365)     | 0x0001       |     19 |              7 |
| [366](#event-366)     | 0x0014       |     15 |              5 |
| [367](#event-367)     | 0x0023       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x25C5      |        9669 |
|       1 | 0x25C6      |        9670 |
|       2 | 0x25C9      |        9673 |
|       3 | 0x25CA      |        9674 |

## String References

- **9669**: Hey, you're supposed to buy these...number things, rrright? I picked "ID$3:$0-$1". Are these supposed to be some kind of code? They're not???
- **9670**: A beastmaster frrriend of mine told me you can make a killing here... What? I've been played for a fool???
- **9673**: Huh? Why do I need to go collect gil from the chocobet center? Oh, I won something!? Whoopeeeeee!
- **9674**: Huh? You're saying I just threw away all my gil? No no no, this is all wrrrong! I want my money back!

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

### Event 365

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 19 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1D 00 80 23 1D 01   J...........#..
0010: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=9669*)
    → "Hey, you're supposed to buy these...number things, rrright? I picked "ID$3:$0-$1". Are these supposed to be some kind of code? They're not???"
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=9670*)
    → "A beastmaster frrriend of mine told me you can make a killing here... What? I've been played for a fool???"
  4: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0012 [0x21] END_EVENT
  6: 0x0013 [0x00] END_REQSTACK()
```

### Event 366

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             4A F8 FF FF  7F F0 FF FF 7F 1D 02 80      J...........
0020: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0014 [0x4A] EventEntity looks at LocalPlayer
  1: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=9673*)
    → "Huh? Why do I need to go collect gil from the chocobet center? Oh, I won something!? Whoopeeeeee!"
  2: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0021 [0x21] END_EVENT
  4: 0x0022 [0x00] END_REQSTACK()
```

### Event 367

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          4A F8 FF FF 7F  F0 FF FF 7F 1D 03 80 23     J...........#
0030: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0023 [0x4A] EventEntity looks at LocalPlayer
  1: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=9674*)
    → "Huh? You're saying I just threw away all my gil? No no no, this is all wrrrong! I want my money back!"
  2: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0030 [0x21] END_EVENT
  4: 0x0031 [0x00] END_REQSTACK()
```
