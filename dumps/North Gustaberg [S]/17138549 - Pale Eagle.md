# 17138549 - Pale Eagle

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | North Gustaberg [S] (ID: 88) |
| Block Size       | 144 bytes                    |
| Total Events     | 6                            |
| References Count | 11                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [4](#event-4)            | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |      5 |              2 |
| [13](#event-13)          | 0x000D       |      7 |              2 |
| [65535.2](#event-655352) | 0x0014       |     16 |              5 |
| [65535.3](#event-655353) | 0x0024       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x013D      |         317 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFC7022  |  4294733858 |
|       3 | 0x1D214     |      119316 |
|       4 | 0xFFFFFE38  |  4294966840 |
|       5 | 0x5D1BD     |      381373 |
|       6 | 0x2A19A     |      172442 |
|       7 | 0x0A91      |        2705 |
|       8 | 0x5CC18     |      379928 |
|       9 | 0x2B477     |      177271 |
|      10 | 0x0994      |        2452 |

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

### Event 4

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

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          B6 09 00 80 00                   .....   
```

#### Opcodes

```
  0: 0x0008 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Sub, value=317*)
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         92 01 F8               ...
0010: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x000D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             33 01 32 01  80 1F 00 02 80 03 80 04      3.2.........
0020: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0014 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0016 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  2: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=-233.438*, Z=119.316*, Y=-0.456*
  3: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 01 80 1F  00 05 80 06 80 07 80 1F      2...........
0030: 01 1F 00 08 80 09 80 0A  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=381.373*, Z=172.442*, Y=2.705*
  2: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=379.928*, Z=177.271*, Y=2.452*
  4: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x003B [0x00] END_REQSTACK()
```
