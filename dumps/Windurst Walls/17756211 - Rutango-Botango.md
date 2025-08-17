# 17756211 - Rutango-Botango

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 388 bytes                |
| Total Events     | 15                       |
| References Count | 21                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      6 |              2 |
| [443](#event-443)        | 0x0017       |      1 |              1 |
| [65535.3](#event-655353) | 0x0018       |     14 |              4 |
| [65535.4](#event-655354) | 0x0026       |     10 |              2 |
| [65535.5](#event-655355) | 0x0030       |     14 |              4 |
| [297](#event-297)        | 0x003E       |     33 |             12 |
| [64](#event-64)          | 0x005F       |      1 |              1 |
| [65](#event-65)          | 0x0060       |     29 |             10 |
| [71](#event-71)          | 0x007D       |     29 |             10 |
| [75](#event-75)          | 0x009A       |      1 |              1 |
| [65535.6](#event-655356) | 0x009B       |     19 |              5 |
| [65535.7](#event-655357) | 0x00AE       |     19 |              5 |
| [76](#event-76)          | 0x00C1       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0055      |          85 |
|       1 | 0x0015      |          21 |
|       2 | 0xFFFF0561  |  4294903137 |
|       3 | 0x1C691     |      116369 |
|       4 | 0xFFFFD65C  |  4294956636 |
|       5 | 0xFFFEC732  |  4294887218 |
|       6 | 0x1B18C     |      110988 |
|       7 | 0xFFFFDA59  |  4294957657 |
|       8 | 0x0A7F      |        2687 |
|       9 | 0x0007      |           7 |
|      10 | 0xFFFEB830  |  4294883376 |
|      11 | 0x1CB47     |      117575 |
|      12 | 0xFFFFE511  |  4294960401 |
|      13 | 0x1ED7      |        7895 |
|      14 | 0x1ED8      |        7896 |
|      15 | 0x1C4F      |        7247 |
|      16 | 0x1C55      |        7253 |
|      17 | 0x1C5B      |        7259 |
|      18 | 0x1C60      |        7264 |
|      19 | 0x1C61      |        7265 |
|      20 | 0x1C62      |        7266 |

## String References

- **7247**: Oh, crumbs! The great, old teacher has lost his voice before he could deliver his famous public speech!
- **7253**: Mister speaker! Please lap up as much of that honey as you can so it fixes your throat up! Then you can tell us more about the great summoner!
- **7259**: Maybe...? Maybe his throat is completely cured!? Wow. Now, can you continue with your stories, sir?
- **7264**: Hurts...?
- **7265**: Oh, great teacher! Allow me to speak for you. I've memorized every word you've said...
- **7266**: That we can now leave here in pieces...under the messed shadow of the Grated Star Tree...easel tanks to the great zero, Kalhua-Milkhua...!
- **7895**: The great summoner Karaha-Baruha is the savior of Windurst. Just when we were completely surrounded by beastmen and faced certain doom, BAM!, he instantaneously blew them all away.
- **7896**: If it weren't for him, we Windurstians would have all been goners! A summoner is really someone, huh?

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 00                               ^idl0.         
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      00                                  .        
```

#### Opcodes

```
  0: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          32 01 80 1F 00 02 80 03          2.......
0020: 80 04 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0018 [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=-64.159*, Z=116.369*, Y=-10.660*
  2: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   37 05  80 06 80 07 80 08 80 00        7.........
```

#### Opcodes

```
  0: 0x0026 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-80.078*, z=110.988*, y=-9.639*, direction=236.2°*
  1: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 32 09 80 1F 00 0A 80 0B  80 0C 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0030 [0x32] ExtData[1]->MainSpeed = 7* * 0.1
  1: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=-83.920*, Z=117.575*, Y=-6.895*
  2: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003D [0x00] END_REQSTACK()
```

### Event 297

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            1E F0                ..
0040: FF FF 7F 6F 70 29 0B 33  F0 0E 01 01 1D 0D 80 23  ...op).3.......#
0050: 1D 0E 80 23 29 0B 33 F0  0E 01 02 20 00 21 00     ...#).3.... .!. 
```

#### Opcodes

```
  0: 0x003E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0043 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0044 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0045 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x01)
  4: 0x004C [0x1D] PRINT_EVENT_MESSAGE(message_id=7895*)
    → "The great summoner Karaha-Baruha is the savior of Windurst. Just when we were completely surrounded by beastmen and faced certain doom, BAM!, he instantaneously blew them all away."
  5: 0x004F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=7896*)
    → "If it weren't for him, we Windurstians would have all been goners! A summoner is really someone, huh?"
  7: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0054 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x02)
  9: 0x005B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x005D [0x21] END_EVENT
 11: 0x005E [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               00                 .
```

#### Opcodes

```
  0: 0x005F [0x00] END_REQSTACK()
```

### Event 65

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 1E F0 FF FF 7F 6F 70 29  0B 33 F0 0E 01 01 1D 0F  .....op).3......
0070: 80 23 29 0B 33 F0 0E 01  02 20 00 21 00           .#).3.... .!.   
```

#### Opcodes

```
  0: 0x0060 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0065 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0066 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0067 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x01)
  4: 0x006E [0x1D] PRINT_EVENT_MESSAGE(message_id=7247*)
    → "Oh, crumbs! The great, old teacher has lost his voice before he could deliver his famous public speech!"
  5: 0x0071 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0072 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x02)
  7: 0x0079 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x007B [0x21] END_EVENT
  9: 0x007C [0x00] END_REQSTACK()
```

### Event 71

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         1E F0 FF               ...
0080: FF 7F 6F 70 29 0B 33 F0  0E 01 01 1D 10 80 23 29  ..op).3.......#)
0090: 0B 33 F0 0E 01 02 20 00  21 00                    .3.... .!.      
```

#### Opcodes

```
  0: 0x007D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0082 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0083 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0084 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x01)
  4: 0x008B [0x1D] PRINT_EVENT_MESSAGE(message_id=7253*)
    → "Mister speaker! Please lap up as much of that honey as you can so it fixes your throat up! Then you can tell us more about the great summoner!"
  5: 0x008E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x02)
  7: 0x0096 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0098 [0x21] END_EVENT
  9: 0x0099 [0x00] END_REQSTACK()
```

### Event 75

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                00                           .     
```

#### Opcodes

```
  0: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   29 0B 33 F0 0E             ).3..
00A0: 01 01 1D 11 80 23 29 0B  33 F0 0E 01 02 00        .....#).3.....  
```

#### Opcodes

```
  0: 0x009B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x01)
  1: 0x00A2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7259*)
    → "Maybe...? Maybe his throat is completely cured!? Wow. Now, can you continue with your stories, sir?"
  2: 0x00A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00A6 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x02)
  4: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            29 0B                ).
00B0: 33 F0 0E 01 01 1D 12 80  23 29 0B 33 F0 0E 01 02  3.......#).3....
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00AE [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x01)
  1: 0x00B5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7264*)
    → "Hurts...?"
  2: 0x00B8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B9 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x02)
  4: 0x00C0 [0x00] END_REQSTACK()
```

### Event 76

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C1   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    29 0B 33 F0 0E 01 01  1D 13 80 23 1E F0 FF FF   ).3.......#....
00D0: 7F 6F 70 1D 14 80 23 29  0B 33 F0 0E 01 02 20 00  .op...#).3.... .
00E0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00C1 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x01)
  1: 0x00C8 [0x1D] PRINT_EVENT_MESSAGE(message_id=7265*)
    → "Oh, great teacher! Allow me to speak for you. I've memorized every word you've said..."
  2: 0x00CB [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00CC [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00D1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00D2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x00D3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7266*)
    → "That we can now leave here in pieces...under the messed shadow of the Grated Star Tree...easel tanks to the great zero, Kalhua-Milkhua...!"
  7: 0x00D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00D7 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x02)
  9: 0x00DE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00E0 [0x21] END_EVENT
 11: 0x00E1 [0x00] END_REQSTACK()
```
