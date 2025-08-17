# 17658598 - Resistance Fighter

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
| [317](#event-317)     | 0x0001       |     15 |              7 |
| [318](#event-318)     | 0x0010       |     56 |             16 |
| [319](#event-319)     | 0x0048       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F88      |        8072 |
|       1 | 0x1F89      |        8073 |
|       2 | 0x1F96      |        8086 |
|       3 | 0x0045      |          69 |
|       4 | 0x1F97      |        8087 |
|       5 | 0x1F98      |        8088 |
|       6 | 0x1F99      |        8089 |

## String References

- **8072**: Well, this here's a sight. Don't get many travelers out this way, y'see.
- **8073**: This is Parradamo Tor. You'd best watch your step around here. It's quite a ways down, as surely ye can see.
- **8086**: Well, this here's a sight. Don't get many travelers out--
- **8087**: What's that y' have with ye? Rations, and a linkpearl to boot!?
- **8088**: Can't thank ye enough, friend. When I lost contact with the camp, I thought I was done for.
- **8089**: Ye take care of yerself, now.

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

### Event 317

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 21 00   ........#...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=8072*)
    → "Well, this here's a sight. Don't get many travelers out this way, y'see."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=8073*)
    → "This is Parradamo Tor. You'd best watch your step around here. It's quite a ways down, as surely ye can see."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 318

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 56 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 42 1E F0 FF FF 7F 6F 70  1D 02 80 23 66 03 80 F8  B.....op...#f...
0020: FF FF 7F F8 FF FF 7F 74  77 61 30 1D 04 80 23 1D  .......twa0...#.
0030: 05 80 23 1D 06 80 23 66  03 80 F8 FF FF 7F F8 FF  ..#...#f........
0040: FF 7F 74 77 61 31 21 00                           ..twa1!.        
```

#### Opcodes

```
  0: 0x0010 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0016 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0017 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=8086*)
    → "Well, this here's a sight. Don't get many travelers out--"
  5: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa0" with entities [EventEntity, EventEntity], work=69*
  7: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=8087*)
    → "What's that y' have with ye? Rations, and a linkpearl to boot!?"
  8: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=8088*)
    → "Can't thank ye enough, friend. When I lost contact with the camp, I thought I was done for."
 10: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=8089*)
    → "Ye take care of yerself, now."
 12: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa1" with entities [EventEntity, EventEntity], work=69*
 14: 0x0046 [0x21] END_EVENT
 15: 0x0047 [0x00] END_REQSTACK()
```

### Event 319

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
  1: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=8089*)
    → "Ye take care of yerself, now."
  2: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0051 [0x21] END_EVENT
  4: 0x0052 [0x00] END_REQSTACK()
```
