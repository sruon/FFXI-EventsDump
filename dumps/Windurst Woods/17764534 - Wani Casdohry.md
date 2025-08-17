# 17764534 - Wani Casdohry

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 380 bytes                |
| Total Events     | 14                       |
| References Count | 15                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [65535.3](#event-655353) | 0x001A       |      9 |              3 |
| [425](#event-425)        | 0x0023       |     33 |             12 |
| [86](#event-86)          | 0x0044       |     33 |             12 |
| [487](#event-487)        | 0x0065       |      1 |              1 |
| [65535.4](#event-655354) | 0x0066       |      5 |              3 |
| [65535.5](#event-655355) | 0x006B       |      5 |              3 |
| [65535.6](#event-655356) | 0x0070       |      5 |              3 |
| [489](#event-489)        | 0x0075       |     29 |             10 |
| [492](#event-492)        | 0x0092       |     37 |             14 |
| [553](#event-553)        | 0x00B7       |     29 |             10 |
| [554](#event-554)        | 0x00D4       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0167      |         359 |
|       1 | 0x001E      |          30 |
|       2 | 0x214F      |        8527 |
|       3 | 0x2150      |        8528 |
|       4 | 0x1DBA      |        7610 |
|       5 | 0x1DBB      |        7611 |
|       6 | 0x220E      |        8718 |
|       7 | 0x2210      |        8720 |
|       8 | 0x2213      |        8723 |
|       9 | 0x2218      |        8728 |
|      10 | 0x221D      |        8733 |
|      11 | 0x221E      |        8734 |
|      12 | 0x221F      |        8735 |
|      13 | 0x24BE      |        9406 |
|      14 | 0x24BF      |        9407 |

## String References

- **7610**: You can get your paws on $1 by defeating those Yagudo beastmen. But you won't please the Tarutaru very much if you go arrround fighting Yagudo!
- **7611**: Windurst is currently trying to maintain amicable relations with the Yagudo. It's a very different worrrld from what it was twenty years ago...
- **8527**: Our chieftainness is verrry old... It seems that she wants to pass the chieftainness's bow onto the Sibyl Guard Semih Lafihna.
- **8528**: But I doubt if Semih Lafihna would accept that honorable responsibility. Quite a prrredicament we're in, eh?
- **8718**: Our chieftainness recently invited Semih Lafihna over to open dialogue, but Semih Lafihna did not take her up on the offerrr.
- **8720**: I wonderrr if the chieftainness was going to tell her the truth. But I guess it doesn't matter whetherrr the truth is told or not, as the bad blood will still run thick between them.
- **8723**: I guess you are right... Oh, and what good timing, for there is an adventurerrr passing by now! Why don't we ask [him/her] whetherrr [he/she] can help us out with that task?
- **8728**: The $1 that can be found in the Meriphataud Mountains belong to the Mithran warriors who were felled there twenty years ago. If you find any, please hand them overrr to Gioh Ajihri, thank you.
- **8733**: Twinstones are, as their name suggests, a perrrfect pair of gemstones that are originally found joined as one.
- **8734**: No otherrr stones can come close to matching them once they are separated. Since they were once a single stone, only their corresponding halves fit perrrfectly back as one.
- **8735**: Utilizing this very properrrty, twinstones are used as proof of bonds between Mithra back in our homeland.
- **9406**: We found many earrings but had a terrible time trying to find the missing halves...I thought furrr was going to fly.
- **9407**: I wonder if the Mithran Tracker really believes that the daughter is dead... We can't let our guarrrd down yet.

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                5E 69 64 6C 30 1C            ^idl0.
0020: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x001A [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x001F [0x1C] WAIT(30* ticks)
  2: 0x0022 [0x00] END_REQSTACK()
```

### Event 425

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1E F0 FF FF 7F  6F 70 29 08 B6 10 0F 01     .....op).....
0030: 01 1D 02 80 23 1D 03 80  23 29 08 B6 10 0F 01 02  ....#...#)......
0040: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0023 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0029 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x01)
  4: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=8527*)
    → "Our chieftainness is verrry old... It seems that she wants to pass the chieftainness's bow onto the Sibyl Guard Semih Lafihna."
  5: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=8528*)
    → "But I doubt if Semih Lafihna would accept that honorable responsibility. Quite a prrredicament we're in, eh?"
  7: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0039 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x02)
  9: 0x0040 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0042 [0x21] END_EVENT
 11: 0x0043 [0x00] END_REQSTACK()
```

### Event 86

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             1E F0 FF FF  7F 6F 70 29 08 B6 10 0F      .....op)....
0050: 01 01 1D 04 80 23 1D 05  80 23 29 08 B6 10 0F 01  .....#...#).....
0060: 02 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0044 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x01)
  4: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=7610*)
    → "You can get your paws on $1 by defeating those Yagudo beastmen. But you won't please the Tarutaru very much if you go arrround fighting Yagudo!"
  5: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=7611*)
    → "Windurst is currently trying to maintain amicable relations with the Yagudo. It's a very different worrrld from what it was twenty years ago..."
  7: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x005A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x02)
  9: 0x0061 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0063 [0x21] END_EVENT
 11: 0x0064 [0x00] END_REQSTACK()
```

### Event 487

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0065  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                00                                      .          
```

#### Opcodes

```
  0: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   1D 06  80 23 00                       ...#.     
```

#### Opcodes

```
  0: 0x0066 [0x1D] PRINT_EVENT_MESSAGE(message_id=8718*)
    → "Our chieftainness recently invited Semih Lafihna over to open dialogue, but Semih Lafihna did not take her up on the offerrr."
  1: 0x0069 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   1D 07 80 23 00             ...#.
```

#### Opcodes

```
  0: 0x006B [0x1D] PRINT_EVENT_MESSAGE(message_id=8720*)
    → "I wonderrr if the chieftainness was going to tell her the truth. But I guess it doesn't matter whetherrr the truth is told or not, as the bad blood will still run thick between them."
  1: 0x006E [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x006F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0070  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 1D 08 80 23 00                                    ...#.           
```

#### Opcodes

```
  0: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=8723*)
    → "I guess you are right... Oh, and what good timing, for there is an adventurerrr passing by now! Why don't we ask [him/her] whetherrr [he/she] can help us out with that task?"
  1: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0074 [0x00] END_REQSTACK()
```

### Event 489

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                1E F0 FF  FF 7F 6F 70 29 08 B6 10       .....op)...
0080: 0F 01 01 1D 09 80 23 29  08 B6 10 0F 01 02 20 00  ......#)...... .
0090: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0075 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x007A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x007B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x007C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x01)
  4: 0x0083 [0x1D] PRINT_EVENT_MESSAGE(message_id=8728*)
    → "The $1 that can be found in the Meriphataud Mountains belong to the Mithran warriors who were felled there twenty years ago. If you find any, please hand them overrr to Gioh Ajihri, thank you."
  5: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0087 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x02)
  7: 0x008E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0090 [0x21] END_EVENT
  9: 0x0091 [0x00] END_REQSTACK()
```

### Event 492

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 37 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       1E F0 FF FF 7F 6F  70 29 08 B6 10 0F 01 01    .....op)......
00A0: 1D 0A 80 23 1D 0B 80 23  1D 0C 80 23 29 08 B6 10  ...#...#...#)...
00B0: 0F 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0092 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0097 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0098 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0099 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x01)
  4: 0x00A0 [0x1D] PRINT_EVENT_MESSAGE(message_id=8733*)
    → "Twinstones are, as their name suggests, a perrrfect pair of gemstones that are originally found joined as one."
  5: 0x00A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A4 [0x1D] PRINT_EVENT_MESSAGE(message_id=8734*)
    → "No otherrr stones can come close to matching them once they are separated. Since they were once a single stone, only their corresponding halves fit perrrfectly back as one."
  7: 0x00A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00A8 [0x1D] PRINT_EVENT_MESSAGE(message_id=8735*)
    → "Utilizing this very properrrty, twinstones are used as proof of bonds between Mithra back in our homeland."
  9: 0x00AB [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00AC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x02)
 11: 0x00B3 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x00B5 [0x21] END_EVENT
 13: 0x00B6 [0x00] END_REQSTACK()
```

### Event 553

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      1E  F0 FF FF 7F 6F 70 29 08         .....op).
00C0: B6 10 0F 01 01 1D 0D 80  23 29 08 B6 10 0F 01 02  ........#)......
00D0: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x00B7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00BC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00BD [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00BE [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x01)
  4: 0x00C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=9406*)
    → "We found many earrings but had a terrible time trying to find the missing halves...I thought furrr was going to fly."
  5: 0x00C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00C9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x02)
  7: 0x00D0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00D2 [0x21] END_EVENT
  9: 0x00D3 [0x00] END_REQSTACK()
```

### Event 554

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D4   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             1E F0 FF FF  7F 6F 70 29 08 B6 10 0F      .....op)....
00E0: 01 01 1D 0D 80 23 1D 0E  80 23 29 08 B6 10 0F 01  .....#...#).....
00F0: 02 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x00D4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00D9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00DA [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00DB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x01)
  4: 0x00E2 [0x1D] PRINT_EVENT_MESSAGE(message_id=9406*)
    → "We found many earrings but had a terrible time trying to find the missing halves...I thought furrr was going to fly."
  5: 0x00E5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00E6 [0x1D] PRINT_EVENT_MESSAGE(message_id=9407*)
    → "I wonder if the Mithran Tracker really believes that the daughter is dead... We can't let our guarrrd down yet."
  7: 0x00E9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00EA [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Wani Casdohry (ID: 17764534/0x010F10B6), tag_num=0x02)
  9: 0x00F1 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00F3 [0x21] END_EVENT
 11: 0x00F4 [0x00] END_REQSTACK()
```
