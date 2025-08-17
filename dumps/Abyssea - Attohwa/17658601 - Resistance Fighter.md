# 17658601 - Resistance Fighter

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Attohwa (ID: 215) |
| Block Size       | 144 bytes                   |
| Total Events     | 4                           |
| References Count | 7                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [326](#event-326)     | 0x0001       |     19 |              9 |
| [327](#event-327)     | 0x0014       |     52 |             14 |
| [328](#event-328)     | 0x0048       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F90      |        8080 |
|       1 | 0x1F91      |        8081 |
|       2 | 0x1F92      |        8082 |
|       3 | 0x1FA1      |        8097 |
|       4 | 0x0013      |          19 |
|       5 | 0x1FA2      |        8098 |
|       6 | 0x1FA3      |        8099 |

## String References

- **8080**: Ho there. Whatever brings you to such a desolate place? Had I not been recruited for a scouting mission, I'd be as far away from here as possible.
- **8081**: On top of that, I seem to have been separated from my companions. They must be around here somewhere...
- **8082**: I'm sorry, but this is hardly the time for idle chitchat. If you know what's good for you, you'll head back to camp before you get lost too.
- **8097**: Oh, a new linkpearl, and a rather exquisite one at that. Now I can reconnect with my fellow scouts in style.
- **8098**: Speaking of which, wherever could they have disappeared to?
- **8099**: You think they'd drop everything once they realized the most attractive member of the team was missing. Didn't anyone ever teach them how to treat a lady?

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

### Event 326

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
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=8080*)
    → "Ho there. Whatever brings you to such a desolate place? Had I not been recruited for a scouting mission, I'd be as far away from here as possible."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=8081*)
    → "On top of that, I seem to have been separated from my companions. They must be around here somewhere..."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=8082*)
    → "I'm sorry, but this is hardly the time for idle chitchat. If you know what's good for you, you'll head back to camp before you get lost too."
  6: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0012 [0x21] END_EVENT
  8: 0x0013 [0x00] END_REQSTACK()
```

### Event 327

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 52 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             42 1E F0 FF  FF 7F 6F 70 1D 03 80 23      B.....op...#
0020: 66 04 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0030: 05 80 23 1D 06 80 23 66  04 80 F8 FF FF 7F F8 FF  ..#...#f........
0040: FF 7F 74 6C 6B 31 21 00                           ..tlk1!.        
```

#### Opcodes

```
  0: 0x0014 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0015 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x001A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x001B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=8097*)
    → "Oh, a new linkpearl, and a rather exquisite one at that. Now I can reconnect with my fellow scouts in style."
  5: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0020 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=19*
  7: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=8098*)
    → "Speaking of which, wherever could they have disappeared to?"
  8: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=8099*)
    → "You think they'd drop everything once they realized the most attractive member of the team was missing. Didn't anyone ever teach them how to treat a lady?"
 10: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=19*
 12: 0x0046 [0x21] END_EVENT
 13: 0x0047 [0x00] END_REQSTACK()
```

### Event 328

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          1E F0 FF FF 7F 1D 06 80          ........
0050: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0048 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=8099*)
    → "You think they'd drop everything once they realized the most attractive member of the team was missing. Didn't anyone ever teach them how to treat a lady?"
  2: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0051 [0x21] END_EVENT
  4: 0x0052 [0x00] END_REQSTACK()
```
