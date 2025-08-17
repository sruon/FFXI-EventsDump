# 17335145 - Akadaemon

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Beaucedine Glacier [S] (ID: 136) |
| Block Size       | 220 bytes                        |
| Total Events     | 14                               |
| References Count | 11                               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [15](#event-15)            | 0x0001       |      1 |              1 |
| [16](#event-16)            | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |      5 |              2 |
| [65535.2](#event-655352)   | 0x0008       |      5 |              2 |
| [65535.3](#event-655353)   | 0x000D       |     11 |              3 |
| [65535.4](#event-655354)   | 0x0018       |     11 |              3 |
| [65535.5](#event-655355)   | 0x0023       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0024       |     18 |              4 |
| [65535.7](#event-655357)   | 0x0036       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0040       |      9 |              3 |
| [65535.9](#event-655359)   | 0x0049       |      9 |              3 |
| [65535.10](#event-6553510) | 0x0052       |     10 |              2 |
| [65535.11](#event-6553511) | 0x005C       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0109      |         265 |
|       1 | 0x08AB      |        2219 |
|       2 | 0xFFFF4757  |  4294920023 |
|       3 | 0xFFFCEC3E  |  4294765630 |
|       4 | 0xFFFF3D80  |  4294917504 |
|       5 | 0xFFFEF608  |  4294899208 |
|       6 | 0xFFFCEC4D  |  4294765645 |
|       7 | 0xFFFF0A9C  |  4294904476 |
|       8 | 0x0000      |           0 |
|       9 | 0x0001      |           1 |
|      10 | 0x0080      |         128 |

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

### Event 15

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

### Event 16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          B6 00 00 80 00                              .....        
```

#### Opcodes

```
  0: 0x0003 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=265*)
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          B6 00 01 80 00                   .....   
```

#### Opcodes

```
  0: 0x0008 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2219*)
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         5A 00 02               Z..
0010: 80 03 80 04 80 5A 01 00                           .....Z..        
```

#### Opcodes

```
  0: 0x000D [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-47.273*, Z=-201.666*, Y=-49.792*
  1: 0x0015 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  2: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          5A 00 05 80 06 80 07 80          Z.......
0020: 5A 01 00                                          Z..             
```

#### Opcodes

```
  0: 0x0018 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-68.088*, Z=-201.651*, Y=-62.820*
  1: 0x0020 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  2: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0023  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          00                                          .            
```

#### Opcodes

```
  0: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             22 00 2F 00  F8 FF FF 7F 6C F8 FF FF      "./.....l...
0030: 7F 08 80 09 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0024 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0026 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x002C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   6C F8  FF FF 7F 0A 80 09 80 00        l.........
```

#### Opcodes

```
  0: 0x0036 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0040  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 22 00 2F 00 F8 FF FF 7F  00                       "./......       
```

#### Opcodes

```
  0: 0x0040 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0042 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0049  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             22 01 2F 01 F8 FF FF           "./....
0050: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0049 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x004B [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       6C F8 FF FF 7F 08  80 09 80 00                l.........    
```

#### Opcodes

```
  0: 0x0052 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      6C F8 FF FF              l...
0060: 7F 0A 80 09 80 00                                 ......          
```

#### Opcodes

```
  0: 0x005C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0065 [0x00] END_REQSTACK()
```
