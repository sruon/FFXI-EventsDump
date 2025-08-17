# 16904375 - Kenkyuin_B

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Monarch Linn (ID: 31) |
| Block Size       | 88 bytes              |
| Total Events     | 4                     |
| References Count | 4                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [15](#event-15)          | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     10 |              2 |
| [32001](#event-32001)    | 0x0018       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFE9D1  |  4294961617 |
|       1 | 0xFFFEA952  |  4294879570 |
|       2 | 0xFFFF7AF5  |  4294933237 |
|       3 | 0x0A14      |        2580 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 00         .............  
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            37 00                7.
0010: 80 01 80 02 80 03 80 00                           ........        
```

#### Opcodes

```
  0: 0x000E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-5.679*, z=-87.726*, y=-34.059*, direction=226.8°*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          92 01 F8 FF FF 7F 94 01          ........
0020: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0018 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x001E [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0024 [0x00] END_REQSTACK()
```
