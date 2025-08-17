# 17064122 - Makrena-Rukrena

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Chocobo Circuit (ID: 70) |
| Block Size       | 112 bytes                |
| Total Events     | 4                        |
| References Count | 5                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [368](#event-368)     | 0x0001       |     25 |              8 |
| [369](#event-369)     | 0x001A       |     16 |              5 |
| [370](#event-370)     | 0x002A       |     16 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x25CF      |        9679 |
|       1 | 0x43EA      |       17386 |
|       2 | 0x25D0      |        9680 |
|       3 | 0x25D3      |        9683 |
|       4 | 0x25D4      |        9684 |

## String References

- **9679**: H-hey, were you eavesdropping? Don't even thinky-wink about bettaruing on "ID$3:$0-$1". You'll reduce my winnings!
- **9680**: I'm gonna getaru myself $0 when I win!
- **9683**: Whootaru, there it is! I am the champion! No timey-wime for losers! $0 comin' my way!
- **9684**: <Sniffle...sob...> Th-that's not how it's supposed to end...

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

### Event 368

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 25 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    79 00 F8 FF FF 7F F0  FF FF 7F 1D 00 80 23 03   y............#.
0010: 02 10 01 80 1D 02 80 23  21 00                    .......#!.      
```

#### Opcodes

```
  0: 0x0001 [0x79] EventEntity looks at LocalPlayer (Basic look)
  1: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=9679*)
    → "H-hey, were you eavesdropping? Don't even thinky-wink about bettaruing on "ID$3:$0-$1". You'll reduce my winnings!"
  2: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000F [0x03] Work_Zone[2] = 17386*
  4: 0x0014 [0x1D] PRINT_EVENT_MESSAGE(message_id=9680*)
    → "I'm gonna getaru myself $0 when I win!"
  5: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0018 [0x21] END_EVENT
  7: 0x0019 [0x00] END_REQSTACK()
```

### Event 369

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                79 00 F8 FF FF 7F            y.....
0020: F0 FF FF 7F 1D 03 80 23  21 00                    .......#!.      
```

#### Opcodes

```
  0: 0x001A [0x79] EventEntity looks at LocalPlayer (Basic look)
  1: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=9683*)
    → "Whootaru, there it is! I am the champion! No timey-wime for losers! $0 comin' my way!"
  2: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0028 [0x21] END_EVENT
  4: 0x0029 [0x00] END_REQSTACK()
```

### Event 370

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                79 00 F8 FF FF 7F            y.....
0030: F0 FF FF 7F 1D 04 80 23  21 00                    .......#!.      
```

#### Opcodes

```
  0: 0x002A [0x79] EventEntity looks at LocalPlayer (Basic look)
  1: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=9684*)
    → "<Sniffle...sob...> Th-that's not how it's supposed to end..."
  2: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0038 [0x21] END_EVENT
  4: 0x0039 [0x00] END_REQSTACK()
```
