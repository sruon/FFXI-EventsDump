# 17441125 - GeDha Evileye

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Castle Zvahl Keep (ID: 162) |
| Block Size       | 156 bytes                   |
| Total Events     | 10                          |
| References Count | 5                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [125](#event-125)        | 0x0001       |      7 |              2 |
| [126](#event-126)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |      7 |              3 |
| [65535.2](#event-655352) | 0x0016       |      7 |              3 |
| [127](#event-127)        | 0x001D       |      7 |              2 |
| [65535.3](#event-655353) | 0x0024       |      5 |              2 |
| [65535.4](#event-655354) | 0x0029       |      5 |              2 |
| [65535.5](#event-655355) | 0x002E       |      5 |              2 |
| [65535.6](#event-655356) | 0x0033       |     27 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0034      |          52 |
|       3 | 0x0E3F      |        3647 |
|       4 | 0x029C      |         668 |

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

### Event 125

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 126

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               AB                 .
0010: 03 AC 01 00 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000F [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0011 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   AC 01  01 80 AB 04 00                 .......   
```

#### Opcodes

```
  0: 0x0016 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x001A [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x001C [0x00] END_REQSTACK()
```

### Event 127

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         92 01 F8               ...
0020: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x001D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             B6 00 02 80  00                           .....       
```

#### Opcodes

```
  0: 0x0024 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             B6 00 03 80 00                 .....  
```

#### Opcodes

```
  0: 0x0029 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=3647*)
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            B6 00                ..
0030: 04 80 00                                          ...             
```

#### Opcodes

```
  0: 0x002E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=668*)
  1: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          2C F8 FF FF 7F  F8 FF FF 7F 64 65 70 6F     ,........depo
0040: 53 F8 FF FF 7F F8 FF FF  7F 64 65 70 6F 00        S........depo.  
```

#### Opcodes

```
  0: 0x0033 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "depo" with entities [EventEntity, EventEntity]
  1: 0x0040 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "depo" with entities [EventEntity, EventEntity]
  2: 0x004D [0x00] END_REQSTACK()
```
