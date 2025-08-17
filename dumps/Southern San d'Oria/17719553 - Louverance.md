# 17719553 - Louverance

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 360 bytes                     |
| Total Events     | 12                            |
| References Count | 26                            |

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
| [757](#event-757)          | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |     10 |              2 |
| [65535.9](#event-655359)   | 0x004F       |     40 |             10 |
| [65535.10](#event-6553510) | 0x0077       |     70 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFB8A89  |  4294675081 |
|       4 | 0x19274     |      103028 |
|       5 | 0xFFFFDC11  |  4294958097 |
|       6 | 0x07F9      |        2041 |
|       7 | 0x002A      |          42 |
|       8 | 0xFFFB7B48  |  4294671176 |
|       9 | 0x1920D     |      102925 |
|      10 | 0xFFFB73DE  |  4294669278 |
|      11 | 0x18851     |      100433 |
|      12 | 0x0028      |          40 |
|      13 | 0xFFFB79BB  |  4294670779 |
|      14 | 0x1908E     |      102542 |
|      15 | 0xFFFB85EC  |  4294673900 |
|      16 | 0x19257     |      102999 |
|      17 | 0xFFFFDBFC  |  4294958076 |
|      18 | 0xFFFB8BD9  |  4294675417 |
|      19 | 0x183DE     |       99294 |
|      20 | 0xFFFB91E3  |  4294676963 |
|      21 | 0x17EF0     |       98032 |
|      22 | 0xFFFFDC06  |  4294958086 |
|      23 | 0xFFFBB747  |  4294686535 |
|      24 | 0x17EEF     |       98031 |
|      25 | 0xFFFFE7C9  |  4294961097 |

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

### Event 757

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                37 03 80  04 80 05 80 06 80 00          7......... 
```

#### Opcodes

```
  0: 0x0045 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-292.215*, z=103.028*, y=-9.199*, direction=179.4°*
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 40 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               32                 2
0050: 07 80 1F 00 08 80 09 80  05 80 1F 01 1F 00 0A 80  ................
0060: 0B 80 05 80 1F 01 6F 4A  F8 FF FF 7F F0 FF FF 7F  ......oJ........
0070: 6F 76 F8 FF FF 7F 00                              ov.....         
```

#### Opcodes

```
  0: 0x004F [0x32] ExtData[1]->MainSpeed = 42* * 0.1
  1: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=-296.120*, Z=102.925*, Y=-9.199*
  2: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=-298.018*, Z=100.433*, Y=-9.199*
  4: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0066 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0067 [0x4A] EventEntity looks at LocalPlayer
  7: 0x0070 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0071 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  9: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 70 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      32  0C 80 1F 00 0D 80 0E 80         2........
0080: 05 80 1F 01 1F 00 0F 80  10 80 11 80 1F 01 1F 00  ................
0090: 12 80 13 80 05 80 1F 01  27 10 93 60 0E 01 02 4A  ........'..`...J
00A0: F0 FF FF 7F F8 FF FF 7F  1F 00 14 80 15 80 16 80  ................
00B0: 1F 01 1F 00 17 80 18 80  19 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x0077 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=-296.517*, Z=102.542*, Y=-9.199*
  2: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0084 [0x1F] MOVE_ENTITY: EventEntity moves to X=-293.396*, Z=102.999*, Y=-9.220*
  4: 0x008C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x008E [0x1F] MOVE_ENTITY: EventEntity moves to X=-291.879*, Z=99.294*, Y=-9.199*
  6: 0x0096 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0098 [0x27] REQ_SET(priority=0x10, entity_id=Door:Count's Manor (ID: 17719443/0x010E6093), tag_num=0x02)
  8: 0x009F [0x4A] LocalPlayer looks at EventEntity
  9: 0x00A8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-290.333*, Z=98.032*, Y=-9.210*
 10: 0x00B0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x00B2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-280.761*, Z=98.031*, Y=-6.199*
 12: 0x00BA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 13: 0x00BC [0x00] END_REQSTACK()
```
