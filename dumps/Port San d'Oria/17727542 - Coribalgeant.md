# 17727542 - Coribalgeant

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 96 bytes                  |
| Total Events     | 2                         |
| References Count | 5                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [599](#event-599)     | 0x0001       |     50 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1DF2      |        7666 |
|       2 | 0x001E      |          30 |
|       3 | 0x1DF3      |        7667 |
|       4 | 0x1DF4      |        7668 |

## String References

- **7666**: The residential area is up these stairs. If you ask me, San d'Orians must cast aside the trappings of wealth.
- **7667**: It's not knightly to sit on cushioned couches in gilt halls! No, we should sleep with the grass as our pillow, the dew our morning gown.
- **7668**: Yet our kingdom supplies those fool Mog Houses for all! Moogles, or whatever they call those demons, have no place in a proper San d'Orian home.

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

### Event 599

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 50 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1C 02 80 1D 03  ...tlk0...#.....
0020: 80 23 1C 02 80 1D 04 80  23 5E 69 64 6C 30 1C 02  .#......#^idl0..
0030: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7666*)
    → "The residential area is up these stairs. If you ask me, San d'Orians must cast aside the trappings of wealth."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1C] WAIT(30* ticks)
  7: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7667*)
    → "It's not knightly to sit on cushioned couches in gilt halls! No, we should sleep with the grass as our pillow, the dew our morning gown."
  8: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0022 [0x1C] WAIT(30* ticks)
 10: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7668*)
    → "Yet our kingdom supplies those fool Mog Houses for all! Moogles, or whatever they call those demons, have no place in a proper San d'Orian home."
 11: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0029 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 13: 0x002E [0x1C] WAIT(30* ticks)
 14: 0x0031 [0x21] END_EVENT
 15: 0x0032 [0x00] END_REQSTACK()
```
