# 17179500 - Noillurie

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 156 bytes                         |
| Total Events     | 8                                 |
| References Count | 10                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [11](#event-11)          | 0x0001       |      7 |              2 |
| [115](#event-115)        | 0x0008       |      7 |              2 |
| [116](#event-116)        | 0x000F       |      7 |              2 |
| [65535.1](#event-655351) | 0x0016       |      5 |              2 |
| [65535.2](#event-655352) | 0x001B       |     14 |              4 |
| [65535.3](#event-655353) | 0x0029       |      5 |              2 |
| [65535.4](#event-655354) | 0x002E       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0968      |        2408 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFE87DB  |  4294871003 |
|       3 | 0x5AC5      |       23237 |
|       4 | 0x0BB8      |        3000 |
|       5 | 0x08F8      |        2296 |
|       6 | 0x000D      |          13 |
|       7 | 0xFFFFFC37  |  4294966327 |
|       8 | 0x1D488     |      119944 |
|       9 | 0x0C1D      |        3101 |

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

### Event 11

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

### Event 115

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

### Event 116

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               92                 .
0010: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x000F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   B6 00  00 80 00                       .....     
```

#### Opcodes

```
  0: 0x0016 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2408*)
  1: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   32 01 80 1F 00             2....
0020: 02 80 03 80 04 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x001B [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=-96.293*, Z=23.237*, Y=3.000*
  2: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             B6 00 05 80 00                 .....  
```

#### Opcodes

```
  0: 0x0029 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2296*)
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            32 06                2.
0030: 80 1F 00 07 80 08 80 09  80 1F 01 1E 79 23 06 01  ............y#..
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x002E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.969*, Z=119.944*, Y=3.101*
  2: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003B [0x1E] EventEntity looks at Portia (ID: 17179513/0x01062379) and starts talking
  4: 0x0040 [0x00] END_REQSTACK()
```
