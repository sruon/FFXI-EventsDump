# 17171138 - Galco-Ralico

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 84 bytes                        |
| Total Events     | 2                               |
| References Count | 4                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [220](#event-220)     | 0x0001       |     43 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FE4      |        8164 |
|       1 | 0x1FE5      |        8165 |
|       2 | 0x001D      |          29 |
|       3 | 0x1FE6      |        8166 |

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

### Event 220

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 2B F8  FF FF 7F 00 80 23 2B F8   .....+......#+.
0010: FF FF 7F 01 80 23 6E F8  FF FF 7F 02 80 99 F8 FF  .....#n.........
0020: FF 7F 2B F8 FF FF 7F 03  80 23 21 00              ..+......#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x2B] EventEntity [8164*]:
    → "Adventurer, you know Shantotto, former Minster of the Orastery?"
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x2B] EventEntity [8165*]:
    → "She is supposed to be in the north, for various reasons, but it seems she has returned leading a unit of volunteer soldiers!"
  4: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0016 [0x6E] EventEntity uses emote 29*
  6: 0x001D [0x99] Wait for EventEntity animation to complete
  7: 0x0022 [0x2B] EventEntity [8166*]:
    → "Knowing Minister Shantotto, the very fact that she has returned must mean that the situation does not bode well... Ah! This was supposed to be a secretaru!"
  8: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002A [0x21] END_EVENT
 10: 0x002B [0x00] END_REQSTACK()
```
