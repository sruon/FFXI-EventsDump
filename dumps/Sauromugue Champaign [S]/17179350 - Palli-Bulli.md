# 17179350 - Palli-Bulli

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 100 bytes                         |
| Total Events     | 4                                 |
| References Count | 6                                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1](#event-1)         | 0x0001       |     11 |              5 |
| [2](#event-2)         | 0x000C       |     28 |             14 |
| [3](#event-3)         | 0x0028       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E48      |        7752 |
|       1 | 0x1E49      |        7753 |
|       2 | 0x1E4A      |        7754 |
|       3 | 0x1E4B      |        7755 |
|       4 | 0x1E4C      |        7756 |
|       5 | 0x1E4D      |        7757 |

## String References

- **7752**: The path through the Meriphataud Mountains is a treacherous one, with Yagudo zealots hiding behind every rock. Stay alert, or you may find yourself impaled on the end of one of their blades.
- **7753**: Stand down, civilian! You're not really thinking of journeying through the mountains, are you? You would be crazy to continue, and I would be even more so to allow you the opportunity.
- **7754**: Though, if you are eager to put your Goddess-granted life at risk, I can offer you a bit of advice.
- **7755**: The Kingdom of San d'Oria has begun fortifying a citadel located due northwest from this garrison. There are guards there who may be able to assist you on your travels.
- **7756**: There also may be someone with information on recruitment, if you are interested in lending your services to the allied forces.
- **7757**: Who knows... The next time we meet, I might have to call you "sir."

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

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7752*)
    → "The path through the Meriphataud Mountains is a treacherous one, with Yagudo zealots hiding behind every rock. Stay alert, or you may find yourself impaled on the end of one of their blades."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 28 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      42 1E F0 FF              B...
0010: FF 7F 1D 01 80 23 1D 02  80 23 1D 03 80 23 1D 04  .....#...#...#..
0020: 80 23 1D 05 80 23 21 00                           .#...#!.        
```

#### Opcodes

```
  0: 0x000C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=7753*)
    → "Stand down, civilian! You're not really thinking of journeying through the mountains, are you? You would be crazy to continue, and I would be even more so to allow you the opportunity."
  3: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=7754*)
    → "Though, if you are eager to put your Goddess-granted life at risk, I can offer you a bit of advice."
  5: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=7755*)
    → "The Kingdom of San d'Oria has begun fortifying a citadel located due northwest from this garrison. There are guards there who may be able to assist you on your travels."
  7: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7756*)
    → "There also may be someone with information on recruitment, if you are interested in lending your services to the allied forces."
  9: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7757*)
    → "Who knows... The next time we meet, I might have to call you "sir.""
 11: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0026 [0x21] END_EVENT
 13: 0x0027 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0028  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          00                               .       
```

#### Opcodes

```
  0: 0x0028 [0x00] END_REQSTACK()
```
