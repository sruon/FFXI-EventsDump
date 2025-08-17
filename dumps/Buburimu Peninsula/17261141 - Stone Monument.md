# 17261141 - Stone Monument

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Buburimu Peninsula (ID: 118) |
| Block Size       | 76 bytes                     |
| Total Events     | 2                            |
| References Count | 6                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [900](#event-900)     | 0x0001       |     26 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CEC      |        7404 |
|       1 | 0x1CED      |        7405 |
|       2 | 0x1CEE      |        7406 |
|       3 | 0x1CEF      |        7407 |
|       4 | 0x1CF0      |        7408 |
|       5 | 0x1CF1      |        7409 |

## String References

- **7404**: You see a message engraved on the stone:
- **7405**: Buburimu is famous for the miraculous rocks of Gibubu, meaning "lighthouse" in the Tarutaru tongue. True to their name, the spires help sailors and fishermen weather the storms.
- **7406**: Like crooked towers they loom, each adorned with a great crystal that glimmers at night.
- **7407**: I theorize that here, in the days of old, was ore of the highest purity, known in our legends as orichalcum.
- **7408**: I believe the ages brought decay to the surrounding bedrock, whilst the ore itself remained. The Tarutaru then wrought their magic upon them to make them shimmer everlastingly.
- **7409**: Still, however, I yearn to know why the ore was here in the first place. --Enid Ironheart, 778 Crystal Era.

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

### Event 900

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 48 01 80  23 48 02 80 23 48 03 80   H..#H..#H..#H..
0010: 23 48 04 80 23 48 05 80  23 21 00                 #H..#H..#!.     
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7404*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7405*]:
    → "Buburimu is famous for the miraculous rocks of Gibubu, meaning "lighthouse" in the Tarutaru tongue. True to their name, the spires help sailors and fishermen weather the storms."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7406*]:
    → "Like crooked towers they loom, each adorned with a great crystal that glimmers at night."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7407*]:
    → "I theorize that here, in the days of old, was ore of the highest purity, known in our legends as orichalcum."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7408*]:
    → "I believe the ages brought decay to the surrounding bedrock, whilst the ore itself remained. The Tarutaru then wrought their magic upon them to make them shimmer everlastingly."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7409*]:
    → "Still, however, I yearn to know why the ore was here in the first place. --Enid Ironheart, 778 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
