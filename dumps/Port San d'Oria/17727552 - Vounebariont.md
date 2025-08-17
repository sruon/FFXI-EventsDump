# 17727552 - Vounebariont

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 328 bytes                 |
| Total Events     | 4                         |
| References Count | 16                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [568](#event-568)     | 0x0001       |     50 |             16 |
| [516](#event-516)     | 0x0033       |     81 |             27 |
| [514](#event-514)     | 0x0084       |     98 |             20 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1DBD      |        7613 |
|       2 | 0x003C      |          60 |
|       3 | 0x1DBE      |        7614 |
|       4 | 0x1DBF      |        7615 |
|       5 | 0x1DB2      |        7602 |
|       6 | 0x1DB3      |        7603 |
|       7 | 0x1DB4      |        7604 |
|       8 | 0x1DB5      |        7605 |
|       9 | 0x0379      |         889 |
|      10 | 0x1DB6      |        7606 |
|      11 | 0x1DB7      |        7607 |
|      12 | 0x1DB8      |        7608 |
|      13 | 0x1DB9      |        7609 |
|      14 | 0x00C9      |         201 |
|      15 | 0x0000      |           0 |

## String References

- **7602**: Hmm... You don't look like the riffraff we get around here. No wet-behind-the-ears recruit, are you?
- **7603**: I be Vounebariont, brewer of potions and medicines.
- **7604**: I've been waiting here a good long time now for a shipment, ingredients for me potions, you see. But it's not arrived!
- **7605**: I don't suppose you could be persuaded to fetch five beetle shells from Jugner Forest, now, could you?
- **7606**: %, some call 'em "coleoptera shells." They're a rare but vital ingredient in potions.
- **7607**: If you'd be so kind as to bring me five of those $0, I'd pay you handsomely, or my name's not Vounebariont!
- **7608**: You're back, and with the shells as requested! Here's your payment then, like I promised you.
- **7609**: Should the mood strike you, I'm willing to buy more $0. Bring five, and we'll do business.
- **7613**: I dare say that our two princes bicker over which is to inherit the throne.
- **7614**: The elder's a warrior, the younger a thinker, and neither bows to the other. The two knightly orders' loyalties are split between them...
- **7615**: With such intrigue inside our walls, beastmen roam the countryside. And there's precious little we can do about it!

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

### Event 568

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 50 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  5B 00 80 F8 FF FF 7F F8   .....op[.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1C 02 80 1D 03  ...tlk0...#.....
0020: 80 23 1C 02 80 1D 04 80  23 5E 69 64 6C 30 1C 02  .#......#^idl0..
0030: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7613*)
    → "I dare say that our two princes bicker over which is to inherit the throne."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1C] WAIT(60* ticks)
  7: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7614*)
    → "The elder's a warrior, the younger a thinker, and neither bows to the other. The two knightly orders' loyalties are split between them..."
  8: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0022 [0x1C] WAIT(60* ticks)
 10: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7615*)
    → "With such intrigue inside our walls, beastmen roam the countryside. And there's precious little we can do about it!"
 11: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0029 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 13: 0x002E [0x1C] WAIT(60* ticks)
 14: 0x0031 [0x21] END_EVENT
 15: 0x0032 [0x00] END_REQSTACK()
```

### Event 516

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 81 bytes |
| Instructions | 27       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          1E F0 FF FF 7F  6F 70 5B 00 80 F8 FF FF     .....op[.....
0040: 7F F8 FF FF 7F 74 6C 6B  30 1D 05 80 23 1C 02 80  .....tlk0...#...
0050: 1D 06 80 23 1C 02 80 1D  07 80 23 1C 02 80 1D 08  ...#......#.....
0060: 80 23 1C 02 80 03 02 10  09 80 1D 0A 80 23 1C 02  .#...........#..
0070: 80 03 02 10 09 80 1D 0B  80 23 5E 69 64 6C 30 1C  .........#^idl0.
0080: 02 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0033 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0038 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0039 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x003A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=7602*)
    → "Hmm... You don't look like the riffraff we get around here. No wet-behind-the-ears recruit, are you?"
  5: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004D [0x1C] WAIT(60* ticks)
  7: 0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=7603*)
    → "I be Vounebariont, brewer of potions and medicines."
  8: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0054 [0x1C] WAIT(60* ticks)
 10: 0x0057 [0x1D] PRINT_EVENT_MESSAGE(message_id=7604*)
    → "I've been waiting here a good long time now for a shipment, ingredients for me potions, you see. But it's not arrived!"
 11: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x005B [0x1C] WAIT(60* ticks)
 13: 0x005E [0x1D] PRINT_EVENT_MESSAGE(message_id=7605*)
    → "I don't suppose you could be persuaded to fetch five beetle shells from Jugner Forest, now, could you?"
 14: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0062 [0x1C] WAIT(60* ticks)
 16: 0x0065 [0x03] Work_Zone[2] = 889*
 17: 0x006A [0x1D] PRINT_EVENT_MESSAGE(message_id=7606*)
    → "%, some call 'em "coleoptera shells." They're a rare but vital ingredient in potions."
 18: 0x006D [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x006E [0x1C] WAIT(60* ticks)
 20: 0x0071 [0x03] Work_Zone[2] = 889*
 21: 0x0076 [0x1D] PRINT_EVENT_MESSAGE(message_id=7607*)
    → "If you'd be so kind as to bring me five of those $0, I'd pay you handsomely, or my name's not Vounebariont!"
 22: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x007A [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 24: 0x007F [0x1C] WAIT(60* ticks)
 25: 0x0082 [0x21] END_EVENT
 26: 0x0083 [0x00] END_REQSTACK()
```

### Event 514

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 98 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             42 20 01 1E  F0 FF FF 7F 6F 70 5B 00      B ......op[.
0090: 80 F8 FF FF 7F F8 FF FF  7F 70 61 73 30 1D 0C 80  .........pas0...
00A0: 23 53 F8 FF FF 7F F8 FF  FF 7F 70 61 73 30 1C 02  #S........pas0..
00B0: 80 5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .[..........tlk0
00C0: 03 02 10 09 80 1D 0D 80  23 5E 69 64 6C 30 45 0E  ........#^idl0E.
00D0: 80 F0 FF FF 7F F0 FF FF  7F 71 73 74 63 0F 80 1C  .........qstc...
00E0: 00 80 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x0084 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0085 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0087 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x008C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x008E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=30*
  6: 0x009D [0x1D] PRINT_EVENT_MESSAGE(message_id=7608*)
    → "You're back, and with the shells as requested! Here's your payment then, like I promised you."
  7: 0x00A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00A1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  9: 0x00AE [0x1C] WAIT(60* ticks)
 10: 0x00B1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
 11: 0x00C0 [0x03] Work_Zone[2] = 889*
 12: 0x00C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7609*)
    → "Should the mood strike you, I'm willing to buy more $0. Bring five, and we'll do business."
 13: 0x00C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00C9 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 15: 0x00CE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 16: 0x00DF [0x1C] WAIT(30* ticks)
 17: 0x00E2 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 18: 0x00E4 [0x21] END_EVENT
 19: 0x00E5 [0x00] END_REQSTACK()
```
