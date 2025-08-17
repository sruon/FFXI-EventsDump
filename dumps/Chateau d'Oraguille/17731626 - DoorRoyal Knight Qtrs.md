# 17731626 - DoorRoyal Knight Qtrs

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 136 bytes                     |
| Total Events     | 21                            |
| References Count | 0                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [121](#event-121)        | 0x0001       |      1 |              1 |
| [120](#event-120)        | 0x0002       |      1 |              1 |
| [563](#event-563)        | 0x0003       |      1 |              1 |
| [564](#event-564)        | 0x0004       |      1 |              1 |
| [571](#event-571)        | 0x0005       |      1 |              1 |
| [578](#event-578)        | 0x0006       |      2 |              2 |
| [579](#event-579)        | 0x0008       |      2 |              2 |
| [580](#event-580)        | 0x000A       |      2 |              2 |
| [583](#event-583)        | 0x000C       |      2 |              2 |
| [586](#event-586)        | 0x000E       |      2 |              2 |
| [590](#event-590)        | 0x0010       |      2 |              2 |
| [591](#event-591)        | 0x0012       |      2 |              2 |
| [597](#event-597)        | 0x0014       |      2 |              2 |
| [598](#event-598)        | 0x0016       |      2 |              2 |
| [65535.1](#event-655351) | 0x0018       |      2 |              2 |
| [65535.2](#event-655352) | 0x001A       |      2 |              2 |
| [604](#event-604)        | 0x001C       |      2 |              2 |
| [605](#event-605)        | 0x001E       |      2 |              2 |
| [606](#event-606)        | 0x0020       |      2 |              2 |
| [609](#event-609)        | 0x0022       |      2 |              2 |

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

### Event 121

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

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 563

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 564

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 571

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                00                                      .          
```

#### Opcodes

```
  0: 0x0005 [0x00] END_REQSTACK()
```

### Event 578

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   4D 00                                 M.        
```

#### Opcodes

```
  0: 0x0006 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 579

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          4D 00                            M.      
```

#### Opcodes

```
  0: 0x0008 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0009 [0x00] END_REQSTACK()
```

### Event 580

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000A  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                4D 00                        M.    
```

#### Opcodes

```
  0: 0x000A [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 583

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      4D 00                    M.  
```

#### Opcodes

```
  0: 0x000C [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x000D [0x00] END_REQSTACK()
```

### Event 586

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            4D 00                M.
```

#### Opcodes

```
  0: 0x000E [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 590

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

### Event 591

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       4D 00                                         M.            
```

#### Opcodes

```
  0: 0x0012 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0013 [0x00] END_REQSTACK()
```

### Event 597

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0014  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             4D 00                                     M.          
```

#### Opcodes

```
  0: 0x0014 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 598

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   4D 00                                 M.        
```

#### Opcodes

```
  0: 0x0016 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0018  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          4C 00                            L.      
```

#### Opcodes

```
  0: 0x0018 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                4D 00                        M.    
```

#### Opcodes

```
  0: 0x001A [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x001B [0x00] END_REQSTACK()
```

### Event 604

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001C  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      4D 00                    M.  
```

#### Opcodes

```
  0: 0x001C [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 605

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            4D 00                M.
```

#### Opcodes

```
  0: 0x001E [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 606

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0020  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 4D 00                                             M.              
```

#### Opcodes

```
  0: 0x0020 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0021 [0x00] END_REQSTACK()
```

### Event 609

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       4D 00                                         M.            
```

#### Opcodes

```
  0: 0x0022 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0023 [0x00] END_REQSTACK()
```
