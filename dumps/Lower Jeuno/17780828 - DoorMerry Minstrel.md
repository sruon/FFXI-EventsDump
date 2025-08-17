# 17780828 - DoorMerry Minstrel

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 80 bytes              |
| Total Events     | 11                    |
| References Count | 0                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [101](#event-101)        | 0x0001       |      1 |              1 |
| [20035](#event-20035)    | 0x0002       |      2 |              2 |
| [20037](#event-20037)    | 0x0004       |      2 |              2 |
| [20039](#event-20039)    | 0x0006       |      2 |              2 |
| [20041](#event-20041)    | 0x0008       |      2 |              2 |
| [20045](#event-20045)    | 0x000A       |      2 |              2 |
| [20052](#event-20052)    | 0x000C       |      2 |              2 |
| [20047](#event-20047)    | 0x000E       |      2 |              2 |
| [65535.1](#event-655351) | 0x0010       |      2 |              2 |
| [65535.2](#event-655352) | 0x0012       |      2 |              2 |

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

### Event 101

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

### Event 20035

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       4D 00                                         M.            
```

#### Opcodes

```
  0: 0x0002 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 20037

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

### Event 20039

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

### Event 20041

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

### Event 20045

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

### Event 20052

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

### Event 20047

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
0010: 4C 00                                             L.              
```

#### Opcodes

```
  0: 0x0010 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

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
