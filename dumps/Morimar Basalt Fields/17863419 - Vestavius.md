# 17863419 - Vestavius

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Morimar Basalt Fields (ID: 265) |
| Block Size       | 160 bytes                       |
| Total Events     | 4                               |
| References Count | 6                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [502](#event-502)     | 0x0001       |     47 |             11 |
| [29](#event-29)       | 0x0030       |     52 |             14 |
| [17](#event-17)       | 0x0064       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x1E7D      |        7805 |
|       2 | 0x1E7E      |        7806 |
|       3 | 0x1F07      |        7943 |
|       4 | 0x1F08      |        7944 |
|       5 | 0x1F09      |        7945 |

## String References

- **7805**: Steam vents dot the area here. Predictably, if you step over one you're in for a bit of a burn.
- **7806**: Plugging them up with rocks should be enough to keep you safe--and you'll be able to cross without any fear of injury.
- **7943**: E'rythin' here's goin' to hell in a han'basket. Y'know those traditionalists from the Order of Renaye were here studyin' the oddities with th' ergon loci here. Musta spooked 'em, too, because they ran back to Adoulin wit' their tails 'tween their legs.
- **7944**: It's all 'bove my head, but they said somethin' about ergon loci poppin' up where none had existed 'fore.
- **7945**: The spot they were talkin' about is to the north of the second frontier bivouac here. If you're a gemoanc'r, y'might learn somethin' by grabbin' a quick look.

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

### Event 502

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 66  ...tlk0...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 65 6E 30 21 00  ..........ten0!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7805*)
    → "Steam vents dot the area here. Predictably, if you step over one you're in for a bit of a burn."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=7806*)
    → "Plugging them up with rocks should be enough to keep you safe--and you'll be able to cross without any fear of injury."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten0" with entities [EventEntity, EventEntity], work=0*
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 52 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 42 1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8  B.....opf.......
0040: FF FF 7F 74 6C 6B 30 1D  03 80 23 1D 04 80 23 1D  ...tlk0...#...#.
0050: 05 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 65  ..#f..........te
0060: 6E 30 21 00                                       n0!.            
```

#### Opcodes

```
  0: 0x0030 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0031 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0036 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0037 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  5: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=7943*)
    → "E'rythin' here's goin' to hell in a han'basket. Y'know those traditionalists from the Order of Renaye were here studyin' the oddities with th' ergon loci here. Musta spooked 'em, too, because they ran back to Adoulin wit' their tails 'tween their legs."
  6: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=7944*)
    → "It's all 'bove my head, but they said somethin' about ergon loci poppin' up where none had existed 'fore."
  8: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=7945*)
    → "The spot they were talkin' about is to the north of the second frontier bivouac here. If you're a gemoanc'r, y'might learn somethin' by grabbin' a quick look."
 10: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0053 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten0" with entities [EventEntity, EventEntity], work=0*
 12: 0x0062 [0x21] END_EVENT
 13: 0x0063 [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             21 00                                     !.          
```

#### Opcodes

```
  0: 0x0064 [0x21] END_EVENT
  1: 0x0065 [0x00] END_REQSTACK()
```
