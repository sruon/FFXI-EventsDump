# 17772563 - Chapi Galepilai

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 340 bytes                 |
| Total Events     | 6                         |
| References Count | 11                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [11](#event-11)       | 0x0001       |     60 |             12 |
| [12](#event-12)       | 0x003D       |     64 |             14 |
| [13](#event-13)       | 0x007D       |     60 |             12 |
| [148](#event-148)     | 0x00B9       |     68 |             14 |
| [10244](#event-10244) | 0x00FD       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003B      |          59 |
|       1 | 0x2B48      |       11080 |
|       2 | 0x2B49      |       11081 |
|       3 | 0x2B4F      |       11087 |
|       4 | 0x2B50      |       11088 |
|       5 | 0x2B51      |       11089 |
|       6 | 0x2B5B      |       11099 |
|       7 | 0x2B5C      |       11100 |
|       8 | 0x27D9      |       10201 |
|       9 | 0x27DA      |       10202 |
|      10 | 0x27DB      |       10203 |

## String References

- **10201**: Lords Kam'lanaut and Eald'narche rarely make public appearances.
- **10202**: And you need a special permit just to have an audience with them.
- **10203**: Both have kept their youth through all these years. Perhaps some otherworldly power watches over them. Great prophets like them are few indeed!
- **11080**: You want to know about the hooded officials in black robes that sometimes appear in the courtyard?
- **11081**: They are all members of the Armathrwn Society--scientists working for the Duchy. I have heard that there are even quite a few female members.
- **11087**: Have you seen a strange-looking boy or girl running about the gardens?
- **11088**: If you have, inform one of the Ducal Guards. There are currently warrrrants out for both of their arrrrests.
- **11089**: Their capture is crucial to the safety of not just Jeuno, but of all Vana'diel. You and your fellow adventurers' assistance in the matter is greatly appreciated.
- **11099**: If you have any information on the whereabouts of the girl the Duchy was searching for, I am sorry, but the warrant for her arrest has been dropped.
- **11100**: The Ducal Guard recently received news of her death...

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

### Event 11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 60 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 66  ...tlk0...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 53 F8  ..........tlk1S.
0030: FF FF 7F F8 FF FF 7F 74  6C 6B 31 21 00           .......tlk1!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=11080*)
    → "You want to know about the hooded officials in black robes that sometimes appear in the courtyard?"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=11081*)
    → "They are all members of the Armathrwn Society--scientists working for the Duchy. I have heard that there are even quite a few female members."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  9: 0x002E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 10: 0x003B [0x21] END_EVENT
 11: 0x003C [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 64 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         1E F0 FF               ...
0040: FF 7F 6F 70 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..opf..........t
0050: 6C 6B 30 1D 03 80 23 1D  04 80 23 1D 05 80 23 66  lk0...#...#...#f
0060: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 53 F8  ..........tlk1S.
0070: FF FF 7F F8 FF FF 7F 74  6C 6B 31 21 00           .......tlk1!.   
```

#### Opcodes

```
  0: 0x003D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0042 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0043 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0044 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  4: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=11087*)
    → "Have you seen a strange-looking boy or girl running about the gardens?"
  5: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0057 [0x1D] PRINT_EVENT_MESSAGE(message_id=11088*)
    → "If you have, inform one of the Ducal Guards. There are currently warrrrants out for both of their arrrrests."
  7: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x005B [0x1D] PRINT_EVENT_MESSAGE(message_id=11089*)
    → "Their capture is crucial to the safety of not just Jeuno, but of all Vana'diel. You and your fellow adventurers' assistance in the matter is greatly appreciated."
  9: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x005F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 11: 0x006E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 12: 0x007B [0x21] END_EVENT
 13: 0x007C [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 60 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         1E F0 FF               ...
0080: FF 7F 6F 70 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..opf..........t
0090: 6C 6B 30 1D 06 80 23 1D  07 80 23 66 00 80 F8 FF  lk0...#...#f....
00A0: FF 7F F8 FF FF 7F 74 6C  6B 31 53 F8 FF FF 7F F8  ......tlk1S.....
00B0: FF FF 7F 74 6C 6B 31 21  00                       ...tlk1!.       
```

#### Opcodes

```
  0: 0x007D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0082 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0083 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0084 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  4: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=11099*)
    → "If you have any information on the whereabouts of the girl the Duchy was searching for, I am sorry, but the warrant for her arrest has been dropped."
  5: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0097 [0x1D] PRINT_EVENT_MESSAGE(message_id=11100*)
    → "The Ducal Guard recently received news of her death..."
  7: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x009B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  9: 0x00AA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 10: 0x00B7 [0x21] END_EVENT
 11: 0x00B8 [0x00] END_REQSTACK()
```

### Event 148

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 68 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             1E F0 FF FF 7F 6F 76           .....ov
00C0: F8 FF FF 7F 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ....f..........t
00D0: 6C 6B 30 1D 08 80 23 1D  09 80 23 1D 0A 80 23 66  lk0...#...#...#f
00E0: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 53 F8  ..........tlk1S.
00F0: FF FF 7F F8 FF FF 7F 74  6C 6B 31 21 00           .......tlk1!.   
```

#### Opcodes

```
  0: 0x00B9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00BE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00BF [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x00C4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  4: 0x00D3 [0x1D] PRINT_EVENT_MESSAGE(message_id=10201*)
    → "Lords Kam'lanaut and Eald'narche rarely make public appearances."
  5: 0x00D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00D7 [0x1D] PRINT_EVENT_MESSAGE(message_id=10202*)
    → "And you need a special permit just to have an audience with them."
  7: 0x00DA [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00DB [0x1D] PRINT_EVENT_MESSAGE(message_id=10203*)
    → "Both have kept their youth through all these years. Perhaps some otherworldly power watches over them. Great prophets like them are few indeed!"
  9: 0x00DE [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00DF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 11: 0x00EE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 12: 0x00FB [0x21] END_EVENT
 13: 0x00FC [0x00] END_REQSTACK()
```

### Event 10244

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00FD  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                         00                     .  
```

#### Opcodes

```
  0: 0x00FD [0x00] END_REQSTACK()
```
