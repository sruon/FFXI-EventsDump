# 17756194 - Luuh Koplehn

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 288 bytes                |
| Total Events     | 10                       |
| References Count | 14                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     22 |              3 |
| [65535.2](#event-655352) | 0x0017       |     28 |              5 |
| [65535.3](#event-655353) | 0x0033       |      9 |              3 |
| [443](#event-443)        | 0x003C       |      7 |              2 |
| [65535.4](#event-655354) | 0x0043       |     14 |              4 |
| [322](#event-322)        | 0x0051       |     22 |              7 |
| [11](#event-11)          | 0x0067       |     10 |              2 |
| [200](#event-200)        | 0x0071       |     33 |             12 |
| [219](#event-219)        | 0x0092       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x016F      |         367 |
|       1 | 0x001E      |          30 |
|       2 | 0x000D      |          13 |
|       3 | 0xFFFEA45E  |  4294878302 |
|       4 | 0x1EDA5     |      126373 |
|       5 | 0xFFFFEB23  |  4294961955 |
|       6 | 0x1F03      |        7939 |
|       7 | 0x9321      |       37665 |
|       8 | 0xFFFF1A06  |  4294908422 |
|       9 | 0xFFFFF63C  |  4294964796 |
|      10 | 0x0BC3      |        3011 |
|      11 | 0x1D7B      |        7547 |
|      12 | 0x1D7C      |        7548 |
|      13 | 0x1DA4      |        7588 |

## String References

- **7547**: A rough black stone? Yeah, the professorrr who lives in this manorrr once tried to give me one of those in lieu of his debts.
- **7548**: Grrrowl! Just remembering it rubs my furrr the wrong way! The old fool claims those strange stones are really starrrs that fell from the sky or some such nonsense.
- **7588**: Shells? What are you asking me about shells forrr? Go to the porrrt and ask the people on the fishing boats or the memberrrs of the Fishermen's Guild if you want to know about seafood!
- **7939**: Come on, Professorrr Koru-Moru. I'm not moving until you cough up the gil forrr yourrr overdue accounts at the Boneworkers' Guild. As both a ministerrr and the principal of our local school, shouldn't you be setting a betterrr example?

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
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    81 00 F8 FF FF 7F 5B  00 80 F8 FF FF 7F F8 FF   ......[........
0010: FF 7F 74 6C 6B 30 00                              ..tlk0.         
```

#### Opcodes

```
  0: 0x0001 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0007 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=367*
  2: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 28 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0020: 74 6C 6B 30 5E 69 64 6C  30 1C 01 80 81 01 F8 FF  tlk0^idl0.......
0030: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x0017 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0024 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0029 [0x1C] WAIT(30* ticks)
  3: 0x002C [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  4: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0033  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          5E 69 64 6C 30  1C 01 80 00                 ^idl0....    
```

#### Opcodes

```
  0: 0x0033 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0038 [0x1C] WAIT(30* ticks)
  2: 0x003B [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      92 01 F8 FF              ....
0040: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x003C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          32 02 80 1F 00  03 80 04 80 05 80 1F 01     2............
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0043 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=-88.994*, Z=126.373*, Y=-5.341*
  2: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0050 [0x00] END_REQSTACK()
```

### Event 322

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 22 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    29 08 22 F0 0E 01 01  1D 06 80 23 29 08 22 F0   ).".......#).".
0060: 0E 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0051 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Luuh Koplehn (ID: 17756194/0x010EF022), tag_num=0x01)
  1: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=7939*)
    → "Come on, Professorrr Koru-Moru. I'm not moving until you cough up the gil forrr yourrr overdue accounts at the Boneworkers' Guild. As both a ministerrr and the principal of our local school, shouldn't you be setting a betterrr example?"
  2: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x005C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Luuh Koplehn (ID: 17756194/0x010EF022), tag_num=0x02)
  4: 0x0063 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  5: 0x0065 [0x21] END_EVENT
  6: 0x0066 [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      37  07 80 08 80 09 80 0A 80         7........
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0067 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=37.665*, z=-58.874*, y=-2.500*, direction=264.6°*
  1: 0x0070 [0x00] END_REQSTACK()
```

### Event 200

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    1E F0 FF FF 7F 6F 70  29 08 22 F0 0E 01 01 1D   .....op).".....
0080: 0B 80 23 1D 0C 80 23 29  08 22 F0 0E 01 02 20 00  ..#...#).".... .
0090: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0071 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0076 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0077 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0078 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Luuh Koplehn (ID: 17756194/0x010EF022), tag_num=0x01)
  4: 0x007F [0x1D] PRINT_EVENT_MESSAGE(message_id=7547*)
    → "A rough black stone? Yeah, the professorrr who lives in this manorrr once tried to give me one of those in lieu of his debts."
  5: 0x0082 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0083 [0x1D] PRINT_EVENT_MESSAGE(message_id=7548*)
    → "Grrrowl! Just remembering it rubs my furrr the wrong way! The old fool claims those strange stones are really starrrs that fell from the sky or some such nonsense."
  7: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0087 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Luuh Koplehn (ID: 17756194/0x010EF022), tag_num=0x02)
  9: 0x008E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0090 [0x21] END_EVENT
 11: 0x0091 [0x00] END_REQSTACK()
```

### Event 219

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       1E F0 FF FF 7F 6F  70 29 08 22 F0 0E 01 01    .....op)."....
00A0: 1D 0D 80 23 29 08 22 F0  0E 01 02 20 00 21 00     ...#).".... .!. 
```

#### Opcodes

```
  0: 0x0092 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0097 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0098 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0099 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Luuh Koplehn (ID: 17756194/0x010EF022), tag_num=0x01)
  4: 0x00A0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7588*)
    → "Shells? What are you asking me about shells forrr? Go to the porrrt and ask the people on the fishing boats or the memberrrs of the Fishermen's Guild if you want to know about seafood!"
  5: 0x00A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Luuh Koplehn (ID: 17756194/0x010EF022), tag_num=0x02)
  7: 0x00AB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00AD [0x21] END_EVENT
  9: 0x00AE [0x00] END_REQSTACK()
```
