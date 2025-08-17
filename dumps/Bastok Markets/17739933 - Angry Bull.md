# 17739933 - Angry Bull

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Bastok Markets (ID: 235) |
| Block Size       | 116 bytes                |
| Total Events     | 2                        |
| References Count | 7                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [472](#event-472)     | 0x0001       |     60 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x3043      |       12355 |
|       2 | 0x0045      |          69 |
|       3 | 0x3044      |       12356 |
|       4 | 0x3045      |       12357 |
|       5 | 0x3046      |       12358 |
|       6 | 0x3047      |       12359 |

## String References

- **12355**: I remember 20 years ago when I was in charge of protecting Galkan Bridge from the beastmen.
- **12356**: For a large part of the Crystal War, we had her blocked off on both sides. The government said it was to keep enemy spies from infiltrating Bastok's central areas. However, there were rumors that it was to prevent Galka from coming over on this side of the river and rioting.
- **12357**: It would be a lie if I told you it wasn't hard for me, a Galka, to work against my brothers like that.
- **12358**: I still have nightmares about the times I had to force back groups of refugees trying to escape the flames that engulfed their homes in the mines district.
- **12359**: And now I'm back here patrolling the bridge as I did so long ago. Perhaps destiny has a tighter grip on us than I thought...

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

### Event 472

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 60 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 1D 01 80 23 66 02 80   ...........#f..
0010: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 03 80 23  ........tlk0...#
0020: 1D 04 80 23 1D 05 80 23  66 02 80 F8 FF FF 7F F8  ...#...#f.......
0030: FF FF 7F 74 6C 6B 31 1D  06 80 23 21 00           ...tlk1...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=12355*)
    → "I remember 20 years ago when I was in charge of protecting Galkan Bridge from the beastmen."
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=12356*)
    → "For a large part of the Crystal War, we had her blocked off on both sides. The government said it was to keep enemy spies from infiltrating Bastok's central areas. However, there were rumors that it was to prevent Galka from coming over on this side of the river and rioting."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=12357*)
    → "It would be a lie if I told you it wasn't hard for me, a Galka, to work against my brothers like that."
  8: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=12358*)
    → "I still have nightmares about the times I had to force back groups of refugees trying to escape the flames that engulfed their homes in the mines district."
 10: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0028 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=69*
 12: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=12359*)
    → "And now I'm back here patrolling the bridge as I did so long ago. Perhaps destiny has a tighter grip on us than I thought..."
 13: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x003B [0x21] END_EVENT
 15: 0x003C [0x00] END_REQSTACK()
```
