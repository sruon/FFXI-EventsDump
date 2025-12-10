# 17195615 - Galaihaurat

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 240 bytes                   |
| Total Events     | 3                           |
| References Count | 8                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [110](#event-110)     | 0x0001       |    104 |             20 |
| [114](#event-114)     | 0x0069       |     73 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1CFA      |        7418 |
|       2 | 0x001E      |          30 |
|       3 | 0x0EE4      |        3812 |
|       4 | 0x1CFB      |        7419 |
|       5 | 0x1D01      |        7425 |
|       6 | 0x1D02      |        7426 |
|       7 | 0x1D03      |        7427 |

## String References

- **7418**: Are you in the rescue drill?
- **7419**: Head to the other side of that valley over there. One of my compatriots will assist you.
- **7425**: Ruillont's sword? Yes, I was keeping it for him during training.
- **7426**: What, Ruillont's stuck in a cave? How typical of him to refuse your help...
- **7427**: Yes, I believe you; I'm sure it's him. Take this to him in there, would you? We'll keep it between you and me.

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

### Event 110

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 104 bytes |
| Instructions | 20        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 5E 69 64 6C 30  ...tlk0...#^idl0
0020: 1C 02 80 39 03 80 6F 70  66 00 80 F8 FF FF 7F F8  ...9..opf.......
0030: FF FF 7F 70 6F 69 31 1D  04 80 23 53 F8 FF FF 7F  ...poi1...#S....
0040: F8 FF FF 7F 70 6F 69 31  66 00 80 F8 FF FF 7F F8  ....poi1f.......
0050: FF FF 7F 70 6F 69 32 53  F8 FF FF 7F F8 FF FF 7F  ...poi2S........
0060: 70 6F 69 32 1C 02 80 21  00                       poi2...!.       
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7418*)
    → "Are you in the rescue drill?"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0020 [0x1C] WAIT(30* ticks)
  8: 0x0023 [0x39] SET_ENTITY_DIRECTION(direction=20.9°*)
  9: 0x0026 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x0027 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 11: 0x0028 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=20*
 12: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=7419*)
    → "Head to the other side of that valley over there. One of my compatriots will assist you."
 13: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x003B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
 15: 0x0048 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi2" with entities [EventEntity, EventEntity], work=20*
 16: 0x0057 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi2" with entities [EventEntity, EventEntity]
 17: 0x0064 [0x1C] WAIT(30* ticks)
 18: 0x0067 [0x21] END_EVENT
 19: 0x0068 [0x00] END_REQSTACK()
```

### Event 114

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 73 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             1E F0 FF FF 7F 6F 70           .....op
0070: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0080: 05 80 23 1C 02 80 1D 06  80 23 1C 02 80 66 00 80  ..#......#...f..
0090: F8 FF FF 7F F8 FF FF 7F  70 61 73 30 1D 07 80 23  ........pas0...#
00A0: 53 F8 FF FF 7F F8 FF FF  7F 70 61 73 30 1C 02 80  S........pas0...
00B0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0069 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x006E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x006F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0070 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x007F [0x1D] PRINT_EVENT_MESSAGE(message_id=7425*)
    → "Ruillont's sword? Yes, I was keeping it for him during training."
  5: 0x0082 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0083 [0x1C] WAIT(30* ticks)
  7: 0x0086 [0x1D] PRINT_EVENT_MESSAGE(message_id=7426*)
    → "What, Ruillont's stuck in a cave? How typical of him to refuse your help..."
  8: 0x0089 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x008A [0x1C] WAIT(30* ticks)
 10: 0x008D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
 11: 0x009C [0x1D] PRINT_EVENT_MESSAGE(message_id=7427*)
    → "Yes, I believe you; I'm sure it's him. Take this to him in there, would you? We'll keep it between you and me."
 12: 0x009F [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00A0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 14: 0x00AD [0x1C] WAIT(30* ticks)
 15: 0x00B0 [0x21] END_EVENT
 16: 0x00B1 [0x00] END_REQSTACK()
```
