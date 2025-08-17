# 17114038 - Lehko Habhoka

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 284 bytes                  |
| Total Events     | 12                         |
| References Count | 16                         |

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
| [216](#event-216)          | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |     30 |              6 |
| [65535.9](#event-655359)   | 0x0063       |     15 |              5 |
| [65535.10](#event-6553510) | 0x0072       |     39 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000C      |          12 |
|       4 | 0x3D995     |      252309 |
|       5 | 0x7E749     |      517961 |
|       6 | 0x019C      |         412 |
|       7 | 0x05A6      |        1446 |
|       8 | 0x3D1EB     |      250347 |
|       9 | 0x7E133     |      516403 |
|      10 | 0x013B      |         315 |
|      11 | 0x000B      |          11 |
|      12 | 0x3D42A     |      250922 |
|      13 | 0x7DFF8     |      516088 |
|      14 | 0x0157      |         343 |
|      15 | 0x05A3      |        1443 |

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

### Event 216

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
| Data Size    | 30 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                32 03 80  1F 00 04 80 05 80 06 80       2..........
0050: 1F 01 6F 5B 07 80 B6 23  05 01 B6 23 05 01 74 68  ..o[...#...#..th
0060: 62 30 00                                          b0.             
```

#### Opcodes

```
  0: 0x0045 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x0048 [0x1F] MOVE_ENTITY: EventEntity moves to X=252.309*, Z=517.961*, Y=0.412*
  2: 0x0050 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0052 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0053 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb0" with entities [Lehko Habhoka (ID: 17114038/0x010523B6), Lehko Habhoka (ID: 17114038/0x010523B6)], work=1446*
  5: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          32 03 80 1F 00  08 80 09 80 0A 80 1F 01     2............
0070: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0063 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x0066 [0x1F] MOVE_ENTITY: EventEntity moves to X=250.347*, Z=516.403*, Y=0.315*
  2: 0x006E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0070 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 39 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       32 0B 80 1F 00 0C  80 0D 80 0E 80 1F 01 6F    2............o
0080: 4A B6 23 05 01 F0 FF FF  7F 5B 0F 80 B6 23 05 01  J.#......[...#..
0090: B6 23 05 01 74 6C 62 30  00                       .#..tlb0.       
```

#### Opcodes

```
  0: 0x0072 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0075 [0x1F] MOVE_ENTITY: EventEntity moves to X=250.922*, Z=516.088*, Y=0.343*
  2: 0x007D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0080 [0x4A] Lehko Habhoka (ID: 17114038/0x010523B6) looks at LocalPlayer
  5: 0x0089 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [Lehko Habhoka (ID: 17114038/0x010523B6), Lehko Habhoka (ID: 17114038/0x010523B6)], work=1443*
  6: 0x0098 [0x00] END_REQSTACK()
```
