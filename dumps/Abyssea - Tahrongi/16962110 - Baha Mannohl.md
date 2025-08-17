# 16962110 - Baha Mannohl

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 460 bytes                   |
| Total Events     | 11                          |
| References Count | 16                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [356](#event-356)     | 0x0001       |     13 |              7 |
| [357](#event-357)     | 0x000E       |     73 |             19 |
| [358](#event-358)     | 0x0057       |     60 |             12 |
| [359](#event-359)     | 0x0093       |     31 |              9 |
| [360](#event-360)     | 0x00B2       |     13 |              7 |
| [361](#event-361)     | 0x00BF       |     65 |             15 |
| [362](#event-362)     | 0x0100       |     13 |              7 |
| [363](#event-363)     | 0x010D       |     31 |              9 |
| [364](#event-364)     | 0x012C       |     13 |              7 |
| [365](#event-365)     | 0x0139       |     22 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F2D      |        7981 |
|       1 | 0x1F2E      |        7982 |
|       2 | 0x1F2F      |        7983 |
|       3 | 0x1F30      |        7984 |
|       4 | 0x0032      |          50 |
|       5 | 0x1F31      |        7985 |
|       6 | 0x1F32      |        7986 |
|       7 | 0x1F33      |        7987 |
|       8 | 0x00C9      |         201 |
|       9 | 0x0000      |           0 |
|      10 | 0x1F34      |        7988 |
|      11 | 0x1F35      |        7989 |
|      12 | 0x1F36      |        7990 |
|      13 | 0x1F37      |        7991 |
|      14 | 0x0005      |           5 |
|      15 | 0x1F38      |        7992 |

## String References

- **7981**: Whatever shall I do...? Why, if I lost herrr, I would be...
- **7982**: Help! You must help me!!!
- **7983**: Forrrgive my poor manners. It's my daughter, you see... She's come down with a terrrible sickness, you see...
- **7984**: We were attacked... It was all we could do to flee here with our lives... She was in shock, the poor girl. Her body...<sniff>...couldn't take any morrre...
- **7985**: They say there's a cactus that yields water only after sundown. Water that can cure the rarest of illnesses... I'd go off in search of it myself, but if I left my daughter's side for even a second...
- **7986**: Please, frrriend, you must help! Why, if I lost her... If I lost her, I would...
- **7987**: Oh, frrriend, you have no idea how much this means to me! I can only hope this helps her... It must...!
- **7988**: Frrriend. You've my thanks for your kindness the other day.
- **7989**: I'm afraid my daughter's sickness still plagues her. The fever subsided for a time, but is back now worse than ever.
- **7990**: Please, you must brrring us more cactus water! My daughter's life depends on it!
- **7991**: Thank you everrr so much! This will cure her for good this time...I just know it will!
- **7992**: Oh, friend... How can I ever rrrepay you? Thanks to your kindness, my daughter is back on her feet again. You have our eternal grrratitude...

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

### Event 356

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
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7981*)
    → "Whatever shall I do...? Why, if I lost herrr, I would be..."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 357

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 73 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            42 1E                B.
0010: F0 FF FF 7F 6F 70 1D 01  80 23 1D 02 80 23 1D 03  ....op...#...#..
0020: 80 23 66 04 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#f..........tlk
0030: 30 1D 05 80 23 1D 06 80  23 66 04 80 F8 FF FF 7F  0...#...#f......
0040: F8 FF FF 7F 74 6C 6B 32  53 F8 FF FF 7F F8 FF FF  ....tlk2S.......
0050: 7F 74 6C 6B 32 21 00                              .tlk2!.         
```

#### Opcodes

```
  0: 0x000E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0014 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0015 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=7982*)
    → "Help! You must help me!!!"
  5: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=7983*)
    → "Forrrgive my poor manners. It's my daughter, you see... She's come down with a terrrible sickness, you see..."
  7: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7984*)
    → "We were attacked... It was all we could do to flee here with our lives... She was in shock, the poor girl. Her body...<sniff>...couldn't take any morrre..."
  9: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0022 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
 11: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=7985*)
    → "They say there's a cactus that yields water only after sundown. Water that can cure the rarest of illnesses... I'd go off in search of it myself, but if I left my daughter's side for even a second..."
 12: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=7986*)
    → "Please, frrriend, you must help! Why, if I lost her... If I lost her, I would..."
 14: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0039 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
 16: 0x0048 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
 17: 0x0055 [0x21] END_EVENT
 18: 0x0056 [0x00] END_REQSTACK()
```

### Event 358

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 60 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      1E  F0 FF FF 7F 6F 70 66 04         .....opf.
0060: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 05 80  .........tlk0...
0070: 23 1D 06 80 23 66 04 80  F8 FF FF 7F F8 FF FF 7F  #...#f..........
0080: 74 6C 6B 32 53 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  tlk2S........tlk
0090: 32 21 00                                          2!.             
```

#### Opcodes

```
  0: 0x0057 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x005D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x005E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x006D [0x1D] PRINT_EVENT_MESSAGE(message_id=7985*)
    → "They say there's a cactus that yields water only after sundown. Water that can cure the rarest of illnesses... I'd go off in search of it myself, but if I left my daughter's side for even a second..."
  5: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0071 [0x1D] PRINT_EVENT_MESSAGE(message_id=7986*)
    → "Please, frrriend, you must help! Why, if I lost her... If I lost her, I would..."
  7: 0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0075 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
  9: 0x0084 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
 10: 0x0091 [0x21] END_EVENT
 11: 0x0092 [0x00] END_REQSTACK()
```

### Event 359

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0093   |
| Data Size    | 31 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          42 1E F0 FF FF  7F 6F 70 1D 07 80 23 45     B.....op...#E
00A0: 08 80 F0 FF FF 7F F0 FF  FF 7F 71 73 74 63 09 80  ..........qstc..
00B0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0093 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0094 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0099 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x009A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x009B [0x1D] PRINT_EVENT_MESSAGE(message_id=7987*)
    → "Oh, frrriend, you have no idea how much this means to me! I can only hope this helps her... It must...!"
  5: 0x009E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x009F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  7: 0x00B0 [0x21] END_EVENT
  8: 0x00B1 [0x00] END_REQSTACK()
```

### Event 360

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       1E F0 FF FF 7F 6F  70 1D 07 80 23 21 00       .....op...#!. 
```

#### Opcodes

```
  0: 0x00B2 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00B8 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7987*)
    → "Oh, frrriend, you have no idea how much this means to me! I can only hope this helps her... It must...!"
  4: 0x00BC [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00BD [0x21] END_EVENT
  6: 0x00BE [0x00] END_REQSTACK()
```

### Event 361

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 65 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               42                 B
00C0: 1E F0 FF FF 7F 6F 70 1D  0A 80 23 66 04 80 F8 FF  .....op...#f....
00D0: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 0B 80 23 1D 0C  ......tlk0...#..
00E0: 80 23 66 04 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#f..........tlk
00F0: 32 53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 32 21 00  2S........tlk2!.
```

#### Opcodes

```
  0: 0x00BF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00C0 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00C5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00C6 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7988*)
    → "Frrriend. You've my thanks for your kindness the other day."
  5: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00CB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  7: 0x00DA [0x1D] PRINT_EVENT_MESSAGE(message_id=7989*)
    → "I'm afraid my daughter's sickness still plagues her. The fever subsided for a time, but is back now worse than ever."
  8: 0x00DD [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00DE [0x1D] PRINT_EVENT_MESSAGE(message_id=7990*)
    → "Please, you must brrring us more cactus water! My daughter's life depends on it!"
 10: 0x00E1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00E2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
 12: 0x00F1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
 13: 0x00FE [0x21] END_EVENT
 14: 0x00FF [0x00] END_REQSTACK()
```

### Event 362

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0100   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100: 1E F0 FF FF 7F 6F 70 1D  0C 80 23 21 00           .....op...#!.   
```

#### Opcodes

```
  0: 0x0100 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0105 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0106 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0107 [0x1D] PRINT_EVENT_MESSAGE(message_id=7990*)
    → "Please, you must brrring us more cactus water! My daughter's life depends on it!"
  4: 0x010A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x010B [0x21] END_EVENT
  6: 0x010C [0x00] END_REQSTACK()
```

### Event 363

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010D   |
| Data Size    | 31 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         42 1E F0               B..
0110: FF FF 7F 6F 70 1D 0D 80  23 45 08 80 F0 FF FF 7F  ...op...#E......
0120: F0 FF FF 7F 71 73 74 63  09 80 21 00              ....qstc..!.    
```

#### Opcodes

```
  0: 0x010D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x010E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0113 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0114 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0115 [0x1D] PRINT_EVENT_MESSAGE(message_id=7991*)
    → "Thank you everrr so much! This will cure her for good this time...I just know it will!"
  5: 0x0118 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0119 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  7: 0x012A [0x21] END_EVENT
  8: 0x012B [0x00] END_REQSTACK()
```

### Event 364

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012C   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                      1E F0 FF FF              ....
0130: 7F 6F 70 1D 07 80 23 21  00                       .op...#!.       
```

#### Opcodes

```
  0: 0x012C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0131 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0132 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0133 [0x1D] PRINT_EVENT_MESSAGE(message_id=7987*)
    → "Oh, frrriend, you have no idea how much this means to me! I can only hope this helps her... It must...!"
  4: 0x0136 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0137 [0x21] END_EVENT
  6: 0x0138 [0x00] END_REQSTACK()
```

### Event 365

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0139   |
| Data Size    | 22 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                             02 02 10 0E 80 00 42           ......B
0140: 01 42 1E F0 FF FF 7F 6F  70 1D 0F 80 23 21 00     .B.....op...#!. 
```

#### Opcodes

```
  0: 0x0139 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x0142
  1: 0x0141 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0142 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0147 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0148 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0149 [0x1D] PRINT_EVENT_MESSAGE(message_id=7992*)
    → "Oh, friend... How can I ever rrrepay you? Thanks to your kindness, my daughter is back on her feet again. You have our eternal grrratitude..."
  6: 0x014C [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x014D [0x21] END_EVENT
  8: 0x014E [0x00] END_REQSTACK()
```
