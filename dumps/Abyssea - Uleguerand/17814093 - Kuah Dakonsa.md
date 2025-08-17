# 17814093 - Kuah Dakonsa

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 152 bytes                      |
| Total Events     | 4                              |
| References Count | 7                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [260](#event-260)     | 0x0001       |     13 |              7 |
| [261](#event-261)     | 0x000E       |     52 |             12 |
| [262](#event-262)     | 0x0042       |     25 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1ECA      |        7882 |
|       1 | 0x06B4      |        1716 |
|       2 | 0x003B      |          59 |
|       3 | 0x1ECB      |        7883 |
|       4 | 0x1ECC      |        7884 |
|       5 | 0x0007      |           7 |
|       6 | 0x1ECD      |        7885 |

## String References

- **7882**: Hail, stranger. What brings you all the way to the third outpost? It must be a vital task indeed, for you to trek to such an inhospitable place as this.
- **7883**: Ah, <Player>. Zauko gave me advance notice of your coming.
- **7884**: We appreciate your assistance. Well, you see the casket, don't you? Go right ahead and put that $3 in.
- **7885**: For a second there, I was afraid you'd start rambling about the Torch and Her divine Light like poor old Zauko. Precious few of the survivors have been able to keep their wits about them, what with the horrors they've seen...

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

### Event 260

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
    → "Hail, stranger. What brings you all the way to the third outpost? It must be a vital task indeed, for you to trek to such an inhospitable place as this."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 261

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            1E F0                ..
0010: FF FF 7F 6F 70 03 02 10  01 80 66 02 80 4D D2 0F  ...op.....f..M..
0020: 01 4D D2 0F 01 74 6C 6B  30 1D 03 80 23 1D 04 80  .M...tlk0...#...
0030: 23 66 02 80 4D D2 0F 01  4D D2 0F 01 74 6C 6B 31  #f..M...M...tlk1
0040: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x000E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0013 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0014 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0015 [0x03] Work_Zone[2] = 1716*
  4: 0x001A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Kuah Dakonsa (ID: 17814093/0x010FD24D), Kuah Dakonsa (ID: 17814093/0x010FD24D)], work=59*
  5: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=7883*)
    → "Ah, <Player>. Zauko gave me advance notice of your coming."
  6: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=7884*)
    → "We appreciate your assistance. Well, you see the casket, don't you? Go right ahead and put that $3 in."
  8: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0031 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Kuah Dakonsa (ID: 17814093/0x010FD24D), Kuah Dakonsa (ID: 17814093/0x010FD24D)], work=59*
 10: 0x0040 [0x21] END_EVENT
 11: 0x0041 [0x00] END_REQSTACK()
```

### Event 262

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 25 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       1E F0 FF FF 7F 6F  70 6E 4D D2 0F 01 05 80    .....opnM.....
0050: 99 4D D2 0F 01 1D 06 80  23 21 00                 .M......#!.     
```

#### Opcodes

```
  0: 0x0042 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0048 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0049 [0x6E] Kuah Dakonsa (ID: 17814093/0x010FD24D) uses emote 7*
  4: 0x0050 [0x99] Wait for Kuah Dakonsa (ID: 17814093/0x010FD24D) animation to complete
  5: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=7885*)
    → "For a second there, I was afraid you'd start rambling about the Torch and Her divine Light like poor old Zauko. Precious few of the survivors have been able to keep their wits about them, what with the horrors they've seen..."
  6: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0059 [0x21] END_EVENT
  8: 0x005A [0x00] END_REQSTACK()
```
