# 17162724 - Aihn Sowlmirih

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 108 bytes                    |
| Total Events     | 4                            |
| References Count | 5                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [412](#event-412)     | 0x0001       |     50 |             12 |
| [231](#event-231)     | 0x0033       |      1 |              1 |
| [232](#event-232)     | 0x0034       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x001A      |          26 |
|       2 | 0x2ACF      |       10959 |
|       3 | 0x2AD0      |       10960 |
|       4 | 0x2AD1      |       10961 |

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

### Event 412

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 50 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 6E F8 FF   J...........n..
0010: FF 7F 01 80 99 F8 FF FF  7F 2B F8 FF FF 7F 02 80  .........+......
0020: 23 2B F8 FF FF 7F 03 80  23 2B F8 FF FF 7F 04 80  #+......#+......
0030: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x6E] EventEntity uses emote 26*
  3: 0x0014 [0x99] Wait for EventEntity animation to complete
  4: 0x0019 [0x2B] EventEntity [10959*]:
    → "<Sigh>... To have come all the way from Olzhirya to Windurst just to be met by this scene of destruction... But we must remain firm."
  5: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0021 [0x2B] EventEntity [10960*]:
    → "They say the weakening of a nation is generally the result of its leadership. I don't know what the Star Sibyl or whoever is running Windurrrst is up to..."
  7: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0029 [0x2B] EventEntity [10961*]:
    → "Strength is everrrything to us Mithra. A leader without strength is no leader at all."
  9: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0031 [0x21] END_EVENT
 11: 0x0032 [0x00] END_REQSTACK()
```

### Event 231

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0033  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          00                                          .            
```

#### Opcodes

```
  0: 0x0033 [0x00] END_REQSTACK()
```

### Event 232

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0034  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             00                                        .           
```

#### Opcodes

```
  0: 0x0034 [0x00] END_REQSTACK()
```
