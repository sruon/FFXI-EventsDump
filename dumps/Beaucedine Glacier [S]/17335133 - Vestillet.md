# 17335133 - Vestillet

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Beaucedine Glacier [S] (ID: 136) |
| Block Size       | 364 bytes                        |
| Total Events     | 19                               |
| References Count | 24                               |

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
| [17](#event-17)            | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |     11 |              3 |
| [19](#event-19)            | 0x0050       |      1 |              1 |
| [65535.9](#event-655359)   | 0x0051       |     11 |              3 |
| [65535.10](#event-6553510) | 0x005C       |     11 |              3 |
| [65535.11](#event-6553511) | 0x0067       |     27 |              7 |
| [16](#event-16)            | 0x0082       |      1 |              1 |
| [65535.12](#event-6553512) | 0x0083       |     21 |              2 |
| [65535.13](#event-6553513) | 0x0098       |     21 |              2 |
| [29](#event-29)            | 0x00AD       |      1 |              1 |
| [30](#event-30)            | 0x00AE       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFBACCD  |  4294683853 |
|       4 | 0xFFFD74FD  |  4294800637 |
|       5 | 0xFFFF633B  |  4294927163 |
|       6 | 0xF7A9      |       63401 |
|       7 | 0x1385C     |       79964 |
|       8 | 0xFFFF66FE  |  4294928126 |
|       9 | 0xFFFB4E3A  |  4294659642 |
|      10 | 0xFFFD4A4B  |  4294789707 |
|      11 | 0xFFFF6277  |  4294926967 |
|      12 | 0xFB4E      |       64334 |
|      13 | 0xEB1C      |       60188 |
|      14 | 0xFFFF63D3  |  4294927315 |
|      15 | 0x0003      |           3 |
|      16 | 0x000B      |          11 |
|      17 | 0x00D9      |         217 |
|      18 | 0x0002      |           2 |
|      19 | 0x000D      |          13 |
|      20 | 0x000C      |          12 |
|      21 | 0x00DD      |         221 |
|      22 | 0x00FA      |         250 |
|      23 | 0x001B      |          27 |

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

### Event 17

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

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                1F 00 03  80 04 80 05 80 1F 01 00       ...........
```

#### Opcodes

```
  0: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=-283.443*, Z=-166.659*, Y=-40.133*
  1: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x004F [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0050  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    1F 00 06 80 07 80 08  80 1F 01 00               ...........    
```

#### Opcodes

```
  0: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=63.401*, Z=79.964*, Y=-39.170*
  1: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      1F 00 09 80              ....
0060: 0A 80 0B 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=-307.654*, Z=-177.589*, Y=-40.329*
  1: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      1F  00 0C 80 0D 80 0E 80 1F         .........
0070: 01 6F 4A 5D 83 08 01 F0  FF FF 7F 6F 76 5D 83 08  .oJ].......ov]..
0080: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0067 [0x1F] MOVE_ENTITY: EventEntity moves to X=64.334*, Z=60.188*, Y=-39.981*
  1: 0x006F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0071 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0072 [0x4A] Vestillet (ID: 17335133/0x0108835D) looks at LocalPlayer
  4: 0x007B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x007C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Vestillet (ID: 17335133/0x0108835D) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0081 [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0082  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       00                                            .             
```

#### Opcodes

```
  0: 0x0082 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0083   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:          B6 0B 0F 80 10  80 00 80 00 80 00 80 11     .............
0090: 80 11 80 00 80 00 80 00                           ........        
```

#### Opcodes

```
  0: 0x0083 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=11*, head=0*, body=0*, hands=0*, legs=217*, feet=217*, main=0*, sub=0*)
  1: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          B6 0B 0F 80 12 80 00 80          ........
00A0: 11 80 13 80 14 80 15 80  16 80 17 80 00           .............   
```

#### Opcodes

```
  0: 0x0098 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=0*, body=217*, hands=13*, legs=12*, feet=221*, main=250*, sub=27*)
  1: 0x00AC [0x00] END_REQSTACK()
```

### Event 29

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AD  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         00                     .  
```

#### Opcodes

```
  0: 0x00AD [0x00] END_REQSTACK()
```

### Event 30

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AE  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            00                   . 
```

#### Opcodes

```
  0: 0x00AE [0x00] END_REQSTACK()
```
