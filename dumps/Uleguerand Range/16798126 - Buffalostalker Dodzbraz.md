# 16798126 - Buffalostalker Dodzbraz

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Uleguerand Range (ID: 5) |
| Block Size       | 220 bytes                |
| Total Events     | 4                        |
| References Count | 13                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [6](#event-6)         | 0x0001       |     71 |             24 |
| [7](#event-7)         | 0x0048       |     23 |             12 |
| [8](#event-8)         | 0x005F       |     41 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CAF      |        7343 |
|       1 | 0x1CB0      |        7344 |
|       2 | 0x1CB1      |        7345 |
|       3 | 0x0000      |           0 |
|       4 | 0x0001      |           1 |
|       5 | 0x1CB2      |        7346 |
|       6 | 0x1CB3      |        7347 |
|       7 | 0x1CB4      |        7348 |
|       8 | 0x0002      |           2 |
|       9 | 0x1CB5      |        7349 |
|      10 | 0x1CB6      |        7350 |
|      11 | 0x1CB7      |        7351 |
|      12 | 0x00C9      |         201 |

## String References

- **7343**: Me hunter. Me gets food for other Orcs. Not here to fights with you.
- **7344**: Nasty snolls in mountains. You climbs mountains?
- **7345**: You climbs mountains? [Yep./Nope.]
- **7346**: Me hates snolls. Me tells you secret.
- **7347**: Brings me two cores from bomb clusters.
- **7348**: Me gives you present.
- **7349**: <Snuffle...grunt> Me needs these cores.
- **7350**: You takes this.
- **7351**: You uses on snolls. They starts to melts. Gahahaha!

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

### Event 6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 71 bytes |
| Instructions | 24       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 1D 01 80 23   .....op...#...#
0010: 24 02 80 03 80 03 80 25  02 00 10 03 80 00 34 00  $......%......4.
0020: 03 01 10 04 80 1D 05 80  23 1D 06 80 23 1D 07 80  ........#...#...
0030: 23 01 44 00 02 00 10 04  80 00 44 00 03 01 10 08  #.D.......D.....
0040: 80 01 44 00 20 00 21 00                           ..D. .!.        
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7343*)
    → "Me hunter. Me gets food for other Orcs. Not here to fights with you."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=7344*)
    → "Nasty snolls in mountains. You climbs mountains?"
  6: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0010 [0x24] CREATE_DIALOG(message_id=7345*, default_option=0*, option_flags=0*)
    → "You climbs mountains? [Yep./Nope.]"
  8: 0x0017 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0018 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0034
 10: 0x0020 [0x03] Work_Zone[1] = 1*
 11: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7346*)
    → "Me hates snolls. Me tells you secret."
 12: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=7347*)
    → "Brings me two cores from bomb clusters."
 14: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=7348*)
    → "Me gives you present."
 16: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0031 [0x01] GOTO 0x0044
 18: 0x0034 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0044
 19: 0x003C [0x03] Work_Zone[1] = 2*
 20: 0x0041 [0x01] GOTO 0x0044

SUBROUTINE_0044:
 21: 0x0044 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 22: 0x0046 [0x21] END_EVENT
 23: 0x0047 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 23 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          1E F0 FF FF 7F 6F 70 1D          .....op.
0050: 05 80 23 1D 06 80 23 1D  07 80 23 20 00 21 00     ..#...#...# .!. 
```

#### Opcodes

```
  0: 0x0048 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x004D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=7346*)
    → "Me hates snolls. Me tells you secret."
  4: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=7347*)
    → "Brings me two cores from bomb clusters."
  6: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0057 [0x1D] PRINT_EVENT_MESSAGE(message_id=7348*)
    → "Me gives you present."
  8: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x005B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x005D [0x21] END_EVENT
 11: 0x005E [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 41 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               42                 B
0060: 1E F0 FF FF 7F 6F 70 1D  09 80 23 1D 0A 80 23 1D  .....op...#...#.
0070: 0B 80 23 45 0C 80 F0 FF  FF 7F F0 FF FF 7F 71 73  ..#E..........qs
0080: 74 63 03 80 20 00 21 00                           tc.. .!.        
```

#### Opcodes

```
  0: 0x005F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0060 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0065 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0066 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=7349*)
    → "<Snuffle...grunt> Me needs these cores."
  5: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x006B [0x1D] PRINT_EVENT_MESSAGE(message_id=7350*)
    → "You takes this."
  7: 0x006E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x006F [0x1D] PRINT_EVENT_MESSAGE(message_id=7351*)
    → "You uses on snolls. They starts to melts. Gahahaha!"
  9: 0x0072 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0073 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 11: 0x0084 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0086 [0x21] END_EVENT
 13: 0x0087 [0x00] END_REQSTACK()
```
