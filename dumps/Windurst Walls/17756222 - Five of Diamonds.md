# 17756222 - Five of Diamonds

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 96 bytes                 |
| Total Events     | 4                        |
| References Count | 4                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [266](#event-266)     | 0x0001       |     15 |              8 |
| [443](#event-443)     | 0x0010       |      7 |              2 |
| [339](#event-339)     | 0x0017       |     23 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E18      |        7704 |
|       1 | 0x1F44      |        8004 |
|       2 | 0x1F45      |        8005 |
|       3 | 0x1F46      |        8006 |

## String References

- **7704**: HErE$26WIndUrSt$26REs-IdEn-tIAl$26a-REa! yOUr mOg$26HOusE$26In$26hErE!
- **8004**: HaVe yoU seEn$26FivE oF$26SpaDes?
- **8005**: He sAy$26hE waNt becOmE$26conQueSt GuaRd! He LeaVe$26WinDurSt!
- **8006**: I$26thInK hE noT$26makE tOo faR!

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

### Event 266

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 20 00 21 00   .....op...# .!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7704*)
    → "HErE$26WIndUrSt$26REs-IdEn-tIAl$26a-REa! yOUr mOg$26HOusE$26In$26hErE!"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x000E [0x21] END_EVENT
  7: 0x000F [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0010 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 339

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 23 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      1E  F0 FF FF 7F 6F 70 1D 01         .....op..
0020: 80 23 1D 02 80 23 1D 03  80 23 20 00 21 00        .#...#...# .!.  
```

#### Opcodes

```
  0: 0x0017 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x001D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=8004*)
    → "HaVe yoU seEn$26FivE oF$26SpaDes?"
  4: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=8005*)
    → "He sAy$26hE waNt becOmE$26conQueSt GuaRd! He LeaVe$26WinDurSt!"
  6: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0026 [0x1D] PRINT_EVENT_MESSAGE(message_id=8006*)
    → "I$26thInK hE noT$26makE tOo faR!"
  8: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x002C [0x21] END_EVENT
 11: 0x002D [0x00] END_REQSTACK()
```
