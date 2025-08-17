# 17162732 - Prucco-Lurucco

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 68 bytes                     |
| Total Events     | 2                            |
| References Count | 3                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [420](#event-420)     | 0x0001       |     30 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2AA8      |       10920 |
|       2 | 0x2AA9      |       10921 |

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

### Event 420

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
  2: 0x000D [0x2B] EventEntity [10920*]:
    → "Those traditionally referred to as Wise Wizards in the Federation have been commissioned to lead units in battle and draw up wartime strategies."
  3: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0015 [0x2B] EventEntity [10921*]:
    → "We military scholars have also been appointed as staff officers and are serving here in Windurst as well."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x21] END_EVENT
  7: 0x001E [0x00] END_REQSTACK()
```
