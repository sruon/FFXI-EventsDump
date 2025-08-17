# 17863432 - Ergon Locus

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Morimar Basalt Fields (ID: 265) |
| Block Size       | 84 bytes                        |
| Total Events     | 5                               |
| References Count | 6                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [30](#event-30)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     16 |              4 |
| [65535.2](#event-655352) | 0x0012       |      5 |              2 |
| [64](#event-64)          | 0x0017       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x49D3F     |      302399 |
|       1 | 0x5F29F     |      389791 |
|       2 | 0xFFFFFF9C  |  4294967196 |
|       3 | 0x0604      |        1540 |
|       4 | 0x0916      |        2326 |
|       5 | 0x0032      |          50 |

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

### Event 30

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
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       33 01 37 00 80 01  80 02 80 03 80 B6 00 04    3.7...........
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0002 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=302.399*, z=389.791*, y=-0.100*, direction=135.3°*
  2: 0x000D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2326*)
  3: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       B6 00 05 80 00                                .....         
```

#### Opcodes

```
  0: 0x0012 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=50*)
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      00                                  .        
```

#### Opcodes

```
  0: 0x0017 [0x00] END_REQSTACK()
```
