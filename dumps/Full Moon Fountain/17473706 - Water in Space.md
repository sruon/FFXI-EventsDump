# 17473706 - Water in Space

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 88 bytes                     |
| Total Events     | 6                            |
| References Count | 0                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [42](#event-42)       | 0x0001       |      1 |              1 |
| [1](#event-1)         | 0x0002       |      1 |              1 |
| [51](#event-51)       | 0x0003       |     15 |              3 |
| [52](#event-52)       | 0x0012       |     28 |              4 |
| [32000](#event-32000) | 0x002E       |      1 |              1 |

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

### Event 42

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

### Event 1

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

### Event 51

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          2D F8 FF FF 7F  F8 FF FF 7F 68 73 68 69     -........hshi
0010: 8E 00                                             ..              
```

#### Opcodes

```
  0: 0x0003 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "hshi" with entities [EventEntity, EventEntity]
  1: 0x0010 [0x8E] EventEntity->StatusEvent = 45
  2: 0x0011 [0x00] END_REQSTACK()
```

### Event 52

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       2D F8 FF FF 7F F8  FF FF 7F 6B 72 6F 69 2D    -........kroi-
0020: F8 FF FF 7F F8 FF FF 7F  6B 69 6C 68 8F 00        ........kilh..  
```

#### Opcodes

```
  0: 0x0012 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kroi" with entities [EventEntity, EventEntity]
  1: 0x001F [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kilh" with entities [EventEntity, EventEntity]
  2: 0x002C [0x8F] SET_ENTITY_STATUS_EVENT_46()
  3: 0x002D [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            00                   . 
```

#### Opcodes

```
  0: 0x002E [0x00] END_REQSTACK()
```
