# 16875899 - Kukki-Chebukki

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Lufaise Meadows (ID: 24) |
| Block Size       | 308 bytes                |
| Total Events     | 14                       |
| References Count | 21                       |

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
| [116](#event-116)          | 0x0044       |      1 |              1 |
| [117](#event-117)          | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0050       |     23 |              7 |
| [65535.10](#event-6553510) | 0x0067       |     10 |              2 |
| [65535.11](#event-6553511) | 0x0071       |     38 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFF873E5  |  4294472677 |
|       4 | 0x58110     |      360720 |
|       5 | 0xFFFF859A  |  4294935962 |
|       6 | 0x082A      |        2090 |
|       7 | 0x0028      |          40 |
|       8 | 0xFFF83736  |  4294457142 |
|       9 | 0x58523     |      361763 |
|      10 | 0xFFFF8459  |  4294935641 |
|      11 | 0x000F      |          15 |
|      12 | 0xFFF7BCD2  |  4294425810 |
|      13 | 0x57E8F     |      360079 |
|      14 | 0xFFFF8CC4  |  4294937796 |
|      15 | 0x05C9      |        1481 |
|      16 | 0xFFF8459D  |  4294460829 |
|      17 | 0x582EF     |      361199 |
|      18 | 0xFFFF851B  |  4294935835 |
|      19 | 0x001E      |          30 |
|      20 | 0x0144      |         324 |

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

### Event 116

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

### Event 117

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   37 03  80 04 80 05 80 06 80 00        7.........
```

#### Opcodes

```
  0: 0x0046 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-494.619*, z=360.720*, y=-31.334*, direction=183.7°*
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 32 07 80 1F 00 08 80 09  80 0A 80 1F 01 6F 1C 0B  2............o..
0060: 80 1E 7D 81 01 01 00                              ..}....         
```

#### Opcodes

```
  0: 0x0050 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=-510.154*, Z=361.763*, Y=-31.655*
  2: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005E [0x1C] WAIT(15* ticks)
  5: 0x0061 [0x1E] EventEntity looks at Vukki-Chebukki (ID: 16875901/0x0101817D) and starts talking
  6: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      37  0C 80 0D 80 0E 80 0F 80         7........
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0067 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-541.486*, z=360.079*, y=-29.500*, direction=130.2°*
  1: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 38 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    32 07 80 1F 00 10 80  11 80 12 80 1F 01 6F 1E   2............o.
0080: 7D 81 01 01 1C 13 80 5B  14 80 7B 81 01 01 7B 81  }......[..{...{.
0090: 01 01 77 61 76 30 00                              ..wav0.         
```

#### Opcodes

```
  0: 0x0071 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0074 [0x1F] MOVE_ENTITY: EventEntity moves to X=-506.467*, Z=361.199*, Y=-31.461*
  2: 0x007C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x007F [0x1E] EventEntity looks at Vukki-Chebukki (ID: 16875901/0x0101817D) and starts talking
  5: 0x0084 [0x1C] WAIT(30* ticks)
  6: 0x0087 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wav0" with entities [Kukki-Chebukki (ID: 16875899/0x0101817B), Kukki-Chebukki (ID: 16875899/0x0101817B)], work=324*
  7: 0x0096 [0x00] END_REQSTACK()
```
