# 17826045 - Berstrogus

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 136 bytes                 |
| Total Events     | 3                         |
| References Count | 4                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [504](#event-504)     | 0x0001       |     47 |             11 |
| [587](#event-587)     | 0x0030       |     43 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x262E      |        9774 |
|       2 | 0x262F      |        9775 |
|       3 | 0x2630      |        9776 |

## String References

- **9774**: Why, you're not even registered as a pioneer!?
- **9775**: Pay a visit to Brenton so he can help you start walking the path to fame and fortune. Coincidentally, he's in the building right across from me.
- **9776**: Pioneers have certainly made a lot of headway recently. Your role in the colonization movement has expanded, and you're more trusted than ever. I don't know exactly how that affects you personally, but I'm sure someone at the various coalitions would.

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

### Event 504

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 66  ...tlk0...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 65 6E 30 21 00  ..........ten0!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=9774*)
    → "Why, you're not even registered as a pioneer!?"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=9775*)
    → "Pay a visit to Brenton so he can help you start walking the path to fame and fortune. Coincidentally, he's in the building right across from me."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten0" with entities [EventEntity, EventEntity], work=0*
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 587

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 6F 70 66  00 80 F8 FF FF 7F F8 FF  .....opf........
0040: FF 7F 74 6C 6B 30 1D 03  80 23 66 00 80 F8 FF FF  ..tlk0...#f.....
0050: 7F F8 FF FF 7F 74 65 6E  30 21 00                 .....ten0!.     
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  4: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=9776*)
    → "Pioneers have certainly made a lot of headway recently. Your role in the colonization movement has expanded, and you're more trusted than ever. I don't know exactly how that affects you personally, but I'm sure someone at the various coalitions would."
  5: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten0" with entities [EventEntity, EventEntity], work=0*
  7: 0x0059 [0x21] END_EVENT
  8: 0x005A [0x00] END_REQSTACK()
```
