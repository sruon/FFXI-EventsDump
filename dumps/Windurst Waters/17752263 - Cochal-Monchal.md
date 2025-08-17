# 17752263 - Cochal-Monchal

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 532 bytes                 |
| Total Events     | 14                        |
| References Count | 16                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     16 |              2 |
| [65535.4](#event-655354) | 0x0037       |     14 |              2 |
| [65535.5](#event-655355) | 0x0045       |     16 |              2 |
| [65535.6](#event-655356) | 0x0055       |     14 |              2 |
| [65535.7](#event-655357) | 0x0063       |     16 |              2 |
| [65535.8](#event-655358) | 0x0073       |     14 |              2 |
| [65535.9](#event-655359) | 0x0081       |      9 |              3 |
| [696](#event-696)        | 0x008A       |     29 |             10 |
| [697](#event-697)        | 0x00A7       |    161 |             36 |
| [698](#event-698)        | 0x0148       |     33 |             12 |
| [699](#event-699)        | 0x0169       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x2574      |        9588 |
|       3 | 0x2575      |        9589 |
|       4 | 0x00C8      |         200 |
|       5 | 0x0000      |           0 |
|       6 | 0x2576      |        9590 |
|       7 | 0x2577      |        9591 |
|       8 | 0x2578      |        9592 |
|       9 | 0x2579      |        9593 |
|      10 | 0x257A      |        9594 |
|      11 | 0x257B      |        9595 |
|      12 | 0x257C      |        9596 |
|      13 | 0x257D      |        9597 |
|      14 | 0x257E      |        9598 |
|      15 | 0x257F      |        9599 |

## String References

- **9588**: Phooey, Dewey! I'm sooo confused. This goes over...no, that goes...no, this needs to be...no...
- **9589**: What? No... Here from Bastok, are we? Yes? How may I help? No...assist, yes, assist.
- **9590**: Really? No... You say you're looking for $3? Yes...yes, I remember that one, I do.
- **9591**: It turned up the last time, or was it the first...no...the last time I cleaned out the old book vault. That text was filled with lots of important-looking blacksmithing techniques.
- **9592**: One look, and I knew this book didn't belong here in Windurst, I mean...not here in this library...I mean.
- **9593**: So, I decided to take it to Bastok and see if I could shed any light on the mystery surrounding the text...and that's when I was attacked by a band of rogues...Yagudo rogues, they were.
- **9594**: If we ever want to see it again, we'll have to travel to Giddeus and get it back from that thief, Vaa Huja the Erudite, ourselves.
- **9595**: Well, I didn't exactly mean "ourselves." You're the adventurer, aren't you...yes?
- **9596**: That thief, Vaa Huja the Erudite, is probably using $6 to line his birdcage as we speak!
- **9597**: We must do something...yes, something quickly!
- **9598**: Well, I'm happy to see that we were successful in retrieving $3... Yes, very happy.
- **9599**: Oh, yes, and when you take that back to Bastok, could you ask them if there are any other books they can donate? If they don't have any, a generous donation of gil would work just as well.

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      66  00 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 74 68 6B 31 00                                    thk1.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
0050: 74 68 6B 32 00                                    thk2.           
```

#### Opcodes

```
  0: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                53 F8 FF  FF 7F F8 FF FF 7F 74 68       S........th
0060: 6B 32 00                                          k2.             
```

#### Opcodes

```
  0: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 64 69     f..........di
0070: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          53 F8 FF FF 7F  F8 FF FF 7F 64 69 73 30     S........dis0
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0081  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0081 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0086 [0x1C] WAIT(30* ticks)
  2: 0x0089 [0x00] END_REQSTACK()
```

### Event 696

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                1E F0 FF FF 7F 6F            .....o
0090: 70 29 08 C7 E0 0E 01 01  1D 02 80 23 29 08 C7 E0  p).........#)...
00A0: 0E 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x008A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x008F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0090 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0091 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x01)
  4: 0x0098 [0x1D] PRINT_EVENT_MESSAGE(message_id=9588*)
    → "Phooey, Dewey! I'm sooo confused. This goes over...no, that goes...no, this needs to be...no..."
  5: 0x009B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x009C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x02)
  7: 0x00A3 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00A5 [0x21] END_EVENT
  9: 0x00A6 [0x00] END_REQSTACK()
```

### Event 697

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00A7    |
| Data Size    | 161 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      42  1E F0 FF FF 7F 6F 70 29         B.....op)
00B0: 08 C7 E0 0E 01 01 1D 03  80 23 29 08 C7 E0 0E 01  .........#).....
00C0: 02 45 04 80 F8 FF FF 7F  F8 FF FF 7F 66 64 6F 31  .E..........fdo1
00D0: 05 80 1C 04 80 29 08 C7  E0 0E 01 03 29 08 C7 E0  .....)......)...
00E0: 0E 01 04 45 04 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ...E..........fd
00F0: 69 31 05 80 1D 06 80 23  29 08 C7 E0 0E 01 05 1D  i1.....#).......
0100: 07 80 23 29 08 C7 E0 0E  01 06 1D 08 80 23 29 08  ..#).........#).
0110: C7 E0 0E 01 01 1D 09 80  23 29 08 C7 E0 0E 01 02  ........#)......
0120: 29 08 C7 E0 0E 01 07 1D  0A 80 23 29 08 C7 E0 0E  ).........#)....
0130: 01 08 29 08 C7 E0 0E 01  01 1D 0B 80 23 29 08 C7  ..).........#)..
0140: E0 0E 01 02 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x00A7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00A8 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00AD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00AE [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00AF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x01)
  5: 0x00B6 [0x1D] PRINT_EVENT_MESSAGE(message_id=9589*)
    → "What? No... Here from Bastok, are we? Yes? How may I help? No...assist, yes, assist."
  6: 0x00B9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00BA [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x02)
  8: 0x00C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  9: 0x00D2 [0x1C] WAIT(200* ticks)
 10: 0x00D5 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x03)
 11: 0x00DC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x04)
 12: 0x00E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 13: 0x00F4 [0x1D] PRINT_EVENT_MESSAGE(message_id=9590*)
    → "Really? No... You say you're looking for $3? Yes...yes, I remember that one, I do."
 14: 0x00F7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00F8 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x05)
 16: 0x00FF [0x1D] PRINT_EVENT_MESSAGE(message_id=9591*)
    → "It turned up the last time, or was it the first...no...the last time I cleaned out the old book vault. That text was filled with lots of important-looking blacksmithing techniques."
 17: 0x0102 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0103 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x06)
 19: 0x010A [0x1D] PRINT_EVENT_MESSAGE(message_id=9592*)
    → "One look, and I knew this book didn't belong here in Windurst, I mean...not here in this library...I mean."
 20: 0x010D [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x010E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x01)
 22: 0x0115 [0x1D] PRINT_EVENT_MESSAGE(message_id=9593*)
    → "So, I decided to take it to Bastok and see if I could shed any light on the mystery surrounding the text...and that's when I was attacked by a band of rogues...Yagudo rogues, they were."
 23: 0x0118 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0119 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x02)
 25: 0x0120 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x07)
 26: 0x0127 [0x1D] PRINT_EVENT_MESSAGE(message_id=9594*)
    → "If we ever want to see it again, we'll have to travel to Giddeus and get it back from that thief, Vaa Huja the Erudite, ourselves."
 27: 0x012A [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x012B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x08)
 29: 0x0132 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x01)
 30: 0x0139 [0x1D] PRINT_EVENT_MESSAGE(message_id=9595*)
    → "Well, I didn't exactly mean "ourselves." You're the adventurer, aren't you...yes?"
 31: 0x013C [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x013D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x02)
 33: 0x0144 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 34: 0x0146 [0x21] END_EVENT
 35: 0x0147 [0x00] END_REQSTACK()
