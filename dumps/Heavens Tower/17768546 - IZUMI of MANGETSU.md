# 17768546 - IZUMI of MANGETSU

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 116 bytes               |
| Total Events     | 9                       |
| References Count | 0                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     14 |              2 |
| [65535.2](#event-655352) | 0x000F       |      1 |              1 |
| [65535.3](#event-655353) | 0x0010       |     14 |              2 |
| [65535.4](#event-655354) | 0x001E       |     14 |              2 |
| [65535.5](#event-655355) | 0x002C       |      1 |              1 |
| [65535.6](#event-655356) | 0x002D       |     14 |              2 |
| [65535.7](#event-655357) | 0x003B       |      1 |              1 |
| [362](#event-362)        | 0x003C       |      1 |              1 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2D F8 FF FF 7F F8 FF  FF 7F 6B 72 6F 69 00      -........kroi. 
```

#### Opcodes

```
  0: 0x0001 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kroi" with entities [EventEntity, EventEntity]
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.2

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

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 2D F8 FF FF 7F F8 FF FF  7F 6B 69 6B 61 00        -........kika.  
```

#### Opcodes

```
  0: 0x0010 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kika" with entities [EventEntity, EventEntity]
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            2D F8                -.
0020: FF FF 7F F8 FF FF 7F 6B  69 6B 62 00              .......kikb.    
```

#### Opcodes

```
  0: 0x001E [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kikb" with entities [EventEntity, EventEntity]
  1: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      00                       .   
```

#### Opcodes

```
  0: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         2D F8 FF               -..
0030: FF 7F F8 FF FF 7F 79 6F  6D 69 00                 ......yomi.     
```

#### Opcodes

```
  0: 0x002D [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "yomi" with entities [EventEntity, EventEntity]
  1: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   00                         .    
```

#### Opcodes

```
  0: 0x003B [0x00] END_REQSTACK()
```

### Event 362

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      00                       .   
```

#### Opcodes

```
  0: 0x003C [0x00] END_REQSTACK()
```
