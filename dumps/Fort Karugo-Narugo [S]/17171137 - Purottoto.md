# 17171137 - Purottoto

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 112 bytes                       |
| Total Events     | 2                               |
| References Count | 5                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [219](#event-219)     | 0x0001       |     64 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0031      |          49 |
|       2 | 0x1FED      |        8173 |
|       3 | 0x1FEE      |        8174 |
|       4 | 0x1FEF      |        8175 |

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

### Event 219

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 64 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  2B F8 FF FF 7F 02 80 23  ....tlk0+......#
0020: 2B F8 FF FF 7F 03 80 23  2B F8 FF FF 7F 04 80 23  +......#+......#
0030: 66 01 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 21  f..........tlk1!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  3: 0x0018 [0x2B] EventEntity [8173*]:
    → "Our path is lit by yon brilliant star, Many on the long journey embark. Guided true by that celestial spark, To find a timeless green that can know no dark."
  4: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0020 [0x2B] EventEntity [8174*]:
    → "Oh, the six points of yon shining star, even the raging of beasts shall slake. In the south heavens glows a pearly lake, traverses the sky and leaves an azure wake."
  6: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0028 [0x2B] EventEntity [8175*]:
    → "Hm? Oh, that's just an old song my grandmother taught me. It's supposed to be about the Horutoto Ruins, if I remember."
  8: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0030 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
 10: 0x003F [0x21] END_EVENT
 11: 0x0040 [0x00] END_REQSTACK()
```
