# 17171127 - Rhant Tamhujya

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 72 bytes                        |
| Total Events     | 2                               |
| References Count | 3                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [209](#event-209)     | 0x0001       |     35 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FCA      |        8138 |
|       1 | 0x001A      |          26 |
|       2 | 0x1FCB      |        8139 |

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

### Event 209

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 2B F8  FF FF 7F 00 80 23 6E F8   .....+......#n.
0010: FF FF 7F 01 80 99 F8 FF  FF 7F 2B F8 FF FF 7F 02  ..........+.....
0020: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x2B] EventEntity [8138*]:
    → "Identify yourself! We are at war. You never know who might be a beastman spy."
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x6E] EventEntity uses emote 26*
  4: 0x0015 [0x99] Wait for EventEntity animation to complete
  5: 0x001A [0x2B] EventEntity [8139*]:
    → "It would be one thing if we had only the Yagudo to worry about. But rumor has it that even fouler beastmen are brooding in the north..."
  6: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0022 [0x21] END_EVENT
  8: 0x0023 [0x00] END_REQSTACK()
```
