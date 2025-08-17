# 17179394 - Doron-Fulun

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 280 bytes                         |
| Total Events     | 13                                |
| References Count | 15                                |

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
| [109](#event-109)          | 0x0044       |      1 |              1 |
| [110](#event-110)          | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     28 |              7 |
| [65535.9](#event-655359)   | 0x0062       |     42 |              9 |
| [65535.10](#event-6553510) | 0x008C       |     12 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x002D      |          45 |
|       4 | 0x0026      |          38 |
|       5 | 0x1B3DF     |      111583 |
|       6 | 0xFFFC069E  |  4294706846 |
|       7 | 0xFFFFE0B1  |  4294959281 |
|       8 | 0x0028      |          40 |
|       9 | 0x107EF     |       67567 |
|      10 | 0xFFFD966F  |  4294809199 |
|      11 | 0x16A3      |        5795 |
|      12 | 0x51FE2     |      335842 |
|      13 | 0xFFFD2DA3  |  4294782371 |
|      14 | 0x24DC      |        9436 |

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

### Event 109

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

### Event 110

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
| Data Size    | 28 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   1C 03  80 79 00 F8 FF FF 7F 01        ...y......
0050: 23 06 01 32 04 80 1F 00  05 80 06 80 07 80 1F 01  #..2............
0060: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0046 [0x1C] WAIT(45* ticks)
  1: 0x0049 [0x79] EventEntity looks at Shantotto (ID: 17179393/0x01062301) (Basic look)
  2: 0x0053 [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  3: 0x0056 [0x1F] MOVE_ENTITY: EventEntity moves to X=111.583*, Z=-260.450*, Y=-8.015*
  4: 0x005E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0060 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 42 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       79 00 F8 FF FF 7F  01 23 06 01 32 08 80 1F    y......#..2...
0070: 00 09 80 0A 80 0B 80 1F  01 6F 1E 14 23 06 01 6E  .........o..#..n
0080: F8 FF FF 7F 00 80 99 F8  FF FF 7F 00              ............    
```

#### Opcodes

```
  0: 0x0062 [0x79] EventEntity looks at Shantotto (ID: 17179393/0x01062301) (Basic look)
  1: 0x006C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x006F [0x1F] MOVE_ENTITY: EventEntity moves to X=67.567*, Z=-158.097*, Y=5.795*
  3: 0x0077 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0079 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x007A [0x1E] EventEntity looks at gian04 (ID: 17179412/0x01062314) and starts talking
  6: 0x007F [0x6E] EventEntity uses emote 0*
  7: 0x0086 [0x99] Wait for EventEntity animation to complete
  8: 0x008B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      1F 00 0C 80              ....
0090: 0D 80 0E 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x008C [0x1F] MOVE_ENTITY: EventEntity moves to X=335.842*, Z=-184.925*, Y=9.436*
  1: 0x0094 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0096 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0097 [0x00] END_REQSTACK()
```
