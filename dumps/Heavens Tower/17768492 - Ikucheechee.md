# 17768492 - Ikucheechee

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 548 bytes               |
| Total Events     | 17                      |
| References Count | 20                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [65535.3](#event-655353) | 0x001A       |     16 |              2 |
| [65535.4](#event-655354) | 0x002A       |     14 |              2 |
| [65535.5](#event-655355) | 0x0038       |     16 |              2 |
| [65535.6](#event-655356) | 0x0048       |     14 |              2 |
| [63](#event-63)          | 0x0056       |     33 |             12 |
| [129](#event-129)        | 0x0077       |     33 |             12 |
| [143](#event-143)        | 0x0098       |     33 |             12 |
| [183](#event-183)        | 0x00B9       |     33 |             12 |
| [208](#event-208)        | 0x00DA       |     33 |             12 |
| [229](#event-229)        | 0x00FB       |     33 |             12 |
| [121](#event-121)        | 0x011C       |      1 |              1 |
| [343](#event-343)        | 0x011D       |     33 |             12 |
| [356](#event-356)        | 0x013E       |     33 |             12 |
| [394](#event-394)        | 0x015F       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x0029      |          41 |
|       3 | 0x002A      |          42 |
|       4 | 0x00FF      |         255 |
|       5 | 0x0100      |         256 |
|       6 | 0x0120      |         288 |
|       7 | 0x0121      |         289 |
|       8 | 0x0179      |         377 |
|       9 | 0x017A      |         378 |
|      10 | 0x01CE      |         462 |
|      11 | 0x01CF      |         463 |
|      12 | 0x01FD      |         509 |
|      13 | 0x01FE      |         510 |
|      14 | 0x2063      |        8291 |
|      15 | 0x2064      |        8292 |
|      16 | 0x20EF      |        8431 |
|      17 | 0x20F0      |        8432 |
|      18 | 0x214B      |        8523 |
|      19 | 0x214C      |        8524 |

## String References

- **41**: You should lock up all memories of this place in the back of your mini-mini miniscule brain and throw away the key. Understood?
- **42**: Nothing good ever comes from curiosity. Even the most beautiful love story can be packed with putrid poison for the mind.
- **255**: You remember when we had our visit from that overly obnoxious Orastery minister, don't you?
- **256**: Well, I heard the captain of the Sibyl Guards, Semih Lafihnam, is on the trail of that fraudulent fiend. It looks like his time to pay has come.
- **288**: I heard that our overtly obsessed Orastery minister traveled to meet the Yagudo king.
- **289**: If only the Yagudo had eaten him up for dinner!
- **377**: You should lock up all memories of this incident in the back of your mini-mini miniscule brain and throw away the key. Understood?
- **378**: No one outside of Heavens Tower, including your abominable adventuring acquaintances, needs to know that anything is wrong. Windurst must maintain its image of peace.
- **462**: Is it absolutely necessary for Windurst to take the lead in this sticky situation of strife?
- **463**: If Jeuno would only take the first step, then Windurst could follow...safely...
- **509**: Night in and night out, I had been having nothing but nasty nightmares. A coffin, shrouded in darkness, opens slowly and...AHHHHH!
- **510**: But I did not have that dreadful dream last night. Does this mean the nightmare is over...or only just...AHHHHH!
- **8291**: I wonder how the sinuously sly Sibyl Guards fared in the battle?
- **8292**: We ladies-in-waiting are not being allowed into the Planetarium. So if you, my admirably acquainted adventurer, could ask for us, we would be most appreciative.
- **8431**: The strenuously striving Sibyl Guards seem terribly tired. They don't seem to have a moment to relax.
- **8432**: I prepared some snacks to refresh their lagging lackluster spirits, but the Mithra probably aren't fond of sweets...
- **8523**: The Sibyl Guards seem to have sustained injuries during their sporadic scuffles with the Cardians.
- **8524**: The wounds were mostaruly cuts and bruises, but injuries are injuries. They should be taking it easy-weasy for a while.

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                66 00 80 F8 FF FF            f.....
0020: 7F F8 FF FF 7F 6F 62 69  30 00                    .....obi0.      
```

#### Opcodes

```
  0: 0x001A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "obi0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                53 F8 FF FF 7F F8            S.....
0030: FF FF 7F 6F 62 69 30 00                           ...obi0.        
```

#### Opcodes

```
  0: 0x002A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "obi0" with entities [EventEntity, EventEntity]
  1: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          66 00 80 F8 FF FF 7F F8          f.......
0040: FF FF 7F 6F 62 69 31 00                           ...obi1.        
```

#### Opcodes

```
  0: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "obi1" with entities [EventEntity, EventEntity], work=40*
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          53 F8 FF FF 7F F8 FF FF          S.......
0050: 7F 6F 62 69 31 00                                 .obi1.          
```

#### Opcodes

```
  0: 0x0048 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "obi1" with entities [EventEntity, EventEntity]
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 63

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   1E F0  FF FF 7F 6F 70 29 08 2C        .....op).,
0060: 20 0F 01 01 1D 02 80 23  1D 03 80 23 29 08 2C 20   ......#...#)., 
0070: 0F 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0056 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x005C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x005D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x01)
  4: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=41*)
    → "You should lock up all memories of this place in the back of your mini-mini miniscule brain and throw away the key. Understood?"
  5: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0068 [0x1D] PRINT_EVENT_MESSAGE(message_id=42*)
    → "Nothing good ever comes from curiosity. Even the most beautiful love story can be packed with putrid poison for the mind."
  7: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x006C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x02)
  9: 0x0073 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0075 [0x21] END_EVENT
 11: 0x0076 [0x00] END_REQSTACK()
```

### Event 129

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      1E  F0 FF FF 7F 6F 70 29 08         .....op).
0080: 2C 20 0F 01 01 1D 04 80  23 1D 05 80 23 29 08 2C  , ......#...#).,
0090: 20 0F 01 02 20 00 21 00                            ... .!.        
```

#### Opcodes

```
  0: 0x0077 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x007C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x007D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x007E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x01)
  4: 0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=255*)
    → "You remember when we had our visit from that overly obnoxious Orastery minister, don't you?"
  5: 0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0089 [0x1D] PRINT_EVENT_MESSAGE(message_id=256*)
    → "Well, I heard the captain of the Sibyl Guards, Semih Lafihnam, is on the trail of that fraudulent fiend. It looks like his time to pay has come."
  7: 0x008C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x008D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x02)
  9: 0x0094 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0096 [0x21] END_EVENT
 11: 0x0097 [0x00] END_REQSTACK()
```

### Event 143

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          1E F0 FF FF 7F 6F 70 29          .....op)
00A0: 08 2C 20 0F 01 01 1D 06  80 23 1D 07 80 23 29 08  ., ......#...#).
00B0: 2C 20 0F 01 02 20 00 21  00                       , ... .!.       
```

#### Opcodes

```
  0: 0x0098 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x009D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x009E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x009F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x01)
  4: 0x00A6 [0x1D] PRINT_EVENT_MESSAGE(message_id=288*)
    → "I heard that our overtly obsessed Orastery minister traveled to meet the Yagudo king."
  5: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=289*)
    → "If only the Yagudo had eaten him up for dinner!"
  7: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00AE [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x02)
  9: 0x00B5 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00B7 [0x21] END_EVENT
 11: 0x00B8 [0x00] END_REQSTACK()
```

### Event 183

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             1E F0 FF FF 7F 6F 70           .....op
00C0: 29 08 2C 20 0F 01 01 1D  08 80 23 1D 09 80 23 29  )., ......#...#)
00D0: 08 2C 20 0F 01 02 20 00  21 00                    ., ... .!.      
```

#### Opcodes

```
  0: 0x00B9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00BE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00BF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00C0 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x01)
  4: 0x00C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=377*)
    → "You should lock up all memories of this incident in the back of your mini-mini miniscule brain and throw away the key. Understood?"
  5: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00CB [0x1D] PRINT_EVENT_MESSAGE(message_id=378*)
    → "No one outside of Heavens Tower, including your abominable adventuring acquaintances, needs to know that anything is wrong. Windurst must maintain its image of peace."
  7: 0x00CE [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00CF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x02)
  9: 0x00D6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00D8 [0x21] END_EVENT
 11: 0x00D9 [0x00] END_REQSTACK()
```

### Event 208

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DA   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                1E F0 FF FF 7F 6F            .....o
00E0: 70 29 08 2C 20 0F 01 01  1D 0A 80 23 1D 0B 80 23  p)., ......#...#
00F0: 29 08 2C 20 0F 01 02 20  00 21 00                 )., ... .!.     
```

#### Opcodes

```
  0: 0x00DA [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00DF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00E0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00E1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x01)
  4: 0x00E8 [0x1D] PRINT_EVENT_MESSAGE(message_id=462*)
    → "Is it absolutely necessary for Windurst to take the lead in this sticky situation of strife?"
  5: 0x00EB [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00EC [0x1D] PRINT_EVENT_MESSAGE(message_id=463*)
    → "If Jeuno would only take the first step, then Windurst could follow...safely..."
  7: 0x00EF [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00F0 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x02)
  9: 0x00F7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00F9 [0x21] END_EVENT
 11: 0x00FA [0x00] END_REQSTACK()
```

### Event 229

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FB   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                   1E F0 FF FF 7F             .....
0100: 6F 70 29 08 2C 20 0F 01  01 1D 0C 80 23 1D 0D 80  op)., ......#...
0110: 23 29 08 2C 20 0F 01 02  20 00 21 00              #)., ... .!.    
```

#### Opcodes

```
  0: 0x00FB [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0100 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0101 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0102 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x01)
  4: 0x0109 [0x1D] PRINT_EVENT_MESSAGE(message_id=509*)
    → "Night in and night out, I had been having nothing but nasty nightmares. A coffin, shrouded in darkness, opens slowly and...AHHHHH!"
  5: 0x010C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x010D [0x1D] PRINT_EVENT_MESSAGE(message_id=510*)
    → "But I did not have that dreadful dream last night. Does this mean the nightmare is over...or only just...AHHHHH!"
  7: 0x0110 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0111 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x02)
  9: 0x0118 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x011A [0x21] END_EVENT
 11: 0x011B [0x00] END_REQSTACK()
```

### Event 121

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                      00                       .   
```

#### Opcodes

```
  0: 0x011C [0x00] END_REQSTACK()
```

### Event 343

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011D   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                         1E F0 FF               ...
0120: FF 7F 6F 70 29 08 2C 20  0F 01 01 1D 0E 80 23 1D  ..op)., ......#.
0130: 0F 80 23 29 08 2C 20 0F  01 02 20 00 21 00        ..#)., ... .!.  
```

#### Opcodes

```
  0: 0x011D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0122 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0123 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0124 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x01)
  4: 0x012B [0x1D] PRINT_EVENT_MESSAGE(message_id=8291*)
    → "I wonder how the sinuously sly Sibyl Guards fared in the battle?"
  5: 0x012E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x012F [0x1D] PRINT_EVENT_MESSAGE(message_id=8292*)
    → "We ladies-in-waiting are not being allowed into the Planetarium. So if you, my admirably acquainted adventurer, could ask for us, we would be most appreciative."
  7: 0x0132 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0133 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x02)
  9: 0x013A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x013C [0x21] END_EVENT
 11: 0x013D [0x00] END_REQSTACK()
```

### Event 356

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013E   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                            1E F0                ..
0140: FF FF 7F 6F 70 29 08 2C  20 0F 01 01 1D 10 80 23  ...op)., ......#
0150: 1D 11 80 23 29 08 2C 20  0F 01 02 20 00 21 00     ...#)., ... .!. 
```

#### Opcodes

```
  0: 0x013E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0143 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0144 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0145 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x01)
  4: 0x014C [0x1D] PRINT_EVENT_MESSAGE(message_id=8431*)
    → "The strenuously striving Sibyl Guards seem terribly tired. They don't seem to have a moment to relax."
  5: 0x014F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0150 [0x1D] PRINT_EVENT_MESSAGE(message_id=8432*)
    → "I prepared some snacks to refresh their lagging lackluster spirits, but the Mithra probably aren't fond of sweets..."
  7: 0x0153 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0154 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x02)
  9: 0x015B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x015D [0x21] END_EVENT
 11: 0x015E [0x00] END_REQSTACK()
```

### Event 394

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015F   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                               1E                 .
0160: F0 FF FF 7F 6F 70 29 08  2C 20 0F 01 01 1D 12 80  ....op)., ......
0170: 23 1D 13 80 23 29 08 2C  20 0F 01 02 20 00 21 00  #...#)., ... .!.
```

#### Opcodes

```
  0: 0x015F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0164 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0165 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0166 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x01)
  4: 0x016D [0x1D] PRINT_EVENT_MESSAGE(message_id=8523*)
    → "The Sibyl Guards seem to have sustained injuries during their sporadic scuffles with the Cardians."
  5: 0x0170 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0171 [0x1D] PRINT_EVENT_MESSAGE(message_id=8524*)
    → "The wounds were mostaruly cuts and bruises, but injuries are injuries. They should be taking it easy-weasy for a while."
  7: 0x0174 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0175 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ikucheechee (ID: 17768492/0x010F202C), tag_num=0x02)
  9: 0x017C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x017E [0x21] END_EVENT
 11: 0x017F [0x00] END_REQSTACK()
```