```

### Event 698

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0148   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                          1E F0 FF FF 7F 6F 70 29          .....op)
0150: 08 C7 E0 0E 01 01 1D 0C  80 23 1D 0D 80 23 29 08  .........#...#).
0160: C7 E0 0E 01 02 20 00 21  00                       ..... .!.       
```

#### Opcodes

```
  0: 0x0148 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x014D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x014E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x014F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x01)
  4: 0x0156 [0x1D] PRINT_EVENT_MESSAGE(message_id=9596*)
    → "That thief, Vaa Huja the Erudite, is probably using $6 to line his birdcage as we speak!"
  5: 0x0159 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x015A [0x1D] PRINT_EVENT_MESSAGE(message_id=9597*)
    → "We must do something...yes, something quickly!"
  7: 0x015D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x015E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x02)
  9: 0x0165 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0167 [0x21] END_EVENT
 11: 0x0168 [0x00] END_REQSTACK()
```

### Event 699

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0169   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                             1E F0 FF FF 7F 6F 70           .....op
0170: 29 08 C7 E0 0E 01 01 1D  0E 80 23 1D 0F 80 23 29  ).........#...#)
0180: 08 C7 E0 0E 01 02 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x0169 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x016E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x016F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0170 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x01)
  4: 0x0177 [0x1D] PRINT_EVENT_MESSAGE(message_id=9598*)
    → "Well, I'm happy to see that we were successful in retrieving $3... Yes, very happy."
  5: 0x017A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x017B [0x1D] PRINT_EVENT_MESSAGE(message_id=9599*)
    → "Oh, yes, and when you take that back to Bastok, could you ask them if there are any other books they can donate? If they don't have any, a generous donation of gil would work just as well."
  7: 0x017E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x017F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cochal-Monchal (ID: 17752263/0x010EE0C7), tag_num=0x02)
  9: 0x0186 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0188 [0x21] END_EVENT
 11: 0x0189 [0x00] END_REQSTACK()
```
