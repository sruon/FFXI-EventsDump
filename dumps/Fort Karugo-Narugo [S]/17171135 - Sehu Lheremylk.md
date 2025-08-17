# 17171135 - Sehu Lheremylk

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 80 bytes                        |
| Total Events     | 2                               |
| References Count | 4                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [217](#event-217)     | 0x0001       |     38 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0020      |          32 |
|       2 | 0x1FDC      |        8156 |
|       3 | 0x1FDD      |        8157 |

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

### Event 217

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 38 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 6E F8 FF FF 7F 01 80   ........n......
0010: 99 F8 FF FF 7F 2B F8 FF  FF 7F 02 80 23 2B F8 FF  .....+......#+..
0020: FF 7F 03 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x6E] EventEntity uses emote 32*
  3: 0x0010 [0x99] Wait for EventEntity animation to complete
  4: 0x0015 [0x2B] EventEntity [8156*]:
    → "Did you see that...that thing in the sky? That disgusting mouth...always open... Ever since it appeared, things haven't been quite normal."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x2B] EventEntity [8157*]:
    → "You'd know what I was talking about if you stood on the frontlines. The enemy...and the atmosphere... There's just something very strange about it all."
  7: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0025 [0x21] END_EVENT
  9: 0x0026 [0x00] END_REQSTACK()
```
