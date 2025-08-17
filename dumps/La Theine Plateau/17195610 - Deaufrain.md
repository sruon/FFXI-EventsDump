# 17195610 - Deaufrain

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 196 bytes                   |
| Total Events     | 3                           |
| References Count | 6                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [102](#event-102)     | 0x0001       |     65 |              9 |
| [113](#event-113)     | 0x0042       |     78 |             18 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1CEF      |        7407 |
|       2 | 0x001E      |          30 |
|       3 | 0x1D01      |        7425 |
|       4 | 0x1D02      |        7426 |
|       5 | 0x1D03      |        7427 |

## String References

- **7407**: They're conducting drills up ahead... At least, I think they are.
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

### Event 102

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 65 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 31   f..........poi1
0010: 1D 01 80 23 53 F8 FF FF  7F F8 FF FF 7F 70 6F 69  ...#S........poi
0020: 31 66 00 80 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 32  1f..........poi2
0030: 53 F8 FF FF 7F F8 FF FF  7F 70 6F 69 32 1C 02 80  S........poi2...
0040: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=20*
  1: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=7407*)
    → "They're conducting drills up ahead... At least, I think they are."
  2: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0014 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
  4: 0x0021 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi2" with entities [EventEntity, EventEntity], work=20*
  5: 0x0030 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi2" with entities [EventEntity, EventEntity]
  6: 0x003D [0x1C] WAIT(30* ticks)
  7: 0x0040 [0x21] END_EVENT
  8: 0x0041 [0x00] END_REQSTACK()
```

### Event 113

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 78 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F    .....opf......
0050: F8 FF FF 7F 74 6C 6B 30  1D 03 80 23 1C 02 80 1D  ....tlk0...#....
0060: 04 80 23 5E 69 64 6C 30  1C 02 80 66 00 80 F8 FF  ..#^idl0...f....
0070: FF 7F F8 FF FF 7F 70 61  73 30 1D 05 80 23 53 F8  ......pas0...#S.
0080: FF FF 7F F8 FF FF 7F 70  61 73 30 1C 02 80 21 00  .......pas0...!.
```

#### Opcodes

```
  0: 0x0042 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0048 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0049 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=7425*)
    → "Ruillont's sword? Yes, I was keeping it for him during training."
  5: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x005C [0x1C] WAIT(30* ticks)
  7: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=7426*)
    → "What, Ruillont's stuck in a cave? How typical of him to refuse your help..."
  8: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0063 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 10: 0x0068 [0x1C] WAIT(30* ticks)
 11: 0x006B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
 12: 0x007A [0x1D] PRINT_EVENT_MESSAGE(message_id=7427*)
    → "Yes, I believe you; I'm sure it's him. Take this to him in there, would you? We'll keep it between you and me."
 13: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x007E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 15: 0x008B [0x1C] WAIT(30* ticks)
 16: 0x008E [0x21] END_EVENT
 17: 0x008F [0x00] END_REQSTACK()
```
