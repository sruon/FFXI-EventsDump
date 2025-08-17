# 17122204 - Nagmolada

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Batallia Downs [S] (ID: 84) |
| Block Size       | 492 bytes                   |
| Total Events     | 21                          |
| References Count | 30                          |

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
| [3](#event-3)              | 0x0044       |      4 |              2 |
| [65535.8](#event-655358)   | 0x0048       |      5 |              2 |
| [65535.9](#event-655359)   | 0x004D       |      5 |              2 |
| [65535.10](#event-6553510) | 0x0052       |     24 |              6 |
| [65535.11](#event-6553511) | 0x006A       |     14 |              4 |
| [4](#event-4)              | 0x0078       |      1 |              1 |
| [65535.12](#event-6553512) | 0x0079       |     14 |              4 |
| [65535.13](#event-6553513) | 0x0087       |     14 |              4 |
| [65535.14](#event-6553514) | 0x0095       |     15 |              5 |
| [65535.15](#event-6553515) | 0x00A4       |     67 |             13 |
| [65535.16](#event-6553516) | 0x00E7       |     25 |              6 |
| [20](#event-20)            | 0x0100       |      7 |              2 |
| [21](#event-21)            | 0x0107       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x084E      |        2126 |
|       4 | 0x03D9      |         985 |
|       5 | 0x002A      |          42 |
|       6 | 0xFFFE5FB3  |  4294860723 |
|       7 | 0xFFFD5FCB  |  4294795211 |
|       8 | 0xFFFE746B  |  4294866027 |
|       9 | 0xFFFD84C1  |  4294804673 |
|      10 | 0x003C      |          60 |
|      11 | 0xFFFE92A5  |  4294873765 |
|      12 | 0xFFFDB6C6  |  4294817478 |
|      13 | 0x000D      |          13 |
|      14 | 0xFFFDA62E  |  4294813230 |
|      15 | 0xFFFDF256  |  4294832726 |
|      16 | 0x39EF      |       14831 |
|      17 | 0xFFFDA813  |  4294813715 |
|      18 | 0xFFFE0FC5  |  4294840261 |
|      19 | 0x3F0E      |       16142 |
|      20 | 0xFFFD79BD  |  4294801853 |
|      21 | 0xFFFDA8D4  |  4294813908 |
|      22 | 0x4DC4      |       19908 |
|      23 | 0x0003      |           3 |
|      24 | 0x0040      |          64 |
|      25 | 0x0800      |        2048 |
|      26 | 0x000B      |          11 |
|      27 | 0xFFFDF46D  |  4294833261 |
|      28 | 0xFFFDEFFB  |  4294832123 |
|      29 | 0x4EE1      |       20193 |

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
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             C0 01 80 00                               ....        
```

#### Opcodes

```
  0: 0x0044 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          B6 00 03 80 00                   .....   
```

#### Opcodes

```
  0: 0x0048 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2126*)
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         B6 00 04               ...
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x004D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=985*)
  1: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       32 05 80 1F 00 06  80 07 80 00 80 1F 01 1F    2.............
0060: 00 08 80 09 80 00 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0052 [0x32] ExtData[1]->MainSpeed = 42* * 0.1
  1: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=-106.573*, Z=-172.085*, Y=0.000*
  2: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=-101.269*, Z=-162.623*, Y=0.000*
  4: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                32 0A 80 1F 00 0B            2.....
0070: 80 0C 80 00 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x006A [0x32] ExtData[1]->MainSpeed = 60* * 0.1
  1: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=-93.531*, Z=-149.818*, Y=0.000*
  2: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0077 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0078  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          00                               .       
```

#### Opcodes

```
  0: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             32 0D 80 1F 00 0E 80           2......
0080: 0F 80 10 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0079 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007C [0x1F] MOVE_ENTITY: EventEntity moves to X=-154.066*, Z=-134.570*, Y=14.831*
  2: 0x0084 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      32  0D 80 1F 00 11 80 12 80         2........
0090: 13 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0087 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x008A [0x1F] MOVE_ENTITY: EventEntity moves to X=-153.581*, Z=-127.035*, Y=16.142*
  2: 0x0092 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                32 0D 80  1F 00 14 80 15 80 16 80       2..........
00A0: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0095 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0098 [0x1F] MOVE_ENTITY: EventEntity moves to X=-165.443*, Z=-153.388*, Y=19.908*
  2: 0x00A0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 67 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             33 01 3B F8  FF FF 7F 00 00 01 00 02      3.;.........
00B0: 00 06 05 00 16 04 00 05  00 17 80 07 02 00 04 00  ................
00C0: 3A F8 FF FF 7F 03 00 37  00 00 01 00 02 00 03 00  :......7........
00D0: 07 05 00 18 80 1C 01 80  01 B4 00 02 05 00 19 80  ................
00E0: 04 E6 00 06 05 00 00                              .......         
```

#### Opcodes

```
  0: 0x00A4 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x00A6 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  2: 0x00B1 [0x06] ExtData[1]->WorkLocal[5] = 0
  3: 0x00B4 [0x16] ExtData[1]->WorkLocal[4] = sin(ExtData[1]->WorkLocal[5]) * 3*
  4: 0x00BB [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[4]
  5: 0x00C0 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[3])
  6: 0x00C7 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
  7: 0x00D0 [0x07] ExtData[1]->WorkLocal[5] += 64*
  8: 0x00D5 [0x1C] WAIT(1* ticks)
  9: 0x00D8 [0x01] GOTO 0x00B4
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00DB [0x02] IF !(ExtData[1]->WorkLocal[5] < 2048*) GOTO 0x00E6
     0x00E3 [0x06] ExtData[1]->WorkLocal[5] = 0
     0x00E6 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E7   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                      79  00 F8 FF FF 7F 98 43 05         y......C.
00F0: 01 32 1A 80 1F 00 1B 80  1C 80 1D 80 1F 01 6F 00  .2............o.
```

#### Opcodes

```
  0: 0x00E7 [0x79] EventEntity looks at Ragelise (ID: 17122200/0x01054398) (Basic look)
  1: 0x00F1 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  2: 0x00F4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-134.035*, Z=-135.173*, Y=20.193*
  3: 0x00FC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00FE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00FF [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0100  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0100 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0106 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0107  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0107 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x010D [0x00] END_REQSTACK()
```
