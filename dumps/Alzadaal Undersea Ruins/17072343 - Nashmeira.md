# 17072343 - Nashmeira

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Alzadaal Undersea Ruins (ID: 72) |
| Block Size       | 592 bytes                        |
| Total Events     | 29                               |
| References Count | 27                               |

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
| [8](#event-8)              | 0x0044       |      1 |              1 |
| [10](#event-10)            | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     15 |              5 |
| [65535.9](#event-655359)   | 0x0055       |     15 |              5 |
| [9](#event-9)              | 0x0064       |      1 |              1 |
| [306](#event-306)          | 0x0065       |      1 |              1 |
| [307](#event-307)          | 0x0066       |      1 |              1 |
| [308](#event-308)          | 0x0067       |      1 |              1 |
| [309](#event-309)          | 0x0068       |      1 |              1 |
| [65535.10](#event-6553510) | 0x0069       |     15 |              5 |
| [65535.11](#event-6553511) | 0x0078       |      4 |              2 |
| [65535.12](#event-6553512) | 0x007C       |      4 |              2 |
| [124](#event-124)          | 0x0080       |      1 |              1 |
| [125](#event-125)          | 0x0081       |      1 |              1 |
| [65535.13](#event-6553513) | 0x0082       |     29 |              4 |
| [65535.14](#event-6553514) | 0x009F       |     29 |              4 |
| [65535.15](#event-6553515) | 0x00BC       |     22 |              6 |
| [65535.16](#event-6553516) | 0x00D2       |     22 |              6 |
| [65535.17](#event-6553517) | 0x00E8       |     48 |             10 |
| [65535.18](#event-6553518) | 0x0118       |     22 |              6 |
| [65535.19](#event-6553519) | 0x012E       |     48 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0028      |          40 |
|       4 | 0xFFF8C286  |  4294492806 |
|       5 | 0x62B42     |      404290 |
|       6 | 0xFFFFF061  |  4294963297 |
|       7 | 0x000A      |          10 |
|       8 | 0xFFF85C88  |  4294466696 |
|       9 | 0x668A0     |      420000 |
|      10 | 0xFFFFEC78  |  4294962296 |
|      11 | 0xFFF8E6C5  |  4294502085 |
|      12 | 0x66ADC     |      420572 |
|      13 | 0x0606      |        1542 |
|      14 | 0x0638      |        1592 |
|      15 | 0x6BEC0     |      442048 |
|      16 | 0xFFF72644  |  4294387268 |
|      17 | 0x001E      |          30 |
|      18 | 0x000D      |          13 |
|      19 | 0x6C7FD     |      444413 |
|      20 | 0xFFF72474  |  4294386804 |
|      21 | 0x0032      |          50 |
|      22 | 0x036E      |         878 |
|      23 | 0xFFF8C67B  |  4294493819 |
|      24 | 0xFFFFF093  |  4294963347 |
|      25 | 0xFFF8BBC6  |  4294491078 |
|      26 | 0x66A7E     |      420478 |

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

### Event 8

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

### Event 10

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
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=-474.490*, Z=404.290*, Y=-3.999*
  2: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                32 07 80  1F 00 08 80 09 80 0A 80       2..........
0060: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0055 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=-500.600*, Z=420.000*, Y=-5.000*
  2: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0062 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0063 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             00                                        .           
```

#### Opcodes

```
  0: 0x0064 [0x00] END_REQSTACK()
```

### Event 306

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

### Event 307

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   00                                    .         
```

#### Opcodes

```
  0: 0x0066 [0x00] END_REQSTACK()
```

### Event 308

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0067  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      00                                  .        
```

#### Opcodes

```
  0: 0x0067 [0x00] END_REQSTACK()
```

### Event 309

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0068  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          00                               .       
```

#### Opcodes

```
  0: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             32 03 80 1F 00 0B 80           2......
0070: 0C 80 06 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0069 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=-465.211*, Z=420.572*, Y=-3.999*
  2: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0076 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0078  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          C0 01 80 00                      ....    
```

#### Opcodes

```
  0: 0x0078 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007C  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      C0 00 80 00              ....
```

#### Opcodes

```
  0: 0x007C [0xC0] EventEntity->Render.Flags3 &= ~0x1000 // Clear bit 12 (from 0*)
  1: 0x007F [0x00] END_REQSTACK()
```

### Event 124

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

### Event 125

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0081  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    00                                              .              
```

#### Opcodes

```
  0: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       B4 00 00 00 41 70  68 6D 61 75 00 00 00 00    ....Aphmau....
0090: 00 00 00 00 00 00 B5 00  00 00 B6 00 0D 80 00     ............... 
```

#### Opcodes

```
  0: 0x0082 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Aphmau")
  1: 0x0096 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x009A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1542*)
  3: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               B4                 .
00A0: 00 00 00 4E 61 73 68 6D  65 69 72 61 00 00 00 00  ...Nashmeira....
00B0: 00 00 00 B5 00 00 00 B6  00 0E 80 00              ............    
```

#### Opcodes

```
  0: 0x009F [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Nashmeira")
  1: 0x00B3 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x00B7 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1592*)
  3: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      32 03 80 1F              2...
00C0: 00 0F 80 10 80 00 80 1F  01 1E 01 81 04 01 1C 11  ................
00D0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00BC [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00BF [0x1F] MOVE_ENTITY: EventEntity moves to X=442.048*, Z=-580.028*, Y=0.000*
  2: 0x00C7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C9 [0x1E] EventEntity looks at Iroha (ID: 17072385/0x01048101) and starts talking
  4: 0x00CE [0x1C] WAIT(30* ticks)
  5: 0x00D1 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D2   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:       32 12 80 1F 00 13  80 14 80 15 80 1F 01 1E    2.............
00E0: 01 81 04 01 1C 11 80 00                           ........        
```

#### Opcodes

```
  0: 0x00D2 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00D5 [0x1F] MOVE_ENTITY: EventEntity moves to X=444.413*, Z=-580.492*, Y=0.050*
  2: 0x00DD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00DF [0x1E] EventEntity looks at Iroha (ID: 17072385/0x01048101) and starts talking
  4: 0x00E4 [0x1C] WAIT(30* ticks)
  5: 0x00E7 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E8   |
| Data Size    | 48 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                          32 03 80 1F 00 13 80 14          2.......
00F0: 80 15 80 1F 01 6F 4A F8  FF FF 7F 01 81 04 01 6F  .....oJ........o
0100: 76 F8 FF FF 7F 1C 07 80  5B 16 80 D7 80 04 01 D7  v.......[.......
0110: 80 04 01 73 68 61 30 00                           ...sha0.        
```

#### Opcodes

```
  0: 0x00E8 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00EB [0x1F] MOVE_ENTITY: EventEntity moves to X=444.413*, Z=-580.492*, Y=0.050*
  2: 0x00F3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00F6 [0x4A] EventEntity looks at Iroha (ID: 17072385/0x01048101)
  5: 0x00FF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0100 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0105 [0x1C] WAIT(10* ticks)
  8: 0x0108 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sha0" with entities [Nashmeira (ID: 17072343/0x010480D7), Nashmeira (ID: 17072343/0x010480D7)], work=878*
  9: 0x0117 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0118   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                          32 03 80 1F 00 17 80 09          2.......
0120: 80 18 80 1F 01 1E 01 81  04 01 1C 11 80 00        ..............  
```

#### Opcodes

```
  0: 0x0118 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x011B [0x1F] MOVE_ENTITY: EventEntity moves to X=-473.477*, Z=420.000*, Y=-3.949*
  2: 0x0123 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0125 [0x1E] EventEntity looks at Iroha (ID: 17072385/0x01048101) and starts talking
  4: 0x012A [0x1C] WAIT(30* ticks)
  5: 0x012D [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012E   |
| Data Size    | 48 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                            32 03                2.
0130: 80 1F 00 19 80 1A 80 18  80 1F 01 6F 4A F8 FF FF  ...........oJ...
0140: 7F 01 81 04 01 6F 76 F8  FF FF 7F 1C 07 80 5B 16  .....ov.......[.
0150: 80 D7 80 04 01 D7 80 04  01 73 68 61 30 00        .........sha0.  
```

#### Opcodes

```
  0: 0x012E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0131 [0x1F] MOVE_ENTITY: EventEntity moves to X=-476.218*, Z=420.478*, Y=-3.949*
  2: 0x0139 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x013B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x013C [0x4A] EventEntity looks at Iroha (ID: 17072385/0x01048101)
  5: 0x0145 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0146 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x014B [0x1C] WAIT(10* ticks)
  8: 0x014E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sha0" with entities [Nashmeira (ID: 17072343/0x010480D7), Nashmeira (ID: 17072343/0x010480D7)], work=878*
  9: 0x015D [0x00] END_REQSTACK()
```
