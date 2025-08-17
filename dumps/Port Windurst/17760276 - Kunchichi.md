# 17760276 - Kunchichi

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 456 bytes               |
| Total Events     | 18                      |
| References Count | 17                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     29 |              4 |
| [65535.2](#event-655352) | 0x001E       |     10 |              3 |
| [228](#event-228)        | 0x0028       |     33 |             12 |
| [90](#event-90)          | 0x0049       |      1 |              1 |
| [274](#event-274)        | 0x004A       |      1 |              1 |
| [280](#event-280)        | 0x004B       |      1 |              1 |
| [284](#event-284)        | 0x004C       |      1 |              1 |
| [262](#event-262)        | 0x004D       |     33 |             12 |
| [265](#event-265)        | 0x006E       |      8 |              2 |
| [271](#event-271)        | 0x0076       |     33 |             12 |
| [492](#event-492)        | 0x0097       |     33 |             12 |
| [456](#event-456)        | 0x00B8       |      1 |              1 |
| [574](#event-574)        | 0x00B9       |     33 |             12 |
| [578](#event-578)        | 0x00DA       |      1 |              1 |
| [581](#event-581)        | 0x00DB       |      1 |              1 |
| [583](#event-583)        | 0x00DC       |      1 |              1 |
| [623](#event-623)        | 0x00DD       |     77 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0BDC      |        3036 |
|       1 | 0x0E44      |        3652 |
|       2 | 0x0E45      |        3653 |
|       3 | 0x0E7B      |        3707 |
|       4 | 0x0E7C      |        3708 |
|       5 | 0x0EA9      |        3753 |
|       6 | 0x0EAA      |        3754 |
|       7 | 0x300D      |       12301 |
|       8 | 0x300E      |       12302 |
|       9 | 0x3143      |       12611 |
|      10 | 0x3144      |       12612 |
|      11 | 0x3321      |       13089 |
|      12 | 0x001E      |          30 |
|      13 | 0x3327      |       13095 |
|      14 | 0x3328      |       13096 |
|      15 | 0x3329      |       13097 |
|      16 | 0x332A      |       13098 |

## String References

- **3652**: This is hopeless-a-wopeless! It's just the same old wow-kapow and kaboom-a-boom-boom on the same old dummy Cardian target, over and over, day in and day out...
- **3653**: It doesn't matter how fantastic-a-wastic the magic is! If I can only use it in here, then it is no more than a boring old fireworks display-a-way. Oh, how I want to try my spells out on real monsters!
- **3707**: Make sure you get us one of those wands the red mage's brigadier general wants!
- **3708**: If the red mage regiment gets more wands, then maybe, just maybe-a-waybe, I'll get a better hand-me-down wand!
- **3753**: Doc Shantotto's one scary-a-wary granny!
- **3754**: Quite a number of my predecessors have whamming-a-bamming fallen victim to her screwball acts.
- **12301**: We've practiced-a-wacticed our fingers to the bone on this high-level magic... It seems the day has finally come where we can put it to the testaru!
- **12302**: Naturally, we Orastery mages are going to break the minister outaru of the Dark Dungeon. The Orastery is invince-a-bubble!
- **12611**: Have you seen Minister Ajido-Marujido around? As usual, he's nowhere to be found in the Orastery.
- **12612**: I was hoping to try out the next level of destructo-dealing dweomers sometime soon, but I'm not sure if I'm ready. I need to ask the minister's opinion.
- **13089**: <Player>'s badge flashes brightly.
- **13095**: Hey, isn't that a mercenary badge? It has magical powers, right? Must be nice!
- **13096**: Mojo-Pojo's badge flashes brightly.

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
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5F 01 50 F8 FF FF 7F  F8 FF FF 7F 63 61 62 6B   _.P........cabk
0010: 50 F8 FF FF 7F F8 FF FF  7F 73 68 62 6B 00        P........shbk.  
```

#### Opcodes

```
  0: 0x0001 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x01 - Toggle Render.Flags0 bit 29)
  1: 0x0003 [0x50] END_SCHEDULER_TASK: End scheduler "ca" with entities [0xFFF8, 0xFFF8], work=[32767, 32767]
  2: 0x0010 [0x50] END_SCHEDULER_TASK: End scheduler "sh" with entities [0xFFF8, 0xFFF8], work=[32767, 32767]
  3: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 10 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            5F 00                _.
0020: 4B 14 00 0F 01 00 80 00                           K.......        
```

#### Opcodes

```
  0: 0x001E [0x5F] MULTI_HANDLER_COMPLEX(mode=0x00 - Toggle Render.Flags0 bit 29)
  1: 0x0020 [0x4B] UPDATE_ENTITY_YAW(entity=Kunchichi (ID: 17760276/0x010F0014), yaw=16.7°*)
  2: 0x0027 [0x00] END_REQSTACK()
```

### Event 228

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          29 08 14 00 0F 01 01 1E          ).......
0030: F0 FF FF 7F 6F 70 1D 01  80 23 1D 02 80 23 29 08  ....op...#...#).
0040: 14 00 0F 01 02 20 00 21  00                       ..... .!.       
```

#### Opcodes

```
  0: 0x0028 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x01)
  1: 0x002F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0034 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0035 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0036 [0x1D] PRINT_EVENT_MESSAGE(message_id=3652*)
    → "This is hopeless-a-wopeless! It's just the same old wow-kapow and kaboom-a-boom-boom on the same old dummy Cardian target, over and over, day in and day out..."
  5: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003A [0x1D] PRINT_EVENT_MESSAGE(message_id=3653*)
    → "It doesn't matter how fantastic-a-wastic the magic is! If I can only use it in here, then it is no more than a boring old fireworks display-a-way. Oh, how I want to try my spells out on real monsters!"
  7: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x003E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x02)
  9: 0x0045 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0047 [0x21] END_EVENT
 11: 0x0048 [0x00] END_REQSTACK()
```

### Event 90

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0049  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             00                             .      
```

#### Opcodes

```
  0: 0x0049 [0x00] END_REQSTACK()
```

### Event 274

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                00                           .     
```

#### Opcodes

```
  0: 0x004A [0x00] END_REQSTACK()
```

### Event 280

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   00                         .    
```

#### Opcodes

```
  0: 0x004B [0x00] END_REQSTACK()
```

### Event 284

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      00                       .   
```

#### Opcodes

```
  0: 0x004C [0x00] END_REQSTACK()
```

### Event 262

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         29 08 14               )..
0050: 00 0F 01 01 1E F0 FF FF  7F 6F 70 1D 03 80 23 1D  .........op...#.
0060: 04 80 23 29 08 14 00 0F  01 02 20 00 21 00        ..#)...... .!.  
```

#### Opcodes

```
  0: 0x004D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x01)
  1: 0x0054 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0059 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x005A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x005B [0x1D] PRINT_EVENT_MESSAGE(message_id=3707*)
    → "Make sure you get us one of those wands the red mage's brigadier general wants!"
  5: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=3708*)
    → "If the red mage regiment gets more wands, then maybe, just maybe-a-waybe, I'll get a better hand-me-down wand!"
  7: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0063 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x02)
  9: 0x006A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x006C [0x21] END_EVENT
 11: 0x006D [0x00] END_REQSTACK()
```

### Event 265

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006E  |
| Data Size    | 8 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            29 08                ).
0070: 14 00 0F 01 01 00                                 ......          
```

#### Opcodes

```
  0: 0x006E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x01)
  1: 0x0075 [0x00] END_REQSTACK()
```

### Event 271

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   29 08  14 00 0F 01 01 1E F0 FF        ).........
0080: FF 7F 6F 70 1D 05 80 23  1D 06 80 23 29 08 14 00  ..op...#...#)...
0090: 0F 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0076 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x01)
  1: 0x007D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0082 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0083 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=3753*)
    → "Doc Shantotto's one scary-a-wary granny!"
  5: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=3754*)
    → "Quite a number of my predecessors have whamming-a-bamming fallen victim to her screwball acts."
  7: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x008C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x02)
  9: 0x0093 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0095 [0x21] END_EVENT
 11: 0x0096 [0x00] END_REQSTACK()
```

### Event 492

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      29  08 14 00 0F 01 01 1E F0         )........
00A0: FF FF 7F 6F 70 1D 07 80  23 1D 08 80 23 29 08 14  ...op...#...#)..
00B0: 00 0F 01 02 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0097 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x01)
  1: 0x009E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00A3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00A4 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=12301*)
    → "We've practiced-a-wacticed our fingers to the bone on this high-level magic... It seems the day has finally come where we can put it to the testaru!"
  5: 0x00A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A9 [0x1D] PRINT_EVENT_MESSAGE(message_id=12302*)
    → "Naturally, we Orastery mages are going to break the minister outaru of the Dark Dungeon. The Orastery is invince-a-bubble!"
  7: 0x00AC [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00AD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x02)
  9: 0x00B4 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00B6 [0x21] END_EVENT
 11: 0x00B7 [0x00] END_REQSTACK()
```

### Event 456

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          00                               .       
```

#### Opcodes

```
  0: 0x00B8 [0x00] END_REQSTACK()
```

### Event 574

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             29 08 14 00 0F 01 01           )......
00C0: 1E F0 FF FF 7F 6F 70 1D  09 80 23 1D 0A 80 23 29  .....op...#...#)
00D0: 08 14 00 0F 01 02 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x00B9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x01)
  1: 0x00C0 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00C5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00C6 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=12611*)
    → "Have you seen Minister Ajido-Marujido around? As usual, he's nowhere to be found in the Orastery."
  5: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00CB [0x1D] PRINT_EVENT_MESSAGE(message_id=12612*)
    → "I was hoping to try out the next level of destructo-dealing dweomers sometime soon, but I'm not sure if I'm ready. I need to ask the minister's opinion."
  7: 0x00CE [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00CF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x02)
  9: 0x00D6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00D8 [0x21] END_EVENT
 11: 0x00D9 [0x00] END_REQSTACK()
```

### Event 578

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DA  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                00                           .     
```

#### Opcodes

```
  0: 0x00DA [0x00] END_REQSTACK()
```

### Event 581

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DB  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   00                         .    
```

#### Opcodes

```
  0: 0x00DB [0x00] END_REQSTACK()
```

### Event 583

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      00                       .   
```

#### Opcodes

```
  0: 0x00DC [0x00] END_REQSTACK()
```

### Event 623

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 77 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         42 29 08               B).
00E0: 14 00 0F 01 01 48 0B 80  1E F0 FF FF 7F 1C 0C 80  .....H..........
00F0: 1D 0D 80 23 48 0E 80 29  08 15 00 0F 01 01 4A 15  ...#H..)......J.
0100: 00 0F 01 F0 FF FF 7F 1C  0C 80 2B 15 00 0F 01 0F  ..........+.....
0110: 80 23 2B 15 00 0F 01 10  80 23 29 08 14 00 0F 01  .#+......#).....
0120: 02 29 08 15 00 0F 01 02  21 00                    .)......!.      
```

#### Opcodes

```
  0: 0x00DD [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00DE [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x01)
  2: 0x00E5 [0x48] [System] [13089*]:
    → "<Player>'s badge flashes brightly."
  3: 0x00E8 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00ED [0x1C] WAIT(30* ticks)
  5: 0x00F0 [0x1D] PRINT_EVENT_MESSAGE(message_id=13095*)
    → "Hey, isn't that a mercenary badge? It has magical powers, right? Must be nice!"
  6: 0x00F3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00F4 [0x48] [System] [13096*]:
    → "Mojo-Pojo's badge flashes brightly."
  8: 0x00F7 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mojo-Pojo (ID: 17760277/0x010F0015), tag_num=0x01)
  9: 0x00FE [0x4A] Mojo-Pojo (ID: 17760277/0x010F0015) looks at LocalPlayer
 10: 0x0107 [0x1C] WAIT(30* ticks)
 11: 0x010A [0x2B] Mojo-Pojo (ID: 17760277/0x010F0015) [13097*]:
    → "I, I, I wish I could go to the Near East as a m-m-mercenary..."
 12: 0x0111 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0112 [0x2B] Mojo-Pojo (ID: 17760277/0x010F0015) [13098*]:
    → "Maybe I could hit it b-b-big there, just like Karaha-Baruha..."
 14: 0x0119 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x011A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kunchichi (ID: 17760276/0x010F0014), tag_num=0x02)
 16: 0x0121 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mojo-Pojo (ID: 17760277/0x010F0015), tag_num=0x02)
 17: 0x0128 [0x21] END_EVENT
 18: 0x0129 [0x00] END_REQSTACK()
```
