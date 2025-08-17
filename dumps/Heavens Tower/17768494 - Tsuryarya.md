# 17768494 - Tsuryarya

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 576 bytes               |
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
| [65](#event-65)          | 0x0056       |     33 |             12 |
| [131](#event-131)        | 0x0077       |     33 |             12 |
| [145](#event-145)        | 0x0098       |     33 |             12 |
| [185](#event-185)        | 0x00B9       |     33 |             12 |
| [210](#event-210)        | 0x00DA       |     33 |             12 |
| [231](#event-231)        | 0x00FB       |     33 |             12 |
| [121](#event-121)        | 0x011C       |      1 |              1 |
| [345](#event-345)        | 0x011D       |     33 |             12 |
| [358](#event-358)        | 0x013E       |     61 |             16 |
| [396](#event-396)        | 0x017B       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x002D      |          45 |
|       3 | 0x002E      |          46 |
|       4 | 0x0103      |         259 |
|       5 | 0x0104      |         260 |
|       6 | 0x0124      |         292 |
|       7 | 0x0125      |         293 |
|       8 | 0x017D      |         381 |
|       9 | 0x017E      |         382 |
|      10 | 0x01D2      |         466 |
|      11 | 0x01D3      |         467 |
|      12 | 0x0201      |         513 |
|      13 | 0x0202      |         514 |
|      14 | 0x2067      |        8295 |
|      15 | 0x2068      |        8296 |
|      16 | 0x20F3      |        8435 |
|      17 | 0x20F4      |        8436 |
|      18 | 0x214F      |        8527 |
|      19 | 0x2150      |        8528 |

## String References

- **45**: Whenever I sneak a peek into the Star Spring, I always, always get this strangey-wangey feeling.
- **46**: It's a feeling like...one day I will become one of those countless, countless stars fleeting and floating in the heavens...
- **259**: The reason that the light of the stars is so dim is because they are so far, far, far away. If you were to get close to them, you would be blinded by their magnificent light.
- **260**: I always thought that being surrounded by such a powerful, powerful force, one day she would collapse...but to think that I was actually right! Oh, Star Sibyl! Forgive me!
- **292**: There was nothing wrong with the talisman in the Horutoto Ruins, was there?
- **293**: I shudder-butter at the thought of having to see the chaos that war brings again and again.
- **381**: Even in this time of despair, the stars in the Star Spring twinkle-winkle softly, softly.
- **382**: From the stars' point of view, our trouble-bubbles and wier-fears must seem as numerous and insignificant as a single blinkle-twinkle of light.
- **466**: At the last Star Reading, the Star Sibyl foresaw everlasting, lasting peace for Windurst, but I don't know if we can call our current situation peaceful.
- **467**: Could it be the Star Sibyl was...?
- **513**: This morning, when the sun rose and the evening stars faded slowly, slowly...I saw the Star Sibyl gazing into the Star Spring.
- **514**: "One great star has vanished..." She must have heard the tale of your wonderful, wonderful victory from the stars.
- **8295**: You've seen that bearer of darkness before!?
- **8296**: And yet you came to confront it! How incredibly, incredibly brave of you!
- **8435**: Heavens Tower has returned to its peaceful state as if nothing had ever happened...
- **8436**: Everyone carries unease in their hearts, though. With the absence of the Star Sibyl, a gloomy, gloomy pall has fallen over us all.
- **8527**: Now that the Star Sibyl is back with us, the ladies-in-waiting can truly, truly smile again.
- **8528**: With the trying events she has been through lately, I don'taru think the Star Sibyl is taking visitors...but for you, she might make a tiny, tiny exception.

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

### Event 65

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   1E F0  FF FF 7F 6F 70 29 08 2E        .....op)..
0060: 20 0F 01 01 1D 02 80 23  1D 03 80 23 29 08 2E 20   ......#...#).. 
0070: 0F 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0056 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x005C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x005D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x01)
  4: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=45*)
    → "Whenever I sneak a peek into the Star Spring, I always, always get this strangey-wangey feeling."
  5: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0068 [0x1D] PRINT_EVENT_MESSAGE(message_id=46*)
    → "It's a feeling like...one day I will become one of those countless, countless stars fleeting and floating in the heavens..."
  7: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x006C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x02)
  9: 0x0073 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0075 [0x21] END_EVENT
 11: 0x0076 [0x00] END_REQSTACK()
```

### Event 131

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
0080: 2E 20 0F 01 01 1D 04 80  23 1D 05 80 23 29 08 2E  . ......#...#)..
0090: 20 0F 01 02 20 00 21 00                            ... .!.        
```

#### Opcodes

```
  0: 0x0077 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x007C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x007D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x007E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x01)
  4: 0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=259*)
    → "The reason that the light of the stars is so dim is because they are so far, far, far away. If you were to get close to them, you would be blinded by their magnificent light."
  5: 0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0089 [0x1D] PRINT_EVENT_MESSAGE(message_id=260*)
    → "I always thought that being surrounded by such a powerful, powerful force, one day she would collapse...but to think that I was actually right! Oh, Star Sibyl! Forgive me!"
  7: 0x008C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x008D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x02)
  9: 0x0094 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0096 [0x21] END_EVENT
 11: 0x0097 [0x00] END_REQSTACK()
```

### Event 145

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
00A0: 08 2E 20 0F 01 01 1D 06  80 23 1D 07 80 23 29 08  .. ......#...#).
00B0: 2E 20 0F 01 02 20 00 21  00                       . ... .!.       
```

#### Opcodes

```
  0: 0x0098 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x009D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x009E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x009F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x01)
  4: 0x00A6 [0x1D] PRINT_EVENT_MESSAGE(message_id=292*)
    → "There was nothing wrong with the talisman in the Horutoto Ruins, was there?"
  5: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=293*)
    → "I shudder-butter at the thought of having to see the chaos that war brings again and again."
  7: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00AE [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x02)
  9: 0x00B5 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00B7 [0x21] END_EVENT
 11: 0x00B8 [0x00] END_REQSTACK()
```

### Event 185

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
00C0: 29 08 2E 20 0F 01 01 1D  08 80 23 1D 09 80 23 29  ).. ......#...#)
00D0: 08 2E 20 0F 01 02 20 00  21 00                    .. ... .!.      
```

#### Opcodes

```
  0: 0x00B9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00BE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00BF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00C0 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x01)
  4: 0x00C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=381*)
    → "Even in this time of despair, the stars in the Star Spring twinkle-winkle softly, softly."
  5: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00CB [0x1D] PRINT_EVENT_MESSAGE(message_id=382*)
    → "From the stars' point of view, our trouble-bubbles and wier-fears must seem as numerous and insignificant as a single blinkle-twinkle of light."
  7: 0x00CE [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00CF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x02)
  9: 0x00D6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00D8 [0x21] END_EVENT
 11: 0x00D9 [0x00] END_REQSTACK()
```

### Event 210

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
00E0: 70 29 08 2E 20 0F 01 01  1D 0A 80 23 1D 0B 80 23  p).. ......#...#
00F0: 29 08 2E 20 0F 01 02 20  00 21 00                 ).. ... .!.     
```

#### Opcodes

```
  0: 0x00DA [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00DF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00E0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00E1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x01)
  4: 0x00E8 [0x1D] PRINT_EVENT_MESSAGE(message_id=466*)
    → "At the last Star Reading, the Star Sibyl foresaw everlasting, lasting peace for Windurst, but I don't know if we can call our current situation peaceful."
  5: 0x00EB [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00EC [0x1D] PRINT_EVENT_MESSAGE(message_id=467*)
    → "Could it be the Star Sibyl was...?"
  7: 0x00EF [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00F0 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x02)
  9: 0x00F7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00F9 [0x21] END_EVENT
 11: 0x00FA [0x00] END_REQSTACK()
```

### Event 231

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
0100: 6F 70 29 08 2E 20 0F 01  01 1D 0C 80 23 1D 0D 80  op).. ......#...
0110: 23 29 08 2E 20 0F 01 02  20 00 21 00              #).. ... .!.    
```

#### Opcodes

```
  0: 0x00FB [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0100 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0101 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0102 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x01)
  4: 0x0109 [0x1D] PRINT_EVENT_MESSAGE(message_id=513*)
    → "This morning, when the sun rose and the evening stars faded slowly, slowly...I saw the Star Sibyl gazing into the Star Spring."
  5: 0x010C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x010D [0x1D] PRINT_EVENT_MESSAGE(message_id=514*)
    → ""One great star has vanished..." She must have heard the tale of your wonderful, wonderful victory from the stars."
  7: 0x0110 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0111 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x02)
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

### Event 345

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
0120: FF 7F 6F 70 29 08 2E 20  0F 01 01 1D 0E 80 23 1D  ..op).. ......#.
0130: 0F 80 23 29 08 2E 20 0F  01 02 20 00 21 00        ..#).. ... .!.  
```

#### Opcodes

```
  0: 0x011D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0122 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0123 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0124 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x01)
  4: 0x012B [0x1D] PRINT_EVENT_MESSAGE(message_id=8295*)
    → "You've seen that bearer of darkness before!?"
  5: 0x012E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x012F [0x1D] PRINT_EVENT_MESSAGE(message_id=8296*)
    → "And yet you came to confront it! How incredibly, incredibly brave of you!"
  7: 0x0132 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0133 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x02)
  9: 0x013A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x013C [0x21] END_EVENT
 11: 0x013D [0x00] END_REQSTACK()
```

### Event 358

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013E   |
| Data Size    | 61 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                            1E F0                ..
0140: FF FF 7F 6F 70 29 08 2E  20 0F 01 01 1D 10 80 23  ...op).. ......#
0150: 29 08 2E 20 0F 01 02 29  08 2E 20 0F 01 03 1D 11  ).. ...).. .....
0160: 80 23 29 08 2E 20 0F 01  04 29 08 2E 20 0F 01 05  .#).. ...).. ...
0170: 29 08 2E 20 0F 01 06 20  00 21 00                 ).. ... .!.     
```

#### Opcodes

```
  0: 0x013E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0143 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0144 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0145 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x01)
  4: 0x014C [0x1D] PRINT_EVENT_MESSAGE(message_id=8435*)
    → "Heavens Tower has returned to its peaceful state as if nothing had ever happened..."
  5: 0x014F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0150 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x02)
  7: 0x0157 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x03)
  8: 0x015E [0x1D] PRINT_EVENT_MESSAGE(message_id=8436*)
    → "Everyone carries unease in their hearts, though. With the absence of the Star Sibyl, a gloomy, gloomy pall has fallen over us all."
  9: 0x0161 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0162 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x04)
 11: 0x0169 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x05)
 12: 0x0170 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x06)
 13: 0x0177 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 14: 0x0179 [0x21] END_EVENT
 15: 0x017A [0x00] END_REQSTACK()
```

### Event 396

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017B   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                   1E F0 FF FF 7F             .....
0180: 6F 70 29 08 2E 20 0F 01  01 1D 12 80 23 1D 13 80  op).. ......#...
0190: 23 29 08 2E 20 0F 01 02  20 00 21 00              #).. ... .!.    
```

#### Opcodes

```
  0: 0x017B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0180 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0181 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0182 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x01)
  4: 0x0189 [0x1D] PRINT_EVENT_MESSAGE(message_id=8527*)
    → "Now that the Star Sibyl is back with us, the ladies-in-waiting can truly, truly smile again."
  5: 0x018C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x018D [0x1D] PRINT_EVENT_MESSAGE(message_id=8528*)
    → "With the trying events she has been through lately, I don'taru think the Star Sibyl is taking visitors...but for you, she might make a tiny, tiny exception."
  7: 0x0190 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0191 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsuryarya (ID: 17768494/0x010F202E), tag_num=0x02)
  9: 0x0198 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x019A [0x21] END_EVENT
 11: 0x019B [0x00] END_REQSTACK()
```
