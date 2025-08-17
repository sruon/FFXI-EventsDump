# 17776662 - Rouliette

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 180 bytes             |
| Total Events     | 5                     |
| References Count | 7                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [159](#event-159)     | 0x0001       |      1 |              1 |
| [30](#event-30)       | 0x0002       |     28 |              8 |
| [36](#event-36)       | 0x001E       |     37 |             11 |
| [37](#event-37)       | 0x0043       |     48 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1BB4      |        7092 |
|       2 | 0x0213      |         531 |
|       3 | 0x1BB5      |        7093 |
|       4 | 0x1BB6      |        7094 |
|       5 | 0x00C9      |         201 |
|       6 | 0x0000      |           0 |

## String References

- **7092**: The Temple of the Goddess welcomes you. If you seek guidance, join us in prayer. Her divine wisdom will light the path.
- **7093**: Oh, all you want is a candle? Very well. Fetch me $7, and a candle will be yours.
- **7094**: Excellent. As promised, I bestow upon you this holy candle. May its light guide you along the path of righteousness!

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

### Event 159

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F    .....opf......
0010: F8 FF FF 7F 74 6C 6B 30  1D 01 80 23 21 00        ....tlk0...#!.  
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7092*)
    → "The Temple of the Goddess welcomes you. If you seek guidance, join us in prayer. Her divine wisdom will light the path."
  5: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001C [0x21] END_EVENT
  7: 0x001D [0x00] END_REQSTACK()
```

### Event 36

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 37 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            1E F0                ..
0020: FF FF 7F 6F 70 03 09 10  02 80 66 00 80 F8 FF FF  ...op.....f.....
0030: 7F F8 FF FF 7F 74 6C 6B  30 1D 01 80 23 1D 03 80  .....tlk0...#...
0040: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x001E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0024 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0025 [0x03] Work_Zone[9] = 531*
  4: 0x002A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  5: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=7092*)
    → "The Temple of the Goddess welcomes you. If you seek guidance, join us in prayer. Her divine wisdom will light the path."
  6: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=7093*)
    → "Oh, all you want is a candle? Very well. Fetch me $7, and a candle will be yours."
  8: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0041 [0x21] END_EVENT
 10: 0x0042 [0x00] END_REQSTACK()
```

### Event 37

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 48 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          20 01 42 1E F0  FF FF 7F 6F 70 66 00 80      .B.....opf..
0050: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 04 80 23  ........tlk0...#
0060: 45 05 80 F0 FF FF 7F F0  FF FF 7F 71 73 74 63 06  E..........qstc.
0070: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0043 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0045 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0046 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x004B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x004D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  6: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=7094*)
    → "Excellent. As promised, I bestow upon you this holy candle. May its light guide you along the path of righteousness!"
  7: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0060 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  9: 0x0071 [0x21] END_EVENT
 10: 0x0072 [0x00] END_REQSTACK()
```
