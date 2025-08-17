# 17768545 - Water in Space

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 80 bytes                |
| Total Events     | 4                       |
| References Count | 0                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     15 |              3 |
| [65535.2](#event-655352) | 0x0010       |     28 |              4 |
| [362](#event-362)        | 0x002C       |      1 |              1 |

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
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2D F8 FF FF 7F F8 FF  FF 7F 68 73 68 69 8E 00   -........hshi..
```

#### Opcodes

```
  0: 0x0001 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "hshi" with entities [EventEntity, EventEntity]
  1: 0x000E [0x8E] EventEntity->StatusEvent = 45
  2: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 2D F8 FF FF 7F F8 FF FF  7F 6B 72 6F 69 2D F8 FF  -........kroi-..
0020: FF 7F F8 FF FF 7F 6B 69  6C 68 8F 00              ......kilh..    
```

#### Opcodes

```
  0: 0x0010 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kroi" with entities [EventEntity, EventEntity]
  1: 0x001D [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kilh" with entities [EventEntity, EventEntity]
  2: 0x002A [0x8F] SET_ENTITY_STATUS_EVENT_46()
  3: 0x002B [0x00] END_REQSTACK()
```

### Event 362

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
