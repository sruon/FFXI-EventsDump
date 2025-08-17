# 17162736 - Ranna-Brunna

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 112 bytes                    |
| Total Events     | 3                            |
| References Count | 5                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [424](#event-424)     | 0x0001       |     30 |              8 |
| [230](#event-230)     | 0x001F       |     30 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2AE4      |       10980 |
|       2 | 0x2AE5      |       10981 |
|       3 | 0x2AFD      |       11005 |
|       4 | 0x2AFE      |       11006 |

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

### Event 424

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 2B F8 FF   J...........+..
0010: FF 7F 01 80 23 2B F8 FF  FF 7F 02 80 23 21 00     ....#+......#!. 
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x2B] EventEntity [10980*]:
    → "People tend to forget, but the real reason that the minister of the Optistery has cooped himself up in the Toraimarai Canal is to save Windurst from the very danger that threatens its existence, not to escape it."
  3: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0015 [0x2B] EventEntity [10981*]:
    → "All alone in that creepy-weepy, dark place for days and days... I can't even imagine what it must be like."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x21] END_EVENT
  7: 0x001E [0x00] END_REQSTACK()
```

### Event 230

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               4A                 J
0020: F8 FF FF 7F F0 FF FF 7F  1C 00 80 2B F8 FF FF 7F  ...........+....
0030: 03 80 23 2B F8 FF FF 7F  04 80 23 21 00           ..#+......#!.   
```

#### Opcodes

```
  0: 0x001F [0x4A] EventEntity looks at LocalPlayer
  1: 0x0028 [0x1C] WAIT(30* ticks)
  2: 0x002B [0x2B] EventEntity [11005*]:
    → "Is it true that Minister Karaha-Baruha summoned the Great Beast? That it was a glorious sightaru, like nothing of this world? I was stuck in Heavens Tower and missed everything!"
  3: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0033 [0x2B] EventEntity [11006*]:
    → "What? You were there!? Consider yourself lucky. That's a moment that will go down in history-wistory!"
  5: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003B [0x21] END_EVENT
  7: 0x003C [0x00] END_REQSTACK()
```
