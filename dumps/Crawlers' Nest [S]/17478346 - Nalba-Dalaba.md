# 17478346 - Nalba-Dalaba

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Crawlers' Nest [S] (ID: 171) |
| Block Size       | 84 bytes                     |
| Total Events     | 2                            |
| References Count | 4                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [104](#event-104)     | 0x0001       |     42 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0013      |          19 |
|       2 | 0x1DC6      |        7622 |
|       3 | 0x1DC7      |        7623 |

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

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 42 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 6E F8 FF   J...........n..
0010: FF 7F 01 80 99 F8 FF FF  7F 2B F8 FF FF 7F 02 80  .........+......
0020: 23 2B F8 FF FF 7F 03 80  23 21 00                 #+......#!.     
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x6E] EventEntity uses emote 19*
  3: 0x0014 [0x99] Wait for EventEntity animation to complete
  4: 0x0019 [0x2B] EventEntity [7622*]:
    → "<Sigh>... Ever since the Federation Forces took over the storerooms for their operations, my business has become a literal casualty of war."
  5: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0021 [0x2B] EventEntity [7623*]:
    → "And the fields are being trompy-stomped flat during the battles with the turtlemen. What's an honestaru merchant to do?"
  7: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0029 [0x21] END_EVENT
  9: 0x002A [0x00] END_REQSTACK()
```
