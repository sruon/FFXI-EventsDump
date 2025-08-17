# 17171120 - Aurhi Rhatelo

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 96 bytes                        |
| Total Events     | 2                               |
| References Count | 5                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [202](#event-202)     | 0x0001       |     51 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1FF2      |        8178 |
|       2 | 0x1FF3      |        8179 |
|       3 | 0x000C      |          12 |
|       4 | 0x1FF4      |        8180 |

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

### Event 202

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 51 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 2B F8 FF FF 7F 01 80   ........+......
0010: 23 2B F8 FF FF 7F 02 80  23 6E F8 FF FF 7F 03 80  #+......#n......
0020: 99 F8 FF FF 7F 2B F8 FF  FF 7F 04 80 23 99 F8 FF  .....+......#...
0030: FF 7F 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x2B] EventEntity [8178*]:
    → "The Mithra Mercenaries are orrrganized into three main factions."
  3: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0011 [0x2B] EventEntity [8179*]:
    → "First, there are the marine forces, who were in Windurst from the beginning. Then there is the unit that hurried to our aid from Elshimo. And finally, the volunteers from Olzhirya."
  5: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0019 [0x6E] EventEntity uses emote 12*
  7: 0x0020 [0x99] Wait for EventEntity animation to complete
  8: 0x0025 [0x2B] EventEntity [8180*]:
    → "They may all be from different areas, but they're all hot-temperrred, short-fused, and never back down from a fight. I'm just glad I'm on their side, hehehe."
  9: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002D [0x99] Wait for EventEntity animation to complete
 11: 0x0032 [0x21] END_EVENT
 12: 0x0033 [0x00] END_REQSTACK()
```
