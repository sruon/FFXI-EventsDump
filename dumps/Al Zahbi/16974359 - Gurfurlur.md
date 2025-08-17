# 16974359 - Gurfurlur

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al Zahbi (ID: 48) |
| Block Size       | 132 bytes         |
| Total Events     | 7                 |
| References Count | 6                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     18 |              4 |
| [65535.2](#event-655352) | 0x0013       |      9 |              3 |
| [65535.3](#event-655353) | 0x001C       |      9 |              3 |
| [65535.4](#event-655354) | 0x0025       |      7 |              2 |
| [11](#event-11)          | 0x002C       |      9 |              3 |
| [65535.5](#event-655355) | 0x0035       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0xFFFE5484  |  4294857860 |
|       3 | 0x10A33     |       68147 |
|       4 | 0x07D0      |        2000 |
|       5 | 0x0FFA      |        4090 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 2F 00 F8 FF FF  7F 6C F8 FF FF 7F 00 80   "./.....l......
0010: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0009 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0013  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          22 00 2F 00 F8  FF FF 7F 00                 "./......    
```

#### Opcodes

```
  0: 0x0013 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0015 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001C  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      22 01 2F 01              "./.
0020: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x001C [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x001E [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0025  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                2F 00 F8  FF FF 7F 00                   /......    
```

#### Opcodes

```
  0: 0x0025 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x002B [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      92 01 F8 FF              ....
0030: FF 7F AB 08 00                                    .....           
```

#### Opcodes

```
  0: 0x002C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0032 [0xAB] EventEntity->Render.Flags2 |= 0x02 // Set bit 1
  2: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                37 02 80  03 80 04 80 05 80 00          7......... 
```

#### Opcodes

```
  0: 0x0035 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-109.436*, z=68.147*, y=2.000*, direction=359.5°*
  1: 0x003E [0x00] END_REQSTACK()
```
