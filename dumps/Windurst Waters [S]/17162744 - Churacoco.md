# 17162744 - Churacoco

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 96 bytes                     |
| Total Events     | 2                            |
| References Count | 5                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [434](#event-434)     | 0x0001       |     50 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2AD2      |       10962 |
|       2 | 0x2AD3      |       10963 |
|       3 | 0x000B      |          11 |
|       4 | 0x2AD4      |       10964 |

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

### Event 434

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 50 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 2B F8 FF   J...........+..
0010: FF 7F 01 80 23 2B F8 FF  FF 7F 02 80 23 6E F8 FF  ....#+......#n..
0020: FF 7F 03 80 99 F8 FF FF  7F 2B F8 FF FF 7F 04 80  .........+......
0030: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x2B] EventEntity [10962*]:
    → "Adventurer, do you know Warlock Warlord Robel-Akbel? I was able to catch only a glimpse of him at the most recent battle."
  3: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0015 [0x2B] EventEntity [10963*]:
    → "He was wielding the most powerful magic I have ever seen! He felled some one hundred Yagudo in the blink of an eye!"
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x6E] EventEntity uses emote 11*
  7: 0x0024 [0x99] Wait for EventEntity animation to complete
  8: 0x0029 [0x2B] EventEntity [10964*]:
    → "I'd give anything to be that powerful..."
  9: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0031 [0x21] END_EVENT
 11: 0x0032 [0x00] END_REQSTACK()
```
