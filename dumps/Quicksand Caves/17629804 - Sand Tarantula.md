# 17629804 - Sand Tarantula

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Quicksand Caves (ID: 208) |
| Block Size       | 208 bytes                 |
| Total Events     | 11                        |
| References Count | 11                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [105](#event-105)        | 0x0001       |      7 |              2 |
| [106](#event-106)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |      5 |              2 |
| [65535.2](#event-655352) | 0x0014       |      9 |              3 |
| [65535.3](#event-655353) | 0x001D       |      5 |              2 |
| [65535.4](#event-655354) | 0x0022       |      5 |              2 |
| [107](#event-107)        | 0x0027       |      1 |              1 |
| [65535.5](#event-655355) | 0x0028       |     14 |              4 |
| [65535.6](#event-655356) | 0x0036       |     34 |              6 |
| [65535.7](#event-655357) | 0x0058       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0E0D      |        3597 |
|       1 | 0x003C      |          60 |
|       2 | 0x0064      |         100 |
|       3 | 0x0136      |         310 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFED2CF  |  4294890191 |
|       6 | 0x47244     |      291396 |
|       7 | 0xFFFF4CD0  |  4294921424 |
|       8 | 0x00C8      |         200 |
|       9 | 0x0018      |          24 |
|      10 | 0x0000      |           0 |

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

### Event 105

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

### Event 106

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
  0: 0x000F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=3597*)
  1: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0014  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             B6 00 00 80  B6 0F 01 80 00               .........   
```

#### Opcodes

```
  0: 0x0014 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=3597*)
  1: 0x0018 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=60*)
  2: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         B6 0F 02               ...
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x001D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=100*)
  1: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       B6 00 03 80 00                                .....         
```

#### Opcodes

```
  0: 0x0022 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=310*)
  1: 0x0026 [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      00                                  .        
```

#### Opcodes

```
  0: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          32 04 80 1F 00 05 80 06          2.......
0030: 80 07 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0028 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002B [0x1F] MOVE_ENTITY: EventEntity moves to X=-77.105*, Z=291.396*, Y=-45.872*
  2: 0x0033 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 34 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   1C 08  80 32 04 80 1F 00 05 80        ...2......
0040: 06 80 07 80 1F 01 D5 09  80 6C 02 0D 01 6C 02 0D  .........l...l..
0050: 01 69 6E 30 30 0A 80 00                           .in00...        
```

#### Opcodes

```
  0: 0x0036 [0x1C] WAIT(200* ticks)
  1: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=-77.105*, Z=291.396*, Y=-45.872*
  3: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0046 [0xD5] LOAD_EVENT_SCHEDULER_ALT8: Load scheduler "in" with entities [Sand Tarantula (ID: 17629804/0x010D026C), Sand Tarantula (ID: 17629804/0x010D026C)], work=ExtData[1]->WorkLocal[10]
  5: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          32 04 80 1F 00 05 80 06          2.......
0060: 80 07 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0058 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=-77.105*, Z=291.396*, Y=-45.872*
  2: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0065 [0x00] END_REQSTACK()
```
