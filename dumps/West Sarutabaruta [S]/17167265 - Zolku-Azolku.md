# 17167265 - Zolku-Azolku

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 276 bytes                      |
| Total Events     | 16                             |
| References Count | 15                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [105](#event-105)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     14 |              4 |
| [65535.2](#event-655352)   | 0x0010       |     14 |              4 |
| [65535.3](#event-655353)   | 0x001E       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0028       |     10 |              2 |
| [107](#event-107)          | 0x0032       |      1 |              1 |
| [112](#event-112)          | 0x0033       |      1 |              1 |
| [65535.5](#event-655355)   | 0x0034       |     15 |              5 |
| [65535.6](#event-655356)   | 0x0043       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0044       |     18 |              4 |
| [65535.8](#event-655358)   | 0x0056       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0060       |      9 |              3 |
| [65535.10](#event-6553510) | 0x0069       |      9 |              3 |
| [65535.11](#event-6553511) | 0x0072       |     10 |              2 |
| [65535.12](#event-6553512) | 0x007C       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000C      |          12 |
|       1 | 0xFFFF7190  |  4294930832 |
|       2 | 0x15B55     |       88917 |
|       3 | 0xFFFFEC78  |  4294962296 |
|       4 | 0x0027      |          39 |
|       5 | 0xFFFF5535  |  4294923573 |
|       6 | 0x1583B     |       88123 |
|       7 | 0xFFFFEC79  |  4294962297 |
|       8 | 0x0000      |           0 |
|       9 | 0x0001      |           1 |
|      10 | 0x0080      |         128 |
|      11 | 0x002A      |          42 |
|      12 | 0x29958     |      170328 |
|      13 | 0xFFFFDA0C  |  4294957580 |
|      14 | 0xFFFFF2F9  |  4294963961 |

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

### Event 105

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-36.464*, Z=88.917*, Y=-5.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 32 04 80 1F 00 05 80 06  80 07 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0010 [0x32] ExtData[1]->MainSpeed = 39* * 0.1
  1: 0x0013 [0x1F] MOVE_ENTITY: EventEntity moves to X=-43.723*, Z=88.123*, Y=-4.999*
  2: 0x001B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            6C F8                l.
0020: FF FF 7F 08 80 09 80 00                           ........        
```

#### Opcodes

```
  0: 0x001E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          6C F8 FF FF 7F 0A 80 09          l.......
0030: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0028 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0031 [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       00                                            .             
```

#### Opcodes

```
  0: 0x0032 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0033  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          00                                          .            
```

#### Opcodes

```
  0: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             32 0B 80 1F  00 0C 80 0D 80 0E 80 1F      2...........
0040: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0034 [0x32] ExtData[1]->MainSpeed = 42* * 0.1
  1: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=170.328*, Z=-9.716*, Y=-3.335*
  2: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0041 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          00                                          .            
```

#### Opcodes

```
  0: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             22 00 2F 00  F8 FF FF 7F 6C F8 FF FF      "./.....l...
0050: 7F 08 80 09 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0044 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0046 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x004C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   6C F8  FF FF 7F 0A 80 09 80 00        l.........
```

#### Opcodes

```
  0: 0x0056 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0060  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 22 00 2F 00 F8 FF FF 7F  00                       "./......       
```

#### Opcodes

```
  0: 0x0060 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0062 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0069  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             22 01 2F 01 F8 FF FF           "./....
0070: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0069 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x006B [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       6C F8 FF FF 7F 08  80 09 80 00                l.........    
```

#### Opcodes

```
  0: 0x0072 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      6C F8 FF FF              l...
0080: 7F 0A 80 09 80 00                                 ......          
```

#### Opcodes

```
  0: 0x007C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0085 [0x00] END_REQSTACK()
```
