# 17776746 - DoorInfirmary

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 108 bytes             |
| Total Events     | 13                    |
| References Count | 0                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [2](#event-2)            | 0x0001       |      7 |              2 |
| [10](#event-10)          | 0x0008       |      7 |              2 |
| [207](#event-207)        | 0x000F       |      7 |              2 |
| [82](#event-82)          | 0x0016       |      7 |              2 |
| [65535.1](#event-655351) | 0x001D       |      2 |              2 |
| [65535.2](#event-655352) | 0x001F       |      2 |              2 |
| [10059](#event-10059)    | 0x0021       |      1 |              1 |
| [10060](#event-10060)    | 0x0022       |      1 |              1 |
| [10205](#event-10205)    | 0x0023       |      1 |              1 |
| [10061](#event-10061)    | 0x0024       |      1 |              1 |
| [10062](#event-10062)    | 0x0025       |      1 |              1 |
| [10207](#event-10207)    | 0x0026       |      1 |              1 |

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

### Event 2

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

### Event 10

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

### Event 207

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

### Event 82

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

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         4C 00                  L. 
```

#### Opcodes

```
  0: 0x001D [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               4D                 M
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x001F [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 10059

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0021  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    00                                              .              
```

#### Opcodes

```
  0: 0x0021 [0x00] END_REQSTACK()
```

### Event 10060

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       00                                            .             
```

#### Opcodes

```
  0: 0x0022 [0x00] END_REQSTACK()
```

### Event 10205

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0023  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          00                                          .            
```

#### Opcodes

```
  0: 0x0023 [0x00] END_REQSTACK()
```

### Event 10061

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             00                                        .           
```

#### Opcodes

```
  0: 0x0024 [0x00] END_REQSTACK()
```

### Event 10062

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0025  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                00                                      .          
```

#### Opcodes

```
  0: 0x0025 [0x00] END_REQSTACK()
```

### Event 10207

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0026  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   00                                    .         
```

#### Opcodes

```
  0: 0x0026 [0x00] END_REQSTACK()
```
