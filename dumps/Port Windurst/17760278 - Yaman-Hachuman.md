# 17760278 - Yaman-Hachuman

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 356 bytes               |
| Total Events     | 19                      |
| References Count | 15                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [233](#event-233)        | 0x001A       |     19 |             10 |
| [90](#event-90)          | 0x002D       |      1 |              1 |
| [274](#event-274)        | 0x002E       |      1 |              1 |
| [280](#event-280)        | 0x002F       |      1 |              1 |
| [284](#event-284)        | 0x0030       |      1 |              1 |
| [256](#event-256)        | 0x0031       |     19 |             10 |
| [268](#event-268)        | 0x0044       |     19 |             10 |
| [495](#event-495)        | 0x0057       |     19 |             10 |
| [456](#event-456)        | 0x006A       |      1 |              1 |
| [577](#event-577)        | 0x006B       |     19 |             10 |
| [578](#event-578)        | 0x007E       |      1 |              1 |
| [581](#event-581)        | 0x007F       |      1 |              1 |
| [583](#event-583)        | 0x0080       |      1 |              1 |
| [624](#event-624)        | 0x0081       |     22 |             10 |
| [907](#event-907)        | 0x0097       |     26 |              8 |
| [907.1](#event-9071)     | 0x00B1       |     27 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x0E4E      |        3662 |
|       3 | 0x0E4F      |        3663 |
|       4 | 0x0E69      |        3689 |
|       5 | 0x0E6A      |        3690 |
|       6 | 0x0EA3      |        3747 |
|       7 | 0x0EA4      |        3748 |
|       8 | 0x3013      |       12307 |
|       9 | 0x3014      |       12308 |
|      10 | 0x314A      |       12618 |
|      11 | 0x314B      |       12619 |
|      12 | 0x3321      |       13089 |
|      13 | 0x332B      |       13099 |
|      14 | 0x332C      |       13100 |

## String References

- **3662**: There ain't enuff War Warlocks for us to fight a war right now. Afta' all, it's only been twenty -dd years since the last one...
- **3663**: There ain't been enuff time to train skilled people, so we'd be in a right proper fix if a war started all o' a sudden, wouldn't we now?
- **3689**: Warfare is all 'bout doin' a pre-emptive strike. That's why black mages are pivotal to any war.
- **3690**: Yet how'z they to win the battle unless they invest in their wands? The black mages in our War Warlocks need $3.
- **3747**: If that's the minister's policy, there ain't much we can do, is there?
- **3748**: Let 'im flower the Operations Division with resources this time. In large-scale warfare, a superior strategy can turn the status of the battle around one-eighty degrees.
- **12307**: There ain't enuff War Warlocks for us to fight a war right now. Afta' all, it's only been twenty-odd years since the last one...
- **12308**: Even with all this goin' on, they're thinking of throwing every one of us, even the minister, into the Dark Dungeon! If a war does start, what will 'appen, the Goddess only knows...
- **12618**: The research of the great Karaha-Baruha ultimately led to 'is death.
- **12619**: Does that mean the Star Sibyl means to just stand around while Minister Ajido-Marujido offs 'imself?
- **13089**: <Player>'s badge flashes brightly.
- **13099**: Twenty years 'ave passed since the last war, but I wonder if something is stirring elsewhere...
- **13100**: The current generation knows nothing of war, though. Battles in faraway lands may be a mere fantasy to you...

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

### Event 233

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 1D 02 80 23 1D 03 80  23 20 00 21 00           p...#...# .!.   
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=3662*)
    → "There ain't enuff War Warlocks for us to fight a war right now. Afta' all, it's only been twenty -dd years since the last one..."
  4: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=3663*)
    → "There ain't been enuff time to train skilled people, so we'd be in a right proper fix if a war started all o' a sudden, wouldn't we now?"
  6: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0029 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x002B [0x21] END_EVENT
  9: 0x002C [0x00] END_REQSTACK()
```

### Event 90

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         00                     .  
```

#### Opcodes

```
  0: 0x002D [0x00] END_REQSTACK()
```

### Event 274

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            00                   . 
```

#### Opcodes

```
  0: 0x002E [0x00] END_REQSTACK()
```

### Event 280

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               00                 .
```

#### Opcodes

```
  0: 0x002F [0x00] END_REQSTACK()
```

### Event 284

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x00] END_REQSTACK()
```

### Event 256

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    1E F0 FF FF 7F 6F 70  1D 04 80 23 1D 05 80 23   .....op...#...#
0040: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0031 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0036 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0037 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=3689*)
    → "Warfare is all 'bout doin' a pre-emptive strike. That's why black mages are pivotal to any war."
  4: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=3690*)
    → "Yet how'z they to win the battle unless they invest in their wands? The black mages in our War Warlocks need $3."
  6: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0040 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0042 [0x21] END_EVENT
  9: 0x0043 [0x00] END_REQSTACK()
```

### Event 268

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             1E F0 FF FF  7F 6F 70 1D 06 80 23 1D      .....op...#.
0050: 07 80 23 20 00 21 00                              ..# .!.         
```

#### Opcodes

```
  0: 0x0044 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=3747*)
    → "If that's the minister's policy, there ain't much we can do, is there?"
  4: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=3748*)
    → "Let 'im flower the Operations Division with resources this time. In large-scale warfare, a superior strategy can turn the status of the battle around one-eighty degrees."
  6: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0055 [0x21] END_EVENT
  9: 0x0056 [0x00] END_REQSTACK()
```

### Event 495

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      1E  F0 FF FF 7F 6F 70 1D 08         .....op..
0060: 80 23 1D 09 80 23 20 00  21 00                    .#...# .!.      
```

#### Opcodes

```
  0: 0x0057 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x005D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x005E [0x1D] PRINT_EVENT_MESSAGE(message_id=12307*)
    → "There ain't enuff War Warlocks for us to fight a war right now. Afta' all, it's only been twenty-odd years since the last one..."
  4: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0062 [0x1D] PRINT_EVENT_MESSAGE(message_id=12308*)
    → "Even with all this goin' on, they're thinking of throwing every one of us, even the minister, into the Dark Dungeon! If a war does start, what will 'appen, the Goddess only knows..."
  6: 0x0065 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0066 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0068 [0x21] END_EVENT
  9: 0x0069 [0x00] END_REQSTACK()
```

### Event 456

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                00                           .     
```

#### Opcodes

```
  0: 0x006A [0x00] END_REQSTACK()
```

### Event 577

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   1E F0 FF FF 7F             .....
0070: 6F 70 1D 0A 80 23 1D 0B  80 23 20 00 21 00        op...#...# .!.  
```

#### Opcodes

```
  0: 0x006B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0070 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0071 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0072 [0x1D] PRINT_EVENT_MESSAGE(message_id=12618*)
    → "The research of the great Karaha-Baruha ultimately led to 'is death."
  4: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0076 [0x1D] PRINT_EVENT_MESSAGE(message_id=12619*)
    → "Does that mean the Star Sibyl means to just stand around while Minister Ajido-Marujido offs 'imself?"
  6: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x007A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x007C [0x21] END_EVENT
  9: 0x007D [0x00] END_REQSTACK()
```

### Event 578

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            00                   . 
```

#### Opcodes

```
  0: 0x007E [0x00] END_REQSTACK()
```

### Event 581

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               00                 .
```

#### Opcodes

```
  0: 0x007F [0x00] END_REQSTACK()
```

### Event 583

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0080  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0080 [0x00] END_REQSTACK()
```

### Event 624

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 22 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    42 48 0C 80 1E F0 FF  FF 7F 1C 01 80 1D 0D 80   BH.............
0090: 23 1D 0E 80 23 21 00                              #...#!.         
```

#### Opcodes

```
  0: 0x0081 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0082 [0x48] [System] [13089*]:
    → "<Player>'s badge flashes brightly."
  2: 0x0085 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x008A [0x1C] WAIT(30* ticks)
  4: 0x008D [0x1D] PRINT_EVENT_MESSAGE(message_id=13099*)
    → "Twenty years 'ave passed since the last war, but I wonder if something is stirring elsewhere..."
  5: 0x0090 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0091 [0x1D] PRINT_EVENT_MESSAGE(message_id=13100*)
    → "The current generation knows nothing of war, though. Battles in faraway lands may be a mere fantasy to you..."
  7: 0x0094 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0095 [0x21] END_EVENT
  9: 0x0096 [0x00] END_REQSTACK()
```

### Event 907

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      4A  F8 FF FF 7F F0 FF FF 7F         J........
00A0: 4A F0 FF FF 7F F8 FF FF  7F 6F 70 1D 05 10 23 21  J........op...#!
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x0097 [0x4A] EventEntity looks at LocalPlayer
  1: 0x00A0 [0x4A] LocalPlayer looks at EventEntity
  2: 0x00A9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00AA [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00AB [0x1D] PRINT_EVENT_MESSAGE(message_id=Work_Zone[5])
  5: 0x00AE [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00AF [0x21] END_EVENT
  7: 0x00B0 [0x00] END_REQSTACK()
```

### Event 907.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    42 4A F8 FF FF 7F F0  FF FF 7F 4A F0 FF FF 7F   BJ........J....
00C0: F8 FF FF 7F 6F 70 1D 05  10 23 21 00              ....op...#!.    
```

#### Opcodes

```
  0: 0x00B1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00B2 [0x4A] EventEntity looks at LocalPlayer
  2: 0x00BB [0x4A] LocalPlayer looks at EventEntity
  3: 0x00C4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00C5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x00C6 [0x1D] PRINT_EVENT_MESSAGE(message_id=Work_Zone[5])
  6: 0x00C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00CA [0x21] END_EVENT
  8: 0x00CB [0x00] END_REQSTACK()
```
