# 17142628 - Cavernous Maw

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Grauberg [S] (ID: 89) |
| Block Size       | 88 bytes              |
| Total Events     | 6                     |
| References Count | 2                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [28](#event-28)          | 0x0001       |      1 |              1 |
| [26](#event-26)          | 0x0002       |     11 |              3 |
| [65535.1](#event-655351) | 0x000D       |      5 |              2 |
| [30](#event-30)          | 0x0012       |     11 |              3 |
| [32](#event-32)          | 0x001D       |     11 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x08E7      |        2279 |
|       1 | 0x0034      |          52 |

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

### Event 28

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

### Event 26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       92 01 F8 FF FF 7F  B6 00 00 80 00             ...........   
```

#### Opcodes

```
  0: 0x0002 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0008 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2279*)
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         B6 00 01               ...
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x000D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       B6 00 01 80 92 01  F8 FF FF 7F 00             ...........   
```

#### Opcodes

```
  0: 0x0012 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x0016 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x001C [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         B6 00 01               ...
0020: 80 92 01 F8 FF FF 7F 00                           ........        
```

#### Opcodes

```
  0: 0x001D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x0021 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0027 [0x00] END_REQSTACK()
```
