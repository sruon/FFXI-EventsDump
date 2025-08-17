# 17658600 - Resistance Fighter

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Attohwa (ID: 215) |
| Block Size       | 152 bytes                   |
| Total Events     | 4                           |
| References Count | 8                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [323](#event-323)     | 0x0001       |     19 |              9 |
| [324](#event-324)     | 0x0014       |     56 |             16 |
| [325](#event-325)     | 0x004C       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F8D      |        8077 |
|       1 | 0x1F8E      |        8078 |
|       2 | 0x1F8F      |        8079 |
|       3 | 0x1F9D      |        8093 |
|       4 | 0x0031      |          49 |
|       5 | 0x1F9E      |        8094 |
|       6 | 0x1F9F      |        8095 |
|       7 | 0x1FA0      |        8096 |

## String References

- **8077**: Ah, pardon me, [mister/missus]. Would you happen-wappen to know where we are?
- **8078**: I say, there are so many crags and crevices in this chasm that you can't tell one from the nextaru!
- **8079**: Are you heading-weading to the top, perhaps? Why, I think I might just do the same!
- **8093**: Rations! Just when my tummy was starting to rumble-wumble. Remarkable timing, I must declare!
- **8094**: You wouldn't happen to have a sip of drink as well? A cup of Windurstian tea, perhaps? 'Cause I'm positively dying of thirstaru!
- **8095**: A new linkpearl? Come to think of it, it's been a while since I heard anything from this one.
- **8096**: At any rate, thanks to you, I'm good to go. Now, last one to the summit is a rotten chocobo egg! Ta-taru!

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

### Event 323

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 19 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 1D 02   ........#...#..
0010: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=8077*)
    → "Ah, pardon me, [mister/missus]. Would you happen-wappen to know where we are?"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=8078*)
    → "I say, there are so many crags and crevices in this chasm that you can't tell one from the nextaru!"
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=8079*)
    → "Are you heading-weading to the top, perhaps? Why, I think I might just do the same!"
  6: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0012 [0x21] END_EVENT
  8: 0x0013 [0x00] END_REQSTACK()
```

### Event 324

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 56 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             42 1E F0 FF  FF 7F 6F 70 1D 03 80 23      B.....op...#
0020: 66 04 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0030: 05 80 23 1D 06 80 23 66  04 80 F8 FF FF 7F F8 FF  ..#...#f........
0040: FF 7F 74 6C 6B 31 1D 07  80 23 21 00              ..tlk1...#!.    
```

#### Opcodes

```
  0: 0x0014 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0015 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x001A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x001B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=8093*)
    → "Rations! Just when my tummy was starting to rumble-wumble. Remarkable timing, I must declare!"
  5: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0020 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  7: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=8094*)
    → "You wouldn't happen to have a sip of drink as well? A cup of Windurstian tea, perhaps? 'Cause I'm positively dying of thirstaru!"
  8: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=8095*)
    → "A new linkpearl? Come to think of it, it's been a while since I heard anything from this one."
 10: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
 12: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=8096*)
    → "At any rate, thanks to you, I'm good to go. Now, last one to the summit is a rotten chocobo egg! Ta-taru!"
 13: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x004A [0x21] END_EVENT
 15: 0x004B [0x00] END_REQSTACK()
```

### Event 325

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      1E F0 FF FF              ....
0050: 7F 1D 07 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x004C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=8096*)
    → "At any rate, thanks to you, I'm good to go. Now, last one to the summit is a rotten chocobo egg! Ta-taru!"
  2: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0055 [0x21] END_EVENT
  4: 0x0056 [0x00] END_REQSTACK()
```
