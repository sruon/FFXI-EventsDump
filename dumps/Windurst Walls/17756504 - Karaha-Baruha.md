# 17756504 - Karaha-Baruha

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 76 bytes                 |
| Total Events     | 6                        |
| References Count | 2                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [569](#event-569)        | 0x0001       |      7 |              2 |
| [570](#event-570)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |      5 |              2 |
| [65535.2](#event-655352) | 0x0014       |      5 |              2 |
| [575](#event-575)        | 0x0019       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0034      |          52 |
|       1 | 0x0902      |        2306 |

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

### Event 569

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 570

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               B6                 .
0010: 00 00 80 00                                       ....            
```

#### Opcodes

```
  0: 0x000F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0014  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             B6 00 01 80  00                           .....       
```

#### Opcodes

```
  0: 0x0014 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2306*)
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 575

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             00                             .      
```

#### Opcodes

```
  0: 0x0019 [0x00] END_REQSTACK()
```
