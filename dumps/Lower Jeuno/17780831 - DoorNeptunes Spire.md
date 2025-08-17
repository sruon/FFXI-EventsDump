# 17780831 - DoorNeptunes Spire

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 92 bytes              |
| Total Events     | 11                    |
| References Count | 2                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10022](#event-10022)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      9 |              5 |
| [10049](#event-10049)    | 0x000B       |      1 |              1 |
| [10050](#event-10050)    | 0x000C       |      1 |              1 |
| [10051](#event-10051)    | 0x000D       |      1 |              1 |
| [65535.2](#event-655352) | 0x000E       |      2 |              2 |
| [65535.3](#event-655353) | 0x0010       |      2 |              2 |
| [10067](#event-10067)    | 0x0012       |      1 |              1 |
| [10094](#event-10094)    | 0x0013       |      2 |              2 |
| [10125](#event-10125)    | 0x0015       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0168      |         360 |
|       1 | 0x0050      |          80 |

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

### Event 10022

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       4C 1C 00 80 4D 1C  01 80 00                   L...M....     
```

#### Opcodes

```
  0: 0x0002 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0003 [0x1C] WAIT(360* ticks)
  2: 0x0006 [0x4D] EventEntity->StatusEvent = 9 // Close door
  3: 0x0007 [0x1C] WAIT(80* ticks)
  4: 0x000A [0x00] END_REQSTACK()
```

### Event 10049

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   00                         .    
```

#### Opcodes

```
  0: 0x000B [0x00] END_REQSTACK()
```

### Event 10050

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      00                       .   
```

#### Opcodes

```
  0: 0x000C [0x00] END_REQSTACK()
```

### Event 10051

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         00                     .  
```

#### Opcodes

```
  0: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            4C 00                L.
```

#### Opcodes

```
  0: 0x000E [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 4D 00                                             M.              
```

#### Opcodes

```
  0: 0x0010 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 10067

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       00                                            .             
```

#### Opcodes

```
  0: 0x0012 [0x00] END_REQSTACK()
```

### Event 10094

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0013  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          4D 00                                       M.           
```

#### Opcodes

```
  0: 0x0013 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0014 [0x00] END_REQSTACK()
```

### Event 10125

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0015  |
| Data Size    | 2 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                26 00                                   &.         
```

#### Opcodes

```
  0: 0x0015 [0x26] DEPRECATED_YIELD
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0016 [0x00] END_REQSTACK()
```
