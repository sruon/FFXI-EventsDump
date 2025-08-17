# 17179377 - Machudiaux

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 340 bytes                         |
| Total Events     | 13                                |
| References Count | 24                                |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [3](#event-3)              | 0x0044       |      1 |              1 |
| [4](#event-4)              | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     15 |              5 |
| [65535.9](#event-655359)   | 0x0055       |     37 |              9 |
| [65535.10](#event-6553510) | 0x007A       |     51 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0050      |          80 |
|       4 | 0xFFF9EBAF  |  4294568879 |
|       5 | 0x4188A     |      268426 |
|       6 | 0x0178      |         376 |
|       7 | 0xFFF9E0B9  |  4294566073 |
|       8 | 0x3ECBC     |      257212 |
|       9 | 0x035C      |         860 |
|      10 | 0x0DFB      |        3579 |
|      11 | 0xFFF9D696  |  4294563478 |
|      12 | 0x3C925     |      248101 |
|      13 | 0x00CB      |         203 |
|      14 | 0x001B      |          27 |
|      15 | 0xFFF9D2A6  |  4294562470 |
|      16 | 0x3B9C4     |      244164 |
|      17 | 0x0019      |          25 |
|      18 | 0x00B4      |         180 |
|      19 | 0x0028      |          40 |
|      20 | 0xFFFA24D5  |  4294583509 |
|      21 | 0x43249     |      275017 |
|      22 | 0x02F8      |         760 |
|      23 | 0x001E      |          30 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   32 03  80 1F 00 04 80 05 80 06        2.........
0050: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=-398.417*, Z=268.426*, Y=0.376*
  2: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                37 07 80  08 80 09 80 0A 80 1C 01       7..........
0060: 80 1F 00 0B 80 0C 80 0D  80 1F 01 32 0E 80 1F 00  ...........2....
0070: 0F 80 10 80 11 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0055 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-401.223*, z=257.212*, y=0.860*, direction=314.6°*
  1: 0x005E [0x1C] WAIT(1* ticks)
  2: 0x0061 [0x1F] MOVE_ENTITY: EventEntity moves to X=-403.818*, Z=248.101*, Y=0.203*
  3: 0x0069 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x006B [0x32] ExtData[1]->MainSpeed = 27* * 0.1
  5: 0x006E [0x1F] MOVE_ENTITY: EventEntity moves to X=-404.826*, Z=244.164*, Y=0.025*
  6: 0x0076 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0078 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 51 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                1E F3 22 06 01 6F            .."..o
0080: 70 6E F8 FF FF 7F 11 80  99 F8 FF FF 7F 99 F8 FF  pn..............
0090: FF 7F 1C 12 80 32 13 80  1F 00 14 80 15 80 16 80  .....2..........
00A0: 1F 01 6F 6C F8 FF FF 7F  00 80 17 80 00           ..ol.........   
```

#### Opcodes

```
  0: 0x007A [0x1E] EventEntity looks at Nalkuku (ID: 17179379/0x010622F3) and starts talking
  1: 0x007F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0080 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0081 [0x6E] EventEntity uses emote 25*
  4: 0x0088 [0x99] Wait for EventEntity animation to complete
  5: 0x008D [0x99] Wait for EventEntity animation to complete
  6: 0x0092 [0x1C] WAIT(180* ticks)
  7: 0x0095 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  8: 0x0098 [0x1F] MOVE_ENTITY: EventEntity moves to X=-383.787*, Z=275.017*, Y=0.760*
  9: 0x00A0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 10: 0x00A2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x00A3 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=30*)
 12: 0x00AC [0x00] END_REQSTACK()
```
