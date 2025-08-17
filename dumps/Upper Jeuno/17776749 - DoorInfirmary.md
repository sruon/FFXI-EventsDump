# 17776749 - DoorInfirmary

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 88 bytes              |
| Total Events     | 10                    |
| References Count | 0                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [33](#event-33)          | 0x0001       |      1 |              1 |
| [34](#event-34)          | 0x0002       |      1 |              1 |
| [2](#event-2)            | 0x0003       |      7 |              2 |
| [82](#event-82)          | 0x000A       |      7 |              2 |
| [75](#event-75)          | 0x0011       |      7 |              2 |
| [65535.1](#event-655351) | 0x0018       |      2 |              2 |
| [65535.2](#event-655352) | 0x001A       |      2 |              2 |
| [10060](#event-10060)    | 0x001C       |      1 |              1 |
| [10205](#event-10205)    | 0x001D       |      1 |              1 |

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

### Event 33

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

### Event 34

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

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          94 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0003 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0009 [0x00] END_REQSTACK()
```

### Event 82

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                94 01 F8 FF FF 7F            ......
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x000A [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 75

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    94 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0011 [0x94] EventEntity->Render.Flags3 ^= 0x01
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

### Event 10060

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      00                       .   
```

#### Opcodes

```
  0: 0x001C [0x00] END_REQSTACK()
```

### Event 10205

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         00                     .  
```

#### Opcodes

```
  0: 0x001D [0x00] END_REQSTACK()
```
