# 17731627 - DoorTemple Knight Qtrs

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 116 bytes                     |
| Total Events     | 17                            |
| References Count | 0                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [43](#event-43)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      2 |              2 |
| [65535.2](#event-655352) | 0x0004       |      2 |              2 |
| [563](#event-563)        | 0x0006       |      1 |              1 |
| [564](#event-564)        | 0x0007       |      1 |              1 |
| [573](#event-573)        | 0x0008       |      1 |              1 |
| [65535.3](#event-655353) | 0x0009       |      2 |              2 |
| [578](#event-578)        | 0x000B       |      2 |              2 |
| [583](#event-583)        | 0x000D       |      2 |              2 |
| [586](#event-586)        | 0x000F       |      2 |              2 |
| [590](#event-590)        | 0x0011       |      2 |              2 |
| [591](#event-591)        | 0x0013       |      2 |              2 |
| [593](#event-593)        | 0x0015       |      2 |              2 |
| [597](#event-597)        | 0x0017       |      2 |              2 |
| [604](#event-604)        | 0x0019       |      2 |              2 |
| [609](#event-609)        | 0x001B       |      2 |              2 |

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

### Event 43

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
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       4C 00                                         L.            
```

#### Opcodes

```
  0: 0x0002 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             4D 00                                     M.          
```

#### Opcodes

```
  0: 0x0004 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 563

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   00                                    .         
```

#### Opcodes

```
  0: 0x0006 [0x00] END_REQSTACK()
```

### Event 564

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      00                                  .        
```

#### Opcodes

```
  0: 0x0007 [0x00] END_REQSTACK()
```

### Event 573

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          00                               .       
```

#### Opcodes

```
  0: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             4D 00                          M.     
```

#### Opcodes

```
  0: 0x0009 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 578

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   4D 00                      M.   
```

#### Opcodes

```
  0: 0x000B [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 583

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         4D 00                  M. 
```

#### Opcodes

```
  0: 0x000D [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 586

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               4D                 M
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x000F [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 590

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    4D 00                                           M.             
```

#### Opcodes

```
  0: 0x0011 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0012 [0x00] END_REQSTACK()
```

### Event 591

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

### Event 593

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0015  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                4D 00                                   M.         
```

#### Opcodes

```
  0: 0x0015 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 597

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      4D  00                              M.       
```

#### Opcodes

```
  0: 0x0017 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 604

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             4D 00                          M.     
```

#### Opcodes

```
  0: 0x0019 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x001A [0x00] END_REQSTACK()
```

### Event 609

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001B  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   4D 00                      M.   
```

#### Opcodes

```
  0: 0x001B [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x001C [0x00] END_REQSTACK()
```
