# 16974258 - Astral Plinth

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al Zahbi (ID: 48) |
| Block Size       | 100 bytes         |
| Total Events     | 9                 |
| References Count | 0                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [6](#event-6)            | 0x0001       |      7 |              2 |
| [9](#event-9)            | 0x0008       |      7 |              2 |
| [12](#event-12)          | 0x000F       |      7 |              2 |
| [7](#event-7)            | 0x0016       |      7 |              2 |
| [10](#event-10)          | 0x001D       |      7 |              2 |
| [13](#event-13)          | 0x0024       |      7 |              2 |
| [65535.1](#event-655351) | 0x002B       |      2 |              2 |
| [65535.2](#event-655352) | 0x002D       |      2 |              2 |

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

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    94 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          94 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               94                 .
0010: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x000F [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   94 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0016 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         94 01 F8               ...
0020: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x001D [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             94 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x0024 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   4C 00                      L.   
```

#### Opcodes

```
  0: 0x002B [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         4D 00                  M. 
```

#### Opcodes

```
  0: 0x002D [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x002E [0x00] END_REQSTACK()
```
