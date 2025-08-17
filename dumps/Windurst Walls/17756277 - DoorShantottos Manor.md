# 17756277 - DoorShantottos Manor

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 124 bytes                |
| Total Events     | 18                       |
| References Count | 0                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [396](#event-396)        | 0x0001       |      2 |              2 |
| [397](#event-397)        | 0x0003       |      2 |              2 |
| [445](#event-445)        | 0x0005       |      2 |              2 |
| [448](#event-448)        | 0x0007       |      2 |              2 |
| [450](#event-450)        | 0x0009       |      2 |              2 |
| [506](#event-506)        | 0x000B       |      2 |              2 |
| [507](#event-507)        | 0x000D       |      2 |              2 |
| [529](#event-529)        | 0x000F       |      1 |              1 |
| [65535.1](#event-655351) | 0x0010       |      2 |              2 |
| [560](#event-560)        | 0x0012       |      2 |              2 |
| [561](#event-561)        | 0x0014       |      2 |              2 |
| [569](#event-569)        | 0x0016       |      2 |              2 |
| [570](#event-570)        | 0x0018       |      2 |              2 |
| [574](#event-574)        | 0x001A       |      2 |              2 |
| [65535.2](#event-655352) | 0x001C       |      2 |              2 |
| [65535.3](#event-655353) | 0x001E       |      2 |              2 |
| [575](#event-575)        | 0x0020       |      2 |              2 |

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

### Event 396

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4D 00                                           M.             
```

#### Opcodes

```
  0: 0x0001 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0002 [0x00] END_REQSTACK()
```

### Event 397

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          4D 00                                       M.           
```

#### Opcodes

```
  0: 0x0003 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0004 [0x00] END_REQSTACK()
```

### Event 445

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                4D 00                                   M.         
```

#### Opcodes

```
  0: 0x0005 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 448

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      4D  00                              M.       
```

#### Opcodes

```
  0: 0x0007 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0008 [0x00] END_REQSTACK()
```

### Event 450

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

### Event 506

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

### Event 507

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

### Event 529

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               00                 .
```

#### Opcodes

```
  0: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.1

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

### Event 560

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

### Event 561

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

### Event 569

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

### Event 570

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0018  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          4D 00                            M.      
```

#### Opcodes

```
  0: 0x0018 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0019 [0x00] END_REQSTACK()
```

### Event 574

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

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001C  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      4C 00                    L.  
```

#### Opcodes

```
  0: 0x001C [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.3

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

### Event 575

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
