# 17171128 - Khari Pulcohtz

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 64 bytes                        |
| Total Events     | 2                               |
| References Count | 3                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [210](#event-210)     | 0x0001       |     26 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1FC8      |        8136 |
|       2 | 0x1FC9      |        8137 |

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

### Event 210

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 2B F8 FF FF 7F 01 80   ........+......
0010: 23 2B F8 FF FF 7F 02 80  23 21 00                 #+......#!.     
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x2B] EventEntity [8136*]:
    → "Have you lost your way? North of here lie the Meriphataud Mountains. To the south, West Sarutabarrruta."
  3: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0011 [0x2B] EventEntity [8137*]:
    → "And going straight along this way will take you into Windurst Waters. If this stronghold falls, then Windurst is doomed. We are preparrred to defend it to the death! You'd best move along now."
  5: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0019 [0x21] END_EVENT
  7: 0x001A [0x00] END_REQSTACK()
```
