# 17183605 - Shikaree G

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Castle Oztroja [S] (ID: 99) |
| Block Size       | 388 bytes                   |
| Total Events     | 20                          |
| References Count | 18                          |

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
| [108](#event-108)          | 0x0044       |      1 |              1 |
| [111](#event-111)          | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     20 |              6 |
| [65535.9](#event-655359)   | 0x005A       |      4 |              2 |
| [65535.10](#event-6553510) | 0x005E       |     10 |              2 |
| [65535.11](#event-6553511) | 0x0068       |     23 |              3 |
| [65535.12](#event-6553512) | 0x007F       |     10 |              2 |
| [65535.13](#event-6553513) | 0x0089       |     19 |              3 |
| [65535.14](#event-6553514) | 0x009C       |     14 |              4 |
| [65535.15](#event-6553515) | 0x00AA       |     15 |              5 |
| [65535.16](#event-6553516) | 0x00B9       |     30 |              8 |
| [65535.17](#event-6553517) | 0x00D7       |      3 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0028      |          40 |
|       4 | 0xFFFE78F2  |  4294867186 |
|       5 | 0xFFFF64D5  |  4294927573 |
|       6 | 0xFFFEE7BA  |  4294895546 |
|       7 | 0x0A8C      |        2700 |
|       8 | 0x000A      |          10 |
|       9 | 0xFFFE7923  |  4294867235 |
|      10 | 0xFFFFA36B  |  4294943595 |
|      11 | 0xFFFEE3D2  |  4294894546 |
|      12 | 0xFFFE79C8  |  4294867400 |
|      13 | 0xFFFF5D29  |  4294925609 |
|      14 | 0x02D4      |         724 |
|      15 | 0x003C      |          60 |
|      16 | 0xFFFE7DD9  |  4294868441 |
|      17 | 0xFFFF7890  |  4294932624 |

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

### Event 108

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

### Event 111

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
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   32 03  80 1F 00 04 80 05 80 06        2.........
0050: 80 1F 01 6F 1E 70 33 06  01 00                    ...o.p3...      
```

#### Opcodes

```
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=-100.110*, Z=-39.723*, Y=-71.750*
  2: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0054 [0x1E] EventEntity looks at Lehko Habhoka (ID: 17183600/0x01063370) and starts talking
  5: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005A  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                39 07 80 00                  9...  
```

#### Opcodes

```
  0: 0x005A [0x39] SET_ENTITY_DIRECTION(direction=14.8°*)
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            6C F8                l.
0060: FF FF 7F 00 80 01 80 00                           ........        
```

#### Opcodes

```
  0: 0x005E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 23 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          BA F8 FF FF 7F 00 80 00          ........
0070: 80 00 80 00 80 6C F8 FF  FF 7F 00 80 01 80 00     .....l......... 
```

#### Opcodes

```
  0: 0x0068 [0xBA] SET_ENTITY_POSITION(entity_id=EventEntity, pos_x=0.000*, pos_z=0.000*, pos_y=0.000*, direction=0.0°*)
  1: 0x0075 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  2: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               6C                 l
0080: F8 FF FF 7F 02 80 01 80  00                       .........       
```

#### Opcodes

```
  0: 0x007F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             6C F8 FF FF 7F 00 80           l......
0090: 01 80 6B 69 64 6C 30 F8  FF FF 7F 00              ..kidl0.....    
```

#### Opcodes

```
  0: 0x0089 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0092 [0x6B] STOP_AND_IDLE: EventEntity stops current action and resets to idle (animation="idl0")
  2: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      32 08 80 1F              2...
00A0: 00 09 80 0A 80 0B 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x009C [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x009F [0x1F] MOVE_ENTITY: EventEntity moves to X=-100.061*, Z=-23.701*, Y=-72.750*
  2: 0x00A7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                32 08 80 1F 00 0C            2.....
00B0: 80 0D 80 06 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x00AA [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x00AD [0x1F] MOVE_ENTITY: EventEntity moves to X=-99.896*, Z=-41.687*, Y=-71.750*
  2: 0x00B5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             4B F8 FF FF 7F 0E 80           K......
00C0: 6F 76 F8 FF FF 7F 1C 0F  80 32 08 80 1F 00 10 80  ov.......2......
00D0: 11 80 06 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x00B9 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=4.0°*)
  1: 0x00C0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00C1 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x00C6 [0x1C] WAIT(60* ticks)
  4: 0x00C9 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  5: 0x00CC [0x1F] MOVE_ENTITY: EventEntity moves to X=-98.855*, Z=-34.672*, Y=-71.750*
  6: 0x00D4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00D6 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D7  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                      A4  01 00                           ...      
```

#### Opcodes

```
  0: 0x00D7 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x00D9 [0x00] END_REQSTACK()
```
