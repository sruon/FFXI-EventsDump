# 17335147 - Bukadaemon2

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Beaucedine Glacier [S] (ID: 136) |
| Block Size       | 140 bytes                        |
| Total Events     | 10                               |
| References Count | 3                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [15](#event-15)          | 0x0001       |      1 |              1 |
| [16](#event-16)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |      1 |              1 |
| [65535.2](#event-655352) | 0x0004       |     18 |              4 |
| [65535.3](#event-655353) | 0x0016       |     10 |              2 |
| [65535.4](#event-655354) | 0x0020       |      9 |              3 |
| [65535.5](#event-655355) | 0x0029       |      9 |              3 |
| [65535.6](#event-655356) | 0x0032       |     10 |              2 |
| [65535.7](#event-655357) | 0x003C       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |

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
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             22 00 2F 00  F8 FF FF 7F 6C F8 FF FF      "./.....l...
0010: 7F 00 80 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0004 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0006 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   6C F8  FF FF 7F 02 80 01 80 00        l.........
```

#### Opcodes

```
  0: 0x0016 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0020  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 22 00 2F 00 F8 FF FF 7F  00                       "./......       
```

#### Opcodes

```
  0: 0x0020 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0022 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             22 01 2F 01 F8 FF FF           "./....
0030: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0029 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x002B [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       6C F8 FF FF 7F 00  80 01 80 00                l.........    
```

#### Opcodes

```
  0: 0x0032 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      6C F8 FF FF              l...
0040: 7F 02 80 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x003C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0045 [0x00] END_REQSTACK()
```
