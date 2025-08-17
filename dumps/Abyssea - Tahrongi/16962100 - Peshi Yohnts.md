# 16962100 - Peshi Yohnts

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 336 bytes                   |
| Total Events     | 7                           |
| References Count | 16                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [388](#event-388)     | 0x0001       |     13 |              7 |
| [313](#event-313)     | 0x000E       |    101 |             30 |
| [314](#event-314)     | 0x0073       |     13 |              7 |
| [315](#event-315)     | 0x0080       |     71 |             15 |
| [316](#event-316)     | 0x00C7       |     13 |              7 |
| [317](#event-317)     | 0x00D4       |     14 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1ECA      |        7882 |
|       1 | 0x1ECB      |        7883 |
|       2 | 0x1ECC      |        7884 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x1ECD      |        7885 |
|       6 | 0x0032      |          50 |
|       7 | 0x1ECE      |        7886 |
|       8 | 0x1ECF      |        7887 |
|       9 | 0x1ED0      |        7888 |
|      10 | 0x1ED1      |        7889 |
|      11 | 0x001E      |          30 |
|      12 | 0x1ED2      |        7890 |
|      13 | 0x1ED3      |        7891 |
|      14 | 0x00C9      |         201 |
|      15 | 0x1ED4      |        7892 |

## String References

- **7882**: No, that won't do... <Sigh>... Nothing I do ever goes rrright...
- **7883**: <Sigh>... Nothing I do ever-- Oh, a visitor. Perrrhaps you could help me. Heaven knows I can't seem to help myself...
- **7884**: Help her? [Sounds like she needs it./Not getting involved.]
- **7885**: Oh, I underrrstand. Too busy being a [hero/heroine] to care about a poor worrrthless loser like me. Fine. Run off and live your wonderful life, and leave me to my miserrry...
- **7886**: Therrre you go again, Peshi... Always countin' on talented strrrangers to do things you're too incompetent to do yourself... "What happened to you? You used to be such a rrray of sunshine!" everyone says. That was before I rrrealized how meaningless everything is... How useless I am...
- **7887**: What was I saying? Oh, I need some $0 to make crrrappy weapons that won't help anyone anyway. They're burrried around here somewhere that my worthless brain couldn't be botherrred to remember.
- **7888**: You'll need $1 to dig them up. Here, take this one. If I tried to use it, I'd prrrobably just drop it and brrreak my foot anyway.
- **7889**: I'd offer my supporrrt, but I'd probably just get in the way. Just like I always do...<sigh>
- **7890**: There's a surrrprise. Once again, a stranger perrrforms with ease a task I couldn't manage if I took a hundrrred years... Ah. I mean, thank you.
- **7891**: 'Course, I'm probably just gonna end up brrreakin' these $0, anyway. Just watch. It's just a matterrr of time before I'll need you to bail me out again.
- **7892**: Oh, look. It's the [man/lady] who's so much better than me at everything. Do you think you could find me some more $0?

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

### Event 388

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
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7882*)
    → "No, that won't do... <Sigh>... Nothing I do ever goes rrright..."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 313

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000E    |
| Data Size    | 101 bytes |
| Instructions | 30        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            42 1E                B.
0010: F0 FF FF 7F 6F 70 1D 01  80 23 24 02 80 03 80 04  ....op...#$.....
0020: 80 25 02 00 10 04 80 00  32 00 03 01 10 04 80 01  .%......2.......
0030: 3D 00 1D 05 80 23 03 01  10 03 80 21 00 66 06 80  =....#.....!.f..
0040: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 07 80 23  ........tlk0...#
0050: 1D 08 80 23 1D 09 80 23  1D 0A 80 23 53 F8 FF FF  ...#...#...#S...
0060: 7F F8 FF FF 7F 74 6C 6B  30 5E 69 64 6C 30 1C 0B  .....tlk0^idl0..
0070: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x000E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0014 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0015 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=7883*)
    → "<Sigh>... Nothing I do ever-- Oh, a visitor. Perrrhaps you could help me. Heaven knows I can't seem to help myself..."
  5: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001A [0x24] CREATE_DIALOG(message_id=7884*, default_option=1*, option_flags=0*)
    → "Help her? [Sounds like she needs it./Not getting involved.]"
  7: 0x0021 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0022 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0032
  9: 0x002A [0x03] Work_Zone[1] = 0*
 10: 0x002F [0x01] GOTO 0x003D
 11: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=7885*)
    → "Oh, I underrrstand. Too busy being a [hero/heroine] to care about a poor worrrthless loser like me. Fine. Run off and live your wonderful life, and leave me to my miserrry..."
 12: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0036 [0x03] Work_Zone[1] = 1*
 14: 0x003B [0x21] END_EVENT
 15: 0x003C [0x00] END_REQSTACK()

SUBROUTINE_003D:
 16: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
 17: 0x004C [0x1D] PRINT_EVENT_MESSAGE(message_id=7886*)
    → "Therrre you go again, Peshi... Always countin' on talented strrrangers to do things you're too incompetent to do yourself... "What happened to you? You used to be such a rrray of sunshine!" everyone says. That was before I rrrealized how meaningless everything is... How useless I am..."
 18: 0x004F [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=7887*)
    → "What was I saying? Oh, I need some $0 to make crrrappy weapons that won't help anyone anyway. They're burrried around here somewhere that my worthless brain couldn't be botherrred to remember."
 20: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=7888*)
    → "You'll need $1 to dig them up. Here, take this one. If I tried to use it, I'd prrrobably just drop it and brrreak my foot anyway."
 22: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=7889*)
    → "I'd offer my supporrrt, but I'd probably just get in the way. Just like I always do...<sigh>"
 24: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x005C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 26: 0x0069 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 27: 0x006E [0x1C] WAIT(30* ticks)
 28: 0x0071 [0x21] END_EVENT
 29: 0x0072 [0x00] END_REQSTACK()
```

### Event 314

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          1E F0 FF FF 7F  6F 70 1D 0A 80 23 21 00     .....op...#!.
```

#### Opcodes

```
  0: 0x0073 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0078 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0079 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x007A [0x1D] PRINT_EVENT_MESSAGE(message_id=7889*)
    → "I'd offer my supporrrt, but I'd probably just get in the way. Just like I always do...<sigh>"
  4: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x007E [0x21] END_EVENT
  6: 0x007F [0x00] END_REQSTACK()
```

### Event 315

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 71 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 42 1E F0 FF FF 7F 6F 70  1D 0C 80 23 66 06 80 F8  B.....op...#f...
0090: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 0D 80 23 53  .......tlk0...#S
00A0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 5E 69 64 6C  ........tlk0^idl
00B0: 30 1C 0B 80 45 0E 80 F0  FF FF 7F F0 FF FF 7F 71  0...E..........q
00C0: 73 74 63 04 80 21 00                              stc..!.         
```

#### Opcodes

```
  0: 0x0080 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0081 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0086 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0087 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=7890*)
    → "There's a surrrprise. Once again, a stranger perrrforms with ease a task I couldn't manage if I took a hundrrred years... Ah. I mean, thank you."
  5: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  7: 0x009B [0x1D] PRINT_EVENT_MESSAGE(message_id=7891*)
    → "'Course, I'm probably just gonna end up brrreakin' these $0, anyway. Just watch. It's just a matterrr of time before I'll need you to bail me out again."
  8: 0x009E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x009F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 10: 0x00AC [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 11: 0x00B1 [0x1C] WAIT(30* ticks)
 12: 0x00B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 13: 0x00C5 [0x21] END_EVENT
 14: 0x00C6 [0x00] END_REQSTACK()
```

### Event 316

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C7   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                      1E  F0 FF FF 7F 6F 70 1D 0D         .....op..
00D0: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x00C7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00CD [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00CE [0x1D] PRINT_EVENT_MESSAGE(message_id=7891*)
    → "'Course, I'm probably just gonna end up brrreakin' these $0, anyway. Just watch. It's just a matterrr of time before I'll need you to bail me out again."
  4: 0x00D1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00D2 [0x21] END_EVENT
  6: 0x00D3 [0x00] END_REQSTACK()
```

### Event 317

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D4   |
| Data Size    | 14 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             42 1E F0 FF  FF 7F 6F 70 1D 0F 80 23      B.....op...#
00E0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00D4 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00D5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00DA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00DB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00DC [0x1D] PRINT_EVENT_MESSAGE(message_id=7892*)
    → "Oh, look. It's the [man/lady] who's so much better than me at everything. Do you think you could find me some more $0?"
  5: 0x00DF [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00E0 [0x21] END_EVENT
  7: 0x00E1 [0x00] END_REQSTACK()
```
