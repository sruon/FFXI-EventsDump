# 17776644 - Constance

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 168 bytes             |
| Total Events     | 4                     |
| References Count | 9                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [90](#event-90)       | 0x0001       |     55 |             13 |
| [180](#event-180)     | 0x0038       |     43 |             17 |
| [33](#event-33)       | 0x0063       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0046      |          70 |
|       1 | 0x1B76      |        7030 |
|       2 | 0x1B77      |        7031 |
|       3 | 0x1B78      |        7032 |
|       4 | 0x1B79      |        7033 |
|       5 | 0x1B7A      |        7034 |
|       6 | 0x0000      |           0 |
|       7 | 0x1B5D      |        7005 |
|       8 | 0x1B5E      |        7006 |

## String References

- **7005**: The petition is complete!
- **7006**: You have $0 more [signature/signatures] to go.
- **7030**: Monberaux and Wolfgang have known each other since they were lads. Indeed, they were like brothers, watching the airships come and go.
- **7031**: And now one's a doctor and the other the captain of the guard. I'm so proud of both of them!
- **7032**: But you know, I hardly see them together anymore. I'm sure they're both very busy.
- **7033**: What, no more clock tower? No! The pride of Jeuno, she saw us through the war! What about Galmut? Good heavens, where do I sign!?
- **7034**: Galmut used to be a regular hooligan, but once he became the clockmaster, he turned over a new leaf and began doing repairs for us, too.

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

### Event 90

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 55 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 76  F8 FF FF 7F 5B 00 80 F8   .....ov....[...
0010: FF FF 7F F8 FF FF 7F 74  68 6B 31 1D 01 80 23 1D  .......thk1...#.
0020: 02 80 23 5B 00 80 F8 FF  FF 7F F8 FF FF 7F 74 68  ..#[..........th
0030: 6B 32 1D 03 80 23 21 00                           k2...#!.        
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x000C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=70*
  4: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=7030*)
    → "Monberaux and Wolfgang have known each other since they were lads. Indeed, they were like brothers, watching the airships come and go."
  5: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=7031*)
    → "And now one's a doctor and the other the captain of the guard. I'm so proud of both of them!"
  7: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0023 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=70*
  9: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=7032*)
    → "But you know, I hardly see them together anymore. I'm sure they're both very busy."
 10: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0036 [0x21] END_EVENT
 12: 0x0037 [0x00] END_REQSTACK()
```

### Event 180

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 43 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          20 01 42 1E F0 FF FF 7F           .B.....
0040: 6F 76 F8 FF FF 7F 1D 04  80 23 1D 05 80 23 02 02  ov.......#...#..
0050: 10 06 80 00 5D 00 48 07  80 23 01 61 00 48 08 80  ....].H..#.a.H..
0060: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0038 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x003A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x003B [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0041 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  5: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=7033*)
    → "What, no more clock tower? No! The pride of Jeuno, she saw us through the war! What about Galmut? Good heavens, where do I sign!?"
  6: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=7034*)
    → "Galmut used to be a regular hooligan, but once he became the clockmaster, he turned over a new leaf and began doing repairs for us, too."
  8: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004E [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x005D
 10: 0x0056 [0x48] [System] [7005*]:
    → "The petition is complete!"
 11: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x005A [0x01] GOTO 0x0061
 13: 0x005D [0x48] [System] [7006*]:
    → "You have $0 more [signature/signatures] to go."
 14: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0061:
 15: 0x0061 [0x21] END_EVENT
 16: 0x0062 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          00                                          .            
```

#### Opcodes

```
  0: 0x0063 [0x00] END_REQSTACK()
```
