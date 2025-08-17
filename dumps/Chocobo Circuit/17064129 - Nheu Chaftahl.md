# 17064129 - Nheu Chaftahl

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
| [386](#event-386)     | 0x0001       |     19 |              7 |
| [387](#event-387)     | 0x0014       |     15 |              5 |
| [388](#event-388)     | 0x0023       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x260D      |        9741 |
|       1 | 0x260E      |        9742 |
|       2 | 0x2611      |        9745 |
|       3 | 0x2612      |        9746 |

## String References

- **9741**: Hey, you want to know which chocobo is fastest? It's my LunarHarvester! I rrraised her myself!
- **9742**: LunarHarvester was my grrrandpa's chocobo's chick. That's why she's so fast!
- **9745**: Yay! Yay! LunarHarvester is the best! I have to go tell Grrrandpa!
- **9746**: S-she lost... Th-this can't be true!

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

### Event 386

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
  1: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=9741*)
    → "Hey, you want to know which chocobo is fastest? It's my LunarHarvester! I rrraised her myself!"
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=9742*)
    → "LunarHarvester was my grrrandpa's chocobo's chick. That's why she's so fast!"
  4: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0012 [0x21] END_EVENT
  6: 0x0013 [0x00] END_REQSTACK()
```

### Event 387

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
  1: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=9745*)
    → "Yay! Yay! LunarHarvester is the best! I have to go tell Grrrandpa!"
  2: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0021 [0x21] END_EVENT
  4: 0x0022 [0x00] END_REQSTACK()
```

### Event 388

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
  1: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=9746*)
    → "S-she lost... Th-this can't be true!"
  2: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0030 [0x21] END_EVENT
  4: 0x0031 [0x00] END_REQSTACK()
```
