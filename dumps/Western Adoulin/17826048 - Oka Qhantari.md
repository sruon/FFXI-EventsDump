# 17826048 - Oka Qhantari

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 144 bytes                 |
| Total Events     | 3                         |
| References Count | 5                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [511](#event-511)     | 0x0001       |     47 |             11 |
| [71](#event-71)       | 0x0030       |     48 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0035      |          53 |
|       1 | 0x262C      |        9772 |
|       2 | 0x262D      |        9773 |
|       3 | 0x1FCF      |        8143 |
|       4 | 0x1FD0      |        8144 |

## String References

- **8143**: Welcome. You're here on behalf of the library, yes?
- **8144**: Their records of our order appear to be complete. Thank you for coming to check.
- **9772**: I take it you've already hearrrd of the Pioneers' Coalition?
- **9773**: Then one of Adoulin's many figures you should learn to rrrecognize is Lhe Lhangavo, the coalition's current maester.

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

### Event 511

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
0010: FF FF 7F 74 6C 62 31 1D  01 80 23 1D 02 80 23 66  ...tlb1...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 32 21 00  ..........tlb2!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=53*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=9772*)
    → "I take it you've already hearrrd of the Pioneers' Coalition?"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=9773*)
    → "Then one of Adoulin's many figures you should learn to rrrecognize is Lhe Lhangavo, the coalition's current maester."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb2" with entities [EventEntity, EventEntity], work=53*
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 71

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 48 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 42 1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8  B.....opf.......
0040: FF FF 7F 74 6C 62 31 1D  03 80 23 1D 04 80 23 66  ...tlb1...#...#f
0050: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 32 21 00  ..........tlb2!.
```

#### Opcodes

```
  0: 0x0030 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0031 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0036 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0037 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=53*
  5: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=8143*)
    → "Welcome. You're here on behalf of the library, yes?"
  6: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=8144*)
    → "Their records of our order appear to be complete. Thank you for coming to check."
  8: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb2" with entities [EventEntity, EventEntity], work=53*
 10: 0x005E [0x21] END_EVENT
 11: 0x005F [0x00] END_REQSTACK()
```
