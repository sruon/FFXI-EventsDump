# 17801252 - Ney Hiparujah

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 352 bytes        |
| Total Events     | 12               |
| References Count | 21               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [252](#event-252)        | 0x001A       |     23 |             12 |
| [253](#event-253)        | 0x0031       |     19 |             10 |
| [254](#event-254)        | 0x0044       |     19 |             10 |
| [255](#event-255)        | 0x0057       |     19 |             10 |
| [256](#event-256)        | 0x006A       |     19 |             10 |
| [257](#event-257)        | 0x007D       |     19 |             10 |
| [258](#event-258)        | 0x0090       |     19 |             10 |
| [259](#event-259)        | 0x00A3       |     19 |             10 |
| [260](#event-260)        | 0x00B6       |     19 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x28D8      |       10456 |
|       3 | 0x28D9      |       10457 |
|       4 | 0x28DA      |       10458 |
|       5 | 0x28DB      |       10459 |
|       6 | 0x28DC      |       10460 |
|       7 | 0x28DD      |       10461 |
|       8 | 0x28DE      |       10462 |
|       9 | 0x28DF      |       10463 |
|      10 | 0x28E0      |       10464 |
|      11 | 0x28E1      |       10465 |
|      12 | 0x28E2      |       10466 |
|      13 | 0x28E3      |       10467 |
|      14 | 0x28E4      |       10468 |
|      15 | 0x28E5      |       10469 |
|      16 | 0x28E6      |       10470 |
|      17 | 0x28E7      |       10471 |
|      18 | 0x28E8      |       10472 |
|      19 | 0x28E9      |       10473 |
|      20 | 0x28EA      |       10474 |

## String References

- **10456**: And you arrre? <Player>? Neverrr heard of you. There are too many adventurers these days to rememberrr every one that waltzes through our village gates.
- **10457**: You're going to have to work harderrr if you want anyone to rememberrr a funny name like that.
- **10458**: And who knows? Someday you could become as famous as me!
- **10459**: What did you say you called yourself? <Player>? I don't know... I might have heard that name somewherrre.
- **10460**: Do a little more for the villagers herrre, and people might start remembering who you arrre.
- **10461**: Wait... Don't tell me... It's...<Player>, right? Yeah, I've been hearing your name more often lately.
- **10462**: A little bit more work, and soon everybody will know who you arrre.
- **10463**: Hi therrre, <Player>. I've been telling everybody about my new friend. We're friends, right?
- **10464**: Keep up the good work. The betterrr my friends look, the betterrr I look!
- **10465**: Oh, <Player>! Long time no see! Your name comes up a lot these days.
- **10466**: And guess what? Nobody has anything bad to say about you. That's a compliment in itself!
- **10467**: You know, I don't think there's a person in this village who doesn't know yourrr name.
- **10468**: You keep up the good work, and I'll have to start calling you [Mister/Miss] <Player>!
- **10469**: [Mister/Miss] <Player>! Arrre you heading out on anotherrr dangerous mission? Be careful! We'll all be rooting for you.
- **10470**: I know it has been hard to get such a good reputation, but don't take it for granted. Yourrr work is farrr from being done!
- **10471**: [Mister/Miss] <Player>! You are one smooth cat! I've neverrr met a mainlander who did so much for us islanders.
- **10472**: I'm proud to call you my acquaintance...my friend!
- **10473**: [Lord/Lady] <Player>! The fame your name carries stretches from here to Windurst.
- **10474**: I cannot begin to put into words the gratitude this village feels forrr you. Live long, hero of Kazham!

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 252

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 23 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 1D 02 80 23 1D 03 80  23 1D 04 80 23 20 00 21  p...#...#...# .!
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=10456*)
    → "And you arrre? <Player>? Neverrr heard of you. There are too many adventurers these days to rememberrr every one that waltzes through our village gates."
  4: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=10457*)
    → "You're going to have to work harderrr if you want anyone to rememberrr a funny name like that."
  6: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=10458*)
    → "And who knows? Someday you could become as famous as me!"
  8: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x002F [0x21] END_EVENT
 11: 0x0030 [0x00] END_REQSTACK()
```

### Event 253

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    1E F0 FF FF 7F 6F 70  1D 05 80 23 1D 06 80 23   .....op...#...#
0040: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0031 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0036 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0037 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=10459*)
    → "What did you say you called yourself? <Player>? I don't know... I might have heard that name somewherrre."
  4: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=10460*)
    → "Do a little more for the villagers herrre, and people might start remembering who you arrre."
  6: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0040 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0042 [0x21] END_EVENT
  9: 0x0043 [0x00] END_REQSTACK()
```

### Event 254

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             1E F0 FF FF  7F 6F 70 1D 07 80 23 1D      .....op...#.
0050: 08 80 23 20 00 21 00                              ..# .!.         
```

#### Opcodes

```
  0: 0x0044 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=10461*)
    → "Wait... Don't tell me... It's...<Player>, right? Yeah, I've been hearing your name more often lately."
  4: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=10462*)
    → "A little bit more work, and soon everybody will know who you arrre."
  6: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0055 [0x21] END_EVENT
  9: 0x0056 [0x00] END_REQSTACK()
```

### Event 255

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      1E  F0 FF FF 7F 6F 70 1D 09         .....op..
0060: 80 23 1D 0A 80 23 20 00  21 00                    .#...# .!.      
```

#### Opcodes

```
  0: 0x0057 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x005D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x005E [0x1D] PRINT_EVENT_MESSAGE(message_id=10463*)
    → "Hi therrre, <Player>. I've been telling everybody about my new friend. We're friends, right?"
  4: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0062 [0x1D] PRINT_EVENT_MESSAGE(message_id=10464*)
    → "Keep up the good work. The betterrr my friends look, the betterrr I look!"
  6: 0x0065 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0066 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0068 [0x21] END_EVENT
  9: 0x0069 [0x00] END_REQSTACK()
```

### Event 256

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                1E F0 FF FF 7F 6F            .....o
0070: 70 1D 0B 80 23 1D 0C 80  23 20 00 21 00           p...#...# .!.   
```

#### Opcodes

```
  0: 0x006A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x006F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0070 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0071 [0x1D] PRINT_EVENT_MESSAGE(message_id=10465*)
    → "Oh, <Player>! Long time no see! Your name comes up a lot these days."
  4: 0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=10466*)
    → "And guess what? Nobody has anything bad to say about you. That's a compliment in itself!"
  6: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0079 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x007B [0x21] END_EVENT
  9: 0x007C [0x00] END_REQSTACK()
```

### Event 257

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         1E F0 FF               ...
0080: FF 7F 6F 70 1D 0D 80 23  1D 0E 80 23 20 00 21 00  ..op...#...# .!.
```

#### Opcodes

```
  0: 0x007D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0082 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0083 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=10467*)
    → "You know, I don't think there's a person in this village who doesn't know yourrr name."
  4: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=10468*)
    → "You keep up the good work, and I'll have to start calling you [Mister/Miss] <Player>!"
  6: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x008C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x008E [0x21] END_EVENT
  9: 0x008F [0x00] END_REQSTACK()
```

### Event 258

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 1E F0 FF FF 7F 6F 70 1D  0F 80 23 1D 10 80 23 20  .....op...#...# 
00A0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0090 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0095 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0096 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0097 [0x1D] PRINT_EVENT_MESSAGE(message_id=10469*)
    → "[Mister/Miss] <Player>! Arrre you heading out on anotherrr dangerous mission? Be careful! We'll all be rooting for you."
  4: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x009B [0x1D] PRINT_EVENT_MESSAGE(message_id=10470*)
    → "I know it has been hard to get such a good reputation, but don't take it for granted. Yourrr work is farrr from being done!"
  6: 0x009E [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x009F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00A1 [0x21] END_EVENT
  9: 0x00A2 [0x00] END_REQSTACK()
```

### Event 259

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          1E F0 FF FF 7F  6F 70 1D 11 80 23 1D 12     .....op...#..
00B0: 80 23 20 00 21 00                                 .# .!.          
```

#### Opcodes

```
  0: 0x00A3 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00A9 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=10471*)
    → "[Mister/Miss] <Player>! You are one smooth cat! I've neverrr met a mainlander who did so much for us islanders."
  4: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00AE [0x1D] PRINT_EVENT_MESSAGE(message_id=10472*)
    → "I'm proud to call you my acquaintance...my friend!"
  6: 0x00B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00B2 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00B4 [0x21] END_EVENT
  9: 0x00B5 [0x00] END_REQSTACK()
```

### Event 260

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B6   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   1E F0  FF FF 7F 6F 70 1D 13 80        .....op...
00C0: 23 1D 14 80 23 20 00 21  00                       #...# .!.       
```

#### Opcodes

```
  0: 0x00B6 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00BB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00BC [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=10473*)
    → "[Lord/Lady] <Player>! The fame your name carries stretches from here to Windurst."
  4: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00C1 [0x1D] PRINT_EVENT_MESSAGE(message_id=10474*)
    → "I cannot begin to put into words the gratitude this village feels forrr you. Live long, hero of Kazham!"
  6: 0x00C4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00C5 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00C7 [0x21] END_EVENT
  9: 0x00C8 [0x00] END_REQSTACK()
```
