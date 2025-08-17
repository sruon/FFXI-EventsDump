# 17175364 - Nhev Befrathi

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Meriphataud Mountains [S] (ID: 97) |
| Block Size       | 156 bytes                          |
| Total Events     | 11                                 |
| References Count | 3                                  |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [3](#event-3)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |      3 |              2 |
| [65535.3](#event-655353) | 0x000F       |      1 |              1 |
| [65535.4](#event-655354) | 0x0010       |     18 |              4 |
| [65535.5](#event-655355) | 0x0022       |     10 |              2 |
| [65535.6](#event-655356) | 0x002C       |      9 |              3 |
| [65535.7](#event-655357) | 0x0035       |      9 |              3 |
| [65535.8](#event-655358) | 0x003E       |     10 |              2 |
| [65535.9](#event-655359) | 0x0048       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0080      |         128 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |

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

### Event 3

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       6C F8 FF FF 7F 00  80 01 80 00                l.........    
```

#### Opcodes

```
  0: 0x0002 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      A4 01 00                 ... 
```

#### Opcodes

```
  0: 0x000C [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               00                 .
```

#### Opcodes

```
  0: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 22 00 2F 00 F8 FF FF 7F  6C F8 FF FF 7F 02 80 01  "./.....l.......
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0010 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0012 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0018 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       6C F8 FF FF 7F 00  80 01 80 00                l.........    
```

#### Opcodes

```
  0: 0x0022 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      22 00 2F 00              "./.
0030: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x002C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x002E [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0035  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                22 01 2F  01 F8 FF FF 7F 00             "./......  
```

#### Opcodes

```
  0: 0x0035 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0037 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            6C F8                l.
0040: FF FF 7F 02 80 01 80 00                           ........        
```

#### Opcodes

```
  0: 0x003E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          6C F8 FF FF 7F 00 80 01          l.......
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0048 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0051 [0x00] END_REQSTACK()
```
