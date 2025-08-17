# 17478343 - Minea-Matea

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
| [101](#event-101)     | 0x0001       |     42 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0015      |          21 |
|       2 | 0x1DC1      |        7617 |
|       3 | 0x1DC2      |        7618 |

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

### Event 101

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
  2: 0x000D [0x6E] EventEntity uses emote 21*
  3: 0x0014 [0x99] Wait for EventEntity animation to complete
  4: 0x0019 [0x2B] EventEntity [7617*]:
    → "Hey hey hey! How did you get in here!? Were you looking for the brewery?"
  5: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0021 [0x2B] EventEntity [7618*]:
    → "We don'taru just make wine here, you know. We also ripen-wipen the rolanberries with the help of crawler saliva. Watch out for the spit puddles..."
  7: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0029 [0x21] END_EVENT
  9: 0x002A [0x00] END_REQSTACK()
```
