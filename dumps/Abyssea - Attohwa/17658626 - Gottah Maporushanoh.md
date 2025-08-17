# 17658626 - Gottah Maporushanoh

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Attohwa (ID: 215) |
| Block Size       | 168 bytes                   |
| Total Events     | 3                           |
| References Count | 10                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [382](#event-382)     | 0x0001       |     39 |             12 |
| [383](#event-383)     | 0x0028       |     60 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0003      |           3 |
|       1 | 0x0013      |          19 |
|       2 | 0x2068      |        8296 |
|       3 | 0x2069      |        8297 |
|       4 | 0x206A      |        8298 |
|       5 | 0x206B      |        8299 |
|       6 | 0x206C      |        8300 |
|       7 | 0x0007      |           7 |
|       8 | 0x206D      |        8301 |
|       9 | 0x206E      |        8302 |

## String References

- **8296**: Gee, my head hurrrts...
- **8297**: I thought it was just the Federation that fell to the horrrdes, but people here're sayin' that Jeuno went down 'n blazes too.
- **8298**: This chasm ain't a frrriendly place, but perhaps it's as good as anywhere under this blood-rrred sky.
- **8299**: <Grrroan>... Sorry, but could ya jus' leave me be?
- **8300**: Ever since I came to this chasm, just walkin' around is sappin' me of all my enerrrgy. I got nothin' left...empty, kaput!
- **8301**: <Grrroan>... Sorry, but could ya jus' leave me be?
- **8302**: The fiends out there are too tough for a rookie like me. I gotta get back trrrainin'...soon as I get over this blasted headache.

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

### Event 382

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 39 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    02 02 10 00 80 03 19  00 6E F8 FF FF 7F 01 80   ........n......
0010: 99 F8 FF FF 7F 1D 02 80  23 1E F0 FF FF 7F 1D 03  ........#.......
0020: 80 23 1D 04 80 23 21 00                           .#...#!.        
```

#### Opcodes

```
  0: 0x0001 [0x02] IF !(Work_Zone[2] >= 3*) GOTO 0x0019
  1: 0x0009 [0x6E] EventEntity uses emote 19*
  2: 0x0010 [0x99] Wait for EventEntity animation to complete
  3: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=8296*)
    → "Gee, my head hurrrts..."
  4: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0019 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=8297*)
    → "I thought it was just the Federation that fell to the horrrdes, but people here're sayin' that Jeuno went down 'n blazes too."
  7: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=8298*)
    → "This chasm ain't a frrriendly place, but perhaps it's as good as anywhere under this blood-rrred sky."
  9: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0026 [0x21] END_EVENT
 11: 0x0027 [0x00] END_REQSTACK()
```

### Event 383

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 60 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          1E F0 FF FF 7F 6F 70 02          .....op.
0030: 02 10 00 80 03 4E 00 6E  F8 FF FF 7F 01 80 99 F8  .....N.n........
0040: FF FF 7F 1D 05 80 23 1D  06 80 23 01 62 00 6E F8  ......#...#.b.n.
0050: FF FF 7F 07 80 99 F8 FF  FF 7F 1D 08 80 23 1D 09  .............#..
0060: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0028 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x002E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002F [0x02] IF !(Work_Zone[2] >= 3*) GOTO 0x004E
  4: 0x0037 [0x6E] EventEntity uses emote 19*
  5: 0x003E [0x99] Wait for EventEntity animation to complete
  6: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=8299*)
    → "<Grrroan>... Sorry, but could ya jus' leave me be?"
  7: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=8300*)
    → "Ever since I came to this chasm, just walkin' around is sappin' me of all my enerrrgy. I got nothin' left...empty, kaput!"
  9: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x004B [0x01] GOTO 0x0062
 11: 0x004E [0x6E] EventEntity uses emote 7*
 12: 0x0055 [0x99] Wait for EventEntity animation to complete
 13: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=8301*)
    → "<Grrroan>... Sorry, but could ya jus' leave me be?"
 14: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x005E [0x1D] PRINT_EVENT_MESSAGE(message_id=8302*)
    → "The fiends out there are too tough for a rookie like me. I gotta get back trrrainin'...soon as I get over this blasted headache."
 16: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0062:
 17: 0x0062 [0x21] END_EVENT
 18: 0x0063 [0x00] END_REQSTACK()
```
