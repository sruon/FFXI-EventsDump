# 17195617 - Vicorpasse

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 304 bytes                   |
| Total Events     | 7                           |
| References Count | 13                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2](#event-2)         | 0x0001       |     13 |              7 |
| [3](#event-3)         | 0x000E       |     13 |              7 |
| [4](#event-4)         | 0x001B       |     13 |              7 |
| [5](#event-5)         | 0x0028       |     13 |              7 |
| [108](#event-108)     | 0x0035       |     50 |             16 |
| [115](#event-115)     | 0x0067       |    104 |             22 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E42      |        7746 |
|       1 | 0x1E43      |        7747 |
|       2 | 0x1E44      |        7748 |
|       3 | 0x1E45      |        7749 |
|       4 | 0x0014      |          20 |
|       5 | 0x1CFC      |        7420 |
|       6 | 0x001E      |          30 |
|       7 | 0x1CFD      |        7421 |
|       8 | 0x1CFE      |        7422 |
|       9 | 0x1D05      |        7429 |
|      10 | 0x0041      |          65 |
|      11 | 0x1D06      |        7430 |
|      12 | 0x1D07      |        7431 |

## String References

- **7420**: Greetings. I'm Vicorpasse, squad captain in the Temple Knights.
- **7421**: We are supposed to be conducting rescue drills, but one of our "injured" soldiers has gone missing. Your assistance in finding him would be appreciated.
- **7422**: The missing soldier is a new recruit by the name of Ruillont. I just hope nothing's happened to him...
- **7429**: What? Ruillont's in that cave? And he doesn't want us to send help, eh? That's my boy! He's an elite in the making, that one!
- **7430**: Well, the rescue training was a wash, but you helped us find our lost soldier. I think you've earned this $3.
- **7431**: No, really. These drills are naught compared to venturing into one of those caves. Hand that certificate to the knight at the gatehouse, and you'll be done.
- **7746**: I have spoken with Sir Elmemague. Narvecaint is currently monitoring the suspect's movements from the entrance to the caves.
- **7747**: Well, I suppose we can regard this as an adequate performance. It will still be necessary to further refine our soldiers' training... However, this was an excellent opportunity for the knights to practice their skills in a real-life situation.
- **7748**: Another chance to test the effectiveness of our training in almost exactly the same setting! This time, I expect perfect coordination and execution from my men.
- **7749**: Hmm, there is still room for improvement. They need to work on communication to facilitate speedier responses... Lady Curilla will not be pleased.

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

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 21 00         .....op...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7746*)
    → "I have spoken with Sir Elmemague. Narvecaint is currently monitoring the suspect's movements from the entrance to the caves."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            1E F0                ..
0010: FF FF 7F 6F 70 1D 01 80  23 21 00                 ...op...#!.     
```

#### Opcodes

```
  0: 0x000E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0013 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0014 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=7747*)
    → "Well, I suppose we can regard this as an adequate performance. It will still be necessary to further refine our soldiers' training... However, this was an excellent opportunity for the knights to practice their skills in a real-life situation."
  4: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0019 [0x21] END_EVENT
  6: 0x001A [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1E F0 FF FF 7F             .....
0020: 6F 70 1D 02 80 23 21 00                           op...#!.        
```

#### Opcodes

```
  0: 0x001B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0020 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0021 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7748*)
    → "Another chance to test the effectiveness of our training in almost exactly the same setting! This time, I expect perfect coordination and execution from my men."
  4: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0026 [0x21] END_EVENT
  6: 0x0027 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          1E F0 FF FF 7F 6F 70 1D          .....op.
0030: 03 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x0028 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x002E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=7749*)
    → "Hmm, there is still room for improvement. They need to work on communication to facilitate speedier responses... Lady Curilla will not be pleased."
  4: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0033 [0x21] END_EVENT
  6: 0x0034 [0x00] END_REQSTACK()
```

### Event 108

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 50 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                1E F0 FF  FF 7F 6F 70 66 04 80 F8       .....opf...
0040: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 05 80 23 1C  .......tlk0...#.
0050: 06 80 1D 07 80 23 1C 06  80 1D 08 80 23 5E 69 64  .....#......#^id
0060: 6C 30 1C 06 80 21 00                              l0...!.         
```

#### Opcodes

```
  0: 0x0035 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x003C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=7420*)
    → "Greetings. I'm Vicorpasse, squad captain in the Temple Knights."
  5: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004F [0x1C] WAIT(30* ticks)
  7: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=7421*)
    → "We are supposed to be conducting rescue drills, but one of our "injured" soldiers has gone missing. Your assistance in finding him would be appreciated."
  8: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0056 [0x1C] WAIT(30* ticks)
 10: 0x0059 [0x1D] PRINT_EVENT_MESSAGE(message_id=7422*)
    → "The missing soldier is a new recruit by the name of Ruillont. I just hope nothing's happened to him..."
 11: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x005D [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 13: 0x0062 [0x1C] WAIT(30* ticks)
 14: 0x0065 [0x21] END_EVENT
 15: 0x0066 [0x00] END_REQSTACK()
```

### Event 115

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0067    |
| Data Size    | 104 bytes |
| Instructions | 22        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      42  1E F0 FF FF 7F 6F 70 66         B.....opf
0070: 04 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 09  ..........tlk0..
0080: 80 23 5E 69 64 6C 30 1C  06 80 66 04 80 F8 FF FF  .#^idl0...f.....
0090: 7F F8 FF FF 7F 70 61 73  30 03 02 10 0A 80 1D 0B  .....pas0.......
00A0: 80 23 53 F8 FF FF 7F F8  FF FF 7F 70 61 73 30 1C  .#S........pas0.
00B0: 06 80 66 04 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  ..f..........tlk
00C0: 30 1D 0C 80 23 5E 69 64  6C 30 1C 06 80 21 00     0...#^idl0...!. 
```

#### Opcodes

```
  0: 0x0067 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0068 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x006D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x006E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x006F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=7429*)
    → "What? Ruillont's in that cave? And he doesn't want us to send help, eh? That's my boy! He's an elite in the making, that one!"
  6: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0082 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  8: 0x0087 [0x1C] WAIT(30* ticks)
  9: 0x008A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
 10: 0x0099 [0x03] Work_Zone[2] = 65*
 11: 0x009E [0x1D] PRINT_EVENT_MESSAGE(message_id=7430*)
    → "Well, the rescue training was a wash, but you helped us find our lost soldier. I think you've earned this $3."
 12: 0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00A2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 14: 0x00AF [0x1C] WAIT(30* ticks)
 15: 0x00B2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 16: 0x00C1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7431*)
    → "No, really. These drills are naught compared to venturing into one of those caves. Hand that certificate to the knight at the gatehouse, and you'll be done."
 17: 0x00C4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x00C5 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 19: 0x00CA [0x1C] WAIT(30* ticks)
 20: 0x00CD [0x21] END_EVENT
 21: 0x00CE [0x00] END_REQSTACK()
```
