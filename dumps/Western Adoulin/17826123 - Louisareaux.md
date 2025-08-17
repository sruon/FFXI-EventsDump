# 17826123 - Louisareaux

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 196 bytes                 |
| Total Events     | 3                         |
| References Count | 11                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [176](#event-176)     | 0x0001       |     28 |             10 |
| [175](#event-175)     | 0x001D       |     92 |             28 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2DB2      |       11698 |
|       1 | 0x2DAB      |       11691 |
|       2 | 0x001E      |          30 |
|       3 | 0x2DAC      |       11692 |
|       4 | 0x2DAD      |       11693 |
|       5 | 0x2DAE      |       11694 |
|       6 | 0x2DAF      |       11695 |
|       7 | 0x2DB0      |       11696 |
|       8 | 0x2DB1      |       11697 |
|       9 | 0x0A18      |        2584 |
|      10 | 0x313D      |       12605 |

## String References

- **11691**: Hm? You wish to hear about the olden days of colonization?
- **11692**: Well, I am never one to turn down a chance to tell a story. How about this one?
- **11693**: You have knowledge of Sverdhried--or at least his eponymous hillock--correct? Well, he supposedly traveled around the world, visiting each and every continent.
- **11694**: If I have yet to lose my marbles, that should have taken place around the time colonization was taking off.
- **11695**: Furthermore, I hear that a long-lost civilization exists on the frozen continent of Rhazowa.
- **11696**: Whether that is genuine fact or pure conjecture I cannot say.
- **11697**: You will have to use your own powers of deduction to determine that yourself.
- **11698**: I have nothing against pioneers...as long as they understand the possible repercussions of their actions.
- **12605**: You scribbled down some information regarding $6.

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

### Event 176

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  4A F0 FF FF 7F F8 FF FF   .....opJ.......
0010: 7F 6F 76 F0 FF FF 7F 1D  00 80 23 21 00           .ov.......#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x4A] LocalPlayer looks at EventEntity
  4: 0x0011 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0012 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=11698*)
    → "I have nothing against pioneers...as long as they understand the possible repercussions of their actions."
  7: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001B [0x21] END_EVENT
  9: 0x001C [0x00] END_REQSTACK()
```

### Event 175

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 92 bytes |
| Instructions | 28       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         42 1E F0               B..
0020: FF FF 7F 6F 70 4A F0 FF  FF 7F F8 FF FF 7F 6F 76  ...opJ........ov
0030: F0 FF FF 7F 1D 01 80 23  5B 02 80 F8 FF FF 7F F8  .......#[.......
0040: FF FF 7F 74 6C 6B 30 1D  03 80 23 1D 04 80 23 1D  ...tlk0...#...#.
0050: 05 80 23 1D 06 80 23 5B  02 80 F8 FF FF 7F F8 FF  ..#...#[........
0060: FF 7F 74 6C 6B 31 1D 07  80 23 1D 08 80 23 03 02  ..tlk1...#...#..
0070: 10 09 80 48 0A 80 23 21  00                       ...H..#!.       
```

#### Opcodes

```
  0: 0x001D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x001E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0024 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0025 [0x4A] LocalPlayer looks at EventEntity
  5: 0x002E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x002F [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=11691*)
    → "Hm? You wish to hear about the olden days of colonization?"
  8: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0038 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
 10: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=11692*)
    → "Well, I am never one to turn down a chance to tell a story. How about this one?"
 11: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=11693*)
    → "You have knowledge of Sverdhried--or at least his eponymous hillock--correct? Well, he supposedly traveled around the world, visiting each and every continent."
 13: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=11694*)
    → "If I have yet to lose my marbles, that should have taken place around the time colonization was taking off."
 15: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=11695*)
    → "Furthermore, I hear that a long-lost civilization exists on the frozen continent of Rhazowa."
 17: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0057 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=30*
 19: 0x0066 [0x1D] PRINT_EVENT_MESSAGE(message_id=11696*)
    → "Whether that is genuine fact or pure conjecture I cannot say."
 20: 0x0069 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x006A [0x1D] PRINT_EVENT_MESSAGE(message_id=11697*)
    → "You will have to use your own powers of deduction to determine that yourself."
 22: 0x006D [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x006E [0x03] Work_Zone[2] = 2584*
 24: 0x0073 [0x48] [System] [12605*]:
    → "You scribbled down some information regarding $6."
 25: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0077 [0x21] END_EVENT
 27: 0x0078 [0x00] END_REQSTACK()
```
