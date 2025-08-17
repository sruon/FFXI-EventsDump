# 17826067 - Marjoirelle

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 800 bytes                 |
| Total Events     | 38                        |
| References Count | 10                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [538](#event-538)          | 0x0001       |     51 |             13 |
| [68](#event-68)            | 0x0034       |     48 |             12 |
| [592](#event-592)          | 0x0064       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0065       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0075       |     22 |              4 |
| [65535.3](#event-655353)   | 0x008B       |     16 |              2 |
| [65535.4](#event-655354)   | 0x009B       |     14 |              2 |
| [65535.5](#event-655355)   | 0x00A9       |     16 |              2 |
| [65535.6](#event-655356)   | 0x00B9       |     14 |              2 |
| [65535.7](#event-655357)   | 0x00C7       |     16 |              2 |
| [65535.8](#event-655358)   | 0x00D7       |     14 |              2 |
| [65535.9](#event-655359)   | 0x00E5       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00F5       |     14 |              2 |
| [65535.11](#event-6553511) | 0x0103       |     16 |              2 |
| [65535.12](#event-6553512) | 0x0113       |     14 |              2 |
| [65535.13](#event-6553513) | 0x0121       |     16 |              2 |
| [65535.14](#event-6553514) | 0x0131       |     14 |              2 |
| [65535.15](#event-6553515) | 0x013F       |     16 |              2 |
| [65535.16](#event-6553516) | 0x014F       |     14 |              2 |
| [65535.17](#event-6553517) | 0x015D       |     16 |              2 |
| [65535.18](#event-6553518) | 0x016D       |     14 |              2 |
| [65535.19](#event-6553519) | 0x017B       |     16 |              2 |
| [65535.20](#event-6553520) | 0x018B       |     14 |              2 |
| [65535.21](#event-6553521) | 0x0199       |     16 |              2 |
| [65535.22](#event-6553522) | 0x01A9       |     14 |              2 |
| [65535.23](#event-6553523) | 0x01B7       |     16 |              2 |
| [65535.24](#event-6553524) | 0x01C7       |     14 |              2 |
| [65535.25](#event-6553525) | 0x01D5       |     16 |              2 |
| [65535.26](#event-6553526) | 0x01E5       |     14 |              2 |
| [65535.27](#event-6553527) | 0x01F3       |     16 |              2 |
| [65535.28](#event-6553528) | 0x0203       |     14 |              2 |
| [65535.29](#event-6553529) | 0x0211       |     16 |              2 |
| [65535.30](#event-6553530) | 0x0221       |     14 |              2 |
| [65535.31](#event-6553531) | 0x022F       |     16 |              2 |
| [65535.32](#event-6553532) | 0x023F       |     14 |              2 |
| [593](#event-593)          | 0x024D       |      1 |              1 |
| [594](#event-594)          | 0x024E       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2688      |        9864 |
|       2 | 0x2689      |        9865 |
|       3 | 0x268A      |        9866 |
|       4 | 0x1FC9      |        8137 |
|       5 | 0x1FCA      |        8138 |
|       6 | 0x003C      |          60 |
|       7 | 0x0021      |          33 |
|       8 | 0x001F      |          31 |
|       9 | 0x0020      |          32 |

## String References

- **8137**: How is the Mummers' Coalition treating you? What? You are here on behalf of the library?
- **8138**: Let me see...no, I do not see anything wrong here. Let them know everything is accurate and up-to-date.
- **9864**: We shan't be able to colonize Ulbuka if pioneers are overly tired, no?
- **9865**: We at the Mummers' Coalition work as hard as possible to ensure those providing a brighter future for the continent never lose their ambition. We endeavor to keep morale high by providing festive functions and other joyous events year-round.
- **9866**: Speaking of our fine institution, this regal estate belongs to Flaviria, the esteemed leader of our coalition. Without her, living in this city would be a much less pleasurable experience.

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

### Event 538

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 51 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 1D  ...tlk0...#...#.
0020: 03 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0030: 6B 31 21 00                                       k1!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=9864*)
    → "We shan't be able to colonize Ulbuka if pioneers are overly tired, no?"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=9865*)
    → "We at the Mummers' Coalition work as hard as possible to ensure those providing a brighter future for the continent never lose their ambition. We endeavor to keep morale high by providing festive functions and other joyous events year-round."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=9866*)
    → "Speaking of our fine institution, this regal estate belongs to Flaviria, the esteemed leader of our coalition. Without her, living in this city would be a much less pleasurable experience."
  9: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0023 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=30*
 11: 0x0032 [0x21] END_EVENT
 12: 0x0033 [0x00] END_REQSTACK()
```

### Event 68

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 48 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             42 1E F0 FF  FF 7F 6F 70 66 00 80 F8      B.....opf...
0040: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 04 80 23 1D  .......tlk0...#.
0050: 05 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0060: 6B 31 21 00                                       k1!.            
```

#### Opcodes

```
  0: 0x0034 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0035 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x003A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x003B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x003C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  5: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=8137*)
    → "How is the Mummers' Coalition treating you? What? You are here on behalf of the library?"
  6: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=8138*)
    → "Let me see...no, I do not see anything wrong here. Let them know everything is accurate and up-to-date."
  8: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0053 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=30*
 10: 0x0062 [0x21] END_EVENT
 11: 0x0063 [0x00] END_REQSTACK()
```

### Event 592

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             00                                        .           
```

#### Opcodes

```
  0: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
0070: 74 6C 6B 30 00                                    tlk0.           
```

#### Opcodes

```
  0: 0x0065 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  1: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                53 F8 FF  FF 7F F8 FF FF 7F 74 6C       S........tl
0080: 6B 30 5E 69 64 6C 30 1C  06 80 00                 k0^idl0....     
```

#### Opcodes

```
  0: 0x0075 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0082 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0087 [0x1C] WAIT(60* ticks)
  3: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   66 07 80 F8 FF             f....
0090: FF 7F F8 FF FF 7F 74 6C  62 30 00                 ......tlb0.     
```

#### Opcodes

```
  0: 0x008B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=33*
  1: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   53 F8 FF FF 7F             S....
00A0: F8 FF FF 7F 74 6C 62 30  00                       ....tlb0.       
```

#### Opcodes

```
  0: 0x009B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb0" with entities [EventEntity, EventEntity]
  1: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             66 07 80 F8 FF FF 7F           f......
00B0: F8 FF FF 7F 74 6C 62 31  00                       ....tlb1.       
```

#### Opcodes

```
  0: 0x00A9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=33*
  1: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             53 F8 FF FF 7F F8 FF           S......
00C0: FF 7F 74 6C 62 31 00                              ..tlb1.         
```

#### Opcodes

```
  0: 0x00B9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
  1: 0x00C6 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C7   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                      66  00 80 F8 FF FF 7F F8 FF         f........
00D0: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x00C7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=30*
  1: 0x00D6 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00E0: 74 68 6B 31 00                                    thk1.           
```

#### Opcodes

```
  0: 0x00D7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x00E4 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
00F0: 74 68 6B 32 00                                    thk2.           
```

#### Opcodes

```
  0: 0x00E5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=30*
  1: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                53 F8 FF  FF 7F F8 FF FF 7F 74 68       S........th
0100: 6B 32 00                                          k2.             
```

#### Opcodes

```
  0: 0x00F5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0102 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0103   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 64 69     f..........di
0110: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x0103 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=30*
  1: 0x0112 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0113   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:          53 F8 FF FF 7F  F8 FF FF 7F 64 69 73 30     S........dis0
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x0113 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x0120 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0121   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 30   f..........poi0
0130: 00                                                .               
```

#### Opcodes

```
  0: 0x0121 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=30*
  1: 0x0130 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0131   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:    53 F8 FF FF 7F F8 FF  FF 7F 70 6F 69 30 00      S........poi0. 
```

#### Opcodes

```
  0: 0x0131 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x013E [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                               66                 f
0140: 00 80 F8 FF FF 7F F8 FF  FF 7F 70 6F 69 31 00     ..........poi1. 
```

#### Opcodes

```
  0: 0x013F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=30*
  1: 0x014E [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                               53                 S
0150: F8 FF FF 7F F8 FF FF 7F  70 6F 69 31 00           ........poi1.   
```

#### Opcodes

```
  0: 0x014F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
  1: 0x015C [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                         66 08 80               f..
0160: F8 FF FF 7F F8 FF FF 7F  77 65 62 30 00           ........web0.   
```

#### Opcodes

```
  0: 0x015D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "web0" with entities [EventEntity, EventEntity], work=31*
  1: 0x016C [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                         53 F8 FF               S..
0170: FF 7F F8 FF FF 7F 77 65  62 30 00                 ......web0.     
```

#### Opcodes

```
  0: 0x016D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "web0" with entities [EventEntity, EventEntity]
  1: 0x017A [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                   66 00 80 F8 FF             f....
0180: FF 7F F8 FF FF 7F 70 61  73 30 00                 ......pas0.     
```

#### Opcodes

```
  0: 0x017B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=30*
  1: 0x018A [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                   53 F8 FF FF 7F             S....
0190: F8 FF FF 7F 70 61 73 30  00                       ....pas0.       
```

#### Opcodes

```
  0: 0x018B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x0198 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0199   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                             66 09 80 F8 FF FF 7F           f......
01A0: F8 FF FF 7F 73 74 64 30  00                       ....std0.       
```

#### Opcodes

```
  0: 0x0199 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=32*
  1: 0x01A8 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A9   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                             53 F8 FF FF 7F F8 FF           S......
01B0: FF 7F 73 74 64 30 00                              ..std0.         
```

#### Opcodes

```
  0: 0x01A9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "std0" with entities [EventEntity, EventEntity]
  1: 0x01B6 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B7   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                      66  09 80 F8 FF FF 7F F8 FF         f........
01C0: FF 7F 73 74 64 31 00                              ..std1.         
```

#### Opcodes

```
  0: 0x01B7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std1" with entities [EventEntity, EventEntity], work=32*
  1: 0x01C6 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
01D0: 73 74 64 31 00                                    std1.           
```

#### Opcodes

```
  0: 0x01C7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "std1" with entities [EventEntity, EventEntity]
  1: 0x01D4 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                66 09 80  F8 FF FF 7F F8 FF FF 7F       f..........
01E0: 74 6C 63 30 00                                    tlc0.           
```

#### Opcodes

```
  0: 0x01D5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=32*
  1: 0x01E4 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                53 F8 FF  FF 7F F8 FF FF 7F 74 6C       S........tl
01F0: 63 30 00                                          c0.             
```

#### Opcodes

```
  0: 0x01E5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc0" with entities [EventEntity, EventEntity]
  1: 0x01F2 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:          66 09 80 F8 FF  FF 7F F8 FF FF 7F 74 6C     f..........tl
0200: 63 31 00                                          c1.             
```

#### Opcodes

```
  0: 0x01F3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc1" with entities [EventEntity, EventEntity], work=32*
  1: 0x0202 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0203   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:          53 F8 FF FF 7F  F8 FF FF 7F 74 6C 63 31     S........tlc1
0210: 00                                                .               
```

#### Opcodes

```
  0: 0x0203 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc1" with entities [EventEntity, EventEntity]
  1: 0x0210 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0211   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:    66 09 80 F8 FF FF 7F  F8 FF FF 7F 74 63 73 74   f..........tcst
0220: 00                                                .               
```

#### Opcodes

```
  0: 0x0211 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tcst" with entities [EventEntity, EventEntity], work=32*
  1: 0x0220 [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0221   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:    53 F8 FF FF 7F F8 FF  FF 7F 74 63 73 74 00      S........tcst. 
```

#### Opcodes

```
  0: 0x0221 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tcst" with entities [EventEntity, EventEntity]
  1: 0x022E [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x022F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                               66                 f
0230: 09 80 F8 FF FF 7F F8 FF  FF 7F 73 74 74 63 00     ..........sttc. 
```

#### Opcodes

```
  0: 0x022F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sttc" with entities [EventEntity, EventEntity], work=32*
  1: 0x023E [0x00] END_REQSTACK()
```

### Event 65535.32

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x023F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                                               53                 S
0240: F8 FF FF 7F F8 FF FF 7F  73 74 74 63 00           ........sttc.   
```

#### Opcodes

```
  0: 0x023F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sttc" with entities [EventEntity, EventEntity]
  1: 0x024C [0x00] END_REQSTACK()
```

### Event 593

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x024D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                         00                     .  
```

#### Opcodes

```
  0: 0x024D [0x00] END_REQSTACK()
```

### Event 594

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x024E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                            00                   . 
```

#### Opcodes

```
  0: 0x024E [0x00] END_REQSTACK()
```
