# 17752593 - Tosuka-Porika

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 108 bytes                 |
| Total Events     | 6                         |
| References Count | 1                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1159](#event-1159)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     16 |              2 |
| [65535.2](#event-655352) | 0x0012       |     14 |              2 |
| [65535.3](#event-655353) | 0x0020       |     16 |              2 |
| [65535.4](#event-655354) | 0x0030       |     14 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0155      |         341 |

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

### Event 1159

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       5B 00 80 F8 FF FF  7F F8 FF FF 7F 64 6F 6C    [..........dol
0010: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0002 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dol0" with entities [EventEntity, EventEntity], work=341*
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       53 F8 FF FF 7F F8  FF FF 7F 64 6F 6C 30 00    S........dol0.
```

#### Opcodes

```
  0: 0x0012 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dol0" with entities [EventEntity, EventEntity]
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 5B 00 80 F8 FF FF 7F F8  FF FF 7F 64 6F 6C 31 00  [..........dol1.
```

#### Opcodes

```
  0: 0x0020 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dol1" with entities [EventEntity, EventEntity], work=341*
  1: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 53 F8 FF FF 7F F8 FF FF  7F 64 6F 6C 31 00        S........dol1.  
```

#### Opcodes

```
  0: 0x0030 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dol1" with entities [EventEntity, EventEntity]
  1: 0x003D [0x00] END_REQSTACK()
```
