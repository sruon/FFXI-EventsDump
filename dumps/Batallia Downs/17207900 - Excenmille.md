# 17207900 - Excenmille

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Batallia Downs (ID: 105) |
| Block Size       | 444 bytes                |
| Total Events     | 23                       |
| References Count | 26                       |

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
| [504](#event-504)          | 0x0044       |      1 |              1 |
| [505](#event-505)          | 0x0045       |      1 |              1 |
| [506](#event-506)          | 0x0046       |      1 |              1 |
| [507](#event-507)          | 0x0047       |      1 |              1 |
| [508](#event-508)          | 0x0048       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0049       |     30 |              6 |
| [65535.9](#event-655359)   | 0x0067       |     43 |              9 |
| [65535.10](#event-6553510) | 0x0092       |      5 |              2 |
| [65535.11](#event-6553511) | 0x0097       |      5 |              2 |
| [65535.12](#event-6553512) | 0x009C       |      5 |              2 |
| [65535.13](#event-6553513) | 0x00A1       |     14 |              4 |
| [65535.14](#event-6553514) | 0x00AF       |     33 |              7 |
| [65535.15](#event-6553515) | 0x00D0       |      4 |              2 |
| [65535.16](#event-6553516) | 0x00D4       |      4 |              2 |
| [65535.17](#event-6553517) | 0x00D8       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x002B      |          43 |
|       4 | 0xFFFD3BC5  |  4294785989 |
|       5 | 0x9069      |       36969 |
|       6 | 0xFFFFFC18  |  4294966296 |
|       7 | 0x0515      |        1301 |
|       8 | 0x0010      |          16 |
|       9 | 0xFFFD25BE  |  4294780350 |
|      10 | 0xE25A      |       57946 |
|      11 | 0xFFFFF769  |  4294965097 |
|      12 | 0x08D4      |        2260 |
|      13 | 0x08EF      |        2287 |
|      14 | 0x08CE      |        2254 |
|      15 | 0x000B      |          11 |
|      16 | 0xFFFD7C08  |  4294802440 |
|      17 | 0x51A9      |       20905 |
|      18 | 0x000D      |          13 |
|      19 | 0xFFFEA0F6  |  4294877430 |
|      20 | 0x80B85     |      527237 |
|      21 | 0xFFFFC413  |  4294951955 |
|      22 | 0x05E0      |        1504 |
|      23 | 0xFFFC423F  |  4294722111 |
|      24 | 0x65E09     |      417289 |
|      25 | 0x5FFC      |       24572 |

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

### Event 504

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

### Event 505

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

### Event 506

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0046  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   00                                    .         
```

#### Opcodes

```
  0: 0x0046 [0x00] END_REQSTACK()
```

### Event 507

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      00                                  .        
```

#### Opcodes

```
  0: 0x0047 [0x00] END_REQSTACK()
```

### Event 508

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          00                               .       
```

#### Opcodes

```
  0: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 30 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             32 03 80 1F 00 04 80           2......
0050: 05 80 06 80 1F 01 6F 5B  07 80 5C 92 06 01 5C 92  ......o[..\...\.
0060: 06 01 6B 65 69 30 00                              ..kei0.         
```

#### Opcodes

```
  0: 0x0049 [0x32] ExtData[1]->MainSpeed = 43* * 0.1
  1: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=-181.307*, Z=36.969*, Y=-1.000*
  2: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0057 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kei0" with entities [Excenmille (ID: 17207900/0x0106925C), Excenmille (ID: 17207900/0x0106925C)], work=1301*
  5: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      32  08 80 1F 00 09 80 0A 80         2........
0070: 0B 80 1F 01 6F 4B 5C 92  06 01 00 80 6F 76 5C 92  ....oK\.....ov\.
0080: 06 01 5B 07 80 5C 92 06  01 5C 92 06 01 6B 65 69  ..[..\...\...kei
0090: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0067 [0x32] ExtData[1]->MainSpeed = 16* * 0.1
  1: 0x006A [0x1F] MOVE_ENTITY: EventEntity moves to X=-186.946*, Z=57.946*, Y=-2.199*
  2: 0x0072 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0075 [0x4B] UPDATE_ENTITY_YAW(entity=Excenmille (ID: 17207900/0x0106925C), yaw=0.0°*)
  5: 0x007C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x007D [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Excenmille (ID: 17207900/0x0106925C) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0082 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kei0" with entities [Excenmille (ID: 17207900/0x0106925C), Excenmille (ID: 17207900/0x0106925C)], work=1301*
  8: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0092  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       B6 00 0C 80 00                                .....         
```

#### Opcodes

```
  0: 0x0092 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2260*)
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0097  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      B6  00 0D 80 00                     .....    
```

#### Opcodes

```
  0: 0x0097 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2287*)
  1: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009C  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      B6 00 0E 80              ....
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x009C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2254*)
  1: 0x00A0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A1   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    32 0F 80 1F 00 10 80  11 80 06 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x00A1 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x00A4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-164.856*, Z=20.905*, Y=-1.000*
  2: 0x00AC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               32                 2
00B0: 12 80 1F 00 13 80 14 80  15 80 1F 01 6F 1C 01 80  ............o...
00C0: 5B 16 80 5C 92 06 01 5C  92 06 01 6B 61 69 30 00  [..\...\...kai0.
```

#### Opcodes

```
  0: 0x00AF [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-89.866*, Z=527.237*, Y=-15.341*
  2: 0x00BA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00BD [0x1C] WAIT(1* ticks)
  5: 0x00C0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kai0" with entities [Excenmille (ID: 17207900/0x0106925C), Excenmille (ID: 17207900/0x0106925C)], work=1504*
  6: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D0  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: C0 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00D0 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x00D3 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D4  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             C0 00 80 00                               ....        
```

#### Opcodes

```
  0: 0x00D4 [0xC0] EventEntity->Render.Flags3 &= ~0x1000 // Clear bit 12 (from 0*)
  1: 0x00D7 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D8   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                          32 12 80 1F 00 17 80 18          2.......
00E0: 80 19 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x00D8 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00DB [0x1F] MOVE_ENTITY: EventEntity moves to X=-245.185*, Z=417.289*, Y=24.572*
  2: 0x00E3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00E6 [0x00] END_REQSTACK()
```
