# 17830122 - Chumli-Mojumli

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 308 bytes                 |
| Total Events     | 7                         |
| References Count | 16                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [547](#event-547)        | 0x0001       |     32 |             10 |
| [48](#event-48)          | 0x0021       |     48 |             12 |
| [592](#event-592)        | 0x0051       |     81 |             13 |
| [98](#event-98)          | 0x00A2       |      1 |              1 |
| [65535.1](#event-655351) | 0x00A3       |     14 |              4 |
| [65535.2](#event-655352) | 0x00B1       |     21 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0029      |          41 |
|       1 | 0x291F      |       10527 |
|       2 | 0x2920      |       10528 |
|       3 | 0x0028      |          40 |
|       4 | 0x1FBD      |        8125 |
|       5 | 0x1FBE      |        8126 |
|       6 | 0x0078      |         120 |
|       7 | 0x2921      |       10529 |
|       8 | 0x005A      |          90 |
|       9 | 0x000D      |          13 |
|      10 | 0x14834     |       84020 |
|      11 | 0xFFFE98E4  |  4294875364 |
|      12 | 0xFFFF6137  |  4294926647 |
|      13 | 0x147F7     |       83959 |
|      14 | 0xFFFE9DF3  |  4294876659 |
|      15 | 0xFFFF632A  |  4294927146 |

## String References

- **8125**: You've brought me a survey-wurvey about the Twelve Orders? I thought pioneers were supposed be out colonizing the land, not running menial tasks in Adoulin.
- **8126**: Everything about Woltaris is correctaru. I suppose that's all you need?
- **10527**: This impressive estataru belongs to Melvien de Malecroix, the minister of finance.
- **10528**: Despite fierce opposition from many in Adoulin, he convinced the council to move forward with the colonization effort. The only reason-weason you're able to stay here is because of him, so he deserves your utmost respect.
- **10529**: But now...none of us will ever see him again. The horrors-worrors of the jungle know no bounds!

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

### Event 547

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 32 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 65 68 6E 30 1D  01 80 23 1D 02 80 23 21  ...ehn0...#...#!
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ehn0" with entities [EventEntity, EventEntity], work=41*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10527*)
    → "This impressive estataru belongs to Melvien de Malecroix, the minister of finance."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=10528*)
    → "Despite fierce opposition from many in Adoulin, he convinced the council to move forward with the colonization effort. The only reason-weason you're able to stay here is because of him, so he deserves your utmost respect."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x21] END_EVENT
  9: 0x0020 [0x00] END_REQSTACK()
```

### Event 48

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 48 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    42 1E F0 FF FF 7F 6F  70 66 03 80 F8 FF FF 7F   B.....opf......
0030: F8 FF FF 7F 74 6C 6B 30  1D 04 80 23 1D 05 80 23  ....tlk0...#...#
0040: 66 03 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 21  f..........tlk1!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0021 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0022 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0028 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0029 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  5: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=8125*)
    → "You've brought me a survey-wurvey about the Twelve Orders? I thought pioneers were supposed be out colonizing the land, not running menial tasks in Adoulin."
  6: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=8126*)
    → "Everything about Woltaris is correctaru. I suppose that's all you need?"
  8: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0040 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 10: 0x004F [0x21] END_EVENT
 11: 0x0050 [0x00] END_REQSTACK()
```

### Event 592

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 81 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    1E F0 FF FF 7F 6F 70  1D 01 80 23 5F 06 03 80   .....op...#_...
0060: F8 FF FF 7F F8 FF FF 7F  67 6B 72 30 06 80 1D 07  ........gkr0....
0070: 80 5F 07 F8 FF FF 7F F8  FF FF 7F 67 6B 72 30 23  ._.........gkr0#
0080: 5F 06 03 80 F8 FF FF 7F  F8 FF FF 7F 67 6B 72 31  _...........gkr1
0090: 08 80 5F 07 F8 FF FF 7F  F8 FF FF 7F 67 6B 72 31  .._.........gkr1
00A0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0051 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0057 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=10527*)
    → "This impressive estataru belongs to Melvien de Malecroix, the minister of finance."
  4: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x005C [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=40*, entity1=EventEntity, entity2=EventEntity, string="gkr0", extra=120*)
  6: 0x006E [0x1D] PRINT_EVENT_MESSAGE(message_id=10529*)
    → "But now...none of us will ever see him again. The horrors-worrors of the jungle know no bounds!"
  7: 0x0071 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  8: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0080 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=40*, entity1=EventEntity, entity2=EventEntity, string="gkr1", extra=90*)
 10: 0x0092 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
 11: 0x00A0 [0x21] END_EVENT
 12: 0x00A1 [0x00] END_REQSTACK()
```

### Event 98

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       00                                            .             
```

#### Opcodes

```
  0: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          32 09 80 1F 00  0A 80 0B 80 0C 80 1F 01     2............
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x00A3 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A6 [0x1F] MOVE_ENTITY: EventEntity moves to X=84.020*, Z=-91.932*, Y=-40.649*
  2: 0x00AE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    32 09 80 1F 00 0D 80  0E 80 0F 80 1F 01 1E F0   2..............
00C0: FF FF 7F 6F 70 00                                 ...op.          
```

#### Opcodes

```
  0: 0x00B1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B4 [0x1F] MOVE_ENTITY: EventEntity moves to X=83.959*, Z=-90.637*, Y=-40.150*
  2: 0x00BC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BE [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00C3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00C4 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x00C5 [0x00] END_REQSTACK()
```
