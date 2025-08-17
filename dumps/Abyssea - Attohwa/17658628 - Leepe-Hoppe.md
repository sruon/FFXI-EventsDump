# 17658628 - Leepe-Hoppe

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Attohwa (ID: 215) |
| Block Size       | 300 bytes                   |
| Total Events     | 4                           |
| References Count | 19                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [385](#event-385)     | 0x0001       |     32 |             11 |
| [386](#event-386)     | 0x0021       |    105 |             29 |
| [387](#event-387)     | 0x008A       |     53 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0006      |           6 |
|       1 | 0x206F      |        8303 |
|       2 | 0x2070      |        8304 |
|       3 | 0x2071      |        8305 |
|       4 | 0x2072      |        8306 |
|       5 | 0x2073      |        8307 |
|       6 | 0x0003      |           3 |
|       7 | 0x2078      |        8312 |
|       8 | 0x0028      |          40 |
|       9 | 0x2079      |        8313 |
|      10 | 0x2076      |        8310 |
|      11 | 0x2077      |        8311 |
|      12 | 0x0007      |           7 |
|      13 | 0x2074      |        8308 |
|      14 | 0x2075      |        8309 |
|      15 | 0x207B      |        8315 |
|      16 | 0x207C      |        8316 |
|      17 | 0x207D      |        8317 |
|      18 | 0x207E      |        8318 |

## String References

- **8303**: Ahhhhhh-choo! <Hack>...<cough>...<wheeze>...
- **8304**: Ahem... Pardon my mucus, if you please.
- **8305**: Since arriving in this chasm, my piteous nose will simply not stop running-wunning, despite numerous blows.
- **8306**: What's that, you say? You're curious as to the quality of the air today?
- **8307**: Well, judging from my sniffle-wiffling frequency...
- **8308**: ...It's quite clear today, oh joy and glee!
- **8309**: That said, if experience is any guide we cannot count on this state to abide.
- **8310**: ...It's still far from ideal, as I'm sure you'll agree.
- **8311**: Still, I can say that it's been much worse. At this rate, we might even see our patients' symptoms reverse.
- **8312**: Ah-choo! Ah-choo! <Cough>, <sniffle>, <hack>, <wheeze>!
- **8313**: Thif if af bad af it'f been...<honk>...bake be fpeak bo more, pfease!
- **8315**: That robed fellow by the conflux, he wears an expression most stern.
- **8316**: He speaks of miasmas contaminating the air...
- **8317**: ...While the Professor speaks of flowers. Could there also be truth there?
- **8318**: Whatever should we do? If we don't solve our air...<wheeze>...problem...ah-ah...ah-chooooo!

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

### Event 385

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 32 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    02 02 10 00 80 03 16  00 1D 01 80 23 1E F0 FF   ...........#...
0010: FF 7F 1D 02 80 23 1E F0  FF FF 7F 1D 03 80 23 21  .....#........#!
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x02] IF !(Work_Zone[2] >= 6*) GOTO 0x0016
  1: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=8303*)
    → "Ahhhhhh-choo! <Hack>...<cough>...<wheeze>..."
  2: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=8304*)
    → "Ahem... Pardon my mucus, if you please."
  5: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0016 [0x1E] EventEntity looks at LocalPlayer and starts talking
  7: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=8305*)
    → "Since arriving in this chasm, my piteous nose will simply not stop running-wunning, despite numerous blows."
  8: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x001F [0x21] END_EVENT
 10: 0x0020 [0x00] END_REQSTACK()
```

### Event 386

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0021    |
| Data Size    | 105 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    1E F0 FF FF 7F 1D 04  80 23 1D 05 80 23 6F 70   ........#...#op
0030: 02 02 10 06 80 03 52 00  1D 07 80 23 66 08 80 F8  ......R....#f...
0040: FF FF 7F F8 FF FF 7F 69  72 6F 30 1D 09 80 23 01  .......iro0...#.
0050: 88 00 02 02 10 00 80 03  74 00 1D 0A 80 23 66 08  ........t....#f.
0060: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 0B 80  .........tlk0...
0070: 23 01 88 00 6E F8 FF FF  7F 0C 80 99 F8 FF FF 7F  #...n...........
0080: 1D 0D 80 23 1D 0E 80 23  21 00                    ...#...#!.      
```

#### Opcodes

```
  0: 0x0021 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0026 [0x1D] PRINT_EVENT_MESSAGE(message_id=8306*)
    → "What's that, you say? You're curious as to the quality of the air today?"
  2: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=8307*)
    → "Well, judging from my sniffle-wiffling frequency..."
  4: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x002E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x002F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0030 [0x02] IF !(Work_Zone[2] >= 3*) GOTO 0x0052
  8: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=8312*)
    → "Ah-choo! Ah-choo! <Cough>, <sniffle>, <hack>, <wheeze>!"
  9: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x003C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=40*
 11: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=8313*)
    → "Thif if af bad af it'f been...<honk>...bake be fpeak bo more, pfease!"
 12: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x004F [0x01] GOTO 0x0088
 14: 0x0052 [0x02] IF !(Work_Zone[2] >= 6*) GOTO 0x0074
 15: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=8310*)
    → "...It's still far from ideal, as I'm sure you'll agree."
 16: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x005E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
 18: 0x006D [0x1D] PRINT_EVENT_MESSAGE(message_id=8311*)
    → "Still, I can say that it's been much worse. At this rate, we might even see our patients' symptoms reverse."
 19: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0071 [0x01] GOTO 0x0088
 21: 0x0074 [0x6E] EventEntity uses emote 7*
 22: 0x007B [0x99] Wait for EventEntity animation to complete
 23: 0x0080 [0x1D] PRINT_EVENT_MESSAGE(message_id=8308*)
    → "...It's quite clear today, oh joy and glee!"
 24: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=8309*)
    → "That said, if experience is any guide we cannot count on this state to abide."
 26: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0088:
 27: 0x0088 [0x21] END_EVENT
 28: 0x0089 [0x00] END_REQSTACK()
```

### Event 387

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 53 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                1E F0 FF FF 7F 1D            ......
0090: 0F 80 23 1D 10 80 23 1D  11 80 23 66 08 80 F8 FF  ..#...#...#f....
00A0: FF 7F F8 FF FF 7F 74 68  6B 31 1D 12 80 23 66 08  ......thk1...#f.
00B0: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 21 00     .........thk2!. 
```

#### Opcodes

```
  0: 0x008A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x008F [0x1D] PRINT_EVENT_MESSAGE(message_id=8315*)
    → "That robed fellow by the conflux, he wears an expression most stern."
  2: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=8316*)
    → "He speaks of miasmas contaminating the air..."
  4: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0097 [0x1D] PRINT_EVENT_MESSAGE(message_id=8317*)
    → "...While the Professor speaks of flowers. Could there also be truth there?"
  6: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x009B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  8: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=8318*)
    → "Whatever should we do? If we don't solve our air...<wheeze>...problem...ah-ah...ah-chooooo!"
  9: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00AE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
 11: 0x00BD [0x21] END_EVENT
 12: 0x00BE [0x00] END_REQSTACK()
```
