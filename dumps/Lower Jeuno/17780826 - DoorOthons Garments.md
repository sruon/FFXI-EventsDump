# 17780826 - DoorOthons Garments

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 64 bytes              |
| Total Events     | 8                     |
| References Count | 0                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [20035](#event-20035) | 0x0001       |      2 |              2 |
| [20037](#event-20037) | 0x0003       |      2 |              2 |
| [20039](#event-20039) | 0x0005       |      2 |              2 |
| [20041](#event-20041) | 0x0007       |      2 |              2 |
| [20045](#event-20045) | 0x0009       |      2 |              2 |
| [20052](#event-20052) | 0x000B       |      2 |              2 |
| [20047](#event-20047) | 0x000D       |      2 |              2 |

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

### Event 20035

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

### Event 20037

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

### Event 20039

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

### Event 20041

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

### Event 20045

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

### Event 20052

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

### Event 20047

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
