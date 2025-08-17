# 17629805 - Sand Lizard

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Quicksand Caves (ID: 208) |
| Block Size       | 96 bytes                  |
| Total Events     | 7                         |
| References Count | 3                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      5 |              2 |
| [65535.2](#event-655352) | 0x0006       |      5 |              2 |
| [65535.3](#event-655353) | 0x000B       |      5 |              2 |
| [105](#event-105)        | 0x0010       |      7 |              2 |
| [106](#event-106)        | 0x0017       |      7 |              2 |
| [107](#event-107)        | 0x001E       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0E0F      |        3599 |
|       1 | 0x0034      |          52 |
|       2 | 0x0148      |         328 |

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
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    B6 00 00 80 00                                  .....          
```

#### Opcodes

```
  0: 0x0001 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=3599*)
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   B6 00  01 80 00                       .....     
```

#### Opcodes

```
  0: 0x0006 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   B6 00 02 80 00             .....
```

#### Opcodes

```
  0: 0x000B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=328*)
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0010 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0017 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            92 01                ..
0020: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x001E [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0024 [0x00] END_REQSTACK()
```
