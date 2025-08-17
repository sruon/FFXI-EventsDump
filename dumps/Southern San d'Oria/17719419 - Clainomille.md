# 17719419 - Clainomille

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 152 bytes                     |
| Total Events     | 4                             |
| References Count | 11                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [503](#event-503)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     23 |              5 |
| [613](#event-613)        | 0x0019       |     50 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFEFB31  |  4294900529 |
|       2 | 0xFFFFD267  |  4294955623 |
|       3 | 0x07CF      |        1999 |
|       4 | 0x0DD5      |        3541 |
|       5 | 0xFFFED336  |  4294890294 |
|       6 | 0xFFFFFD4A  |  4294966602 |
|       7 | 0x001E      |          30 |
|       8 | 0x1FC4      |        8132 |
|       9 | 0x1FC5      |        8133 |
|      10 | 0x1FC6      |        8134 |

## String References

- **8132**: Just head west down this street and take a right at the end of it. That will lead you to Watchdog Alley.
- **8133**: It now serves as a residential area for our kingdom's squires, so it's quite safe. But it was once a haven for criminals and all sorts of sordid types.
- **8134**: During the Great War the quarter was even used for the public hangings of captured beastmen. To think...

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

### Event 503

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 37 01 80  02 80 03 80 04 80 1F 00    2..7..........
0010: 05 80 06 80 03 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-66.767*, z=-11.673*, y=1.999*, direction=311.2°*
  2: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-77.002*, Z=-0.694*, Y=1.999*
  3: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0018 [0x00] END_REQSTACK()
```

### Event 613

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 50 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             86 00 7B 60 0E 01 1E           ..{`...
0020: F0 FF FF 7F 6F 70 66 07  80 F8 FF FF 7F F8 FF FF  ....opf.........
0030: 7F 74 6C 6B 30 1D 08 80  23 1D 09 80 23 1D 0A 80  .tlk0...#...#...
0040: 23 5E 69 64 6C 30 1C 07  80 21 00                 #^idl0...!.     
```

#### Opcodes

```
  0: 0x0019 [0x86] Clainomille (ID: 17719419/0x010E607B)->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x001F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0024 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0025 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0026 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  5: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=8132*)
    → "Just head west down this street and take a right at the end of it. That will lead you to Watchdog Alley."
  6: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=8133*)
    → "It now serves as a residential area for our kingdom's squires, so it's quite safe. But it was once a haven for criminals and all sorts of sordid types."
  8: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=8134*)
    → "During the Great War the quarter was even used for the public hangings of captured beastmen. To think..."
 10: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0041 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 12: 0x0046 [0x1C] WAIT(30* ticks)
 13: 0x0049 [0x21] END_EVENT
 14: 0x004A [0x00] END_REQSTACK()
```
